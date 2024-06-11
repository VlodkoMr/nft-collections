from helpers.web3_helper import *
from helpers.functions import int_to_wei, wei_to_int, get_min_balance
from modules.stargate_v2_bridge.config import *


def stargate_v2_eth_bridge(web3, private_key, _amount, from_chain, to_chain):
	wallet_address = web3.eth.account.from_key(private_key).address

	fee_contract_address = web3.to_checksum_address(STARGATE_V2_FEE_CONTRACTS[from_chain])
	bridge_contract_address = web3.to_checksum_address(STARGATE_V2_BRIDGE_CONTRACTS[from_chain])
	fee_contract = web3.eth.contract(address=fee_contract_address, abi=ABI_STARGATE_V2_FEE)
	bridge_contract = web3.eth.contract(address=bridge_contract_address, abi=ABI_STARGATE_V2_BRIDGE)

	cprint(f'/-- Bridge by stargate {from_chain} => {to_chain}, wallet {wallet_address} -->', 'green')

	if _amount > 0:
		amount = int_to_wei(_amount, 18)
	else:
		balance = get_token_balance(web3, wallet_address, '')
		amount = balance - int_to_wei(get_min_balance(from_chain), 18)

	if amount:
		dst_chain_id = STARGATE_V2_ENDPOINT_IDS[to_chain]
		fees = fee_contract.functions.quoteRideBus(
			dst_chain_id, False
		).call()
		lz_fee = fees[0]
		print('LZ Fees:', wei_to_int(lz_fee, 18))

		amount -= lz_fee
		amount -= int_to_wei(0.0003, 18)

		data = (
			STARGATE_V2_ENDPOINT_IDS[to_chain],
			address_to_bytes32(wallet_address),
			amount,
			int(amount * (1 - STARGATE_V2_SLIPPAGE)),
			bytes(0),
			bytes(0),
			bytes([1])
		)

		contract_txn = bridge_contract.functions.send(
			data,
			fees,
			web3.to_checksum_address(wallet_address)
		).build_transaction(
			{
				'from': wallet_address,
				'nonce': web3.eth.get_transaction_count(wallet_address),
				'value': amount + lz_fee,
				'gasPrice': 0,
				'gas': 0,
			}
		)

		contract_txn = add_gas_price(web3, contract_txn, from_chain)
		contract_txn = add_gas_limit(web3, contract_txn, from_chain)

		return sign_tx(web3, contract_txn, private_key)
	else:
		cprint(f'No token balance to bridge, skip.', 'red')
		raise Exception(f'{from_chain} No token balance to bridge')


def address_to_bytes32(address):
	if address.startswith('0x'):
		address = address[2:]

	if len(address) != 40:
		raise ValueError("Invalid address length")

	address_int = int(address, 16)
	return address_int.to_bytes(32, byteorder='big')
