# -*- coding: utf-8 -*-
import csv

reader = csv.reader(open("../multas.csv"), delimiter=";")

first_line = "fecha, total\n"

out = open("../multas_agregado.csv", "w")
out.write(first_line)

#"1","Amenazas en Parque Hernandez","2009-05-15 01:06:00","Santa  Tecla","Amenazas a comerciantes, etc, etc","AMENAZAS",YES,YES
#exp; sancionado; dni; localidad; fecha; matricula; euros; precepto; articulo; puntos; observaciones
#020044066564;EL FARH , ABDELKADER;X4297581P;LA RODA;2011-05-22;M 6448MP;1500.00;RDL 8/2004;003.A;0;a
line = "%s, %d\n"

fechas = {}
reader.next()
for row in reader:
    if not fechas.has_key(row[4]): fechas[row[4]] = 0 
    fechas[row[4]] += float(row[6])

for fecha in fechas:
    out.write( line % (fecha, fechas[fecha] ) )
