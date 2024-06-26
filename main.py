from termcolor import cprint

from config.settings import CHAINS, MIN_SLEEP, MAX_SLEEP
from helpers.functions import sleeping
from helpers.settings_helper import get_private_keys
from helpers.web3_helper import get_web3
from modules.balance.module import interface_check_balance
from modules.filter_tx.module import interface_last_tx, interface_tx_count
from modules.orbiter_bridge.functions import claim_points
from modules.orbiter_bridge.module import interface_orbiter_bridge
from modules.relay_bridge.module import interface_relay_bridge
from modules.stargate_v2_bridge.module import interface_stargate_bridge
from modules.unused_contracts.config import UNUSED_CONTRACTS
from modules.unused_contracts.functions import mint_random_nft

from modules.unused_contracts.module import run_unused_fn
from modules.zora_official.module import zora_official_interface

if __name__ == '__main__':
	try:
		while True:
			cprint(f'Select an action:', 'yellow')
			cprint(f'0. Exit', 'yellow')
			cprint(f'1. Check balances', 'yellow')
			cprint(f'2. Filter wallets by last TX Date', 'yellow')
			cprint(f'3. Filter wallets by TX Count', 'yellow')

			cprint(f'-------- Unused NFT Contracts --------', 'blue')
			cprint(f'5. Arbitrum Nova', 'yellow')
			cprint(f'6. Base', 'yellow')
			cprint(f'7. Blast', 'yellow')
			cprint(f'8. Degen', 'yellow')
			cprint(f'9. Scroll', 'yellow')
			cprint(f'10. Ethereum', 'yellow')
			cprint(f'11. Zora', 'yellow')
			cprint(f'12. ZkSync Era', 'yellow')
			cprint(f'13. Mode', 'yellow')
			cprint(f'14. Polygon zkEVM (random NFT)', 'yellow')
			cprint(f'15. Taiko', 'yellow')

			cprint(f'-------- Special NFT Collections --------', 'blue')
			cprint(f'20. Zora official NFTs / zora.co', 'yellow')

			cprint(f'-------- Tokens / Bridge --------', 'blue')
			cprint(f'30. Relay Bridge', 'yellow')
			cprint(f'31. Orbiter Bridge - ETH bridge', 'yellow')
			cprint(f'32. Orbiter Bridge - claim points', 'yellow')
			cprint(f'33. Stargate v2 ETH Bridge', 'yellow')

			option = input("> ")

			if option == '0':
				cprint(f'Exit, bye bye.', 'green')
				break

			elif option == '1':
				interface_check_balance()
				break

			elif option == '2':
				interface_last_tx()
				break

			elif option == '3':
				interface_tx_count()
				break

			elif option == '5':
				run_unused_fn('nova')
				break

			elif option == '6':
				run_unused_fn('base')
				break

			elif option == '7':
				run_unused_fn('blast')
				break

			elif option == '8':
				run_unused_fn('degen')
				break

			elif option == '9':
				run_unused_fn('scroll')
				break

			elif option == '10':
				run_unused_fn('ethereum')
				break

			elif option == '11':
				run_unused_fn('zora')
				break

			elif option == '12':
				run_unused_fn('zksync')
				break

			elif option == '13':
				run_unused_fn('mode')
				break

			elif option == '14':
				chain = 'polygon_zkevm'
				mint_random_nft(chain, UNUSED_CONTRACTS[chain])
				break

			elif option == '15':
				run_unused_fn('taiko')
				break

			elif option == '20':
				zora_official_interface()
				break

			elif option == '21':

				break

			elif option == '30':
				interface_relay_bridge()
				break

			elif option == '31':
				interface_orbiter_bridge()
				break

			elif option == '32':
				prt_keys = get_private_keys()
				web3 = get_web3(CHAINS['zksync']['rpc'])

				for index, item in enumerate(prt_keys):
					account = web3.eth.account.from_key(item['private_key'])
					claim_points(index, account.address)
					sleeping(MIN_SLEEP, MAX_SLEEP)
				break

			elif option == '33':
				interface_stargate_bridge()
				break

			else:
				cprint(f'Wrong action. Please try again.\n', 'red')
				continue



	except KeyboardInterrupt:
		cprint(f' Exit, bye bye\n', 'red')
		raise SystemExit
