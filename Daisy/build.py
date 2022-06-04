import UtilsManager
import subprocess

command = "pyside6-rcc resources.qrc -o ./modules/resources_rc.py"
subprocess.run(command.split(' '), shell=True, check=True)
command = "pyside6-uic main.ui > ./modules/ui_main.py"
subprocess.run(command.split(' '), shell=True, check=True)

um = UtilsManager.UtilsManager(dev=True)
um.requirements_txt()
um.build("Daisy.py", withconsole=True)
