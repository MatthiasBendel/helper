import sys
import os

from module import Module


class BackupModule(Module):
    def run(self):
        self.main()

    def get_description(self):
        return "Backup ..."

    def print_options(self):
        print("Welches Backup soll durchgeführt werden?")
        print("1 : Backup von matze@raspi nach ~/Archiv/Backup/ (exclude ~/Backup)")
        print("2 : Backup von matze@L540  nach matze@raspi:~/Backup")
        print("3 : beide vorherige")
        print("4 : vorhandene Backups anzeigen (@raspi)")
        print("5 : Log-File anzeigen")
        print("")

    def read_number(self):
        user_input = sys.stdin.readline()
        try:
            return int(user_input)
        except ValueError:
            print("Ihre Eingabe wurde nicht erkannt.\n")

    def call_option(self, option):
        import os
        if option == 1:
            os.system("rsync --delete --numeric-ids --relative --delete-excluded "
                      "--exclude=/home/matze/.local/share/Trash/ --exclude=/home/matze/Backup/ "
                      "--exclude=/home/matze/.cache/ -avze ssh matze@192.168.0.100:/home/matze "
                      "/home/matze/Archiv/Backup/matze@raspi")

        if option == 2:
            os.system("ssh -t raspi sudo ./my_rsnapshot.sh hourly")

        if option == 3:
            os.system("rsync --delete --numeric-ids --relative --delete-excluded "
                      "--exclude=/home/matze/.local/share/Trash/ --exclude=/home/matze/Backup/ "
                      "--exclude=/home/matze/.cache/ -avze ssh matze@192.168.0.100:/home/matze "
                      "/home/matze/Archiv/Backup/matze@raspi")
            os.system("ssh -t raspi sudo ./my_rsnapshot.sh hourly")

        if option == 4:
            os.system("ssh raspi ls -lAt Backup/")

        if option == 5:
            os.system("ssh raspi tail -23 Backup/rsnapshot.log | less -S")

        else:
            print("Ihre Eingabe wurde nicht erkannt.\n")

    def main(self):
        self.print_options()
        option = self.read_number()
        self.call_option(option)
