from config.settings import *
from helpers.cli import get_int_in_range
from helpers.factory import run_script
from helpers.functions import sleeping, api_call
from helpers.settings_helper import get_private_keys
from helpers.web3_helper import get_web3
from loguru import logger
import random

from modules.unused_contracts.config import ALL_FUNCTIONS, API_URL

# https://explorer-ui.cardona.zkevm-rpc.com/api-docs

def get_api_url(chain, address):
    if chain == 'scroll':
        return API_URL[chain]
    elif chain == 'zksync':
        return API_URL[chain]
    elif chain == 'base':
        return f'{API_URL[chain]}/{address}/transactions'
    elif chain == 'blast':
        return API_URL[chain]
    elif chain == 'zora':
        return API_URL[chain]
    elif chain == 'polygon_zkevm':
        return f'{API_URL[chain]}/{address}/transactions_v3/'
    elif chain == 'nova':
        return ''

def request_params(address, chain):
    if chain == 'scroll':
        return {
            'module': 'account',
            'action': 'txlist',
            'address': address,
            'startblock': 0,
            'endblock': 99999999,
            'page': 1,
            'offset': 200,
        }
    elif chain == 'zksync':
        return {
            'address': address,
            'limit': 200,
        }
    elif chain == 'base':
        return {
            'filter': 'from',
        }
    elif chain == 'blast':
        return {
            'count': False,
            'fromAddresses': address,
            'includedChainIds': 81457,
            'limit': 200,
            'sort': 'desc',
        }
    elif chain == 'zora':
        return {
            'count': False,
            'fromAddresses': address,
            'includedChainIds': 7777777,
            'limit': 200,
            'sort': 'desc',
        }
    elif chain == 'polygon_zkevm':
        return {}
    elif chain == 'nova':
        return {

        }

def parse_response_to(web3, response, chain) -> set:
    result = set()
    if chain == 'scroll':
        for tx in response['result']:
            result.add(web3.to_checksum_address(tx['to']))
    elif chain == 'zksync':
        for tx in response['items']:
            result.add(web3.to_checksum_address(tx['to']))
    elif chain == 'base':
        for tx in response['items']:
            result.add(web3.to_checksum_address(tx['to']['hash']))
    elif chain == 'blast':
        for tx in response['items']:
            result.add(web3.to_checksum_address(tx['to']['id']))
    elif chain == 'zora':
        for tx in response['items']:
            result.add(web3.to_checksum_address(tx['to']['id']))
    elif chain == 'polygon_zkevm':
        for tx in response['items']:
            result.add(web3.to_checksum_address(tx['to_address']))
    elif chain == 'nova':
        pass

    return result


def run_unused_fn(rpc_chain):
    prt_keys = get_private_keys()
    web3 = get_web3(CHAINS[rpc_chain]['rpc'])
    all_contracts = ALL_FUNCTIONS[rpc_chain]

    if USE_SHUFFLE:
        random.shuffle(prt_keys)

    for key in prt_keys:
        address = web3.eth.account.from_key(key['private_key']).address
        logger.info(f'Start on {address}')

        api_url = get_api_url(rpc_chain, address)
        repeats = get_int_in_range(UNUSED_REPEAT)

        for step in range(repeats):
            logger.info(f'Step {step + 1}/{repeats}')
            tx_list = api_call(api_url, request_params(address, rpc_chain), request_headers(rpc_chain))

            contract_addresses = parse_response_to(web3, tx_list, rpc_chain)

            filtered_contracts = [
                (value, key) for key, value in all_contracts.items() if
                web3.to_checksum_address(key) not in contract_addresses
            ]

            if len(filtered_contracts):
                random_choose = random.choice(filtered_contracts)
                random_fn = random_choose[0]

                if isinstance(random_fn, list):
                    # for Lending
                    logger.info(f'Random chosen  {random_fn[0].__name__}, left {len(filtered_contracts)}')

                    run_script(random_fn[0], rpc_chain, '', [], key)
                    sleeping(30, 60)
                    run_script(random_fn[1], rpc_chain, '', [], key)

                else:
                    f_name = random_fn.__name__
                    logger.info(f'Random chosen {f_name}, left {len(filtered_contracts)}')

                    params = [rpc_chain, random_choose[1]]
                    run_script(random_fn, rpc_chain, '', params, key)
            else:
                logger.info(f'No unused contracts found for   {address}')
                break
