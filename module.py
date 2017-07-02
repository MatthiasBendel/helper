import os
from abc import abstractmethod


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

    def get_description(self):
        return "apt upgrade and clean up"


class StartOSModule(Module):
    # has to identical to the grub name. See 'man grub-reboot' for details.
    os_name = "Windows 10 (auf /dev/sda2)"

    def run(self):
        print("setting os for next start...")
        os.system("sudo grub-reboot '" + self.os_name + "'")
        print("reboot...")
        os.system("sudo reboot")

    def get_description(self):
        return "start " + self.os_name
