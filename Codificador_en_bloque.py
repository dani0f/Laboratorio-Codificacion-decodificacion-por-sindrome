import numpy as np
def Codificacion(archivo_texto):
    #print("-------Archivo de entrada",archivo_texto)
    file = open(archivo_texto)                 
    data = file.read() 
    x=[]  
    for i in range(len(data)):
        x.append(int(data[i]))
    file.close
            #Matriz de paridad
    P=np.array([[1,1,0,1,0,0,0,0,1],[1,0,1,0,1,0,1,0,0],[0,1,1,1,0,1,0,1,0]])
            #Matriz generadora 
    I=np.identity(9)
    G=np.concatenate((I, np.transpose(P)), axis=1)
    #print("Matriz de generación G\n",G)
            #Vector de entrada
    X=np.array(x)
    #print("Vector de entrada a codificar X:\n",X)
        #Se genera el codigo con XxorG=C
    C=np.dot(X,G)
        #xor es funcion de paridad
    strC=""
    for i in range(len(C)):
        if C[i] % 2 == 0:
            strC=strC+"0"
        else:
            strC=strC+"1"
    #print("Vector codificado C:\n",strC)
    return(strC)
