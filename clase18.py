#Búsqueda en bases de datos | Caso práctico |Información estudiantes| Pandas| Python | Parte 1

import pandas as pd
import matplotlib.pyplot as plt

datos=pd.read_csv('student-mat.csv')

#Tipos de informacion
print(datos.dtypes)
print(datos.info())
print(datos.describe())
print(datos.head(n=5))

#Dividir en 2 dataframes
df1=datos.loc[(datos['school']=='GP')]
print(df1.info())

df2=datos.loc[(datos['school']=='MS')]
print(df2.info())

#minuto10














