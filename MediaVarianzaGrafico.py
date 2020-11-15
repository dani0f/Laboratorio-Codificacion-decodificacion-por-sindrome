import matplotlib.pyplot as plt
import numpy as np
def archivo_array(archivo):
    file = open(archivo)                 
    data = file.read() 
    file.close()
    lista_1=list(data)
    lista_2=[]
    for i in range(len(data)):
        if( data[i] != "-" ):
            lista_2.append(int(lista_1[i]))
    return(lista_2)
def graficar(archivoa01,archivoa001,archivoa0001,archivod01,archivod001,archivod0001):
   
    listaea01=np.array( archivo_array(archivoa01) ,float)
    listaed01=np.array(archivo_array(archivod01),float)
    listaea001=np.array(archivo_array(archivoa001),float)
    listaed001=np.array(archivo_array(archivod001),float)
    listaea0001=np.array(archivo_array(archivoa0001),float)
    listaed0001=np.array(archivo_array(archivod0001),float)

    medialistaea01=listaea01.mean()
    medialistaed01=listaed01.mean()
    medialistaea001=listaea001.mean()
    medialistaed001=listaed001.mean()
    medialistaea0001=listaea0001.mean()
    medialistaed0001=listaed0001.mean()

    varianzalistaea01=listaea01.var()
    varianzalistaed01=listaed01.var()
    varianzalistaea001=listaea001.var()
    varianzalistaed001=listaed001.var()
    varianzalistaea0001=listaea0001.var()
    varianzalistaed0001=listaed0001.var()

    probabilidades=[0.001,0.01,0.1,]

    y=probabilidades
    x=[medialistaea0001,medialistaea001,medialistaea01]
    x1=[medialistaed0001,medialistaed001,medialistaed01]
    x2=[varianzalistaea0001,varianzalistaea001,varianzalistaea01]
    x3=[varianzalistaed0001,varianzalistaed001,varianzalistaed01]
    #plt.ylim(75.3124, 75.57)
    #plt.xlim(14.6163, 14.624)
    #plt.ioff()
    plt.plot(x, y,'o-',color='red')
    plt.plot(x1,y,'o-',color='blue')
    plt.grid()
    plt.legend(('Antes de decodificación', 'Despues de decodificación'),
    prop = {'size': 10}, loc='upper left')
    plt.xlabel('Media')
    plt.ylabel('Probabilidad de error en 1 bit')
    plt.title("Media de errores en 30 archivos de largo 13 bits")
    plt.show()

    plt.plot(x2, y,'o-',color='red')
    plt.plot(x3,y,'o-',color='blue')

    plt.grid()

    plt.legend(('Antes de decodificación', 'Despues de decodificación'),
    prop = {'size': 10}, loc='upper left')
    plt.xlabel('Varianza')
    plt.ylabel('Probabilidad de error en 1 bit')
    plt.title("Varianza de errores en 30 archivos de largo 13 bits")
    plt.show()


