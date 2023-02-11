#Leer un archivo xls| Pandas | Python | ¡Muy Básico!

import pandas as pd
xls=pd.ExcelFile('sales2.xls')

#Nombres de hojas
print(xls.sheet_names)

#La hoja que queres convertir en dataframes
df=xls.parse('Users')
print(df)

df2=xls.parse('Orders')
print(df2)




