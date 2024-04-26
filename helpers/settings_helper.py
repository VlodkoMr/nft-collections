import csv
import random
from termcolor import cprint
from config.settings import USE_PROXY
from helpers.csv_helper import get_csv_separator


def get_private_keys():
	with open('config/wallets.csv', newline='') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=get_csv_separator())
		private_keys = [row['private_key'].strip() for row in reader if row['private_key'].strip()]
		account_proxy = None
		if USE_PROXY:
			proxy = get_proxy_list()
			account_proxy = {key: proxy[i % len(proxy)] for i, key in enumerate(private_keys)}

		privates = []

		for index, prt in enumerate(private_keys):
			obj = {
				'private_key': prt.strip(),
				'index': index,
				'proxy': None

			}
			if account_proxy:
				obj['proxy'] = {
					'http': account_proxy[prt],
					'https': account_proxy[prt],
				}
			privates.append(obj)

	if len(privates) == 0:
		cprint("No private keys found in wallets.csv", "red")
	return privates


def get_proxy_list():
	with open("config/proxies.txt", "r") as f:
		recipients = [row.strip() for row in f]
	if len(recipients) == 0:
		cprint("No proxy found in config/proxies.txt", "red")
	return recipients


def get_random_proxy():
	proxies = {}
	proxy_list = get_proxy_list()
	if len(proxy_list) > 0:
		proxy = random.choice(proxy_list)
		proxies = {
			'http': proxy,
			'https': proxy,
		}

	return proxies
