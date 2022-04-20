"""
Public and private data access and management module.
All project global constants are defined here as well.

:author: Max Milazzo
"""


import json_list as jlst


MAIN_BLOCKCHAIN_PATH = "data\\public\\main-blockchain.jlst"
UNVERIFIED_FINISHED_CODE_PATH = "data\\public\\unverified-finished-code.jlst"
SUBMISSIONS_MINER_CLAIMS_PATH = "data\\public\\submissions-miner-claims.jlst"
CODE_SUBMISSION_QUEUE_PATH = "data\\public\\code-submission-queue.jlst"
# public data file paths


PRIVATE_WALLET_KEY_PATH = "data\\keys\\private-wallet-key.txt"
PUBLIC_WALLET_KEY_PATH = "data\\keys\\public-wallet-key.txt"
RECIPIENT_WALLET_ADDRESS_PATH = "data\\keys\\recipient-wallet-address.txt"
IP_ADDRESS_PATH = "data\\ip.txt"
# personal data file paths


MIN_MINER_CLAIMS = 15
MAX_MINER_CLAIMS = 30
# miner claims count data


MAX_IP_CODE_SUBMISSIONS = 20
MINER_IP_CAP = MAX_IP_CODE_SUBMISSIONS
# maximum submissions and miners per IP address


MAX_CHECK_ITERATIONS = 600
MAX_OUTPUT_LENGTH = 10000
# submitted code execution constraints


def add_to_main_blockchain(data):
    """
    Wrapper function for JSON List module to add block to the main blockchain.

    :param: data to be added to the blockchain
    :type data: JSON str
    """

    jlst.add(MAIN_BLOCKCHAIN_PATH, data)
    
    print("MAIN BLOCKCHAIN DATA SUCCESSFULLY ADDED")


def get_from_main_blockchain():
    """
    Wrapper function for JSON List module to accesses most current block in the main blockchain.

    :return: block data, last line index
    :rtype: dict (JSON object), int
    """

    data, line_count = jlst.get_from_back(MAIN_BLOCKCHAIN_PATH)

    print("MAIN BLOCKCHAIN DATA PULL SUCCESSFUL")

    return data, line_count


def search_in_main_blockchain(json_elem, match, count):
    """
    Wrapper function for JSON List module to search blockchain by data in a specified JSON element.

    :param json_elem: JSON element ID location to search for data
    :param match: data to compare with JSON element data
    :param count: number of items to search for (-1 for no specified limit)
    :type json_elem: str
    :type match: str (if not of type str, will be converted to str)
    :type count: int
    :return: JSON object list, JSON object line indicies list
    :rtype: list, list
    """

    obj_list, index_list = jlst.get_by_match(MAIN_BLOCKCHAIN_PATH, json_elem, match, count)

    print("MAIN BLOCKCHAIN DATA SEARCH COMPLETE")

    return obj_list, index_list


def add_to_code_submission_queue(data):
    """
    Wrapper function for JSON List module to add code submission data to queue.

    :param: data to be added to the code submission queue
    :type data: JSON str
    """

    jlst.add(CODE_SUBMISSION_QUEUE_PATH, data)

    print("CODE SUBMISSION SUCCESSFULLY ADDED TO QUEUE")


def search_for_compatible_code_submission(id_compatibility):
    """
    Wrapper function for JSON List module to search for network compatible user code.

    :param id_compatibility: value to compare with JSON objects' "id" elements
    :type id_compatibility: int or str
    :return: compatible code submission data, submission data index
    :rtype: dict (JSON object), int
    """

    obj_list, index_list = jlst.get_by_match(CODE_SUBMISSION_QUEUE_PATH, "id", id_compatibility, 1)

    if obj_list is None:
        print("NO COMPATIBLE USER CODE FOUND")

        return None, None
    
    print("A COMPATIBLE USER CODE SUBMISSION HAS BEEN FOUND")

    return obj_list[0], index_list[0]


def count_code_submission_queue_ips(ip_value):
    """
    Wrapper function for JSON List module to count the number of a certain IP in the file.

    :param ip_value: IP value to check for
    :type ip_value: str
    :return: number of IP values found
    :rtype: int
    """

    obj_list, _ = jlst.get_by_match(CODE_SUBMISSION_QUEUE_PATH, "ip", ip_value, MAX_IP_CODE_SUBMISSIONS)

    count = len(obj_list)
    
    print(f"{count} MATCHING IP(s) FOUND IN CODE SUBMISSION QUEUE")

    return count


def remove_from_submission_queue_by_index(index):
    """
    Wrapper function for JSON List module to remove data at a specified index.

    :param index: line index of data to remove
    :type index: int
    """

    jlst.remove_index(CODE_SUBMISSION_QUEUE_PATH, [index])

    print(f"SUBMISSION QUEUE DATA AT INDEX {index} HAS BEEN REMOVED")


def remove_from_submission_queue_by_id(id_value):
    """
    Wrapper function for JSON List module to remove data with a specified "id" value.

    :param id_value: value of JSON "id" element for data to remove
    :param id_value: int or str
    """

    _, index_list = jlst.get_by_match(CODE_SUBMISSION_QUEUE_PATH, "id", id_value, 1)

    if index_list is None:
        print(f'NO SUBMISSION QUEUE DATA WITH ID VALUE "{id_value}"')

        return
    
    jlst.remove_index(CODE_SUBMISSION_QUEUE_PATH, index_list)

    print(f'REMOVED SUBMISSION QUEUE DATA WITH ID VALUE "{id_value}"')


def add_to_submissions_miner_claims(data):
    """
    Wrapper function for JSON List module to add submission miner claims.

    :param: data to be added to the submissions miner claims
    :type data: JSON str
    """

    jlst.add(SUBMISSIONS_MINER_CLAIMS_PATH, data)

    print("SUBMISSION MINER CLAIM SUCCESSFULLY ADDED")


def search_in_submission_miner_claims(json_elem, match, count):
    """
    Wrapper function for JSON List module to search submission miner claims by data in a specified JSON element.

    :param json_elem: JSON element ID location to search for data
    :param match: data to compare with JSON element data
    :param count: number of items to search for (-1 for no specified limit)
    :type json_elem: str
    :type match: str (if not of type str, will be converted to str)
    :type count: int
    :return: JSON object list, JSON object line indicies list
    :rtype: list, list
    """

    obj_list, index_list = jlst.get_by_match(SUBMISSIONS_MINER_CLAIMS_PATH, json_elem, match, count)

    print("SUBMISSION MINER CLAIMS DATA SEARCH COMPLETE")

    return obj_list, index_list


def count_submissions_miner_claim_ips(ip_value):
    """
    Wrapper function for JSON List module to count the number of a certain claim IP in the file.

    :param ip_value: claim IP value to check for
    :type ip_value: str
    :return: number of claim IP values found
    :rtype: int
    """

    obj_list, _ = jlst.get_by_match(SUBMISSIONS_MINER_CLAIMS_PATH, "claim_ip", ip_value, MINER_IP_CAP)

    count = len(obj_list)
    
    print(f"{count} MATCHING IP(s) FOUND IN SUBMISSION MINER CLAIMS")

    return count


def remove_from_submission_miner_claims_by_index(index):
    """
    Wrapper function for JSON List module to remove data at a specified index.

    :param index: line index of data to remove
    :type index: int
    """

    jlst.remove_index(SUBMISSIONS_MINER_CLAIMS_PATH, [index])

    print(f"SUBMISSION MINER CLAIM AT INDEX {index} HAS BEEN REMOVED")


def remove_from_submission_miner_claims_by_submission_id(id_value):
    """
    Wrapper function for JSON List module to remove data with a specified "submission_id" value.

    :param id_value: value of JSON "submission_id" elements for data to remove
    :param id_value: int or str
    """

    _, index_list = jlst.get_by_match(SUBMISSIONS_MINER_CLAIMS_PATH, "submission_id", id_value, MAX_MINER_CLAIMS)

    if index_list is None:
        print(f'NO SUBMISSION CLAIMS DATA WITH SUBMISSION ID VALUE "{id_value}"')

        return
    
    jlst.remove_index(SUBMISSIONS_MINER_CLAIMS_PATH, index_list)

    print(f'REMOVED SUBMISSION CLAIMS DATA WITH SUBMISSION ID VALUES "{id_value}"')


def add_to_unverified_finished_code(data):
    """
    Wrapper function for JSON List module to add unverified finished code data.

    :param: data to be added to the unverified finished code file
    :type data: JSON str
    """

    jlst.add(UNVERIFIED_FINISHED_CODE_PATH, data)

    print("DATA SUCCESSFULLY ADDED TO UNVERIFIED FINISHED CODE FILE")


def get_from_unverified_finished_code():
    """
    Wrapper function for JSON List module to accesses least current block in the unverified finished code file.

    :return: block data, first line index
    :rtype: dict (JSON object), int
    """

    data, line_count = jlst.get(UNVERIFIED_FINISHED_CODE_PATH)

    print("UNVERIFIED FINISHED CODE DATA PULL SUCCESSFUL")

    return data, line_count


def search_unverified_finished_code_by_submission_id(id_value):
    """
    Wrapper function for JSON List module to search for unverified finished code data by submission id.

    :param wallet_value: value to compare with JSON objects' "submision_id" elements
    :type wallet_value: int or str
    :return: finished code JSON object list, JSON object line indicies list
    :rtype: list, list
    """

    obj_list, index_list = jlst.get_by_match(UNVERIFIED_FINISHED_CODE_PATH, "submission_id", id_value, MAX_MINER_CLAIMS * 2)

    if obj_list is None:
        print("NO FINISHED CODE DATA FOUND WITH THIS SUBMISSION ID")

        return None, None
    
    print(f"{len(obj_list)} FINISHED CODE DATA ENTRIES FOUND WITH THIS SUBMISSION ID")

    return obj_list, index_list


def search_unverified_finished_code_by_claim_id(id_value):
    """
    Wrapper function for JSON List module to search for unverified finished code data by wallet address.

    :param wallet_value: value to compare with JSON objects' "wallet" elements
    :type wallet_value: int or str
    :return: finished code JSON object list, JSON object line indicies list
    :rtype: list, list
    """

    obj_list, index_list = jlst.get_by_match(UNVERIFIED_FINISHED_CODE_PATH, "claim_id", id_value, 2)

    if obj_list is None:
        print("NO FINISHED CODE DATA FOUND WITH THIS CLAIM ID")

        return None, None
    
    print(f"{len(obj_list)} of 2 FINISHED CODE DATA ENTRIES FOUND WITH THIS CLAIM ID")

    return obj_list, index_list


def remove_from_unverified_finished_code_by_index(index):
    """
    Wrapper function for JSON List module to remove data at a specified index.

    :param index: line index of data to remove
    :type index: int
    """

    jlst.remove_index(UNVERIFIED_FINISHED_CODE_PATH, [index])

    print(f"UNVERIFIED FINISHED CODE DATA AT INDEX {index} HAS BEEN REMOVED")


def remove_from_unverified_finished_code_by_submission_id(id_value):
    """
    Wrapper function for JSON List module to remove data with a specified "submission_id" value.

    :param id_value: value of JSON "submission_id" elements for data to remove
    :param id_value: int or str
    """

    _, index_list = jlst.get_by_match(UNVERIFIED_FINISHED_CODE_PATH, "submission_id", id_value, MAX_MINER_CLAIMS * 2)

    if index_list is None:
        print(f'NO FINISHED CODE DATA WITH SUBMISSION ID VALUE "{id_value}"')

        return
    
    jlst.remove_index(UNVERIFIED_FINISHED_CODE_PATH, index_list)

    print(f'REMOVED FINISHED CODE DATA WITH SUBMISSION ID VALUES "{id_value}"')


def get_private_key():
    """
    Retrieves stored private wallet key.

    :return: private wallet key
    :rtype: str
    """

    with open(PRIVATE_WALLET_KEY_PATH, "r") as f:
        return f.read()


def get_public_key():
    """
    Retrieves stored public wallet key.

    :return: public wallet key
    :rtype: str
    """

    with open(PUBLIC_WALLET_KEY_PATH, "r") as f:
        return f.read()


def get_recipient_wallet():
    """
    Retrieves stored recipient wallet address.

    :return: recipient wallet address
    :rtype: str
    """

    with open(RECIPIENT_WALLET_ADDRESS_PATH, "r") as f:
        return f.read()


if __name__ == "__main__":  # testing block
    print("NO TEST CASES")