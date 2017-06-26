#!/usr/bin/env python3
import os
import backup_helper
import sys

import updater
import version
from module import UpdateModule
from module import Module


modules = UpdateModule(), Module


def print_options():
    print("Please type a number:")
    print("Hint: call 'h [number]' to skip this dialog.")
    print("-u or --update")
    print("-v or --version\n")
    print("1 : " + modules[0].get_description())
    print("2 : Backup ...")
    print("3 : ssh raspi")
    print("5 : Frequently used programs")
    print("6 : XAMPP")
    print("7 : ssh vp94hyso@clientssh1.rbg.informatik.tu-darmstadt.de -X ...")


def wrong_input():
    print("Ihre Eingabe wurde nicht erkannt.\n")


def read_number():
    user_input = sys.stdin.readline()
    try:
        return int(user_input)
    except ValueError:
        wrong_input()


def call_option(option: int):
    if option == 1:
        modules[0].run()
    if option == 2:
        backup_h = backup_helper.BackupHelper()
        backup_h.main()
    if option == 3:
        os.system("ssh raspi")
    if option == 5:
        os.system("cd ~/Dokumente/Installation/; ./Programme_installieren_1.3.sh")
    if option == 6:
        os.system("gksudo /opt/lampp/manager-linux-x64.run")
    if option == 7:
        print("Please choose a client (1 - 3)")
        client = read_number()
        os.system("ssh vp94hyso@clientssh" + str(client) + ".rbg.informatik.tu-darmstadt.de -X")


def main():
    if len(sys.argv) == 1:  # do standard
        print_options()
        option = read_number()
        call_option(option)
    else:
        arg = sys.argv[1]
        if arg == "-v" or arg == "--version":
            print("version: " + str(version.__version__))
            sys.exit()
        if arg == "-u" or arg == "--update":
            updater.check_for_update()
            sys.exit()

        try:
            int(arg)
            call_option(int(arg))
            sys.exit()
        except ValueError:
            print("wrong input...")


if __name__ == '__main__':
    main()
