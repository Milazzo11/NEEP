"""
"""


from keys import get_public_key, private_key_encrypt
from data_access import PUBLIC_WALLET_KEY_PATH
from uuid import uuid4


def make_transaction_package(wallet, amount):
    """
    """

    public_key = get_public_key()

    data_string = '"public_key":"' + public_key + '","wallet":"' + wallet + '","amount":' + str(amount)
    data_id = uuid4().hex
    encrypted_data = private_key_encrypt(data_string)
    
    return '{"id":"' + data_id + '","type":"transaction","data":{' + data_string + '},"encryption":"' + encrypted_data + '"}'


if __name__ == "__main__":  # testing block
    print(make_transaction_package("15bnjBxdTHTZnN2fR1XKmvUak6RB8DYq79", 500))