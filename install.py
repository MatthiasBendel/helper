#!/usr/bin/env python3
import os
import shutil
import sys
#  - - - What the user should do - - -
# 1. download helper-master.zip
# 2. unzip updater.py in same folder
# 3. cd in this folder and run "python3 updater.py"
# => files are in INSTALL_PATH and main is global executable by "h"
import zipfile

# import setup
from distutils.util import strtobool
from urllib.request import urlretrieve

installation_path = "/opt/helper/"
exec_path = "/usr/local/bin/h"
main_path = "helper-master/helper.py"
global_archive_path = "https://github.com/MatthiasBendel/helper/archive/master.zip"


def ask_bool_question(question: str):
    """This function is copied from input_analyzer.py. It's located here to use this file without dependencies."""
    print(question + " [y/n]")
    answer = sys.stdin.readline().strip()
    return bool(strtobool(answer))


def remove_archive(path):
    shutil.rmtree(path)
    print("removed " + path)


def download_zip(path="/tmp/helper/"):
    if os.path.exists(path):
        if ask_bool_question(path + " already exists! Do you want to remove it?"):
            remove_archive(path)
        else:
            sys.exit()

    os.makedirs(path)
    file = "master.zip"
    urlretrieve(global_archive_path, path + file)
    print("downloaded archive to " + path + file)
    return path, file


def extract_zip(extract_path, archive_path="/tmp/helper/master.zip"):
    while True:
        try:
            with zipfile.ZipFile(archive_path, "r") as zip_ref:
                zip_ref.extractall(extract_path)
            zip_ref.close()
            break
        except PermissionError as permission_error:
            print(permission_error)
            print("Please specify the installation path (ending with /) or run this with sudo:")
            extract_path = sys.stdin.readline().strip()

    print("Files where moved to " + extract_path)


def install():
    path = download_zip()
    extract_zip(installation_path, path[0] + path[1])
    remove_archive(path[0])

    # make it global executable
    try:
        if os.path.exists(exec_path):
            output = os.popen("ls -l /usr/local/bin/h").read()
            if ask_bool_question("h exists already:\n" + output + "\nDo you want to overwrite it?"):
                os.remove(exec_path)
            else:
                print("Okay, h stays untouched.")
                sys.exit()
        os.system("sudo ln -s " + installation_path + main_path + " " + exec_path)
        print(installation_path + main_path + " is linked to " + exec_path)
        os.system("sudo chmod +x " + exec_path)
        print("Execute h to run this.\n")
        print("removing " + sys.argv[0] + " ...")
        os.remove(sys.argv[0])
    except PermissionError as pe:
        print("Couldn't check for global accessibility...")
        print(pe)


if __name__ == '__main__':
    install()
