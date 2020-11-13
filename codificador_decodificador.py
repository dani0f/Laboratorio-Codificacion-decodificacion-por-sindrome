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
        Tabla_sindrome.append([ s ,i])
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


def Decodificacion_sindrome(Ht,Tabla_sindrome,codigo):
    x=[]  
    for i in range(len(codigo)):
        x.append(int(codigo[i]))
    X=np.array(x)
    sindrome=np.dot(X,Ht)
    strS=""
    for i in range(len(sindrome)):
        if sindrome[i] % 2 == 0:
            strS=strS+"0"
        else:
            strS=strS+"1"
    if(strS=="0000"):
        print("no hay error")
    else:
        for i in range(len(Tabla_sindrome)):
            if(Tabla_sindrome[i][0] == strS):
                print("error detectado en bit ",Tabla_sindrome[i][1])
"""    
P=Matriz_paridad()
Ht=H_transpuesta(P)
tabla_sindrome=Tabla_sindrome(Ht)
print("Generadora",Matriz_generadora(P))
G=Matriz_generadora(P)
codigo=Codificacion(Matriz_generadora(P),"datos_generados_2.txt")
print("codigo",codigo)
print(tabla_sindrome)
print(P)
print(Matriz_generadora(P)) 
Decodificacion_sindrome(Ht,tabla_sindrome,codigo)"""