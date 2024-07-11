from termcolor import cprint

from helpers.factory import run_script
from modules.zora_official.functions import run_zora_official


def zora_official_interface():
	try:
		while True:
			cprint(f'Select an action:', 'yellow')
			cprint(f'0. Exit', 'yellow')
			cprint(f'1. Mint Random available NFT', 'yellow')
			cprint(f'NOTE: Price 0.000777 ETH/NFT for zora.co', 'blue')

			option = input("> ")
			chain = 'zora'

			if option == '0':
				cprint(f'Exit, bye bye.', 'green')
				break

			elif option == '1':
				params = [chain, '', '']
				run_script(run_zora_official, chain, "0.000777", params)
				break

			# elif option == '2':
				# params = [
				# 	chain,
				# 	'0xe67be3e7a65023299fc706a9f5fef134c2a76dfd',
				# 	'0x359f130200000000000000000000000004e2516a2c207e84a1839755675dfd8ef6302f0a0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000a000000000000000000000000000000000000000000000000000000000000000e000000000000000000000000000000000000000000000000000000000000000010000000000000000000000004de574a3335a1f5e390bfcf216ce12a3242488fa0000000000000000000000000000000000000000000000000000000000000020000000000000000000000000__wallet__'
				# ]
				# run_script(run_zora_official, chain, "0.000777", params)
				# break

			# elif option == '3':
				# params = [
				# 	chain,
				# 	'0xf70da97812cb96acdf810712aa562db8dfa3dbef',
				# 	'0x00c32222',
				# ]
				# run_script(run_zora_official, chain, "0.000812244552809031", params)
				# break

			else:
				cprint(f'Wrong action. Please try again.\n', 'red')
				continue
	except KeyboardInterrupt:
		cprint(f' Exit, bye bye\n', 'red')
		raise SystemExit

# network = 'zora'
# contract = '0xe67be3e7a65023299fc706a9f5fef134c2a76dfd'
# value = '0.000777'
# data = '0x359f130200000000000000000000000004e2516a2c207e84a1839755675dfd8ef6302f0a0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000a000000000000000000000000000000000000000000000000000000000000000e000000000000000000000000000000000000000000000000000000000000000010000000000000000000000004de574a3335a1f5e390bfcf216ce12a3242488fa0000000000000000000000000000000000000000000000000000000000000020000000000000000000000000__wallet__'
#
# cprint(f"/-- Run {network} transactions -->", "green")
#
# params = [
# 	network,
# 	contract,
# 	data
# ]
#
# run_script(run_zora_official, network, value, params)
