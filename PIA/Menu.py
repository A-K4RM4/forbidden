import os, requests, re
from bs4 import BeautifulSoup as bs

def funcionMenu():
    count=0
    pr=input("¿Conoce el nombre del archivo de texto que desea abrir? ")
    if pr=="si":
        nom=input("Ingrese el nombre ")
    elif pr=="no":
        for dirpath, dirnames, filenames in os.walk("."):
            for name in filenames:
                if ".txt" in name:
                    print("Archivo",count,":",os.path.join(dirpath,name))
                    count +=1
        nombre=input("¿Que archivo desea abrir? ")
     
    cont=0
    while cont==0:
        Menu=int(input("¿Selecciona que opcion quieres?\n1)Agregar enlaces\n2)Leer enlaces\n3)Actualizar enlaces\n4)Modificar enlaces\n5)Hacer Busqueda Personalizada\n6)Salir\n"))
        if Menu == 1: #Agregar
            Fuentes=open("Fuentes.txt","a")
            agregarenlace=input("Ingresa el Link: ")
            Fuentes.write(agregarenlace+"\n")
            otro=input("Deseas agregar otro enlace?")
            if otro == "si":
                Fuentes=open("Fuentes.txt","a")
                agregarenlace=input("Ingresa el Link: ")
                Fuentes.write(agregarenlace+"\n")
                Fuentes.close()
                cont=0          
        elif Menu==2: #Leer
            with open("Fuentes.txt","r") as file:
                for line in file:
                    print(line)
        #Para que agregar y actualizar sean diferentes, en actualizar solo se podra agregar un link
        elif Menu==3: #Actualizar
            Fuentes=open("Fuentes.txt","a")
            agregarenlace=input("Ingresa el Link: ")
            Fuentes.write(agregarenlace+"\n")
            Fuentes.close()
            cont=0
        elif Menu==4: #Modificar
            Fuentes=open("Fuentes.txt","a")
            agregarenlace=input("Ingresa el Link: ")
            Fuentes.write(agregarenlace+"\n")
            Fuentes.close()
            cont=0
        elif Menu==5: #Busqueda en Google
            import Busqueda
            Busqueda.BusqPersonalizada()
            cont=0
        elif Menu==6: #Salir
            break



























