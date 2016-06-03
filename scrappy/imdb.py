#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import urllib.request as urllib2
import importlib.reload as reload
from bs4 import BeautifulSoup #sudo apt-get install python-bs4

reload(sys)
sys.setdefaultencoding('utf8')

imdb = "http://www.imdb.com"

pelicula = str(sys.argv[1].strip())
peli = str(pelicula.replace(" ","%20").strip())
url = imdb + "/find?q=" + peli + "&s=tt&ttype=ft&exact=true&ref_=fn_tt_ex"
ua = "Mozilla/5.0 (X11; Linux i686; rv:6.0.2) Gecko/20100101 Firefox/6.0.2"
h = {"User-Agent": ua}

peticion = urllib2.Request(url, headers=h)

#Descargo el recurso para luego leerlo y analizarlo
try:
	recurso = urllib2.urlopen(peticion)
except:
	print ("No se ha podido conectar a la web de los resultados")
	sys.exit()

#Leo y analizo el recurso
try:
	doc = BeautifulSoup(recurso.read())
except:
	print ("No se ha podido analizar correctamente el documento")
	sys.exit(-1)

#Busco en primer lugar que haya una pelicula que coincida exactamente con el criterio de busqueda
#Si no hay coincidencia exacta aborto el script.
try:
	h1 = doc.find("h1", {"class": "findHeader"})
	if h1.contents[0] == "No results found for ":
		print ("No existe ninguna pelicula que coincida con ese título")
		sys.exit(-1)
except:
	print ("Error en la busqueda de resultados")
	sys.exit()


#Llegados a este punto hay peliculas que se llaman como peli (puede haber varias)
try:
	td = doc.findAll("td", {"class": "result_text"})
	urls = []
	for t in td:
		a = t.find("a")

		#Obtengo solo las urls de aquellas que se llamen exactamente igual
		if a.get_text().lower() == pelicula.lower():
			url = imdb + a['href']
			#print "Obteniendo pagina " + url
			urls.append(url)
except:
	print ("No se ha podido conseguir la url de la pelicula")
	sys.exit()

for url in urls:
	peticion = urllib2.Request(url, headers=h)

	try:
		recurso = urllib2.urlopen(peticion)
	except:
		print ("No se ha podido conectar con la web de la pelicula")
		sys.exit()

	#Analizo el documento
	try:
		doc = BeautifulSoup(recurso.read())
	except:
		print ("No se ha podido leer el documento de la pelicula")
		sys.exit(-1)

	# Obtengo la nota
	try:
		h1 = doc.find("h1", {"itemprop": "name"})
		year = doc.find("span", {"id": "titleYear"})
		nota = doc.find("span", {"itemprop": "ratingValue"})
		print ("Nota IMDB para: %s %s " % (h1.get_text(), nota.get_text()))
	except AttributeError:
		h1 = doc.find("h1", {"itemprop": "name"})
		year = doc.find("span", {"id": "titleYear"})
		nota = doc.find("div", {"class": "notEnoughRatings"})
		print ("Nota IMDB para: %s SIN NOTA " % (h1.get_text()))

