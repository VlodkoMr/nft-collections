import random
from termcolor import cprint
from config.settings import NATIVE_TOKEN_ADDRESS, USE_SHUFFLE, MIN_SLEEP, MAX_SLEEP
from helpers.factory import call_function
from helpers.functions import int_to_wei, sleeping
from helpers.settings_helper import get_private_keys
from helpers.web3_helper import add_gas_price, add_gas_limit, sign_tx, get_erc1155_abi, get_erc721_abi


def mint_random_nft(chain, nft_list):
	prt_keys = get_private_keys()
	if USE_SHUFFLE:
		random.shuffle(prt_keys)

	for prt_key in prt_keys:
		random_contract = random.choice(list(nft_list.keys()))
		params = [chain, random_contract]

		call_function(prt_key, nft_list[random_contract], chain, '', params)
		sleeping(MIN_SLEEP, MAX_SLEEP)


# Mint NFTs using nfts2me.com
def mint_nfts2_me(web3, private_key, amount, chain_id, contract_address):
	from modules.unused_contracts.config import CONTRACT_PAYMENT

	wallet = web3.eth.account.from_key(private_key).address
	cprint(f'/-- Mint NFT, wallet {wallet} -->', 'green')

	if not amount:
		amount = CONTRACT_PAYMENT[chain_id].get(contract_address, 0.0001)
	amount = int_to_wei(amount, 18)

	contract_txn = {
		"chainId": web3.eth.chain_id,
		"from": wallet,
		"to": web3.to_checksum_address(contract_address),
		"nonce": web3.eth.get_transaction_count(wallet),
		'gasPrice': 0,
		'gas': 0,
		"value": amount,
		"data": "0x1249c58b"
	}

	contract_txn = add_gas_price(web3, contract_txn, chain_id)
	contract_txn = add_gas_limit(web3, contract_txn, chain_id)

	tx_hash = sign_tx(web3, contract_txn, private_key)
	return tx_hash


# Mint NFTs using ERC1155 contract
def mint_collection(web3, private_key, amount, chain_id, contract_address):
	from modules.unused_contracts.config import CONTRACT_PAYMENT

	wallet = web3.eth.account.from_key(private_key).address
	cprint(f'/-- Mint NFT, wallet {wallet} -->', 'green')

	if not amount:
		amount = CONTRACT_PAYMENT[chain_id].get(contract_address, 0.0001)

	contract = web3.eth.contract(address=contract_address, abi=get_erc1155_abi())
	amount = int_to_wei(amount, 18)

	contract_txn = contract.functions.claim(
		wallet,
		0,
		1,
		NATIVE_TOKEN_ADDRESS,
		amount,
		[
			[bytes.fromhex("0000000000000000000000000000000000000000000000000000000000000000")],
			115792089237316195423570985008687907853269984665640564039457584007913129639935,
			amount,
			NATIVE_TOKEN_ADDRESS
		],
		b''
	).build_transaction(
		{
			'from': wallet,
			'nonce': web3.eth.get_transaction_count(wallet),
			'value': amount,
			'gasPrice': 0,
			'gas': 0,
		})

	contract_txn = add_gas_price(web3, contract_txn, chain_id)
	contract_txn = add_gas_limit(web3, contract_txn, chain_id)

	tx_hash = sign_tx(web3, contract_txn, private_key)
	return tx_hash


# Mint ERC721 NFT
def mint_erc721(web3, private_key, amount, chain_id, contract_address):
	from modules.unused_contracts.config import CONTRACT_PAYMENT

	wallet = web3.eth.account.from_key(private_key).address
	cprint(f'/-- Mint NFT, wallet {wallet} -->', 'green')

	if not amount:
		amount = CONTRACT_PAYMENT[chain_id].get(contract_address, 0.0001)

	contract = web3.eth.contract(address=contract_address, abi=get_erc721_abi())
	amount = int_to_wei(amount, 18)

	contract_txn = contract.functions.claim(
		wallet,
		1,
		NATIVE_TOKEN_ADDRESS,
		amount,
		[
			[bytes.fromhex("0000000000000000000000000000000000000000000000000000000000000000")],
			115792089237316195423570985008687907853269984665640564039457584007913129639935,
			amount,
			NATIVE_TOKEN_ADDRESS
		],
		b''
	).build_transaction(
		{
			'from': wallet,
			'nonce': web3.eth.get_transaction_count(wallet),
			'value': amount,
			'gasPrice': 0,
			'gas': 0,
		})

	contract_txn = add_gas_price(web3, contract_txn, chain_id)
	contract_txn = add_gas_limit(web3, contract_txn, chain_id)

	tx_hash = sign_tx(web3, contract_txn, private_key)
	return tx_hash


# Mint NFTs using mint.fun
def mintfun_mint_nft(web3, private_key, amount, chain_id, contract_address):
	from modules.unused_contracts.config import CONTRACT_DATA, CONTRACT_PAYMENT

	wallet = web3.eth.account.from_key(private_key).address
	cprint(f'/-- Mint NFT, wallet {wallet} -->', 'green')

	data = CONTRACT_DATA[chain_id].get(contract_address, '')
	data = data.replace('__wallet__', wallet.replace('0x', ''))

	if not amount:
		amount = CONTRACT_PAYMENT[chain_id].get(contract_address, 0.0001)

	contract_txn = {
		'from': wallet,
		'nonce': web3.eth.get_transaction_count(wallet),
		'value': int_to_wei(amount, 18),
		'gasPrice': 0,
		'gas': 0,
		'to': web3.to_checksum_address(contract_address),
		'data': data,
		'chainId': web3.eth.chain_id
	}

	contract_txn = add_gas_price(web3, contract_txn, chain_id)
	contract_txn = add_gas_limit(web3, contract_txn, chain_id)

	tx_hash = sign_tx(web3, contract_txn, private_key)
	return tx_hash
