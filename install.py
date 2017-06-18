#!/usr/bin/env python3

import sys
#  - - - What the user should do - - -
# 1. download helper-master.zip
# 2. unzip setup.py in same folder
# 3. cd in this folder and run "python3 setup.py"
# => files are in INSTALL_PATH and main is global executable by "h"
import zipfile

# import setup
import setup

installation_path = "/opt/helper_test"

while True:
    try:
        with zipfile.ZipFile("helper-master.zip", "r") as zip_ref:
            zip_ref.extractall(installation_path)
        zip_ref.close()
        break
    except PermissionError as permission_error:
        print(permission_error)
        print("Please specify the installation path:")
        installation_path = sys.stdin.readline().strip()

print("Files where moved to " + installation_path)
setup.check_global_accessibility()
