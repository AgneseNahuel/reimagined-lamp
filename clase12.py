#Agrupar datos |Groupby | Pandas | Python |

import pandas as pd

datos=pd.read_csv('movies2.csv')
df=pd.DataFrame(datos)
print("Maxima duracion********")

#Devolucion de columna con la funcion max
print(df['duration'].max())

#Pasando minutos a horas
minutos=df['duration'].max()
print('Horas: ', minutos/60)

#Devuelve el indice maximo
print(df['duration'].idxmax())

#Para el nombre
#print(df.get_values(df['duration'].idxmax(), 'movie_title'))

print("Comparacion de likes entre generos*****")
print("\n"*2)
#groupby compara (estudiarlo)
df1=df.groupby(['genres'])[['movie_facebook_likes']].sum()
print(df1)
print("\n"*2)

print("genero mas buscado: ")
likes=df.groupby(['genres'])[['movie_facebook_likes']].sum()
print(likes['movie_facebook_likes'].idxmax(), end='')
print(' con: ', likes['movie_facebook_likes'].max(), ' likes')

print("Promedio gastado en las peliculas*******")
df2=df.groupby(['director_name'])[['budget']].sum()
df2=df.groupby(['director_name'])[['budget']].mean()
print(df2)
print("\n"*2)


print("¿Cual genero gasta mas dinero?")
print("\n"*2)
dinero=df.groupby(['genres'])[['budget']].sum()
print(dinero)
print("el genero: ", dinero['budget'].idxmax(), " con ", dinero['budget'].max())


"""
groupby: 1 .divide el dataframe en grupos
         2 .les aplica una funcion
         3 .combina los resultados en un dataframe
         Basicamente agrupa...
"""



