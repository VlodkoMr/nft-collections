from config.settings import *
from helpers.cli import get_int_in_range
from helpers.factory import run_script
from helpers.functions import sleeping, api_call
from helpers.settings_helper import get_private_keys
from helpers.web3_helper import get_web3
from loguru import logger
import random

from modules.unused_contracts.config import ALL_FUNCTIONS, API_URL


def run_unused_fn(rpc_chain):
    prt_keys = get_private_keys()
    web3 = get_web3(CHAINS[rpc_chain]['rpc'])
    all_contracts = ALL_FUNCTIONS[rpc_chain]
    api_url = API_URL[rpc_chain]

    if USE_SHUFFLE:
        random.shuffle(prt_keys)

    for key in prt_keys:
        address = web3.eth.account.from_key(key['private_key']).address
        logger.info(f'Start on {address}')
        repeats = get_int_in_range(UNUSED_REPEAT)

        for step in range(repeats):
            logger.info(f'Step {step + 1}/{repeats}')
            tx_list = api_call(api_url, {
                'module': 'account',
                'action': 'txlist',
                'address': address,
                'startblock': 0,
                'endblock': 99999999,
                'page': 1,
                'offset': 200,
            })

            contract_addresses = set()

            for tx in tx_list['result']:
                to_address = tx['to']
                if to_address:
                    contract_addresses.add(web3.to_checksum_address(to_address))

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
