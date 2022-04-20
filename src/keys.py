"""
Generates and stores key and wallet data.
Handles two-way Fernet key encryption.
NEEP uses the same wallet key encryption structure as Bitcoin.

:author: Max Milazzo
"""


from cryptography.fernet import Fernet
from bitcoin import random_key, privkey_to_pubkey, pubkey_to_address, ecdsa_sign, ecdsa_verify
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




def get_private_key():
    """
    """

    with open(PRIVATE_WALLET_KEY_PATH, "r") as f:
        private_key = f.read()
    
    print("PRIVATE KEY RETRIEVED")

    return private_key


def get_public_key():
    """
    """

    with open(PUBLIC_WALLET_KEY_PATH, "r") as f:
        public_key = f.read()
    
    print("PUBLIC KEY RETRIEVED")

    return public_key


def get_wallet_address():
    """
    """

    with open(RECIPIENT_WALLET_ADDRESS_PATH, "r") as f:
        wallet_address = f.read()
    
    print("WALLET ADDRESS RETRIEVED")

    return wallet_address



def private_key_encrypt(data):
    """
    """

    encrypted_data = ecdsa_sign(data, get_private_key())

    print("DATA ENCRYPTED WITH PRIVATE KEY")

    return encrypted_data


def verify_key_encryption(data, encrypted_data, public_key):
    """
    """

    print("VERIFYING MESSAGE ENCRYPTION")

    is_valid = ecdsa_verify(data, encrypted_data, public_key)

    if is_valid:
        print("KEY ENCRYPTION VALID")
    else:
        print("KEY ENCRYPTION IS NOT VALID")

    return is_valid


def get_fernet_key():
    """
    Generates a two-way Fernet encryption key.

    :return: Fernet key
    :rtype: byte str
    """

    key = Fernet.generate_key()

    print("TWO-WAY FERNET KEY GENERATED")

    return key


def fernet_encrypt_text(key, text):
    """
    Encrypts text using Fernet two-way encryption.

    :param key: Fernet key
    :param text: text to be encrypted
    :type key: byte str
    :type text: str
    :return: encrypted text
    :rtype: byte str
    """

    encrypted_text = Fernet(key).encrypt(text)

    print("TEXT ENCRYPTED WITH FERNET KEY")

    return encrypted_text


def fernet_key_encrypt(text):
    """
    Handles Fernet encryption.

    :param text: text to be encrypted
    :type text: str
    :return: Fernet key, encrypted text
    :rtype: str, str
    """

    key = get_fernet_key()

    encrypted_text = fernet_encrypt_text(key, text.encode())

    return key.decode(), encrypted_text.decode()


def fernet_key_decrypt(key, encrypted_text):
    """
    Handles Fernet decryption.

    :param key: Fernet key
    :param encrypted_text: encrypted text
    :type key: str
    :type encrypted_text: str
    """

    decrypted_text = Fernet(key.encode()).decrypt(encrypted_text.encode())

    print("TEXT DECRYPTED WITH FERNET KEY")

    return decrypted_text.decode()


if __name__ == "__main__":  # testing block
    file_setup()

    key, encrypted_text = fernet_key_encrypt("Hello World!")

    print("\nkey: " + key)
    print("encrypted text: " + encrypted_text + "\n")
    print("\ndecoded text: " + fernet_key_decrypt(key, encrypted_text))