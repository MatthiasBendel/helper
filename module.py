import os
from abc import abstractmethod

import updater


class Module:
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def run(self):
        pass


class UpdateModule(Module):
    def run(self):
        os.system("sudo apt full-upgrade; sudo apt autoremove; sudo apt autoclean")
        updater.check_for_update()

    def get_description(self):
        return "apt upgrade, clean up & update this helper"


class StartOSModule(Module):
    # has to identical to the grub name. See 'man grub-reboot' for details.
    def __init__(self, os_name):
        self.os_name = os_name

    def run(self):
        print("setting os for next start...")
        os.system("sudo grub-reboot '" + self.os_name + "'")
        print("reboot...")
        os.system("sudo reboot")

    def get_description(self):
        return "start " + self.os_name


class SshModule(Module):
    # host is stored in ~/.ssh/config or /etc/hosts
    def __init__(self, host):
        self.host = host

    def run(self):
        os.system("ssh " + self.host)

    def get_description(self):
        return "ssh " + self.host
