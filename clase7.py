#Ordenar valores por columna (¡Muy Básico!)

import pandas as pd
import numpy as np

datos=pd.read_csv('DatosYT.csv')

#Ordenando por ATP y de mayor al menor con ASCENDING=False
#SORT_VALUES
print(datos.sort_values(by=['id'], ascending=False))

#Otra base de datos es necesaria para que funcione bien (DatosYT.csv)
datos1=pd.DataFrame(np.sort(datos.values, axis=0),index=datos.index, columns=datos.columns)
print(datos1)



