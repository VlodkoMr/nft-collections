from web3 import Web3
from termcolor import cprint
from config.settings import CHAINS
from helpers.cli import print_input_contract_address, print_input_network
from helpers.settings_helper import get_private_keys
from helpers.web3_helper import get_token_balance, get_token_symbol


def interface_check_balance():
    network = print_input_network()
    contract_address = print_input_contract_address()
    web3 = Web3(Web3.HTTPProvider(CHAINS[network]['rpc']))

    cprint("/-- Check balances & transactions -->", "green")

    for private_key in get_private_keys():
        wallet_address = web3.eth.account.from_key(private_key['private_key']).address

        balance = get_token_balance(web3, wallet_address, contract_address, True)
        symbol = get_token_symbol(web3, network, contract_address)
        nonce = web3.eth.get_transaction_count(wallet_address)

        cprint(f'Wallet [{private_key["index"] + 1}] {wallet_address}', 'green')
        cprint(f'Balance: {balance} {symbol} | {nonce + 1} transactions', 'green')
        cprint(f'---', 'green')
