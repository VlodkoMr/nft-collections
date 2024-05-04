from web3 import Web3
from datetime import datetime, timezone
from modules.unused_contracts.config import API_URL, API_KEYS


class ApiService:
    def __init__(self, chain: str, address: str):
        self.chain = chain
        self.address = address

    def get_api_url(self) -> str:
        if self.chain in ['base', 'degen']:
            return f'{API_URL[self.chain]}/{self.address}/transactions'
        elif self.chain == 'polygon_zkevm':
            return f'{API_URL[self.chain]}/{self.address}/transactions_v3/'
        else:
            return API_URL[self.chain]

    def request_params(self) -> dict:
        if self.chain == 'zksync':
            return {
                'address': self.address,
                'limit': 100,
            }
        elif self.chain in ['base', 'degen']:
            return {
                'filter': 'from',
            }
        else:
            return {
                'module': 'account',
                'action': 'txlist',
                'address': self.address,
                'startblock': 0,
                'endblock': 99999999,
                'page': 1,
                'offset': 200,
                'sort': 'desc',
                'apikey': API_KEYS[self.chain],
            }

    def parse_response_to(self, response) -> set:
        result = set()

        if self.chain == 'zksync':
            for tx in response['items']:
                if tx.get('to'):
                    result.add(Web3.to_checksum_address(tx['to']))
        elif self.chain in ['base', 'degen']:
            for tx in response['items']:
                if tx.get('to').get('hash'):
                    result.add(Web3.to_checksum_address(tx['to']['hash']))
        else:
            for tx in response['result']:
                if tx.get('to'):
                    result.add(Web3.to_checksum_address(tx['to']))
        return result

    def parse_response_timestamp(self, response) -> int:
        if self.chain == 'zksync':
            if response.get('items') and len(response['items']) > 0:
                item = response['items'][0]
                dt = datetime.fromisoformat(item['receivedAt'].rstrip('Z')).replace(tzinfo=timezone.utc)
                return int(dt.timestamp())

        elif self.chain in ['base', 'degen']:
            if response.get('items') and len(response['items']) > 0:
                item = response['items'][0]
                dt = datetime.fromisoformat(item['timestamp'].rstrip('Z')).replace(tzinfo=timezone.utc)
                return int(dt.timestamp())

        else:
            if response.get('result') and len(response['result']) > 0:
                item = response['result'][0]
                return int(item['timeStamp'])
