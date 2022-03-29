"""
User submitted code execution management module.

:author: Max Milazzo
"""


import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from data_access import MAX_CHECK_ITERATIONS, MAX_OUTPUT_LENGTH


def get_driver():
    """
    Sets up selenium webdriver.

    :return: selenium webdriver
    :rtype: webdriver
    """
    
    options_driver = Options()
    options_driver.add_argument("headless")
    options_driver.add_argument("--log-level=3")
    # defines extra driver options

    driver = webdriver.Chrome(executable_path="netlib\\chromedriver.exe", options=options_driver)
    # creates the web driver

    return driver


def exec():
    """
    Main execution function.

    :return: JSON-formatted output
    :rtype: str
    """

    print("STARTING NEW SCRIPT EXECUTION")

    driver = get_driver()

    run_path = os.path.join(os.getcwd(), "run\\run.html")
    # gets path of run folder in system

    driver.get(f"file:///{run_path}")

    start_time = time.time()
    check_complete(driver)
    # checks code run completion

    final_time = time.time() - start_time
    # calculates run time

    return get_output(driver, final_time)


def check_complete(driver):
    """
    Waits for code completion signature for allotted time.

    :param driver: selenium webdriver
    :type driver: webdriver
    """

    print("COMPLETION STATUS:")

    for _ in range(MAX_CHECK_ITERATIONS):  # checks for completion for allotted time

        file_data = driver.execute_script("return window.localStorage;")
        fin_data = file_data["neep.is-finished"][0]
        # gets completion local storage data

        print(fin_data)

        if fin_data == "1":  # ends loop if completion signature found
            print("COMPLETION SIGNATURE RETURNED - ENDING EXECUTION")
            break

        time.sleep(1)


def get_output(driver, run_time):
    """
    Gets final code output.

    :param driver: selenium webdriver
    :type driver: webdriver
    :param run_time: code run time
    :type run_time: float
    :return: final output
    :rtype: str
    """

    file_data = driver.execute_script("return window.localStorage;")
    output = file_data["neep.output"]
    finished = file_data["neep.is-finished"]
    # gets local storage data

    print("OUTPUT RETRIEVED")

    if (len(output) > MAX_OUTPUT_LENGTH):
        print("OUTPUT EXCEEDS MAXIMUM LENGTH:")
        print(str(len(output)) + " > " + str(MAX_OUTPUT_LENGTH))

        output = output[:MAX_OUTPUT_LENGTH]

        print("OUTPUT SHORTENED")

    print("OUTPUT LENGTH:")
    print(len(output))

    return '{"result_string":"'+ output + '","time":' + str(run_time) + ',"finished":' + finished + "}"
    # returns formatted output


if __name__ == "__main__":  # test entry block
    print(exec())