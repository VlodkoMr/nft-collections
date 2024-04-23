from helpers.functions import int_to_wei
from helpers.web3_helper import add_gas_price, add_gas_limit, sign_tx


def mint_nfts2_me(web3, private_key, _amount, chain_id, contract_address):
    from modules.unused_contracts.config import CONTRACT_PAYMENT

    wallet = web3.eth.account.from_key(private_key).address
    cprint(f'/-- Mint NFT, wallet {wallet} / nfts2me.com -->', 'green')

    if not _amount:
        _amount = CONTRACT_PAYMENT[chain_id].get(contract_address, 0.0002)

    amount = int_to_wei(_amount, 18)
    contract_txn = {
        "chainId": web3.eth.chain_id,
        "from": wallet,
        "to": contract_address,
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


def zora_mintfun_nft(web3, private_key, _amount, chain_id, contract_address, data):
    wallet = web3.eth.account.from_key(private_key).address
    cprint(f'/-- Mint NFT, wallet {wallet} / mint.fun -->', 'green')

    data = data.replace('__wallet__', wallet.replace('0x', ''))

    contract_txn = {
        'from': wallet,
        'nonce': web3.eth.get_transaction_count(wallet),
        'value': int_to_wei(_amount, 18),
        'gasPrice': 0,
        'gas': 0,
        'to': contract_address,
        'data': data,
        'chainId': web3.eth.chain_id
    }

    contract_txn = add_gas_price(web3, contract_txn, chain_id)
    contract_txn = add_gas_limit(web3, contract_txn, chain_id)

    tx_hash = sign_tx(web3, contract_txn, private_key)
    return tx_hash

# def mint_origin_nft(web3, private_key, _amount=0):
#     chain = 'scroll'
#     address_contract = web3.to_checksum_address(NFT_ORIGINS_CONTRACT)
#     wallet = web3.eth.account.from_key(private_key).address
#     cprint(f'/-- Wallet {wallet} --> Mint Origin NFT', 'green')
#
#     params = {'address': wallet}
#     metadata, proof = origin_nft_request(params)
#
#     cprint(f'/-- Rarity {int(metadata.get("rarityData", 0), 16)} ', 'blue')
#
#     contract = web3.eth.contract(address=address_contract, abi=NFT_ORGINS_ABI)
#     contract_txn = contract.functions.mint(
#         wallet,
#         (
#             metadata.get("deployer"),
#             metadata.get("firstDeployedContract"),
#             metadata.get("bestDeployedContract"),
#             int(metadata.get("rarityData", 0), 16),
#         ),
#         proof
#
#     ).build_transaction(
#         {
#             'from': wallet,
#             'nonce': web3.eth.get_transaction_count(wallet),
#             'value': 0,
#             'gasPrice': 0,
#             'gas': 0,
#         }
#     )
#
#     contract_txn = add_gas_price(web3, contract_txn, chain)
#     contract_txn = add_gas_limit(web3, contract_txn, chain)
#     tx_hash = sign_tx(web3, contract_txn, private_key)
#     return tx_hash
#
#
# def origin_nft_request(params, retry=0):
#     proxies = get_random_proxy()
#     url = f"https://nft.scroll.io/p/{params['address']}.json"
#
#     response_req = requests.get(url=url, params=[], proxies=proxies)
#     if response_req.status_code == 200:
#         response = response_req.json()
#         if 'metadata' in response:
#             return response["metadata"], response["proof"]
#
#     if retry < MAX_RETRIES:
#         cprint(f'error: status code {response_req.status_code}, retry...', 'red')
#         return origin_nft_request(params, retry + 1)
#     else:
#         raise Exception(f'SKIP. Responce error')
#
#
# def generate_collection_name():
#     fake = Faker()
#     title = fake.word()
#     while len(title) > 15 or len(title) <= 5:
#         title = fake.word()
#
#     symbol = fake.word()
#     while len(symbol) > 6 or len(symbol) <= 3:
#         symbol = fake.word()
#
#     return title, symbol
#
#
# def create_omnisea_collection(web3, private_key, _amount=0):
#     chain = 'scroll'
#     address_contract = web3.to_checksum_address(OMNISEA_CONTRACT)
#     wallet = web3.eth.account.from_key(private_key).address
#     cprint(f'/-- Wallet {wallet} --> Create NFT collection on Omnisea', 'green')
#
#     title, symbol = generate_collection_name()
#
#     contract = web3.eth.contract(address=address_contract, abi=OMNISEA_ABI)
#     contract_txn = contract.functions.create([
#         title,
#         symbol,
#         "",
#         "",
#         0,
#         True,
#         0,
#         int(time.time()) + 1000000]
#     ).build_transaction(
#         {
#             'from': wallet,
#             'nonce': web3.eth.get_transaction_count(wallet),
#             'value': 0,
#             'gasPrice': 0,
#             'gas': 0,
#         }
#     )
#
#     contract_txn = add_gas_price(web3, contract_txn, chain)
#     contract_txn = add_gas_limit(web3, contract_txn, chain)
#     tx_hash = sign_tx(web3, contract_txn, private_key)
#     return tx_hash
