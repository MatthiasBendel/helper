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

