import random
from config.settings import *
from helpers.cli import get_int_in_range
from helpers.factory import run_script
from helpers.functions import api_call, sleeping
from helpers.settings_helper import get_private_keys
from helpers.web3_api import ApiService
from helpers.web3_helper import get_web3
from loguru import logger

from modules.unused_contracts.config import UNUSED_CONTRACTS


def run_unused_fn(network):
    prt_keys = get_private_keys()
    web3 = get_web3(CHAINS[network]['rpc'])
    all_contracts = UNUSED_CONTRACTS[network]

    if USE_SHUFFLE:
        random.shuffle(prt_keys)

    for key in prt_keys:
        address = web3.eth.account.from_key(key['private_key']).address
        logger.info(f'Start on {address}')

        api_service = ApiService(network, address)
        repeats = get_int_in_range(UNUSED_REPEAT)

        for step in range(repeats):
            logger.info(f'Step {step + 1}/{repeats}')

            tx_list = api_call(api_service.get_api_url(), api_service.request_params())
            contract_addresses = api_service.parse_response_to(tx_list)

            filtered_contracts = [
                (value, key) for key, value in all_contracts.items() if
                web3.to_checksum_address(key) not in contract_addresses
            ]

            if len(filtered_contracts):
                random_choose = random.choice(filtered_contracts)
                random_fn = random_choose[0]

                if isinstance(random_fn, list):
                    # for Lending
                    logger.info(f'Random chosen {random_fn[0].__name__}, left {len(filtered_contracts)}')

                    run_script(random_fn[0], network, '', [], key)
                    sleeping(30, 60)
                    run_script(random_fn[1], network, '', [], key)

                else:
                    f_name = random_fn.__name__
                    logger.info(f'Random chosen {f_name}, left {len(filtered_contracts)}')

                    params = [network, random_choose[1]]
                    run_script(random_fn, network, '', params, key)
            else:
                logger.info(f'No unused contracts found for   {address}')
                break
