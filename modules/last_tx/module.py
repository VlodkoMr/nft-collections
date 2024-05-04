from web3 import Web3
from termcolor import cprint
from config.settings import CHAINS
from helpers.cli import print_input_network
from helpers.functions import api_call
from helpers.settings_helper import get_private_keys
from helpers.web3_api import ApiService


def interface_last_tx():
    network = print_input_network()
    web3 = Web3(Web3.HTTPProvider(CHAINS[network]['rpc']))

    cprint("/-- Check last transactions -->", "green")

    for private_key in get_private_keys():
        address = web3.eth.account.from_key(private_key['private_key']).address

        api_service = ApiService(network, address)
        tx_list = api_call(api_service.get_api_url(), api_service.request_params())

        timestamp = api_service.parse_response_timestamp(tx_list)

        cprint(f'Wallet [{private_key["index"] + 1}] {address}', 'green')
        cprint(f'Last: {timestamp}', 'green')
        cprint(f'---', 'green')
