#!/usr/bin/env python3
import os
import backup_helper
import sys

import setup


def print_options():
    print("Please type a number:")
    print("1 : apt upgrade")
    print("2 : Backup ...")
    print("3 : ssh raspi")
    print("5 : Frequently used programs")
    print("6 : XAMPP")
    print("7 : ssh vp94hyso@clientssh1.rbg.informatik.tu-darmstadt.de -X ...")
    print("")


def wrong_input():
    print("Ihre Eingabe wurde nicht erkannt.\n")


def read_number():
    user_input = sys.stdin.readline()
    try:
        return int(user_input)
    except ValueError:
        wrong_input()


def ssh_tu():
    print("Please choose a client (1 - 3)")
    client = read_number()
    os.system("ssh vp94hyso@clientssh" + str(client) + ".rbg.informatik.tu-darmstadt.de -X")


def call_option(option: int):
    if option == 1:
        os.system("sudo apt full-upgrade; sudo apt autoremove; sudo apt autoclean")
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
        ssh_tu()


# def main():
setup.check_for_update()
setup.initialize()
print_options()
option = read_number()
call_option(option)
sys.exit()
