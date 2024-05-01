import random

from helpers.functions import int_to_wei
from helpers.web3_helper import add_gas_price, add_gas_limit, sign_tx
from modules.zora_official.config import OFFICIAL_RANDOM_CONTRACTS


def run_zora_official(web3, private_key, amount, chain, contract, data):
	wallet = web3.eth.account.from_key(private_key).address

	if not contract:
		nft_count = len(OFFICIAL_RANDOM_CONTRACTS)
		contract = OFFICIAL_RANDOM_CONTRACTS[random.randint(0, nft_count - 1)]
		data = "0x359f130200000000000000000000000004e2516a2c207e84a1839755675dfd8ef6302f0a0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000a000000000000000000000000000000000000000000000000000000000000000e0000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000020000000000000000000000000__wallet__"

	data = data.replace('__wallet__', wallet.replace('0x', ''))

	contract_txn = {
		'from': wallet,
		'nonce': web3.eth.get_transaction_count(wallet),
		'value': int_to_wei(amount, 18),
		'gasPrice': 0,
		'gas': 0,
		'to': web3.to_checksum_address(contract),
		'data': data,
		'chainId': web3.eth.chain_id
	}

	contract_txn = add_gas_price(web3, contract_txn, chain)
	contract_txn = add_gas_limit(web3, contract_txn, chain)
	tx_hash = sign_tx(web3, contract_txn, private_key)

	return tx_hash
