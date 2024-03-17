from mnemonic import Mnemonic
import bip32utils
from check import check_btc_transactions

mnemo = Mnemonic('english')

while True:
    words = mnemo.generate(strength=256)
    seed = mnemo.to_seed(words, passphrase="")
    #words = mnemon.generate(256)
    ##print(words)
    #mnemon.check(words)
    #seed = mnemon.to_seed(words)
    #seed = mnemon.to_seed(b'lucky labor rally law toss orange weasel try surge meadow type crumble proud slide century')
    
    ###print(f'BIP39 Seed: {seed.hex()}\n')

    root_key = bip32utils.BIP32Key.fromEntropy(seed)
    root_address = root_key.Address()
    root_public_hex = root_key.PublicKey().hex()
    root_private_wif = root_key.WalletImportFormat()
    ##print('Root key:')
    print(f'\tAddress: {root_address}')
    ##print(f'\tPublic : {root_public_hex}')
    ##print(f'\tPrivate: {root_private_wif}\n')

    ##child_key = root_key.ChildKey(0).ChildKey(0)
    ##child_address = child_key.Address()
    ##child_public_hex = child_key.PublicKey().hex()
    ##child_private_wif = child_key.WalletImportFormat()
    ##print('Child key m/0/0:')
    ##print(f'\tAddress: {child_address}')
    ##print(f'\tPublic : {child_public_hex}')
    ##print(f'\tPrivate: {child_private_wif}\n')

    btc_address=root_address
    if check_btc_transactions(btc_address)==True:
        print('Ok')
        with open("log.txt", "a") as f:
            f.write(f"\nMnemonic words: {words}\nBIP39 Seed: {seed.hex()}\nAddress: {btc_address}\n\n")
    else:
        print('vuoto')


    #print(has_transactions)