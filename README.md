# BTC BIP39 Wallet Miner
Bitcoin BIP39 Wallet Miner written in Python.

## Requirements:
You should pip install the following packages:
- bitcoinlib
- mnemonic
- bip32utils

## How to use it:

Run gen.py. It will create a log.txt file when it finds a wallet which has transactions.

## How does it work?

This program will generate mnemonic phrases -> which will become seeds -> which will show us the root address (Base58 (P2PKH) address format).

After obtaining the root address, it will use the check.py function to check if that specific address ever did any transaction on the BTC blockchain.

If so, it will create a log.txt file and append the mnemonic phrase, the seed and the wallet address.
