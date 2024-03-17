from bitcoinlib.services.services import Service

def check_btc_transactions(address):
    service = Service()
    transactions = service.gettransactions(address)
    if transactions:
        return True
    else:
        return False

# Example Bitcoin address
btc_address = "15Zpz6hJkSkAiw1A5Sm9UoemCVBCuW1SSP"

# Check if the address has made transactions
has_transactions = check_btc_transactions(btc_address)
print(has_transactions)