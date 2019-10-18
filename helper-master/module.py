import os
from abc import abstractmethod
from urllib.request import urlretrieve

import updater


class Module:
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def run(self):
        pass


from backup_helper import BackupModule

class ShellModule(Module):
    def run(self):
        os.system("h")

    def get_description(self):
        return "This as a Shell-Script"


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


class JetbrainsModule(Module):
    def get_description(self):
        return "Jetbrains-Toolbox"

    def run(self):
        os.system("/opt/jetbrains-toolbox")

    @staticmethod
    def install():
        """ Downloads Jetbrains-Toolbox to /opt/jetbrains-toolbox (needs root access)"""
        urlretrieve("https://download.jetbrains.com/toolbox/jetbrains-toolbox-1.4.2492.tar.gz",
                    "/opt/jetbrains-toolbox")


# These are the modules which are shown when starting the helper script!
modules = UpdateModule(), \
          StartOSModule("Windows 10 (auf /dev/sda2)"), \
          BackupModule(), \
          SshModule("raspi"), \
          JetbrainsModule(), \
          ShellModule()
