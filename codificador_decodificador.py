import numpy as np

def Matriz_paridad():
    return(np.array([[1,1,0,1,0,0,0,1,1],[1,0,1,0,1,0,1,1,0],[0,1,1,1,0,1,1,0,0],[0,1,0,0,1,1,1,1,1]]))

def Matriz_generadora(P):
    I=np.identity(9)
    G=np.concatenate((I, np.transpose(P)), axis=1)
    return(G)

def H_transpuesta(P):
    I_4=np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
    I_4=np.identity(4)
    H=np.concatenate((P, I_4), axis=1)
    Ht=np.transpose(H)
    return(Ht)

def Tabla_sindrome(Ht): 
    Tabla_sindrome=[]
    s=""
    vector_nulo=np.zeros(13)
    vector_resultante=np.dot(vector_nulo,Ht)
    for i in range(len(vector_nulo)):
        s=""
        vector_nulo=np.zeros(13)
        vector_nulo[i]=1
        vector_resultante=np.dot(vector_nulo,Ht)
        for j in range(len(vector_resultante)):
            if (vector_resultante[j] == float(1)):
                s=s+"1"
            else:
                s=s+"0"
        Tabla_sindrome.append([ s ,vector_nulo])
    return(Tabla_sindrome)


def Codificacion(G,archivo_texto):
    file = open(archivo_texto)                 
    data = file.read() 
    x=[]  
    for i in range(len(data)):
        x.append(int(data[i]))
    file.close
    X=np.array(x) #Vector de entrada a codificar
    C=np.dot(X,G) #Se genera el codigo con XxorG=C
    strC=""
    for i in range(len(C)):
        if C[i] % 2 == 0:
            strC=strC+"0"
        else:
            strC=strC+"1"
    return(strC)


def Decodificacion_sindrome(Ht,Tabla_sindrome,archivo_texto,numero_archivo,archivo_resultados,bool_correcion):
    file = open(archivo_texto)                 
    data = file.read() 
    x=[]  
    for i in range(len(data)):
        x.append(int(data[i]))
    X=np.array(x)
    sindrome=np.dot(X,Ht)
    strS=""
    for i in range(len(sindrome)):
        if sindrome[i] % 2 == 0:
            strS=strS+"0"
        else:
            strS=strS+"1"
    contador_errores_detectados=0
    contador_errores_corregidos=0
    if(strS!="0000"):
        #print("archivo:",numero_archivo,"error para corregir en bit ",Tabla_sindrome[i][1])
        for i in range(len(Tabla_sindrome)):
            if((Tabla_sindrome[i][0] == strS) and bool_correcion==1): 
                Str_cod_transmitido=""
                e=Tabla_sindrome[i][1]
                for z in range(len(e)):
                    if (e[z] + X[z]) %2 ==float(0):
                        Str_cod_transmitido=Str_cod_transmitido+"0"
                    else:
                        Str_cod_transmitido=Str_cod_transmitido+"1"
                #print("Codigo original",Str_cod_transmitido)
                #print("eerror")
                output_file = open("datos_generados_"+str(numero_archivo)+".txt", "w")
                output_file.write(Str_cod_transmitido)
                output_file.close()
                contador_errores_corregidos=contador_errores_corregidos+1
                bool_correcion=0 #solo se tiene 1 intento de correción

    #if(numero_archivo==0):
    #    f = open(archivo_resultados,'w')
    #else:
    #    f = open(archivo_resultados,'a')
    #f.write(str(numero_archivo)+","+str(contador_errores_detectados)+","+str(contador_errores_corregidos)+"\n")
    #f.close()            
                
                

