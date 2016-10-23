import csv


def aguaControlada():
    
    #abrimos archivo
    archivoAgua = open("agua_eprtr_2008_030412.csv")
    lectorAgua = csv.reader(archivoAgua, delimiter=";")
    diccionario = dict()
    
    #recorremos el lector
    for linea in lectorAgua:
        #quitamos las 2 ineas primeras
        if lectorAgua.line_num > 2:
            linea8 = str(linea[8])
            linea2 = str(linea[2])
            #dependiendo si esta o no en el diccionario
            if  linea8 in diccionario:   
                diccionario[linea8].append(linea2)
            else:
                diccionario[linea8] = [linea2]

    #guardamos en el otro archivo lo almacenado en el diccionario           
    archivoWrite = open("AguaAgrupada.csv", "w")
    salidaEscrito = csv.writer(archivoWrite)
    salidaEscrito.writerow(["Contaminacion", "Empresa"])
    for linea in diccionario:
        for lin in diccionario[linea]:
            salidaEscrito.writerow([ linea + ',' + lin ])
    archivoWrite.close()




def numFrecuencia():

    #abrimos archivo CSV y creamos diccionario
    archivoRes = open("residuos_peligrosos_eprtr_2008_040412.csv")
    lectorRes = csv.reader(archivoRes, delimiter=";")
    diccionario = dict()
    for linea in lectorRes:      
        if lectorRes.line_num > 2:
            linea2 = str(linea[2])
            #vamos recopilando las veces que aparece
            if linea2 in diccionario:   
                diccionario[linea2] += 1
            else:
                diccionario[linea2] = 1

    #guardamos en otro archivo CSV
    archivoWrite = open("FrecuenciaResiduos.csv", "w")
    salidaEscrito = csv.writer(archivoWrite)
    salidaEscrito.writerow(["Empresa","Frecuencia"])
    for linea in diccionario:
        salidaEscrito.writerow([linea, diccionario[linea]])

    archivoWrite.close()


def infoEmpresas():

    #abrimos archivo CSV y recorremos el lector
    archivoRes = open("aire_eprtr_2008_030412.csv")
    lectorRes = csv.reader(archivoRes, delimiter=";")
    diccionario = dict()
    for linea in lectorRes:
        if lectorRes.line_num > 2:
            linea2 = str(linea[2])
            linea10 = str(linea[10])
            #convertimos la cantidad
            aux = linea[10].split(",")
            linea10 = ".".join(aux)
        
        #vamos acumulando en el diccionario
            if linea2 in diccionario:   
                diccionario[linea2] += float(linea10)
            else:
                diccionario[linea2] = float(linea10)
        
    #abrimos el archivo CSV para escribir
    archivoWrite = open("Contaminantes.csv", "w")
    salidaEscrito = csv.writer(archivoWrite)
    lista = []
    # a continuacion, algoritmo para almacenar los menores
    i = 0
    menor = i
    for linea in diccionario:
        if len(lista) <= 10:
            lista.append(linea)
            if(diccionario[linea] < lista[menor]):
                menor = len(lista) - 1
        elif(diccionario[linea] < lista[menor]):
            lista[menor] = linea
    
    #recorremos la lista y vamos guardando
    for linea in lista:
        salidaEscrito.writerow([linea, diccionario[linea]])
             
    archivoWrite.close()

aguaControlada()
numFrecuencia()
infoEmpresas()
