from helpers.cli import *
from helpers.factory import run_script
from modules.stargate_v2_bridge.config import STARGATE_V2_FEE_CONTRACTS
from modules.stargate_v2_bridge.functions import stargate_v2_eth_bridge


def interface_stargate_bridge():
	available_chains = list(STARGATE_V2_FEE_CONTRACTS.keys())
	disabled_chains = [key for key in CHAINS.keys() if key not in available_chains]

	from_network = print_input_network("From network", disabled_chains)
	to_network = print_input_network("To network", disabled_chains)
	amount_str = print_input_amounts_range()

	params = [from_network, to_network]
	run_script(stargate_v2_eth_bridge, from_network, amount_str, params)
