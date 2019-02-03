 #!/usr/bin/python3
 # -*- coding: utf-8 -*-

import random as rand
import time
import os

def zahl1_erzeugen():
    global zahl1
    zahl1 = rand.randint(1,11)


def zahl2_erzeugen():
    global zahl2
    zahl2 = rand.randint(1,11)


def ergebnis_berechnen():
    global dasergebnis
    dasergebnis = int(zahl1)*int(zahl2)
    os.chdir("/home/berphi/Downloads")
    f = open("ergebnis.txt","w")
    f.write(str(dasergebnis))
    f.close()
    return dasergebnis


def aufgabe_stellen():
    return "Berechne: {} x {}".format(zahl1, zahl2)


def input_lesen():
    os.chdir("/home/berphi/Downloads")
    global data_input
    with open ("input.txt", "r") as myfile:
      data_input = myfile.readlines()
    print("input_lesen: ", data_input)

def ergebnis_lesen():
    os.chdir("/home/berphi/Downloads")
    global ergebnis
    with open ("ergebnis.txt", "r") as myfile:
      ergebnis = myfile.readlines()
    print("Ergebnis: ", ergebnis)

    
def remove():
    try:
        os.chdir("/home/berphi/Downloads")
        os.remove("input.txt")
        os.remove("ergebnis.txt")
        print("Löschen erfolgreich.")
    except:
        print("Löschen war nicht möglich.")

def ergebnis_pruefen_web():
    
    global richtig
    richtig = 0

    global falsch
    falsch = 0
    
    if ergebnis == data_input:
       print("Das war korrekt")
       richtig += 1
    else:
        print("Das war falsch...")
        falsch += 1

def main():

    print("\nDas Python Skript läuft.\n")
    
    while True:

        try :
            input_lesen()
            print("User Input erfolgreich gelesen.")
            time.sleep(2)
            ergebnis_lesen()
            print("Ergebnis der Aufgabe eingelesen.")
            time.sleep(2)
            ergebnis_pruefen_web()
            print("Ergebnis und User-Input abgeglichen.")
            time.sleep(2)
            remove()
            time.sleep(2)

        except:
            time.sleep(3)
            print("Nichts zu tun...")
            pass
        
    return 0
        

if __name__ == "__main__":
    main()