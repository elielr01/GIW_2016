import csv


def aguaControlada():
    
    archivoAgua = open("agua_eprtr_2008_030412.csv")
    lectorAgua = csv.reader(archivoAgua, delimiter=";")
    diccionario = dict()
    for linea in lectorAgua:
        if lectorAgua.line_num > 2:
            linea8 = str(linea[8])
            linea2 = str(linea[2])
            if  linea8 in diccionario:   
                diccionario[linea8].append(linea2)
            else:
                diccionario[linea8] = [linea2]

                
    archivoWrite = open("AguaAgrupada.csv", "w")
    salidaEscrito = csv.writer(archivoWrite)
    salidaEscrito.writerow(["Contaminacion", "Empresa"])
    for linea in diccionario:
        for lin in diccionario[linea]:
            salidaEscrito.writerow([ linea + ',' + lin ])
    archivoWrite.close()




def numFrecuencia():

    archivoRes = open("residuos_peligrosos_eprtr_2008_040412.csv")
    lectorRes = csv.reader(archivoRes, delimiter=";")
    diccionario = dict()
    for linea in lectorRes:      
        if lectorRes.line_num > 2:
            linea2 = str(linea[2])
            if linea2 in diccionario:   
                diccionario[linea2] += 1
            else:
                diccionario[linea2] = 1


    archivoWrite = open("FrecuenciaResiduos.csv", "w")
    salidaEscrito = csv.writer(archivoWrite)
    salidaEscrito.writerow(["Empresa","Frecuencia"])
    for linea in diccionario:
        salidaEscrito.writerow([linea, diccionario[linea]])

    archivoWrite.close()


#########holaaaaaaaaaaaaaaaaaaa

def infoEmpresas():

    archivoRes = open("aire_eprtr_2008_030412.csv")
    lectorRes = csv.reader(archivoRes, delimiter=";")
    diccionario = dict()
    for linea in lectorRes:
        if lectorRes.line_num > 2:
            linea2 = str(linea[2])
            linea10 = str(linea[10])
            aux = linea[10].split(",")
            linea10 = ".".join(aux)
        
            if linea2 in diccionario:   
                diccionario[linea2] += float(linea10)
            else:
                diccionario[linea2] = float(linea10)
        

    archivoWrite = open("Contaminantes.csv", "w")
    salidaEscrito = csv.writer(archivoWrite)
    lista = []
    i = 0
    menor = i
    for linea in diccionario:
        if len(lista) <= 10:
            lista.append(linea)
            if(diccionario[linea] < lista[menor]):
                menor = len(lista) - 1
        elif(diccionario[linea] < lista[menor]):
            lista[menor] = linea
    

    for linea in lista:
        salidaEscrito.writerow([linea, diccionario[linea]])
             
    archivoWrite.close()

aguaControlada()
numFrecuencia()
infoEmpresas()
