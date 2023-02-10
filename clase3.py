#¿Cómo seleccionar renglones y columnas de un archivo CSV? (Muy Básico)

import pandas as pd
datos=pd.read_csv('ATP.csv')

#selecion de renglones (iloc)
print(datos.iloc[0:5])

#selecion de renglones salteados
print(datos.iloc[[0,3,5,7,9],[0,5,6]])
print('\n'*2)

#trabajar con columnas
print(datos.iloc[: , 0:3])

#rango de renglones y columnas
print(datos.iloc[0:5,6:8])
