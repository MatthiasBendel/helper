#!/usr/bin/env python3

import os.path
import sys
import version

INSTALL_PATH = "/usr/local/bin/h"


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

def is_up_to_date(): bool
    actual_version = 
    if version.__version__ == actual_version
