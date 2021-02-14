import requests,json,time
from datetime import datetime
#La probabilidad de lluvia se obtuvo de la documentación de la API
#En dicha documentación no venia la probabilidad de todo, solo agregamos la que si venia

def funcionClima():
    appid=input("Ingresa tu APPID: ")
    #Ámsterdam - Concierto 1 
    lat = "52.3740311"
    lon = "4.8896899"
    page= requests.get("https://api.openweathermap.org/data/2.5/onecall?lat="+lat+"&lon="+lon+"&exclude=minutely,hourly,daily&units=metric&appid="+appid)
    weatherData=json.loads(page.content)
    #Aqui sacamos la temperatura del día
    for elem in weatherData["current"]:
        if elem == "temp":
            T1=weatherData["current"][elem]
    #Aqui obtenemos la probabilidad de lluvia
    for key in weatherData["current"]["weather"][0]:
        if key == "id":
            if (weatherData["current"]["weather"][0][key]) == 801:
                PLL1= "Probabilidad de lluvia: 11-25%"
            elif (weatherData["current"]["weather"][0][key]) == 802:
                PLL1= "Probabilidad de lluvia: 25-50%"
            elif (weatherData["current"]["weather"][0][key]) == 803:
                PLL1= "Probabilidad de lluvia: 51-84%"
            elif (weatherData["current"]["weather"][0][key]) == 804:
                PLL1= "Probabilidad de lluvia: 85-100%"
    #Aqui obtenemos la salida y entrada del sol
    dt = 1591900805
    SS1=datetime.utcfromtimestamp(dt).strftime("%d-%m-%Y %H:%M:%S")
    ES1=time.strftime("%d-%m-%Y %H:%M:%S",time.localtime(dt))
    print("Clima del primer concierto obtenido")

    #Paris
    lat = "48.8534088"
    lon = "2.3487999"
    page= requests.get("https://api.openweathermap.org/data/2.5/onecall?lat="+lat+"&lon="+lon+"&exclude=minutely,hourly,daily&units=metric&appid="+appid)
    weatherData=json.loads(page.content)
    for elem in weatherData["current"]:
        if elem == "temp":
            T2=weatherData["current"][elem]
    for key in weatherData["current"]["weather"][0]:
        if key == "id":
            if (weatherData["current"]["weather"][0][key]) == 801:
                PLL2= "Probabilidad de lluvia: 11-25%"
            elif (weatherData["current"]["weather"][0][key]) == 802:
                PLL2= "Probabilidad de lluvia: 25-50%"
            elif (weatherData["current"]["weather"][0][key]) == 803:
                PLL2= "Probabilidad de lluvia: 51-84%"
            elif (weatherData["current"]["weather"][0][key]) == 804:
                PLL2= "Probabilidad de lluvia: 85-100%"         
    dt = 1591900805
    SS2=datetime.utcfromtimestamp(dt).strftime("%d-%m-%Y %H:%M:%S")
    ES2=time.strftime("%d-%m-%Y %H:%M:%S",time.localtime(dt))
    print("Clima del segundo concierto obtenido")

    #Nueva York
    lat = "40.66"
    lon = "-73.93"
    page= requests.get("https://api.openweathermap.org/data/2.5/onecall?lat="+lat+"&lon="+lon+"&exclude=minutely,hourly,daily&units=metric&appid="+appid)
    weatherData=json.loads(page.content)
    for elem in weatherData["current"]:
        if elem == "temp":
            T3=weatherData["current"][elem]
    for key in weatherData["current"]["weather"][0]:
        if key == "id":
            if (weatherData["current"]["weather"][0][key]) == 801:
                PLL3= "Probabilidad de lluvia: 11-25%"
            elif (weatherData["current"]["weather"][0][key]) == 802:
                PLL3= "Probabilidad de lluvia: 25-50%"
            elif (weatherData["current"]["weather"][0][key]) == 803:
                PLL3= "Probabilidad de lluvia: 51-84%"
            elif (weatherData["current"]["weather"][0][key]) == 804:
                PLL3= "Probabilidad de lluvia: 85-100%"         
    dt = 1591996452
    SS3=datetime.utcfromtimestamp(dt).strftime("%d-%m-%Y %H:%M:%S")
    ES3=time.strftime("%d-%m-%Y %H:%M:%S",time.localtime(dt))
    print("Clima del tercer concierto obtenido")
          
    #Buenos Aires
    lat = "-34.6131516"
    lon = "-58.3772316"
    page= requests.get("https://api.openweathermap.org/data/2.5/onecall?lat="+lat+"&lon="+lon+"&exclude=minutely,hourly,daily&units=metric&appid="+appid)
    weatherData=json.loads(page.content)
    for elem in weatherData["current"]:
        if elem == "temp":
            T4=weatherData["current"][elem]
    for key in weatherData["current"]["weather"][0]:
        if key == "id":
            if (weatherData["current"]["weather"][0][key]) == 801:
                PLL4= "Probabilidad de lluvia: 11-25%"
            elif (weatherData["current"]["weather"][0][key]) == 802:
                PLL4= "Probabilidad de lluvia: 25-50%"
            elif (weatherData["current"]["weather"][0][key]) == 803:
                PLL4= "Probabilidad de lluvia: 51-84%"
            elif (weatherData["current"]["weather"][0][key]) == 804:
                PLL4= "Probabilidad de lluvia: 85-100%"         
    dt = 1592082852
    SS4=datetime.utcfromtimestamp(dt).strftime("%d-%m-%Y %H:%M:%S")
    ES4=time.strftime("%d-%m-%Y %H:%M:%S",time.localtime(dt))
    print("Clima del cuarto concierto obtenido")

    #Madrid
    lat = "40.4165"
    lon = "-3.7025"
    page= requests.get("https://api.openweathermap.org/data/2.5/onecall?lat="+lat+"&lon="+lon+"&exclude=minutely,hourly,daily&units=metric&appid="+appid)
    weatherData=json.loads(page.content)
    for elem in weatherData["current"]:
        if elem == "temp":
            T5=weatherData["current"][elem]
    for key in weatherData["current"]["weather"][0]:
        if key == "id":
            if (weatherData["current"]["weather"][0][key]) == 801:
                PLL5= "Probabilidad de lluvia: 11-25%"
            elif (weatherData["current"]["weather"][0][key]) == 802:
                PLL5= "Probabilidad de lluvia: 25-50%"
            elif (weatherData["current"]["weather"][0][key]) == 803:
                PLL5= "Probabilidad de lluvia: 51-84%"
            elif (weatherData["current"]["weather"][0][key]) == 804:
                PLL5= "Probabilidad de lluvia: 85-100%"         
    dt = 1592082852
    SS5=datetime.utcfromtimestamp(dt).strftime("%d-%m-%Y %H:%M:%S")
    ES5=time.strftime("%d-%m-%Y %H:%M:%S",time.localtime(dt))
    print("Clima del quinto concierto obtenido")

    #Monterrey
    lat = "25.6714"
    lon = "-100.309"
    page= requests.get("https://api.openweathermap.org/data/2.5/onecall?lat="+lat+"&lon="+lon+"&exclude=minutely,hourly,daily&units=metric&appid="+appid)
    weatherData=json.loads(page.content)
    for elem in weatherData["current"]:
        if elem == "temp":
            T6=weatherData["current"][elem]
    for key in weatherData["current"]["weather"][0]:
        if key == "id":
            if (weatherData["current"]["weather"][0][key]) == 801:
                PLL6= "Probabilidad de lluvia: 11-25%"
            elif (weatherData["current"]["weather"][0][key]) == 802:
                PLL6= "Probabilidad de lluvia: 25-50%"
            elif (weatherData["current"]["weather"][0][key]) == 803:
                PLL6= "Probabilidad de lluvia: 51-84%"
            elif (weatherData["current"]["weather"][0][key]) == 804:
                PLL6= "Probabilidad de lluvia: 85-100%"         
    dt = 1592169252
    SS6=datetime.utcfromtimestamp(dt).strftime("%d-%m-%Y %H:%M:%S")
    ES6=time.strftime("%d-%m-%Y %H:%M:%S",time.localtime(dt))
    print("Clima del sexto concierto obtenido")

    #Londres
    lat = "51.5072"
    lon = "-0.1275"
    page= requests.get("https://api.openweathermap.org/data/2.5/onecall?lat="+lat+"&lon="+lon+"&exclude=minutely,hourly,daily&units=metric&appid="+appid)
    weatherData=json.loads(page.content)
    for elem in weatherData["current"]:
        if elem == "temp":
            T7=weatherData["current"][elem]
    for key in weatherData["current"]["weather"][0]:
        if key == "id":
            if (weatherData["current"]["weather"][0][key]) == 801:
                PLL7= "Probabilidad de lluvia: 11-25%"
            elif (weatherData["current"]["weather"][0][key]) == 802:
                PLL7= "Probabilidad de lluvia: 25-50%"
            elif (weatherData["current"]["weather"][0][key]) == 803:
                PLL7= "Probabilidad de lluvia: 51-84%"
            elif (weatherData["current"]["weather"][0][key]) == 804:
                PLL7= "Probabilidad de lluvia: 85-100%"         
    dt = 1592169252
    SS7=datetime.utcfromtimestamp(dt).strftime("%d-%m-%Y %H:%M:%S")
    ES7=time.strftime("%d-%m-%Y %H:%M:%S",time.localtime(dt))
    print("Clima del septimo concierto obtenido")

    #Tokio
    lat = "35.6894"
    lon = "139.692"
    page= requests.get("https://api.openweathermap.org/data/2.5/onecall?lat="+lat+"&lon="+lon+"&exclude=minutely,hourly,daily&units=metric&appid="+appid)
    weatherData=json.loads(page.content)
    for elem in weatherData["current"]:
        if elem == "temp":
            T8=weatherData["current"][elem]
    for key in weatherData["current"]["weather"][0]:
        if key == "id":
            if (weatherData["current"]["weather"][0][key]) == 801:
                PLL8= "Probabilidad de lluvia: 11-25%"
            elif (weatherData["current"]["weather"][0][key]) == 802:
                PLL8= "Probabilidad de lluvia: 25-50%"
            elif (weatherData["current"]["weather"][0][key]) == 803:
                PLL8= "Probabilidad de lluvia: 51-84%"
            elif (weatherData["current"]["weather"][0][key]) == 804:
                PLL8= "Probabilidad de lluvia: 85-100%"         
    dt = 1592255652
    SS8=datetime.utcfromtimestamp(dt).strftime("%d-%m-%Y %H:%M:%S")
    ES8=time.strftime("%d-%m-%Y %H:%M:%S",time.localtime(dt))
    print("Clima del octavo concierto obtenido")

    #Bruselas
    lat = "50.85044"
    lon = "4.348780"
    page= requests.get("https://api.openweathermap.org/data/2.5/onecall?lat="+lat+"&lon="+lon+"&exclude=minutely,hourly,daily&units=metric&appid="+appid)
    weatherData=json.loads(page.content)
    for elem in weatherData["current"]:
        if elem == "temp":
            T9=weatherData["current"][elem]
    for key in weatherData["current"]["weather"][0]:
        if key == "id":
            if (weatherData["current"]["weather"][0][key]) == 801:
                PLL9= "Probabilidad de lluvia: 11-25%"
            elif (weatherData["current"]["weather"][0][key]) == 802:
                PLL9= "Probabilidad de lluvia: 25-50%"
            elif (weatherData["current"]["weather"][0][key]) == 803:
                PLL9= "Probabilidad de lluvia: 51-84%"
            elif (weatherData["current"]["weather"][0][key]) == 804:
                PLL9= "Probabilidad de lluvia: 85-100%"         
    dt = 1592342052
    SS9=datetime.utcfromtimestamp(dt).strftime("%d-%m-%Y %H:%M:%S")
    ES9=time.strftime("%d-%m-%Y %H:%M:%S",time.localtime(dt))
    print("Clima del noveno concierto obtenido")

    #São Paulo
    lat = "-23.5475"
    lon = "-46.6361"
    page= requests.get("https://api.openweathermap.org/data/2.5/onecall?lat="+lat+"&lon="+lon+"&exclude=minutely,hourly,daily&units=metric&appid="+appid)
    weatherData=json.loads(page.content)
    for elem in weatherData["current"]:
        if elem == "temp":
            T10=weatherData["current"][elem]
    for key in weatherData["current"]["weather"][0]:
        if key == "id":
            if (weatherData["current"]["weather"][0][key]) == 801:
                PLL10= "Probabilidad de lluvia: 11-25%"
            elif (weatherData["current"]["weather"][0][key]) == 802:
                PLL10= "Probabilidad de lluvia: 25-50%"
            elif (weatherData["current"]["weather"][0][key]) == 803:
                PLL10= "Probabilidad de lluvia: 51-84%"
            elif (weatherData["current"]["weather"][0][key]) == 804:
                PLL10= "Probabilidad de lluvia: 85-100%"         
    dt = 1592428452
    SS10=datetime.utcfromtimestamp(dt).strftime("%d-%m-%Y %H:%M:%S")
    ES10=time.strftime("%d-%m-%Y %H:%M:%S",time.localtime(dt))
    print("Clima del decimo concierto obtenido")
