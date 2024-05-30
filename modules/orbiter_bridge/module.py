from helpers.cli import *
from modules.orbiter_bridge.config import ORBITER_AMOUNT
from modules.orbiter_bridge.functions import orbiter_eth_bridge
from helpers.factory import run_script


def interface_orbiter_bridge():
	chains = list(ORBITER_AMOUNT.keys())

	from_network = print_input_network_list("From network", chains)
	to_network = print_input_network_list("To network", chains)
	# token_address = print_input_contract_address("Token address")
	amount_str = print_input_amounts_range('Bridge ETH Amount')

	params = [from_network, to_network]
	run_script(orbiter_eth_bridge, from_network, amount_str, params)
