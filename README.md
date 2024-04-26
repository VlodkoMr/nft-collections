# NFT Contracts

Increasing activity in various blockchains - cheap NFT transactions.
Analyze existing contracts, mint NFT, claim limited collections and bridge tokens.

For mint NFT on Ethereum you can set MAX_GWEI and wait for the transaction to be confirmed.

### Requirements:

- python 3.10+

### Install:

``` 
python3 -m venv venv
source venv/bin/activate
pip3 install wheel
pip3 install -r requirements.txt
```

#### Copy config:

``` 
cp config_sample config
```

### Usage:

``` 
source venv/bin/activate
python3 main.py
```