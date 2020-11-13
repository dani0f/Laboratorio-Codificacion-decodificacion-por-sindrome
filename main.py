import Codificador_en_bloque
import numpy as np

for i in range(30):
    C=Codificador_en_bloque.Codificacion(Codificador_en_bloque.Matriz_paridad(),"datos_generados_"+str(i)+".txt")
    output_file = open("datos_generados_"+str(i)+".txt", "w")
    output_file.write(C)
    output_file.close()