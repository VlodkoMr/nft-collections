import json
import random
import sys
import time
import math

from termcolor import cprint
from config.settings import *
from web3 import Web3
from config_sample.settings import NATIVE_TOKEN_ADDRESS, NULL_TOKEN_ADDRESS
from helpers.functions import sleeping, wei_to_int
from loguru import logger


def approve_token(web3, private_key, chain, token_address, spender, retry=0):
	try:
		wallet = web3.eth.account.from_key(private_key).address
		contract, decimals, symbol = check_data_token(web3, token_address)
		module_str = f'Approve : {symbol}'

		contract_txn = contract.functions.approve(
			spender,
			115792089237316195423570985008687907853269984665640564039457584007913129639935
		).build_transaction(
			{
				"chainId": web3.eth.chain_id,
				"from": wallet,
				"nonce": web3.eth.get_transaction_count(wallet),
				'gasPrice': 0,
				'gas': 0,
				"value": 0
			}
		)

		contract_txn = add_gas_price(web3, contract_txn, chain)
		contract_txn = add_gas_limit(web3, contract_txn, chain, 1)

		tx_hash = sign_tx(web3, contract_txn, private_key)
		tx_link = f'{CHAINS[chain]["scan"]}/{tx_hash}'

		status = check_status_tx(web3, chain, tx_hash)

		if status == 1:
			cprint(f"{STR_DONE} {module_str} success: {tx_link}", 'green')
		else:
			raise Exception(f"{module_str} failed: {tx_link}")

	except Exception as error:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		cprint(
			f'{STR_CANCEL} Approve error: {str(error)}. {exc_tb.tb_frame.f_code.co_filename}, line: {exc_tb.tb_lineno}',
			'red')
		if retry < MAX_RETRIES:
			cprint(f'Retry again in few seconds.', 'red')
			sleeping(7, 8)
			approve_token(web3, private_key, chain, token_address, spender, retry + 1)


def add_gas_limit(web3, contract_txn, chain, approve=0):
	if chain == 'metis':
		contract_txn['gas'] = 572686
		return contract_txn
	elif chain == 'moonriver' or chain == 'moonbeam':
		contract_txn['gas'] = 348350
		return contract_txn

	gas_limit = web3.eth.estimate_gas(contract_txn)

	if chain == 'scroll':
		if int(gas_limit) < 200000:
			contract_txn['gas'] = int(gas_limit * 1.5)
		else:
			contract_txn['gas'] = int(gas_limit)
	else:
		multiplier = [1.1, 1.2]
		contract_txn['gas'] = int(gas_limit * random.uniform(multiplier[0], multiplier[1]))

	return contract_txn


def add_gas_price(web3, contract_txn, chain=''):
	try:
		if chain in ['moonbeam', 'moonriver', 'polygon_zkevm', 'nova']:
			contract_txn['gasPrice'] = int(web3.eth.gas_price * 1.1)
		elif chain == 'goerly':
			contract_txn['gasPrice'] = int(web3.eth.gas_price * 2)
		elif chain == 'bsc':
			contract_txn['gasPrice'] = int(1000000000)
		else:
			contract_txn['gasPrice'] = int(web3.eth.gas_price)

	except Exception as error:
		cprint(f"Gas Price error: {error}. Random gasPrice: {contract_txn['gasPrice']}", 'red')

	return contract_txn


def sign_tx(web3, contract_txn, private_key):
	signed_tx = web3.eth.account.sign_transaction(contract_txn, private_key)
	raw_tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
	tx_hash = web3.to_hex(raw_tx_hash)

	return tx_hash


def check_status_tx(web3, chain, tx_hash):
	cprint(f'Checking tx_status: {tx_hash}', 'blue')
	repeat_count = 0
	while True:
		try:
			web3.eth.wait_for_transaction_receipt(tx_hash)
			status_ = web3.eth.get_transaction_receipt(tx_hash)
			status = status_["status"]
			if status in [0, 1]:
				return status
			time.sleep(3)
		except Exception as error:
			repeat_count += 1
			if repeat_count > 27:
				return 1
			else:
				cprint(f'{error} retry...', 'red')
				time.sleep(5)


def check_data_token(web3, token_address, abi=None):
	if abi is None:
		abi = get_erc20_abi()

	try:
		token_contract = web3.eth.contract(address=web3.to_checksum_address(token_address), abi=abi)
		decimals = token_contract.functions.decimals().call()
		symbol = token_contract.functions.symbol().call()

		if symbol == 'WETH':
			symbol = 'ETH'

		return token_contract, decimals, symbol

	except Exception as error:
		cprint(f'Error: {error}', 'red')


def check_allowance(web3, token_address, wallet, spender):
	try:
		contract = web3.eth.contract(address=web3.to_checksum_address(token_address), abi=get_erc20_abi())
		amount_approved = contract.functions.allowance(wallet, spender).call()

		return amount_approved

	except Exception as error:
		cprint(f'Error: {error}', 'red')


def get_token_balance(web3, wallet_address, contract_address='', balance_round=False):
	try:
		if contract_address in ['', NATIVE_TOKEN_ADDRESS, NULL_TOKEN_ADDRESS]:
			balance = web3.eth.get_balance(web3.to_checksum_address(wallet_address))
			token_decimal = 18
		else:
			token_contract, token_decimal, symbol = check_data_token(web3, contract_address)
			balance = token_contract.functions.balanceOf(web3.to_checksum_address(wallet_address)).call()

		if balance_round:
			wei = wei_to_int(balance, token_decimal)
			# float number
			decimal_places = 8
			factor = 10 ** decimal_places
			rounded_number = math.floor(wei * factor) / factor
			return rounded_number
		return int(balance)
	except Exception as error:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		cprint(f'{STR_CANCEL} {exc_type}: {str(error)}. {exc_tb.tb_frame.f_code.co_filename}, line: {exc_tb.tb_lineno}',
			   'red')
		time.sleep(10)
		return get_token_balance(web3, wallet_address, contract_address='', balance_round=False)


def get_token_symbol(web3, chain, contract_address=''):
	if contract_address == '':
		return CHAINS[chain]["token"]
	else:
		token_contract, token_decimal, symbol = check_data_token(web3, contract_address)
		return symbol


def check_wait_web3_balance(web3_provider, chain, wallet_address, token, amount):
	if CHECK_GWEI:
		wait_gas()

	while True:
		cprint(f"/-- Check {chain} wallet balance: {wallet_address} ({amount})", "blue")
		balance = get_token_balance(web3_provider, wallet_address, token, True)
		if balance >= amount:
			cprint(f"/-- {balance} found", "green")
			time.sleep(5)
			return balance

		sleeping(MIN_SLEEP, MAX_SLEEP)
		continue


def get_web3(url, proxy=None):
	if proxy:
		logger.info(f"Use proxy {proxy['http']}")

		return Web3(Web3.HTTPProvider(
			url,
			request_kwargs={"proxies": proxy}
		))
	else:
		return Web3(Web3.HTTPProvider(url))


def get_erc20_abi():
	with open("config/abi/erc20.json", "r") as file:
		erc20_abi = json.load(file)
	return erc20_abi


def get_erc1155_abi():
	with open("config/abi/erc1155.json", "r") as file:
		abi = json.load(file)
	return abi


def get_erc721_abi():
	with open("config/abi/erc721.json", "r") as file:
		abi = json.load(file)
	return abi


def get_gas():
	web3 = Web3(Web3.HTTPProvider(CHAINS['ethereum']['rpc']))
	gas_price = web3.eth.gas_price
	gwei_gas_price = web3.from_wei(gas_price, 'gwei')

	return gwei_gas_price


def wait_gas():
	while True:
		current_gas = get_gas()

		if current_gas > MAX_GWEI:
			logger.info(f'Сurrent_gas : {current_gas} > {MAX_GWEI}')
			time.sleep(100)
		else:
			break
