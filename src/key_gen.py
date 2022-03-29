"""
"""


import secrets


def generate_private_key(rand_data):
    """
    Generates a cryptographic private key.
    """

    bits = secrets.randbits(256)
    bits_hex = hex(bits)
    private_key = bits_hex[2:]

    print("NEW PRIVATE KEY GENERATED")

    return private_key


def generate_public_key(private_key):
    """
    Generates a cryptographic public key using the previously generated private key.
    This public key also doubles as a sender wallet.
    """


def generate_recipient_wallet(public_key):
    """
    Generates a recipient wallet using the previously generated public key.
    """


def file_setup():
    """
    """


if __name__ == "__main__":  # testing block
    file_setup()