import sys
import traceback
import random
import time

from datetime import datetime
from termcolor import cprint
from config.settings import *
from helpers.cli import get_amount_in_range
from helpers.csv_helper import start_csv, write_csv_error
from helpers.functions import sleeping, wait_schedule
from helpers.settings_helper import get_private_keys
from helpers.web3_helper import get_web3, check_status_tx, wait_gas
from loguru import logger

logger.remove()
logger.add(sys.stderr,
		   format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level:<8}</level>| <level>{message}</level>")


def call_function(item, method, rpc_chain, _amount, params=[], csv='', retry=0):
	if CHECK_GWEI:
		wait_gas()

	web3 = get_web3(CHAINS[rpc_chain]['rpc'], item['proxy'])
	amount = get_amount_in_range(_amount)
	address = web3.eth.account.from_key(item['private_key']).address
	current_datetime = datetime.now()
	formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
	csv_name = method.__name__

	if csv != '':
		csv_name = csv

	try:
		logger.info(f'[{item["index"]}][{address}] | {method.__name__}')

		tx_hash = method(web3, item['private_key'], amount, *params)
		tx_link = f'{CHAINS[rpc_chain]["scan"]}/{tx_hash}'
		time.sleep(2)
		status = check_status_tx(web3, rpc_chain, tx_hash)
		if status == 1:
			logger.success(f'{STR_DONE} {rpc_chain} transaction: {tx_link}')
			return True
		else:
			raise Exception(f'{rpc_chain} transaction failed: {tx_link}')
	except Exception as error:
		if retry < MAX_RETRIES:
			cprint(f'Error: {error}, retry...', 'red')
			time.sleep(3)
			call_function(item, method, rpc_chain, _amount, params, csv, retry + 1)
		else:
			exc_type, exc_value, exc_traceback = sys.exc_info()

			traceback_details = traceback.format_exception(exc_type, exc_value, exc_traceback)
			full_track_error = "".join(traceback_details)
			logger.error(full_track_error)

			write_csv_error(csv_name, [address, item['private_key'], method.__name__, params, full_track_error, formatted_datetime])


def run_script(method, rpc_chain, _amount, params=[], specific_prt={}):
	if SCHEDULE_TIME:
		wait_schedule(SCHEDULE_TIME)

	csv_name = method.__name__
	start_csv(csv_name)

	prt_keys = get_private_keys()

	# Filter by specific keys
	if specific_prt:
		prt_keys = [specific_prt]

	if USE_SHUFFLE:
		random.shuffle(prt_keys)

	for item in prt_keys:
		call_function(item, method, rpc_chain, _amount, params)
		sleeping(MIN_SLEEP, MAX_SLEEP)
