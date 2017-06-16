#!/usr/bin/env python3

import os.path
import sys
import version
import urllib

INSTALL_PATH = "/usr/local/bin/h"
ONLINE_VERSION_FILE = "https://raw.githubusercontent.com/MatthiasBendel/helper/master/version.py"


def initialize():
    if not os.path.isfile(INSTALL_PATH):
        print("Do you want to make this file global executable? (Y/N)"
              "Hint: First move the file where you want to leave it.")
        input = sys.stdin.readline()
        input = input.strip()

        if input == 'Y' or input == 'y':
            os.system("sudo ln -s " + os.path.realpath(__file__) + " " + INSTALL_PATH)
            print("This file was linked to " + INSTALL_PATH)
            # if not os.access(INSTALL_PATH, os.X_OK):
            os.system("sudo chmod +x " + INSTALL_PATH)
            print("Type h to run this.\n")


def download_file():
    import httplib2
    h = httplib2.Http(".cache")
    resp, content = h.request(ONLINE_VERSION_FILE, "GET")
    return str(content)


def is_up_to_date():
    file = download_file()
    online_version = float(file[16:19])
    is_up_to_date = version.__version__ == online_version
    if is_up_to_date:
        return True
    else:
        print("There is a new version available.\n"
              "Current version: " + str(version.__version__) + "\n"
                                                               "New version:\t " + str(online_version))
        return False


def check_for_update():
    try:
        if not is_up_to_date():
            print("Do you want to update now? (Y / N)")
    except():
        print("Can't check for updates. Try again next time.")


print(check_for_update())
