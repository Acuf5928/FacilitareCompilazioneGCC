#!/usr/bin/python

import os

percorsofile = ""

while percorsofile!="-1": 
    percorsofile = input("Percosso file da compilare con gcc: ")

    if percorsofile == "-1":
        break

    salvataggio = percorsofile.replace('.c', '.exe')

    os.system("gcc -std=c99 -o " + salvataggio + " " + percorsofile)

