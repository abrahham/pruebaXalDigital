## Utilizo el lenguaje de python ya que con este es muy fácil de manejar conjuntos de datos
import json
import requests
import datetime
# 1. cargar data
url = "https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow"
respuesta = json.loads(requests.get(url).text)

print("*** Punto 2 - Obteniendo respuestas contestadas y no contestadas***")
#	2. Obteniendo respuestas contestadas y no contestadas
contestadas = 0
noContestadas = 0
for obj in respuesta["items"]:
	if obj["is_answered"]:
		contestadas += 1
	else:
		noContestadas += 1
		
print("Contestadas:\t" + str(contestadas))
print("No contestadas:\t" + str(noContestadas))


print("*** Punto 3 - Obtener la respuesta con menor número de vistas***")
# 3. Obtener la respuesta con menor número de vistas
menorVista = {}
vistas = 0
for obj in respuesta["items"]:
	if(vistas < obj["view_count"]):
		menorVista = obj
		visas = obj["view_count"]

print("Id y título:\t" + str(menorVista["question_id"]) + ", " + menorVista["title"]
	+ "\nCantidad de vistas:\t" + str(menorVista["view_count"])
)


print("*** Punto 4 - Obtener la respuesta más vieja y más actual***")
# 4. Obtener la respuesta más vieja y más actual
fechas = []
for obj in respuesta["items"]:     #min_price = min(item['price'] for item in items)
	fechas.append(obj["creation_date"])
respAntigua = min(fechas)
respActual = max(fechas)
for obj in respuesta["items"]:
	if(respAntigua == obj["creation_date"]):
		valAntigua = obj
	if(respActual == obj["creation_date"]):
		valActual = obj
		
print("-Más antigua-")	
print("Título:\t" + valAntigua["title"]
	+ "\nId:\t" + str(valAntigua["question_id"])
	+ "\nFecha:\t" + str(datetime.datetime.fromtimestamp(valAntigua["creation_date"]))[:10])
print("-Más actual-")	
print("Título:\t" + valActual["title"]
	+"\nId:\t" + str(valActual["question_id"])
	+"\nFecha:\t" + str(datetime.datetime.fromtimestamp(valActual["creation_date"]))[:10])


print("*** Punto 5 - Obtener la respuesta del owner que tenga una mayor reputación***")
# 5. Obtener la respuesta del owner que tenga una mayor reputación
duenio = {}
reputacion = 0;
for	obj in respuesta["items"]:
	if(obj["owner"]["reputation"] >= reputacion):
		duenio = {
			"respuesta":{
				"id":obj["question_id"],"titulo":obj["title"]
			},"usuario":{
				"id":obj["owner"]["user_id"],"nombre":obj["owner"]["display_name"],
				"reputacion":obj["owner"]["reputation"],
			}
		}
		reputacion = obj["owner"]["reputation"]
print("Título e id:\t" + duenio["respuesta"]["titulo"] + ", " + str(duenio["respuesta"]["id"])
	+ "\nId, nombre y reputación de usuario:\t" + str(duenio["usuario"]["id"]) + ", " + duenio["usuario"]["nombre"] + ", "
	+ str(duenio["usuario"]["reputacion"])
)




