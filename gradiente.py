#------------ EJEMPLO DE CORRIDA DE PRUEBA
#--- python gradiente.py xp1.csv yp1.csv 0.01 7


#!/usr/bin/python
#!dar permisos de ejecucion

# -*- coding: utf-8 -*-

import sys
import os
import shutil
import csv
#from decimal import *

print "...:::Gradiente Descendente:::..."

filCsv = open('funcionCosto.csv','w')
wrtEscritor = csv.writer(filCsv,delimiter=',',quotechar=';',quoting=csv.QUOTE_MINIMAL)
wrtEscritor.writerow(['funcionCosto'])
filCsv.close()

#!--- inicio
variables = 3
theta = [1,1,1]
X = [0,0,0]
Y = 0 
alfa = float(sys.argv[3]) #0.01
#!tolerancia, numero maximo de iteraciones
n = int(sys.argv[4]) #3
m = 4
contador = 0
#!salida, escribir parametros theta
#!archivo csv con el valor de la funcion de costo
#ejemplo m 4 n 3

while contador<n:
	print "----------- Iteracion No. " + str(contador) + "------------"
	#!--- obtener valores de Xi
	strNombreArchivoX = sys.argv[1]
	filArchivoX = open(strNombreArchivoX,'r')
	rdrLectorX = csv.reader(filArchivoX,delimiter=',')
	
	for indice,linea in enumerate(rdrLectorX):
		if indice == contador:
			#print "Linea X: " + str(indice)
			X[0] = linea[0]
			X[1] = linea[1]
			X[2] = linea[2]
			print "Valores de X: " + str(X[0]) + ", " + str(X[1]) + ", " + str(X[2])
	filArchivoX.close()

	#--- obtener valores de Y
	strNombreArchivoY = sys.argv[2]
	filArchivoY = open(strNombreArchivoY,'r')
	rdrLectorY = csv.reader(filArchivoY,delimiter=',')
	
	for indice,linea in enumerate(rdrLectorY):
		if indice == contador:
			#print "Linea Y: " + str(indice)
			Y = linea[0]
			print "Valor de Y: " + str(Y)
	filArchivoY.close()

	#subindice de variables theta	
	i = 0
	#--- calculando theta_i
	dJi = 0
	while i < variables:
		mwh = 1
		while mwh <= m:
			dJi = float(dJi) + ((float(theta[0])*float(X[0]) + float(theta[1])*float(X[1]) + float(theta[2])*float(X[2])) - float(Y)) * float(X[i])
			#print "dJi interno No." + str(mwh) + ": " + str(dJi)
			mwh = int(mwh)+1
		dJi = (float('1')/float(m)) * float(dJi)
		print "dJi: " + str(dJi)
		theta[i] = float(theta[i]) - (float(alfa)*float(dJi))
		print "theta" + str(i) + ": " + str(theta[i]) 
		i = int(i) + 1

#--- calcular el valor de la funcion de costo
	mwh = 1
	Jthi = 0

	while mwh < m:
		Jthi = float(Jthi) + (float('1')/(float('2')*float(m))) * (( (float(theta[0])*float(X[0]) + float(theta[1])*float(X[1]) + float(theta[2])*float(X[2])) - float(Y) )**float('2')) 
		mwh = int(mwh) + 1
	print "Valor de la funcion de costo: " + str(Jthi)
	#a: append, w: sobreescribir
	filCsv = open('funcionCosto.csv','a')
	wrtEscritor = csv.writer(filCsv,delimiter=',',quotechar=';',quoting=csv.QUOTE_MINIMAL)
	wrtEscritor.writerow([str(Jthi)])
	filCsv.close()
	contador = int(contador) + 1

#--- fin

#------------------- Notas ----------------------------------------
#h(X0,X1,X2) = th0*X0 + th1*X1 + th2*X2
#fth0 = th0 - alfa * (dJ/dth0)
#--- abrir archivo
#strNombreArchivo = sys.argv[0]
#filArchivo = open(strNombreArchivo,'r')
#for line in filArchivo:
#	print(line)
#filArchivo.close()

#strNombreArchivo = sys.argv[1]
#filArchivo = open(strNombreArchivo,'r')
#rdrLector = csv.reader(filArchivo,delimiter=',')
#for indice,linea in enumerate(rdrLector):
	#linea = line.split(',')
#	print "------- Linea: " + str(indice)
#	x0 = linea[0]
#	x1 = linea[1]	
#	x2 = linea[2]
#	print x0 + "," + x1 + "," + x2
#filArchivo.close() 


#rdrLector.index(linea)
#--- escribir archivo
#--- graficar
#--- generar numeros aleatorios
