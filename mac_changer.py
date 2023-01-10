#Author: Manuel Ramos
#v 1.1

import subprocess
import sys

#PANEL DE AYUDA
def help_panel():
	return """
Metodo de uso:

python mac_changer.py <Interfaz> <Dirección MAC> 

"""

#CODIGO

i = input("Interfaz: ")
mac = input("Dirección MAC: ")

subprocess.run(["ifconfig", i, "down"])

try:
	subprocess.run(["ifconfig", i, "hw", "ether", mac])
except:
	help_panel()
	sys.exit(1)
else:
	print("\n\n[+] Direccion MAC cambiada con éxito\n")
finally:
	subprocess.run(["ifconfig", i, "up"])
	sys.exit(0)




