import random
from web3 import Web3
from config.settings import *
from helpers.cli import get_int_in_range
from helpers.factory import run_script
from helpers.functions import api_call, sleeping
from helpers.settings_helper import get_private_keys
from helpers.web3_helper import get_web3
from loguru import logger

from modules.unused_contracts.config import UNUSED_CONTRACTS, API_URL, API_KEYS


class ApiService:
	def __init__(self, chain: str, address: str):
		self.chain = chain
		self.address = address

	def get_api_url(self) -> str:
		if self.chain in ['base', 'degen']:
			return f'{API_URL[self.chain]}/{self.address}/transactions'
		elif self.chain == 'polygon_zkevm':
			return f'{API_URL[self.chain]}/{self.address}/transactions_v3/'
		else:
			return API_URL[self.chain]

	def request_params(self) -> dict:
		if self.chain == 'zksync':
			return {
				'address': self.address,
				'limit': 100,
			}
		elif self.chain in ['base', 'degen']:
			return {
				'filter': 'from',
			}
		else:
			return {
				'module': 'account',
				'action': 'txlist',
				'address': self.address,
				'startblock': 0,
				'endblock': 99999999,
				'page': 1,
				'offset': 200,
				'apikey': API_KEYS[self.chain],
			}

	def parse_response_to(self, response) -> set:
		result = set()
		if self.chain == 'zksync':
			for tx in response['items']:
				if tx.get('to'):
					result.add(Web3.to_checksum_address(tx['to']))
		elif self.chain in ['base', 'degen']:
			for tx in response['items']:
				if tx.get('to').get('hash'):
					result.add(Web3.to_checksum_address(tx['to']['hash']))
		else:
			for tx in response['result']:
				if tx.get('to'):
					result.add(Web3.to_checksum_address(tx['to']))
		return result


def run_unused_fn(rpc_chain):
	prt_keys = get_private_keys()
	web3 = get_web3(CHAINS[rpc_chain]['rpc'])
	all_contracts = UNUSED_CONTRACTS[rpc_chain]

	if USE_SHUFFLE:
		random.shuffle(prt_keys)

	for key in prt_keys:
		address = web3.eth.account.from_key(key['private_key']).address
		logger.info(f'Start on {address}')

		api_service = ApiService(rpc_chain, address)
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
