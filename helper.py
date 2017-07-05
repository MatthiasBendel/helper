#!/usr/bin/env python3
import argparse
import os
import sys

import updater
import version
from module import UpdateModule, StartOSModule, SshModule
from backup_helper import BackupModule

modules = UpdateModule(), StartOSModule("Windows 10 (auf /dev/sda2)"), BackupModule(), SshModule("raspi")


def print_options():
    print("Hint: call 'h [number]' to skip this dialog.")
    i = 1
    for module in modules:
        print(str(i) + "\t" + module.get_description())
        i += 1

    print(str(i) + "\tFrequently used programs")
    i += 1
    print(str(i) + "\tXAMPP")
    i += 1
    print(str(i) + "\tssh vp94hyso@clientssh1.rbg.informatik.tu-darmstadt.de -X ...")

    print("Please type a number:")


def wrong_input():
    print("Ihre Eingabe wurde nicht erkannt.\n")


def read_number():
    try:
        user_input = sys.stdin.readline()
        return int(user_input)
    except ValueError:
        wrong_input()
    except KeyboardInterrupt:
        print()
        sys.exit()


def call_option(option: int):
    if option <= modules.__len__():
        modules[option-1].run()

    if option == modules.__len__()+1:
        os.system("cd ~/Dokumente/Installation/; ./Programme_installieren_1.3.sh")
    if option == modules.__len__()+2:
        os.system("gksudo /opt/lampp/manager-linux-x64.run")
    if option == modules.__len__()+3:
        print("Please choose a client (1 - 3)")
        client = read_number()
        os.system("ssh vp94hyso@clientssh" + str(client) + ".rbg.informatik.tu-darmstadt.de -X")


def main():
    if len(sys.argv) == 1:  # do standard
        print_options()
        option = read_number()
        call_option(option)
    else:
        parser = argparse.ArgumentParser()
        parser.add_argument("update", help="update this helper")
        parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
        parser.add_argument("--version", help="output version information and exit", action="store_true")
        args = parser.parse_args()

        if args.update == "update":
            updater.check_for_update()
            sys.exit()
        if args.version:
            print("version: " + str(version.__version__))
            sys.exit()
        if args.verbose:
            print("verbosity turned on, but that's not implemented...")
        try:
            arg = sys.argv[1]
            int(arg)
            call_option(int(arg))
        except ValueError:
            print("wrong input...")


if __name__ == '__main__':
    main()
