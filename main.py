#!/usr/bin/python

import os
import glob

percorsofile = ""
Selta = "0"
commenti = ""

while percorsofile!="-1":
    while percorsofile!="-1": 
        percorsofile = ""

        while percorsofile=="":
            percorsofile = input("Percosso file o cartella con i file da compilare con gcc: ")

        if percorsofile == "-1": #termina il programma se verificato
            break

        Scelta = input("Vuoi inserire commenti al compilatore?\n1)Si 2)No\n")

        if Scelta == "1":
            commenti = input("Inserire commento:")
                
        if percorsofile[-2]!=".": #blocco codice da eseguire se viene inserita una cartella
            if percorsofile[-3]!=".":
                percorsofile = percorsofile.replace('\"', '') #elimina eventuali " ' nel path della cartella, passo necessario a far funzionare glob, verranno riaggiuni direttamente in os.system
                percorsofile = percorsofile.replace('\'', '')
                
                if percorsofile[-1]!="\"": #viene aggiunto \ ala fine del path, se non è presente
                    percorsofile = percorsofile + "\\"
                
                file_paths = glob.glob(percorsofile + "*.c") #genera la lista dei file

                Contatore = 1
                
                for f in file_paths:
                    f = f.replace('\'','\"') #sostituisce ' con "
                    salvataggio = f.replace('.c', '.exe') #genera il percorso del file generato
                    print("\nCompilazione:",Contatore,"\n",f,"\n")
                    os.system("gcc -o \"" + salvataggio + "\" " + commenti + " \"" + f + "\"") #invia i comandi a gcc
                    Contatore += 1

        if percorsofile[-2]=="." or percorsofile[-3]==".": #blocco codice da eseguire se viene inserito un file
            if percorsofile[-1]!="c":
                if percorsofile[-2]!="c": #verifica l'esensione del file
                    print("File non valido")
                    break

            salvataggio = percorsofile.replace('.c', '.exe') #genera il percorso del file generato
            print("Compilazione")
            os.system("gcc -o " + salvataggio + " " + commenti + " " + percorsofile) #invia i comandi a gcc
        
        Scelta = "0"
