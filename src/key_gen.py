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
    :rtype: str
    """

    key = random_key()

    print("PRIVATE CRYPTOGRAPHIC KEY GENERATED")

    return key


def generate_public_key(private_key):
    """
    Generates a cryptographic public key using the previously generated private key.
    This public key also doubles as a sender wallet.

    :param private_key: previously generated private key
    :type private_key: str
    :return: generated private key
    :rtype: str
    """

    key = privkey_to_pubkey(private_key)

    print("PUBLIC CRYPTOGRAPHIC KEY GENERATED")

    return key


def generate_recipient_wallet(public_key):
    """
    Generates a recipient wallet using the previously generated public key.

    :param public_key: previously generated public key
    :type public_key: str
    :return: generated recipient wallet address
    :rtype: str
    """

    address = pubkey_to_address(public_key)

    print("RECIPIENT WALLET ADDRESS GENERATED")

    return address


def file_setup():
    """
    Configures user key data files.
    """

    private_key = generate_private_key()
    public_key = generate_public_key(private_key)
    wallet_address = generate_recipient_wallet(public_key)
    # generates data

    with open(PRIVATE_WALLET_KEY_PATH, "w") as f:  # stores private key
        f.write(private_key)
    
    with open(PUBLIC_WALLET_KEY_PATH, "w") as f:  # stores public key
        f.write(public_key)

    with open(RECIPIENT_WALLET_ADDRESS_PATH, "w") as f:  # stores recipient walley address
        f.write(wallet_address)
    
    print("KEY FILE DATA UPDATED")


if __name__ == "__main__":  # testing block
    file_setup()