#Estadísticas básicas para un archivo CSV (+4000 registros)

import pandas as pd
import numpy as np

#leer el archivo
datos= pd.read_csv('ATP.csv')
print(datos.info())
print('\n'*2)

#instrucion para ver las primeras lineas
print(datos.head())

#creacion de dataframe
nuevo=pd.DataFrame(datos)

print(nuevo)
print('\n'*2)
nuevo=nuevo.replace(np.nan, '0')
print("impresion sin nan****************")
print(nuevo.info())
print('\n'*2)
print("estadisticas sin nan***************")
print(nuevo.describe())
print('\n'*2)

print("******estadisticas solamente con numeros")
#convertir numeros en enteros para hacer operaciones
print(nuevo.describe(include=[np.number]))

nuevo=nuevo.replace("N/A", "0")
nuevo=nuevo.replace("NR", "0")
print("******SIN N/A NI NR*****")
print(nuevo.describe())
print('\n'*2)

#impresion de los encabezados!!!! (importante)
print(list(nuevo))
print('\n'*2)

#agarrar una columna y transformarla
nuevo['Wsets']=nuevo.Wsets.astype(int)
nuevo['WRank']=nuevo.WRank.astype(int)
print(nuevo.describe())
print('\n'*2)

#opcion para eliminar los nan
#elimina toda la columna...
datos.dropna(how='any', inplace=True)
print(datos.head())