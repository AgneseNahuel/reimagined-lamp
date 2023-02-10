#¿Cómo hacer un Data frame? (Básico)
#----------------------------------------------
#El DateFrame es el tipo de datos principal que se ultilisa en pandas

#Importacion del modulo de base de datos
import pandas as pd

#libreria para manejo de numeros
import numpy as np

#Un diccionario
#Las columnas se separan por comas despues de los corchetes
datos={'Nombre':['Chalio','Marisol','Yolanda','Tina'], 'Calificaciones':['100','90','80','100'], 'Deportes':['futbol','natacion','basquetbol','beisbol'],'materias':['calculo','metodos numericos', 'cocina', 'quimica']}

#Construcion del tipo de datos DataFrame
df=pd.DataFrame(datos)
print(df)
print('\n'*2)

#Datos no Validos
#NaN = Not A Number
datos2={'Nombre':['Chalio','Marisol','Yolanda','N/A'],
    'Calificaciones':[np.nan,'90','80','100'],
    'Deportes':['futbol','natacion','basquetbol','N/A'],
    'Materias':['calculo','metodos numericos', 'N/A', 'quimica']}
df2=pd.DataFrame(datos2)
print(df2)
print('\n'*2)

#mas informacion con info()
print(df2.info())
print('\n'*2)

#estadisticas basicas describe()
print(df2.describe())
print('\n'*2)

#nuevo dataframe
nuevo=pd.DataFrame(df2)
#reemplazar el valor nan numerico por 0
nuevo=nuevo.replace(np.nan, "0")
print(nuevo)
print('\n'*2)

nuevo2=pd.DataFrame(df2)
#dropna elimina sola la linea que tenga 0
nuevo2.dropna(how="any", inplace=True)
print(nuevo2)
print('\n'*2)

#eliminar registro buscando por columna (importante)
columna=df2[df2['Nombre']!='N/A']
print(columna)
print('\n'*2)

#llenar con ceros cualquier valor 0 cualquier valor nan
nuevo3=pd.DataFrame(df2)
nuevo3.fillna(0, inplace=True)
print(nuevo3)
print('\n'*2)

#estadisticas
print(nuevo3.describe())
print('\n'*2)

#convertir a numeros enteros
nuevo2['Calificaciones']=nuevo2.Calificaciones.astype(int)
print(nuevo2.describe())
print('\n'*2)

#caracteristicas individuales
#mean=promedio
#max
#min
print("promedio", nuevo2["Calificaciones"].mean())
