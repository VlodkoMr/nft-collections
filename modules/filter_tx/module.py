from web3 import Web3
from datetime import datetime, timezone
from termcolor import cprint
from config.settings import CHAINS, FILTER_TX_DAYS, FILTER_MIN_TX_COUNT, STR_DONE, STR_CANCEL
from helpers.cli import print_input_network
from helpers.functions import api_call
from helpers.settings_helper import get_private_keys
from helpers.web3_api import ApiService
from modules.unused_contracts.config import UNUSED_CONTRACTS


def interface_last_tx():
    available_chains = list(UNUSED_CONTRACTS.keys())
    disabled_chains = [key for key in CHAINS.keys() if key not in available_chains]
    disabled_chains.append('polygon_zkevm')

    network = print_input_network('Select network', disabled_chains)
    web3 = Web3(Web3.HTTPProvider(CHAINS[network]['rpc']))

    now = datetime.now(timezone.utc)
    current_timestamp = now.timestamp()

    cprint("/-- Check last transaction days -->", "green")

    filtered_private_keys = []
    for item in get_private_keys():
        address = web3.eth.account.from_key(item['private_key']).address
        api_service = ApiService(network, address)
        tx_list = api_call(api_service.get_api_url(), api_service.request_params())

        last_tx_timestamp = api_service.parse_response_timestamp(tx_list)
        diff_seconds = current_timestamp - last_tx_timestamp
        diff_days = diff_seconds / (60 * 60 * 24)
        diff_days = round(diff_days, 1)

        if diff_days <= FILTER_TX_DAYS:
            cprint(f'{STR_DONE}[{item["index"] + 1}] {address}: {diff_days} days ago', 'white')
        else:
            cprint(f'{STR_CANCEL}[{item["index"] + 1}] {address}: {diff_days} days ago', 'red')
            filtered_private_keys.append(item['private_key'])

    if len(filtered_private_keys) and print_approve_replace():
        replace_private_keys(filtered_private_keys)


def interface_tx_count():
    network = print_input_network()
    web3 = Web3(Web3.HTTPProvider(CHAINS[network]['rpc']))

    cprint("/-- Check transactions count -->", "green")

    filtered_private_keys = []
    for item in get_private_keys():
        address = web3.eth.account.from_key(item['private_key']).address
        nonce = web3.eth.get_transaction_count(address)

        if nonce >= FILTER_MIN_TX_COUNT:
            cprint(f'{STR_DONE}[{item["index"] + 1}] {address}: {nonce}', 'white')
        else:
            cprint(f'{STR_CANCEL}[{item["index"] + 1}] {address}: {nonce}', 'red')
            filtered_private_keys.append(item['private_key'])

    if len(filtered_private_keys) and print_approve_replace():
        replace_private_keys(filtered_private_keys)


def print_approve_replace():
    try:
        approval = input("Filter and replace wallets list in wallets.csv? (y/N): ")
        if approval.lower() != "y":
            cprint(f'Action Canceled.\n', 'red')
            return False
        return True
    except KeyboardInterrupt:
        cprint(f' Exit, bye bye\n', 'red')
        raise SystemExit


def replace_private_keys(private_keys):
    source_file = "config/wallets.csv"
    output_lines = []

    # Open and read the source file
    with open(source_file, 'r') as source_csv:
        source_lines = source_csv.readlines()

    # Keep the header
    output_lines.append(source_lines[0])

    # Filter the private keys
    for line in source_lines[1:]:
        key = line.split(',')[0]
        if key in private_keys:
            output_lines.append(line)

    # Write the filtered lines back to the file
    with open(source_file, 'w') as source_csv:
        source_csv.writelines(output_lines)
