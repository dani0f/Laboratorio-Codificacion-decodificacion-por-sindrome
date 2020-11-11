import numpy as np

def Codificacion(archivo_texto):
            #Matriz de paridad
    P=np.array([[1,1,0,1],[1,0,1,0],[0,1,1,1]])
    #print("Matriz de paridad P:\n", P)
            #Matriz de verificación
    I_3=np.array([[1,0,0],[0,1,0],[0,0,1]])
    I_3=np.identity(3)
    #H=np.concatenate((P, I_3), axis=1)
    #print("Matriz de verificación H\n",H)
            #Matriz generadora
    I_4=np.identity(4)
    G=np.concatenate((I_4, np.transpose(P)), axis=1)
    #print("Matriz de generación G\n",G)
            #Vector de entrada
    print("archivo de entrada",archivo_texto)
    X=np.array([1,0,0,1])
    print("Vector de entrada a codificar X:\n",X)
        #Se genera el codigo con XxorG=C
    C=np.dot(X,G)
        #xor es funcion de paridad
    for i in range(len(C)):
        if C[i] % 2 == 0:
            C[i]=0
        else:
            C[i]=1
    print("Vector codificado C:\n",C)
    return(C)

Codificacion("archivo_1.txt")