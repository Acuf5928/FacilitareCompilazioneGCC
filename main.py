#!/usr/bin/python

import os

percorsofile = ""
Selto = "0"
commenti = ""

while percorsofile!="-1":
    while percorsofile!="-1": 
        percorsofile = input("Percosso file da compilare con gcc: ")

        if percorsofile[-1]!="c":
            if percorsofile[-2]!="c":
                print("File non valido")
                break
        
        Scelta = input("Vuoi inserire commenti al compilatore?\n 1)Si 2)No\n")

        if Scelta == "1":
            commenti = input("Inserire commento:")
    
        if percorsofile == "-1":
            break

        salvataggio = percorsofile.replace('.c', '.exe')

        os.system("gcc -o " + salvataggio + " " + commenti + " " + percorsofile)

        Scelta = "0"
