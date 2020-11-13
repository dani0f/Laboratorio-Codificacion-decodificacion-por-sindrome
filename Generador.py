from random import choice,randrange
import codificador_decodificador as cod
import numpy as np

P=cod.Matriz_paridad()
G=cod.Matriz_generadora(P)
Ht=cod.H_transpuesta(P)
tabla_sindrome=cod.Tabla_sindrome(Ht)

def generar_30_archivos():
    for j in range(30):
        cadena=""
        for i in range(9):
            cadena=cadena+choice(["0","1"])
        output_file = open("datos_generados_"+str(j)+".txt", "w")
        output_file.write(cadena)
        output_file.close()

#se codifican los 30 archivos creados por generar_30, la matriz de paridad esta definida en archivo codificador_decodificador
def codificar_30_archivos():
    for i in range(30):
        C=cod.Codificacion(G,"datos_generados_"+str(i)+".txt")
        output_file = open("datos_generados_"+str(i)+".txt", "w")
        output_file.write(C)
        output_file.close()
        output_file = open("datos_generados_original"+str(i)+".txt", "w")
        output_file.write(C)
        output_file.close()

def generador_errores(prob,archivo_posicion_errores):
    prob=1/prob
    posicion_errores=""
    contador_errores=0
    for i in range(30):#cantidad de archivos
        contador_errores=0
        for j in range(13):#largo de archivo
            num_elegido=randrange(prob)
            if(num_elegido==5):
                contador_errores=contador_errores+1
                #print("se genero un error en archivo ",i,"bit en posicion ",j)
                file = open("datos_generados_"+str(i)+".txt")                 
                data = list(file.read())
                file.close()
                if(data[j] == "0"):
                    data[j]="1"
                else:
                    data[j]="0"
                #print(data)
                Strdata="".join(data)
                file = open("datos_generados_"+str(i)+".txt", "w") 
                file.write(Strdata)
                file.close()
        posicion_errores=posicion_errores+str(i)+","+str(contador_errores)+"\n"
        file = open(archivo_posicion_errores, "w") 
        file.write(posicion_errores)
        file.close()

def corregir_errores_30(archivo_resultados,bool_correcion):
    for i in range(30):
        cod.Decodificacion_sindrome(Ht,tabla_sindrome,"datos_generados_"+str(i)+".txt",i,archivo_resultados,bool_correcion)

def comparar_archivos(archivo):
    posicion_errores=""
    for i in range(30):
        file1 = open("datos_generados_"+str(i)+".txt")                 
        data1 = file1.read()     
        file1.close()
        file2 = open("datos_generados_original"+str(i)+".txt")                 
        data2 = file2.read() 
        file2.close()
        e=0
        for p in range(len(data1)):   
            if(data1[p]!=data2[p]):
                e=e+1
        #print(data1,"vs",data2,"errores",e)
        posicion_errores=posicion_errores+str(i)+","+str(e)+"\n"
    file = open(archivo, "w") 
    file.write(posicion_errores)
    file.close()




probabilidad=[0.1,0.01,0.001]
for i in range(len(probabilidad)):
    print("----------------------------PROBABILIDAD DE ",probabilidad[i])
    generar_30_archivos()  
    codificar_30_archivos()         
    generador_errores(probabilidad[i],archivo_posicion_errores="errores_antes_"+str(probabilidad[i])+".txt")
    corregir_errores_30("resultados_1_prob_"+ str(probabilidad[i]) +".txt",bool_correcion = 1)
    comparar_archivos("errores_despues_"+str(probabilidad[i])+".txt")
#graficos de varianza/media
