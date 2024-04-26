# How long sleep between tx
MIN_SLEEP = 10
MAX_SLEEP = 40

USE_PROXY = False
USE_SHUFFLE = True

CHECK_GWEI = True
MAX_GWEI = 32

# False or '2023-08-15 22:36' format
SCHEDULE_TIME = ''

# How many times should retry if tx failed
MAX_RETRIES = 2

UNUSED_REPEAT = 1
USE_CSV = True

MIN_BALANCE = {
	'ethereum': 0.01,
	'optimism': 0.0002,
	'bsc': 0.0002,
	'polygon': 0.01,
	'polygon_zkevm': '0.007-0.0075',
	'arbitrum': '0.0008-0.00085',
	'avalanche': 0.001,
	'fantom': 0.05,
	'nova': '0.005-0.0055',
	'zksync': '0.01-0.011',
	'coredao': 0.01,
	'moonriver': 0.00001,
	'metis': 0.00001,
	'linea': '0.005-0.0055',
	'zora': '0.005-0.0055',
	'base': '0.005-0.0055',
	'scroll': '0.01-0.0105',
	'degen': '0.1-0.11',
	'mode': '0.005-0.006',
	'blast': '0.005-0.006',
}

CHAINS = {
	'ethereum': {
		'rpc': 'https://ethereum-rpc.publicnode.com',
		'scan': 'https://etherscan.io/tx',
		'token': 'ETH',
		'chain_id': 1
	},
	'optimism': {
		'rpc': 'https://opt-mainnet.g.alchemy.com/v2/ZlBxXxXF5NNbl7kcRzvOs8V8XnRRhT3W',
		'scan': 'https://optimistic.etherscan.io/tx',
		'token': 'ETH',
		'chain_id': 10
	},
	'bsc': {
		'rpc': 'https://rpc.ankr.com/bsc/5324a45ea14743aaaa0f04a9d0b1edf96196bf36f2985f3c51369cf43f948dde',
		'scan': 'https://bscscan.com/tx',
		'token': 'BNB',
		'chain_id': 56
	},
	'polygon': {
		'rpc': 'https://polygon.blockpi.network/v1/rpc/public',
		'scan': 'https://polygonscan.com/tx',
		'token': 'MATIC',
		'chain_id': 137
	},
	'polygon_zkevm': {
		'rpc': 'https://polygonzkevm-mainnet.g.alchemy.com/v2/8oc0GKbOQRG0--LcTd_1QUkaNUjWqIoU',
		'scan': 'https://zkevm.polygonscan.com/tx',
		'token': 'ETH',
		'chain_id': 1101
	},
	'arbitrum': {
		'rpc': 'https://rpc.ankr.com/arbitrum',
		'scan': 'https://arbiscan.io/tx',
		'token': 'ETH',
		'chain_id': 42161
	},
	'avalanche': {
		'rpc': 'https://avalanche-c-chain.publicnode.com',
		'scan': 'https://snowtrace.io/tx',
		'token': 'AVAX',
		'chain_id': 43114
	},
	'fantom': {
		'rpc': 'https://fantom.publicnode.com',
		'scan': 'https://ftmscan.com/tx',
		'token': 'FTM',
		'chain_id': 250
	},
	'nova': {
		'rpc': 'https://arbitrum-nova.public.blastapi.io',
		'scan': 'https://nova.arbiscan.io/tx',
		'token': 'ETH',
		'chain_id': 42170
	},
	'zksync': {
		'rpc': 'https://zksync.meowrpc.com',
		'scan': 'https://explorer.zksync.io/tx',
		'token': 'ETH',
		'chain_id': 324
	},
	'moonbeam': {
		'rpc': 'https://moonbeam.api.onfinality.io/public',
		'scan': 'https://moonscan.io/tx',
		'token': 'GLMR',
		'chain_id': 1284
	},
	'moonriver': {
		'rpc': 'https://moonriver.public.blastapi.io',
		'scan': 'https://moonriver.moonscan.io/tx',
		'token': 'MOVR',
		'chain_id': 1285
	},
	'metis': {
		'rpc': 'https://andromeda.metis.io/?owner=1088',
		'scan': 'https://andromeda-explorer.metis.io/tx',
		'token': 'METIS',
		'chain_id': 1088
	},
	'harmony': {
		'rpc': 'https://a.api.s0.t.hmny.io',
		'scan': 'https://explorer.harmony.one/tx',
		'token': 'ONE',
		'chain_id': 1666600000
	},
	'coredao': {
		'rpc': 'https://rpc.coredao.org',
		'scan': 'https://scan.coredao.org/tx',
		'token': 'CORE',
		'chain_id': 1116
	},
	'gnosis': {
		'rpc': 'https://rpc.ankr.com/gnosis',
		'scan': 'https://gnosisscan.io/tx',
		'token': 'xDAI',
		'chain_id': 100
	},
	'celo': {
		'rpc': 'https://forno.celo.org',
		'scan': 'https://celoscan.io/tx',
		'token': 'CELO',
		'chain_id': 42220
	},
	'kava': {
		'rpc': 'https://evm.kava.io',
		'scan': 'https://explorer.kava.io/tx',
		'token': 'KAVA',
		'chain_id': 2222
	},
	'okx': {
		'rpc': 'https://exchainrpc.okex.org',
		'scan': 'https://www.okx.com/ru/explorer/oktc/tx',
		'token': 'OKT',
		'chain_id': 66
	},
	'klaytn': {
		'rpc': 'https://klaytn.blockpi.network/v1/rpc/public',
		'scan': 'https://scope.klaytn.com/tx',
		'token': 'KLAY'
	},
	'fuse': {
		'rpc': 'https://rpc.fuse.io',
		'scan': 'https://explorer.fuse.io/tx',
		'token': 'FUSE'
	},
	'linea': {
		'rpc': 'https://linea-mainnet.infura.io/v3/7064390927dd49ebbf576d876293842d',
		'scan': 'https://lineascan.build/tx',
		'token': 'ETH',
		'chain_id': 59144
	},
	'base': {
		'rpc': 'https://mainnet.base.org',
		'scan': 'https://basescan.org/tx',
		'token': 'ETH',
		'chain_id': 8453
	},
	'scroll': {
		'rpc': 'https://rpc.ankr.com/scroll/7bb32945254fe5721c5e8957c67779b637a8278acb4e51c340abef7b92c138ca',
		'scan': 'https://scrollscan.com/tx',
		'token': 'ETH',
		'chain_id': 534352
	},
	'manta': {
		'rpc': 'https://1rpc.io/manta',
		'scan': 'https://manta.socialscan.io/tx',
		'token': 'ETH',
		'chain_id': 169
	},
	'mantle': {
		'rpc': 'https://rpc.mantle.xyz',
		'scan': 'https://explorer.mantle.xyz/tx',
		'token': 'MNT',
		'chain_id': 5000
	},
	'telos': {
		'rpc': 'https://mainnet.telos.net/evm',
		'scan': 'https://rpc.scroll.io/tx',
		'token': 'TLOS',
		'chain_id': 40
	},
	'zora': {
		'rpc': 'https://rpc.zora.energy',
		'scan': 'https://explorer.zora.energy/tx',
		'token': 'ETH',
		'chain_id': 7777777
	},
	'loot': {
		'rpc': 'https://rpc.lootchain.com/http',
		'scan': 'https://rpc.scroll.io/tx',
		'token': 'AGLD',
		'chain_id': 5151706
	},
	'conflux': {
		'rpc': 'https://evm.confluxrpc.com',
		'scan': 'https://evm.confluxscan.net/tx',
		'token': 'CFX',
		'chain_id': 1030
	},
	'astar': {
		'rpc': 'https://evm.astar.network',
		'scan': 'https://astar.subscan.io/tx',
		'token': 'ASTR',
		'chain_id': 592
	},
	'canto': {
		'rpc': 'https://canto.gravitychain.io',
		'scan': 'https://astar.subscan.io/tx',
		'token': 'CANTO',
		'chain_id': 7700
	},
	'degen': {
		'rpc': 'https://rpc.degen.tips',
		'scan': 'https://explorer.degen.tips/tx',
		'token': 'DEGEN',
		'chain_id': 666666666
	},
	'mode': {
		'rpc': 'https://mainnet.mode.network',
		'scan': 'https://modescan.io/tx',
		'token': 'ETH',
		'chain_id': 4443
	},
	'blast': {
		'rpc': 'https://rpc.ankr.com/blast',
		'scan': 'https://blastscan.io/tx',
		'token': 'ETH',
		'chain_id': 81457
	},
}

TESTNET_CHAINS = {
	'goerly': {
		'rpc': 'https://eth-goerli.g.alchemy.com/v2/Ubjli4dGwpq7pYiUhVLDGjgrHizGlGZt',
		'scan': 'https://goerli.etherscan.io/tx',
		'token': 'ETH'
	},
	'bsc_testnet': {
		'rpc': 'https://bsc-testnet.publicnode.com',
		'scan': 'https://testnet.bscscan.com/tx',
		'token': 'tBNB'
	},
	'opbnb_testnet': {
		'rpc': 'https://opbnb-testnet-rpc.bnbchain.org',
		'scan': 'https://opbnbscan.com/tx',
		'token': 'tBNB'
	},
}

CURRENCY_MAP = {
	1: 'wei',
	3: 'kwei',
	6: 'mwei',
	9: 'gwei',
	12: 'micro',
	15: 'milli',
	18: 'ether'
}

NATIVE_TOKEN_ADDRESS = '0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE'
NULL_TOKEN_ADDRESS = '0x0000000000000000000000000000000000000000'
ONE_TOKEN_ADDRESS = '0x0000000000000000000000000000000000000001'

STR_DONE = '✅ '
STR_CANCEL = '❌ '
ABI_ERC721 = '[{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"mint","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint16","name":"dstChainId","type":"uint16"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"crossChain","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"approved","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"constant":true,"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"}]'
