from helpers.functions import int_to_wei
from helpers.web3_helper import add_gas_price, add_gas_limit, sign_tx


def mint_nfts2_me(web3, private_key, amount, chain_id, contract_address):
    from modules.unused_contracts.config import CONTRACT_PAYMENT

    wallet = web3.eth.account.from_key(private_key).address
    cprint(f'/-- Mint NFT, wallet {wallet} / nfts2me.com -->', 'green')

    if not amount:
        amount = CONTRACT_PAYMENT[chain_id].get(contract_address, 0.0002)

    amount = int_to_wei(amount, 18)
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


def mintfun_mint_nft(web3, private_key, amount, chain_id, contract_address, data):
    from modules.unused_contracts.config import CONTRACT_DATA

    wallet = web3.eth.account.from_key(private_key).address
    cprint(f'/-- Mint NFT, wallet {wallet} / mint.fun -->', 'green')

    data = CONTRACT_DATA[chain_id].get(contract_address, data)
    data = data.replace('__wallet__', wallet.replace('0x', ''))

    contract_txn = {
        'from': wallet,
        'nonce': web3.eth.get_transaction_count(wallet),
        'value': int_to_wei(amount, 18),
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
