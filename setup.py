#!/usr/bin/env python3

import os.path
import input_analyzer
import version

EXEC_PATH = "/usr/local/bin/h"
INSTALL_PATH = "/opt/helper/helper.py"
ONLINE_VERSION_FILE = "https://raw.githubusercontent.com/MatthiasBendel/helper/master/version.py"


def install():
    os.system("sudo git clone https://github.com/MatthiasBendel/helper.git /opt/helper")
    check_global_accessibility()


def check_global_accessibility():
    try:
        if not os.path.isfile(EXEC_PATH):
            if input_analyzer.ask_bool_question("Do you want to make this file global executable?"):
                os.system("sudo ln -s " + INSTALL_PATH + " " + EXEC_PATH)
                print("helper.py is linked to " + EXEC_PATH)
                # if not os.access(INSTALL_PATH, os.X_OK):
                os.system("sudo chmod +x " + EXEC_PATH)
                print("Execute h to run this.\n")
    except():
        print("Couldn't check for global accessibility...")


def download_file():
    import httplib2
    h = httplib2.Http(".cache")
    resp, content = h.request(ONLINE_VERSION_FILE, "GET")
    return str(content)


def is_up_to_date():
    file = download_file()
    online_version = float(file[16:19])
    is_up_to_date = version.__version__ == online_version
    if not is_up_to_date:
        print("There is a new version available.\n"
              "Current version: " + str(version.__version__) + "\n"
              "New version:\t " + str(online_version))
    return is_up_to_date


def update():
    os.system("git pull")


def check_for_update():
    try:
        if not is_up_to_date():
            if input_analyzer.ask_bool_question("Do you want to update now?"):
                update()
    except():
        print("Can't check for updates. Try again next time.")

