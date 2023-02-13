#Extraer horas, minutos y segundos de columnas archivo csv|DataFrame | Pandas | Datetime | Python

import pandas as pd
import datetime

datos=pd.read_csv('datosnum.csv')
df=pd.DataFrame(datos)

#Extrae de una manera legible la hora que tiene la base de datos
hora=df['A'].str.extract('((?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d)')
print(hora)
print('\n'*2)

df2=pd.DataFrame()

#Para que no aparescan Nan se los cambia por un 0
df2=df2.fillna(0)

df2['A']=df['A'].str.extract('((?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d)')
df2['C']=df['C'].str.extract('((?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d)')
df2['F']=df['F'].str.extract('(\d+(?:\.\d+)?)')
df2['G']=df['G'].str.extract('(\d+(?:\.\d+)?)')
print('Nuevo: ', df2)
print('\n'*2)

print("AGRUPACION POR MINUTOS")
print('\n')
df2['A']=pd.DatetimeIndex(df2['A'])
df2.set_index(keys='A', inplace=True)
first=datetime.time(11, 18, 0)
last=datetime.time(11,19,0)
print(df2[['F']].between_time(first,last))



"""
Un vistaso a la libreria datetime!, muy utilisada
"""










