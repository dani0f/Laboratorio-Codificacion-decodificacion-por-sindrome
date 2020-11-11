import numpy as np

def Not_binary(binary_num):
    if(binary_num==0):
        return(1)
    else:
        return(0)

def xor_vector(cad1,cad2):
    cad3=[]
    for i in range(len(cad1)):
        cad3.append(cad1[i]*Not_binary(cad2[i]) + cad2[i]*Not_binary(cad1[i]))
    print(cad3)

a=np.array( [[1,0,0],[0,1,0],[0,0,1]])
b=np.array([[0,1,1],[1,0,1],[1,1,0]])
c = np.concatenate((b, a), axis=1)
c= np.transpose(c)
#print(c)
#[[sindrome,e]]
list=[]

for i in range(6):
    codigo=[0,0,0,0,0,0]
    codigo[i]=1
    sindrome=c[i]
    list.append([sindrome,codigo])
   
print(list) 