# -*- coding: utf-8 -*-
import csv

reader = csv.reader(open("../multas.csv"), delimiter=";")

first_line = "#,INCIDENT TITLE,INCIDENT, DATE,LOCATION,DESCRIPTION,CATEGORY,APPROVED,VERIFIED\n"

out = open("out_multas.csv", "w")
out.write(first_line)

#"1","Amenazas en Parque Hernandez","2009-05-15 01:06:00","Santa  Tecla","Amenazas a comerciantes, etc, etc","AMENAZAS",YES,YES
#exp; sancionado; dni; localidad; fecha; matricula; euros; precepto; articulo; puntos; observaciones
#020044066564;EL FARH , ABDELKADER;X4297581P;LA RODA;2011-05-22;M 6448MP;1500.00;RDL 8/2004;003.A;0;a
line = "%d, \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", %s, %s\n"

i = 0
reader.next()
for row in reader:
    i += 1
    out.write( line % (i, row[7]+" "+row[8], row[6]+" €, "+row[9]+" puntos", row[4], row[3]+",Spain", row[7]+" "+row[8], " ", "YES", "YES") )
