import os
from urllib.request import urlretrieve

import input_analyzer


class JetbrainsModule:
    def get_description(self):
        return "Jetbrains-Toolbox"

    def run(self):
         # Downloads Jetbrains-Toolbox to /opt/jetbrains-toolbox (needs root access)
        install_path = "/opt/jetbrains-toolbox"
        urlretrieve("https://download.jetbrains.com/toolbox/jetbrains-toolbox-1.4.2492.tar.gz", install_path)
        print("Downloaded ")

get_modules = JetbrainsModule(),