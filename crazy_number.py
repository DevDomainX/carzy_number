#!/usr/bin/env python3 
from colorama import init, Fore, Style
from time import sleep
import os
import sys
from random import randint, choice
init()

class Crazy:
    

    def num():
        code = "+569"
        number = randint(19999999, 99999999)
        telefone = "{}{}".format(code, number)
        print(f"El numero al azar es : {telefone}\n")
        op = input("desea volver al menu (s/n): ")
        if op == 's':
            Crazy.menu()
        if op == "n":
            print("gracias Hasta pronto")

    def frase():
        frases = 'Hola, esta el jose...(contesta y dice que jose ).... el que telo puso y se fue ', 'Hola  esta el renato....el que te lo puso en el labaplato', 'contesta el dice alo y tu dise no esta el lalo', 'hola esta el simon ...... el que te lo puso en el barcon'
        f = choice(frases)
        for i in f:
            print(i, end="", flush=True)
            sleep(0.1)
        op = input("\n\ndesea volver al menu (s/n): ")
        if op == 's':
            Crazy.menu()
        if op == "n":
            print("gracias Hasta pronto")


    def CrearFrases():
        while True:
            with open("listaFrases.txt", "a") as con:
                frase = input("Ingresa la frase: ")
                con.write(f"{frase}\n")
                print("Frase guardada con exito")
                op = input("deseas seguir agregando frases? (y/n): ")
                if op == "y":
                    Crazy.menu()
                if op == "n":
                    print("Hasta pronto")
                    sys.exit()

    def listFrase():
        with open("listaFrases.txt", "r") as con:
            for i in con.readline():
                print(choice(i), end="", flush=True)
                sleep(0.1)
        return Crazy.menu()
    
    
    def ruleta():
        code = "+569"
        number = randint(19999999, 99999999)
        telefone = "{}{}".format(code, number)
        frases = 'Hola, esta el jose...(contesta y dice que jose ).... el que telo puso y se fue ', 'Hola  esta el renato....el que te lo puso en el labaplato', 'contesta el dice alo y tu dise no esta el lalo', 'hola esta el simon ...... el que te lo puso en el barcon'
        f = f"{choice(frases)} \n\nnumero: {telefone}"
        for i in f:
            print(i, end="", flush=True)
            sleep(0.1) 

    def menu():
        
        title = Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"""

            $ Script bromas telefonicas al azar \neste script es solo para mera educacion de programacion\nno me ago responsable del mal uso\n\nCreated by: Hans Saldias\n\nBy: 1LugarParprogramar\n\n

            [ 1 => pedir numero telefonico al azar]

            [ 2 => pedir frase de broma al azar   ]

            [ 3 => crear frases tuyas y guardarlas]

            [ 4 => pedir una frase tuya de las guardadas]

            [ 5 => ruleta numero y frase ]

            [ 00 => salir .....]
            \n\n"""
        print(title)
        try:
            op = int(input("Ingrese opcion: "))
            if op == 1:
                Crazy.num()
            elif op == 2:
                Crazy.frase()
            elif op == 3:
                Crazy.CrearFrases()
            elif op == 4:
                Crazy.listFrase()
            elif op == 5:
                Crazy.ruleta()
            elif op == 00:
                 exit()
        except ValueError:
            print("ingrese una opcion valida, e intente nuevamente")
            p = input("desea volver al menu (s/n): ")
            if p == "s":
                Crazy.menu()
            else:
                print("Hasta pronto 1LugarParaProgramar")
            
if __name__ == '__main__':
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("pip install colorama")
    os.system("pip install sys")
    os.system("pip install time")
    print("paquetes actualizados correctamente")
    sleep(5)
    Crazy.menu()
