def BusqPersonalizada():
    import os, time,random
    fo=open("Busqueda.txt","w")
    try:
        from googlesearch import search
    except ImportError:
        os.system('pip install google')
        print('installing google... Ejecute de nuevo')
        exit()

    query = input('¿Qué quiere buscar?: ')
    print('Buscando...Espere un momento ')
    time.sleep(2)
    selec = random.randint(0,14)
    valor=0
    for enlace in search(query, tld="com", num=15, stop=15, pause=5):
        print(enlace)
        fo = open('Busqueda.txt','a')
        fo.write ("\n")
        fo.write(enlace)
        if valor == selec:
            print(selec,enlace)
            break
        valor += 1
    fo.close()

