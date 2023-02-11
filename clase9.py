#Escribir información a un archivo csv| Pandas | Python | ¡Muy Básico!

dic={"aguascalientes":"aguascalientes", 
     "sonora":"hermosillo",
     "nayarit":"tepic"}

archivo="estadosmx.csv"

#Abrir un archivo para escribir con "w"
csv=open(archivo, "w")
titulor="estado, capital\n"
csv.write(titulor)

#Los dicionarios son llave:valor
for key in dic.keys():
    estado=key
    capital=dic[key]
    filas=estado+","+capital+"\n"
    csv.write(filas)




