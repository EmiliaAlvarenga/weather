import json
import requests

#Creamos una cadena en la que almacenamos todas las opciones deseadas

cadena = """
1. Almeria
2. Cadiz
3. Cordoba
4. Granada
5. Huelva
6. Jaen
7. Malaga
8. Sevilla
"""
print cadena

# creacion del diccionario en python, el la que indicamos el la clave y el valor. 
dicc_ciudad={'1':'Almeria','2':'Cadiz','3':'Cordoba','4':'Granada','5':'Huelva','6':'Jaen','7':'Malaga','8':'Sevilla'}

# vamos a utilizar la api de estado del tiempo de: http://api.openweathermap.org
# preguntamos de cual de las provincias, se desea conocer el tiempo que hace

id_ciudad=raw_input("De que ciudad quieres saber la temperatura actual? : ")

# buscamos en el diccionario que creamos el valor de la clave se ha seleccionado

provincia=dicc_ciudad[id_ciudad]

# se realiza la consulta utilizando los parametros donde en este caso spain es una constante
respuesta=requests.get("http://api.openweathermap.org/data/2.5/weather?",params={'q':'%s,spain' %provincia})

# guardamos la respuesta obtenida desde el sitio en un archivo de texto plano
datos= respuesta.text

# la respuesta que obtuvimos esta en formato json por lo que podemos cargarlo de la manera siguiente:
dicc_api=json.loads(datos)

# los datos de la temperatura estan en grados celcius por lo que en este
kelvin=dicc_api["main"]["temp"]
celcius=kelvin-273
print "La temperatura en %s es de: %.2f grados centigrados"% (provincia,celcius)
