#Selección de renglones y columnas por nombre LOC (Muy Básico)

import pandas as pd
import numpy as np

datos=pd.read_csv('ATP.csv')
print(datos.head())

#dejar columna con set index
#El comando inplace=True es para que quede asi
datos.set_index("Location", inplace=True)
print("Melbourne")

#Solo ver relacionados con Melbourne
print(datos.loc["Melbourne"])

print("Atlanta")
print(datos.loc["Atlanta", "Surface"])
print('\n'*2)

print("seleccion amplia***")
print(datos.loc[["Atlanta","Melbourne"],
                ["Series","Court"]])
print('\n'*2)

#Para seleccion por slicing se puede presindir de los corchetes
print(datos.loc[["Atlanta","Melbourne"],
                "Series":"Round"])
print('\n'*2)

#Para que termine con algo en especifico
print(datos.loc[datos["Series"].str.endswith("Slam")])



"""
OBSERVACION: ILOC utiliza numeros de indices
en cambio LOC utilisa los mismos nombres de 
columnas y filas...
"""