#!/usr/bin/env python3

import os.path

import sys

import input_analyzer
import install
import version

INSTALL_PATH = "/opt/helper/"
ONLINE_VERSION_FILE = "https://raw.githubusercontent.com/MatthiasBendel/helper/master/version.py"


def get_online_version():
    import httplib2
    h = httplib2.Http(".cache")
    resp, content = h.request(ONLINE_VERSION_FILE, "GET")
    online_version = str(content, 'utf-8')[14:]
    return online_version


def update():   # remove old installation and copy the updated version again to the same path
    installation_path = os.path.realpath(sys.argv[0])[:-9]
    path, file = install.download_zip()
    install.extract_zip(installation_path, path + file)
    # todo offer git update


def check_for_update():
    try:
        online_version = get_online_version()
        is_up_to_date = version.__version__ >= float(online_version)
        if is_up_to_date:
            print("This is the actual version ({}).".format(version.__version__))
        else:
            print("There is a new version available.\n"
                  "Current version:\t{}\n"
                  "New version:\t\t{} ".format(str(version.__version__), str(online_version)))

            if input_analyzer.ask_bool_question("Do you want to update now?"):
                update()
    except():
        print("Can't check for updates.")


def main():
    (is_up_to_date, online_version) = get_online_version()
    print("Running version " + str(version.__version__))
    print("Found online version: " + online_version)
    print("So there is " + ("no " if is_up_to_date else "a ") + "new version!")

if __name__ == '__main__':
    main()
