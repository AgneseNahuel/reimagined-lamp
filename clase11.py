#Operaciones con condición en columnas | Pandas | Python |

import pandas as pd
datos=pd.read_csv('minutos2.csv')
df=pd.DataFrame(datos)

alto=df.loc[0, 'B']

for i in range(1, len(df)):
    #loc va a permitirnos usar matematicas, si seria iloc seria imposible solo manejar los titulos
    if df.loc[i, 'B']>df.loc[i-1, 'B'] and df.loc[i, 'B']>alto:
        df.loc[i, 'dB']=df.loc[i, 'B']-alto
        alto=df.loc[i, 'B']
    else:
        df.loc[i, 'dB']=0

print(df)

total=df['dB'].sum()
print("El total es: ", total)





