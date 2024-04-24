from termcolor import cprint
from modules.balance.module import interface_check_balance

from modules.unused_contracts.module import run_unused_fn

if __name__ == '__main__':
    try:
        while True:
            cprint(f'Select an action:', 'yellow')
            cprint(f'0. Exit', 'yellow')
            cprint(f'1. Check Balances', 'yellow')

            cprint(f'-------- Unused NFT Contract --------', 'blue')
            cprint(f'2. Arbitrum Nova', 'yellow')
            cprint(f'3. Base', 'yellow')
            cprint(f'4. Blast', 'yellow')
            cprint(f'5. Scroll', 'yellow')
            cprint(f'6. Zora', 'yellow')
            cprint(f'7. ZkSync Era', 'yellow')
            cprint(f'8. Mode', 'yellow')
            cprint(f'9. Polygon zkEVM: mint random NFT', 'yellow')
            cprint(f'10. Ethereum', 'yellow')

            cprint(f'-------- Special NFT Collections --------', 'blue')
            cprint(f'20. Zora official NFTs / zora.co', 'yellow')



            option = input("> ")

            if option == '0':
                cprint(f'Exit, bye bye.', 'green')
                break

            elif option == '1':
                interface_check_balance()
                break

            elif option == '2':
                run_unused_fn('nova')
                break

            elif option == '3':
                run_unused_fn('base')
                break

            elif option == '4':
                run_unused_fn('blast')
                break

            elif option == '5':
                run_unused_fn('scroll')
                break

            elif option == '6':
                run_unused_fn('zora')
                break

            elif option == '7':
                run_unused_fn('zksync')
                break

            elif option == '8':
                run_unused_fn('mode')
                break

            elif option == '9':
                # TODO: mint random NFT
                # run_unused_fn('polygon_zkevm')
                break

            elif option == '10':
                run_unused_fn('ethereum')
                break

            elif option == '20':
                # run_script(mint_origin_nft, 'scroll', 0, [])
                break

            else:
                cprint(f'Wrong action. Please try again.\n', 'red')
                continue



    except KeyboardInterrupt:
        cprint(f' Exit, bye bye\n', 'red')
        raise SystemExit
