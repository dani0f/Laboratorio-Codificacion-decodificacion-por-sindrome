from random import choice,randrange
import codificador_decodificador as cod
import numpy as np

P=cod.Matriz_paridad()
G=cod.Matriz_generadora(P)

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

def generador_errores(prob):
    prob=1/prob
    print(prob)
    posicion_errores=""
    contador_errores=0
    for i in range(30):#cantidad de archivos
        for j in range(12):#largo de archivo
            num_elegido=randrange(prob)
            if(num_elegido==5):
                print("se genero un error en archivo ",i,"bit en posicion ",j)
                file = open("datos_generados_"+str(i)+".txt")                 
                data = list(file.read())
                file.close()
                print(data)
                contador_errores=contador_errores+1
                posicion_errores=posicion_errores+"[error: "+str(contador_errores)+" archivo: "+str(i)+" bit "+str(j)+" ]\n"
                if(data[j] == "0"):
                    data[j]="1"
                else:
                    data[j]="0"
                print(data)
                Strdata="".join(data)
                file = open("datos_generados_"+str(i)+".txt", "w") 
                file.write(Strdata)
                file.close()
        file = open("Posicion_errores_generador.txt", "w") 
        file.write(posicion_errores)
        file.close()

#generar_30_archivos()  
#codificar_30_archivos()         
#generador_errores(0.1)
#decodificador_sindrome()
#graficos de varianza/media
