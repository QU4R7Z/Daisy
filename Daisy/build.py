import UtilsManager

um = UtilsManager.UtilsManager(dev=True)
um.requirements_txt()
um.build("Daisy.py", withconsole=True)
