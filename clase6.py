#Búsqueda de datos con condiciones (Muy Básico)

import pandas as pd
datos=pd.read_csv("ATP.csv")
print(datos.head(10))
print("\n"*2)

#fijar indice
#El inplace True es para que ya se lleve a cabo esa indicacion 
datos.set_index("Location",inplace=True)

#Para agarrar informacion especifica 
print(datos.loc[datos['Court']=='Outdoor', ['Surface']])
print(datos.loc[datos['Court']=='Outdoor', ['Surface', 'Winner']])
print("Mas condiciones***************")
print(datos.loc[datos['Series'].str.endswith("Slam")&(datos["Surface"]=="Clay")&(datos["Winner"]=="Federer R.")&(datos["Round"]=="The Final")])

"""
OBSERVACIONES: Despues del "&" los datos tienen
que estar encerrados por parentesis ()
"""


