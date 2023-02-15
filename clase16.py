#Agregar una columna a un Data Frame| CSV | Pandas | Python | ¡Muy básico!

import pandas as pd

#header=0, para que no agarre el encabezado?
datos=pd.read_csv('energy.csv')
df=pd.DataFrame(datos)
print(df)

#Conversion a Kelvins
TK=df['T1']+273.15
#Para asignar
df=df.assign(Kelvin=TK.values)
print(df['Kelvin'])
#Guardar
df.to_csv('energy2.csv', sep='\t')






















