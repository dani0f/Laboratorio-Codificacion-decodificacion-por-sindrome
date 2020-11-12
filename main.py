import Codificador_en_bloque

for i in range(30):
    C=Codificador_en_bloque.Codificacion("datos_generados_"+str(i)+".txt")
    output_file = open("datos_generados_"+str(i)+".txt", "w")
    output_file.write(C)
    output_file.close()