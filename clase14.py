#Cómo restar tiempo| Extraer strings | Expresión regular | csv | Pandas | Python | ¡Muy fácil!

import pandas as pd
import matplotlib.pyplot as plt

"""datos=pd.read_csv('ArtJan2018resumido.csv')
df=pd.DataFrame(datos)

#Los '.' son digitos 
df['date']=df['pubDate'].str.extract('(../../..)', expand=True)
print(df['date'])
"""
datos=pd.read_csv('Ejemplo.csv')
df=pd.DataFrame(datos)

#Creacion de nueva columna
df['hora']=df['fecha'].str.extract('(..:..:..)', expand=True)
print(df['hora'])

#conversion a datetime
df['hora']=pd.to_datetime(df['hora'])
df['hora 1']=pd.to_datetime(df['hora 1'])
df['diferencia']=df['hora']-df['hora 1']
print(df['diferencia'])

#Graficar
plt.plot(df['hora'],df['valor 2'], '-')
_=plt.xticks(rotation=45)
plt.show()










