#!/usr/bin/env python3
import os
import sys
#  - - - What the user should do - - -
# 1. download helper-master.zip
# 2. unzip setup.py in same folder
# 3. cd in this folder and run "python3 setup.py"
# => files are in INSTALL_PATH and main is global executable by "h"
import zipfile

# import setup

installation_path = "/opt/helper/"
exec_path = "/usr/local/bin/h"
main_path = "helper-master/helper.py"

while True:
    try:
        with zipfile.ZipFile("helper-master.zip", "r") as zip_ref:
            zip_ref.extractall(installation_path)
        zip_ref.close()
        break
    except PermissionError as permission_error:
        print(permission_error)
        print("Please specify the installation path (ending with /):")
        installation_path = sys.stdin.readline().strip()

print("Files where moved to " + installation_path)

# make it global executable
try:
    os.remove(exec_path)
    os.system("sudo ln -s " + installation_path + main_path + " " + exec_path)
    print(installation_path + main_path + " is linked to " + exec_path)
    os.system("sudo chmod +x " + exec_path)
    print("Execute h to run this.\n")
except():
    print("Couldn't check for global accessibility...")
