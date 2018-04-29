#!/usr/bin/python3

import os
import glob

percorsofile = ""
Selta = "0"
commenti = ""

if os.name == "nt":
    estensione = ".exe"
    slash = "\\"

else:
    estensione = ".out"
    slash = "/"

while percorsofile!="-1":
    while percorsofile!="-1": 
        percorsofile = ""

        while percorsofile=="":
            percorsofile = input("Percosso file o cartella con i file da compilare con gcc: ")

        if percorsofile == "-1": #termina il programma se verificato
            break

        if len(percorsofile) < 3:
            print("Input non riconociuto")
            break
        
        Scelta = input("Vuoi inserire commenti al compilatore?\n1)Si 2)No\n")

        if Scelta == "1":
            commenti = input("Inserire commento:")
        
        percorsofile = percorsofile.replace('\"', '') #elimina eventuali " ' nel path della cartella, passo necessario a far funzionare glob, verranno riaggiuni direttamente in os.system
        percorsofile = percorsofile.replace('\'', '')

        if os.path.isdir(percorsofile): #blocco codice da eseguire se viene inserita una cartella
            if percorsofile[-1]!="\"": #viene aggiunto \ ala fine del path, se non e' presente
                percorsofile = percorsofile + slash

            try:
                file_paths = glob.glob(percorsofile + "*.c") #genera la lista dei file

            except Exception:
                print("Input non riconociuto")
                break
                
            Contatore = 1
                
            for f in file_paths:
                f = f.replace('\'','\"') #sostituisce ' con "
                salvataggio = f.replace('.c', estensione) #genera il percorso del file generato
                print("\n Compilazione:",Contatore,"\n",f,"\n")
                os.system("gcc -o \"" + salvataggio + "\" " + commenti + " \"" + f + "\"") #invia i comandi a gcc
                Contatore += 1

        if os.path.isfile(percorsofile): #blocco codice da eseguire se viene inserito un file
            if percorsofile[-1]!="c":
                if percorsofile[-2]!="c": #verifica l'esensione del file
                    print("File non valido")
                    break

            salvataggio = percorsofile.replace('.c', estensione) #genera il percorso del file generato
            print("Compilazione")
            os.system("gcc -o " + salvataggio + " " + commenti + " " + percorsofile) #invia i comandi a gcc
        
        else:
            print("2")
        Scelta = "0"
