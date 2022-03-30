"""
Generates and stores key and wallet data.
NEEP uses the same key encryption structure as Bitcoin.

:author: Max Milazzo
"""


from bitcoin import random_key, privkey_to_pubkey, pubkey_to_address
from data_access import PRIVATE_WALLET_KEY_PATH, PUBLIC_WALLET_KEY_PATH, RECIPIENT_WALLET_ADDRESS_PATH


def generate_private_key():
    """
    Generates a cryptographic private key.

    :return: random private key
    :rtype:
    """

    key = random_key()

    print("PRIVATE CRYPTOGRAPHIC KEY GENERATED")

    return key


def generate_public_key(private_key):
    """
    Generates a cryptographic public key using the previously generated private key.
    This public key also doubles as a sender wallet.

    :
    """

    key = privkey_to_pubkey(private_key)

    print("PUBLIC CRYPTOGRAPHIC KEY GENERATED")

    return key


def generate_recipient_wallet(public_key):
    """
    Generates a recipient wallet using the previously generated public key.
    """

    address = pubkey_to_address(public_key)

    print("RECIPIENT WALLET ADDRESS GENERATED")

    return address


def file_setup():
    """
    """

    private_key = generate_private_key()
    public_key = generate_public_key(private_key)
    wallet_address = generate_recipient_wallet(public_key)

    with open(PRIVATE_WALLET_KEY_PATH, "w") as f:
        f.write(private_key)
    
    with open(PUBLIC_WALLET_KEY_PATH, "w") as f:
        f.write(public_key)

    with open(RECIPIENT_WALLET_ADDRESS_PATH, "w") as f:
        f.write(wallet_address)
    
    print("KEY FILE DATA UPDATED")


if __name__ == "__main__":  # testing block
    file_setup()