#Exportar a archivo CSV (Muy Básico)

import pandas as pd
datos=pd.read_csv("ATP.csv")
df=pd.DataFrame(datos)

#reseteo de index, exportar, encabezado y no exportar el index
df.reset_index().to_csv("PrimeraEx.csv", header=True, index=False)

datos.set_index("Location", inplace=True)
df=datos.loc["Melbourne"]
df.reset_index().to_csv("MelbourneATP.csv", header=True, index=False)

df2=datos.loc[datos["Series"].str.endswith("Slam")]
df2.reset_index().to_csv("GSlamATP.csv", header=True, index=False)

"""
Para guardar los archivos csv
"""
