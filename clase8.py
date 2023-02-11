#Borrar renglones de un archivo csv| Pandas | Python | ¡Muy Básico!

import pandas as pd
df=pd.read_csv('canciones.csv')
print(df.info())
print(df)

#Usar len para ver cuantas filas son
filas=len(df.index)
print("Filas: ", filas)

#Usar drop para eliminar con el index
#Usar inplace=True para que en la siguiente impresion funcione bien
df.drop(df.index[[filas-1]], inplace=True)
print(df)



