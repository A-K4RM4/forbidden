def funcionRegExp():
    import os, re, requests
    from bs4 import BeautifulSoup as bs
    #El grupo (0)es todo el mensaje de Reynolds/grupo(1) es la fecha/grupos(2,3,4)corresponden a d/m/a /grupo(5) es el lugar,(6 y 7) son la ciudad y estado
    patnDR=re.compile(r' naciÃ³ el ((\d{2}) de (\w+) de (\d{4})) en ((\w+) (\w+))')
    #Grupo(1) es la fecha de Platzman/Gpos(2,3,4) son d/m/a 
    patnDJ=re.compile(r' nacido el ((\d{2}) de (\w+) de (\d{4}))')
    #Grupo(1) aqui corresponde al lugar de nacimiento de Platzman
    patlDJ=re.compile(r'naciÃ³ en ((\w+), (\w+))')
    #Grupo(1) fecha nacimiento de Benjamin
    patnBAM=re.compile(r'naciÃ³ el ((\d{2}) de (\w+) de (\d{4}))')
    #Grupo(1) lugar de nacimineto de Ben
    patlBAM=re.compile(r' en ((\w+) en (\w+))')
    #Ojo aqui, el grupo 1 es el lugar y el grupo 4 es la fecha, Wayne es el unico que tiene un orden de busqueda de su info distinto
    patnDW=re.compile(r'naciÃ³ en ((\w+) (\w+)) el ((\d{2}) de (\w+) de (\d{4}))')
        
    directorio = "C:/Paginas"
    try:
        os.mkdir(directorio)
    except OSError:
        print("En el directorio %s estan guardadas las fuentes a usar" % directorio)
    else:
        print("Las paginas se guardaran en el achivo creado en el directorio: %s " % directorio)

    r = requests.get('https://www.imaginedragonsmusic.com/')
    soup = bs(r.content,"html.parser") #Clase beautifulSoup
    print (soup.prettify())
    #Creamos un archivo html para referencia
    fo = open ("C:/Paginas/Pagina1.txt","w", encoding="utf-8")
    fo.write (str(soup.prettify()))
    fo.close()
    print("Pagina 1 Guardada Exitosamente")

    #Cerramos el archivo html
    r = requests.get('https://imagine-dragons.fandom.com/es/wiki/Dan_Reynolds')
    soup = bs(r.content,"html.parser") #Clase beautifulSoup
    print (soup.prettify())
    #Creamos un archivo html para referencia
    fo = open ("C:/Paginas/Integrante1.txt","w", encoding="utf-8")
    fo.write (str(soup.prettify()))
    fo.close()
    print("Pagina 2 Guardada Exitosamente")
    #Cerramos el archivo html
    #Leemos el txt para sacar informacion
    with open ("C:/Paginas/Integrante1.txt",'r') as file:
        for line in file:
            if " naciÃ³ el" in line:
                patron=patnDR.search(line)
                fechaDR=patron.group(1)
                lugarDR=patron.group(5)
                break

    r = requests.get('https://imagine-dragons.fandom.com/es/wiki/Daniel_Platzman')
    soup = bs(r.content,"html.parser") #Clase beautifulSoup
    print (soup.prettify())
    #Creamos un archivo html para referencia
    fo = open ("C:/Paginas/Integrante2.txt","w", encoding="utf-8")
    fo.write (str(soup.prettify()))
    fo.close()
    print("Pagina 3 Guardada Exitosamente")
    #Cerramos el archivo html
    #Leemos el txt para sacar informacion
    with open ("C:/Paginas/Integrante2.txt",'r') as file:
        for line in file:
            if "nacido el" in line:
                patron=patnDJ.search(line)
                fechaDJ=patron.group(1)
                break
    with open ("C:/Paginas/Integrante2.txt",'r') as file:
        for line in file:
            if "naciÃ³ en" in line:
                patl=patlDJ.search(line)
                lugarDJ=patl.group(1)
                break

    r = requests.get('https://imagine-dragons.fandom.com/es/wiki/Ben_McKee')
    soup = bs(r.content,"html.parser") #Clase beautifulSoup
    print (soup.prettify())
    #Creamos un archivo html para referencia
    fo = open ("C:/Paginas/Integrante3.txt","w", encoding="utf-8")
    fo.write (str(soup.prettify()))
    fo.close()
    print("Pagina 4 Guardada Exitosamente")
    #Cerramos el archivo html
    #Leemos el txt para sacar informacion
    with open ("C:/Paginas/Integrante3.txt",'r') as file:
        for line in file:
            if " naciÃ³ el" in line:
                patron=patnBAM.search(line)
                fechaBAM=patron.group(1)
                break
    with open ("C:/Paginas/Integrante3.txt",'r') as file:
        for line in file:
            if "Ben viviÃ³" in line:
                patlb=patlBAM.search(line)
                lugarBAM=patlb.group(1)
                lugarBAM=patron.group(1)
                break
    
    r = requests.get('https://imagine-dragons.fandom.com/es/wiki/Wayne_Sermon')
    soup = bs(r.content,"html.parser") #Clase beautifulSoup
    print (soup.prettify())
    #Creamos un archivo html para referencia
    fo = open ("C:/Paginas/Integrante4.txt","w", encoding="utf-8")
    fo.write (str(soup.prettify()))
    fo.close()
    print("Pagina 5 Guardada Exitosamente")
    #Cerramos el archivo html
    #Leemos el txt para sacar informacion
    with open ("C:/Paginas/Integrante4.txt",'r') as file:
        for line in file:
            if " naciÃ³ en" in line:
                patron=patnDW.search(line)
                lugarDW=patron.group(1)
                fechaDW=patron.group(4)
                break

def funcionRegExp2():
    import os, re, requests
    from bs4 import BeautifulSoup as bs
    #El grupo (0)es todo el mensaje de Reynolds/grupo(1) es la fecha/grupos(2,3,4)corresponden a d/m/a /grupo(5) es el lugar,(6 y 7) son la ciudad y estado
    patnDR=re.compile(r' naciÃ³ el ((\d{2}) de (\w+) de (\d{4})) en ((\w+) (\w+))')
    #Grupo(1) es la fecha de Platzman/Gpos(2,3,4) son d/m/a 
    patnDJ=re.compile(r' nacido el ((\d{2}) de (\w+) de (\d{4}))')
    #Grupo(1) aqui corresponde al lugar de nacimiento de Platzman
    patlDJ=re.compile(r'naciÃ³ en ((\w+), (\w+))')
    #Grupo(1) fecha nacimiento de Benjamin
    patnBAM=re.compile(r'naciÃ³ el ((\d{2}) de (\w+) de (\d{4}))')
    #Grupo(1) lugar de nacimineto de Ben
    patlBAM=re.compile(r' en ((\w+) en (\w+))')
    #Ojo aqui, el grupo 1 es el lugar y el grupo 4 es la fecha, Wayne es el unico que tiene un orden de busqueda de su info distinto
    patnDW=re.compile(r'naciÃ³ en ((\w+) (\w+)) el ((\d{2}) de (\w+) de (\d{4}))')
        
    directorio = "C:/Paginas"
    r = requests.get('https://www.imaginedragonsmusic.com/')
    soup = bs(r.content,"html.parser") #Clase beautifulSoup
    #Creamos un archivo html para referencia
    fo = open ("C:/Paginas/Pagina1.txt","w", encoding="utf-8")
    fo.write (str(soup.prettify()))
    fo.close()

    #Cerramos el archivo html
    r = requests.get('https://imagine-dragons.fandom.com/es/wiki/Dan_Reynolds')
    soup = bs(r.content,"html.parser") #Clase beautifulSoup
    #Creamos un archivo html para referencia
    fo = open ("C:/Paginas/Integrante1.txt","w", encoding="utf-8")
    fo.write (str(soup.prettify()))
    fo.close()
    #Cerramos el archivo html
    #Leemos el txt para sacar informacion
    with open ("C:/Paginas/Integrante1.txt",'r') as file:
        for line in file:
            if " naciÃ³ el" in line:
                patron=patnDR.search(line)
                fechaDR=patron.group(1)
                lugarDR=patron.group(5)
                break

    r = requests.get('https://imagine-dragons.fandom.com/es/wiki/Daniel_Platzman')
    soup = bs(r.content,"html.parser") #Clase beautifulSoup
    #Creamos un archivo html para referencia
    fo = open ("C:/Paginas/Integrante2.txt","w", encoding="utf-8")
    fo.write (str(soup.prettify()))
    fo.close()
    #Cerramos el archivo html
    #Leemos el txt para sacar informacion
    with open ("C:/Paginas/Integrante2.txt",'r') as file:
        for line in file:
            if "nacido el" in line:
                patron=patnDJ.search(line)
                fechaDJ=patron.group(1)
                break
    with open ("C:/Paginas/Integrante2.txt",'r') as file:
        for line in file:
            if "naciÃ³ en" in line:
                patl=patlDJ.search(line)
                lugarDJ=patl.group(1)
                break

    r = requests.get('https://imagine-dragons.fandom.com/es/wiki/Ben_McKee')
    soup = bs(r.content,"html.parser") #Clase beautifulSoup
    #Creamos un archivo html para referencia
    fo = open ("C:/Paginas/Integrante3.txt","w", encoding="utf-8")
    fo.write (str(soup.prettify()))
    fo.close()
    #Cerramos el archivo html
    #Leemos el txt para sacar informacion
    with open ("C:/Paginas/Integrante3.txt",'r') as file:
        for line in file:
            if " naciÃ³ el" in line:
                patron=patnBAM.search(line)
                fechaBAM=patron.group(1)
                break
    with open ("C:/Paginas/Integrante3.txt",'r') as file:
        for line in file:
            if "Ben viviÃ³" in line:
                patlb=patlBAM.search(line)
                lugarBAM=patlb.group(1)
                lugarBAM=patron.group(1)
                break
    
    r = requests.get('https://imagine-dragons.fandom.com/es/wiki/Wayne_Sermon')
    soup = bs(r.content,"html.parser") #Clase beautifulSoup
    #Creamos un archivo html para referencia
    fo = open ("C:/Paginas/Integrante4.txt","w", encoding="utf-8")
    fo.write (str(soup.prettify()))
    fo.close()
    #Cerramos el archivo html
    #Leemos el txt para sacar informacion
    with open ("C:/Paginas/Integrante4.txt",'r') as file:
        for line in file:
            if " naciÃ³ en" in line:
                patron=patnDW.search(line)
                lugarDW=patron.group(1)
                fechaDW=patron.group(4)
                break
