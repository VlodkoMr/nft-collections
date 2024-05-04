from termcolor import cprint
from modules.balance.module import interface_check_balance
from modules.last_tx.module import interface_last_tx
from modules.relay_bridge.module import interface_relay_bridge
from modules.unused_contracts.config import UNUSED_CONTRACTS
from modules.unused_contracts.functions import mint_random_nft

from modules.unused_contracts.module import run_unused_fn

if __name__ == '__main__':
	try:
		while True:
			cprint(f'Select an action:', 'yellow')
			cprint(f'0. Exit', 'yellow')
			cprint(f'1. Check balances & transactions', 'yellow')
			cprint(f'2. Check last transaction date', 'yellow')

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
			cprint(f'14. Polygon zkEVM: random NFT', 'yellow')

			cprint(f'-------- Special NFT Collections --------', 'blue')
			cprint(f'20. Zora official NFTs / zora.co', 'yellow')

			cprint(f'-------- Tokens / Bridge --------', 'blue')
			cprint(f'30. Relay Bridge', 'yellow')

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

			elif option == '20':
				# run_script(mint_origin_nft, 'scroll', 0, [])
				break

			elif option == '21':

				break

			elif option == '30':
				interface_relay_bridge()
				break

			else:
				cprint(f'Wrong action. Please try again.\n', 'red')
				continue



	except KeyboardInterrupt:
		cprint(f' Exit, bye bye\n', 'red')
		raise SystemExit
