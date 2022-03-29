"""
Defines JSON List data structure file operations used for public storage.
Marked by the JLST file extension.

:author: Max Milazzo
"""


import json
import os


FIRST_LINE_INDEX = 0
# first line index will start at 0


def add(path, data):
    """
    Adds data to the back of a JSON List (bottom of JLST file).

    :param path: file path
    :param data: block data to add to JLST file
    :type path: str
    :type data: dict (JSON object) or str
    """

    with open(path, "a") as f:
        f.write(str(data) + "\n")


def get(path):
    """
    Gets data from the front of a JSON List (top of JLST file).
    By default, all data will be extracted from the front.
    To get data from the back of a JSON list, use get_from_back function.

    :param path: file path
    :type path: str
    :return: block data, line index (0)
    :rtype: dict (JSON object), int
    """

    if os.path.getsize(path) == 0:  # returns None for all data if empty file
        return None, None

    with open(path, "r") as f:  # gets first line
        data = f.readline()
    
    return json.loads(data), FIRST_LINE_INDEX


def get_from_back(path):
    """
    Gets data from the back of a JSON List (bottom of JLST file).

    :param path: file path
    :type path: str
    :return: block data, last line index
    :rtype: dict (JSON object), int
    """

    if os.path.getsize(path) == 0:  # returns None for all data if empty file
        return None, None

    line_count = -1

    with open(path, "rb") as f:
        line_count = sum(1 for _ in f)

        try:  # attempts to seek last line of file assuming a muli-line file is opened
            f.seek(-2, os.SEEK_END)

            while f.read(1) != b'\n':
                f.seek(-2, os.SEEK_CUR)

        except OSError:  # catch OSError in case of a one line file 
            f.seek(0)
        
        return json.loads(f.readline().decode()), line_count


def get_by_match(path, json_elem, match, count):
    """
    Gets a list of JSON object data based on JSON element matches.
    If the length of the match test is less than element data, shortened element data is compared.

    :param path: file path
    :param json_elem: JSON element ID location to search for data
    :param match: data to compare with JSON element data
    :param count: number of items to search for (-1 for no specified limit)
    :type path: str
    :type json_elem: str
    :type match: str (if not of type str, will be converted to str)
    :type count: int
    :return: JSON object list, JSON object line indicies list
    :rtype: list, list
    """

    match = str(match)
    match_len = len(match)
    # match string variable initialization

    obj_list = []
    index_list = []
    # data lists

    line_count = 0

    with open(path, "r") as f:
        for line in f:
            line_json = json.loads(line)

            if match == str(line_json[json_elem])[:match_len]:  # checks comparison
                obj_list.append(line_json)
                index_list.append(line_count)
            
            if len(obj_list) == count:  # ends loop if count limit reached
                break

            line_count += 1
    
    if len(obj_list) == 0:  # returns None for all data if no objects added to data list
        return None, None
    
    return obj_list, index_list


def remove_index(path, index_list):
    """
    Removes JSON object from JSON List at specified index (index of JLST file).

    :param path: file path
    :param index: JSON List indicies of data to remove
    :type path: str
    :type index: list
    """

    is_skipped = False
    current_index = 0
    dummy_file = path + ".bak"
    # file parsing utility variables
 
    with open(path, "r") as read_f, open(dummy_file, "w") as write_f:
        for line in read_f:

            if current_index not in index_list:  # adds data to dummy file if not at specified index
                write_f.write(line)
            else:
                is_skipped = True

            current_index += 1

    if is_skipped:  # if line has been skipped reassigns file names, if not deletes dummy file
        os.remove(path)
        os.rename(dummy_file, path)
    else:
        os.remove(dummy_file)


if __name__ == "__main__":  # testing block
    print("NO TEST CASES")