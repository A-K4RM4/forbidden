#Integrantes del equipo QuaranTeam
#Roberto Almaguer Garza             1862977
#Bárbara Azalia Cantú Peña          1986233
#Jair Caleb Hernández Polendo      1923292
#Jared Abraham Perez Guerrero       1863721
#Alejandra Nohemí Tamez Montes      1925345

import os, requests, re
from bs4 import BeautifulSoup as bs
print("Aqui inicia el programa")
import Menu
Menu.funcionMenu()
print("A continuación usando las Expresiones Regulares obtenemos la información significativa")
import RegExp
RegExp.funcionRegExp()
print("A continuación utilizando la Api obtenemos la información del clima de la gira")
import Clima
Clima.funcionClima()
print("A continuación creamos el Excel y almacenamos la información obtenida")
import Excel
Excel.funcionExcel()
print("Aquí termina el programa")































