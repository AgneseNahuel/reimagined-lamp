#Cargar un archivo CSV en línea | Colaboratory Google | Python | ¡Muy básico!

"""
Es una clase de como usar google colaboratory, agrega graficas y como leer
archivos csv...
"""

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('precioOro.csv')
x=df['Name']
y=df['US dollar']

#tipo de grafica
plt.scatter(x,y)
plt.show()



















