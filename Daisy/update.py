import os
import subprocess
import time

command = "pyside6-rcc resources.qrc -o ./modules/resources_rc.py"
subprocess.run(command.split(' '), shell=True, check=True)
command = "pyside6-uic main.ui > ./modules/ui_main.py"
subprocess.run(command.split(' '), shell=True, check=True)
# from . resources_rc import *
