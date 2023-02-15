#Buscar un valor en una columna y extraer datos de otra| csv | Pandas | Python | ¡Muy básico!

def pago(piezas,precio):
    costo=piezas*precio
    return(costo)

import pandas as pd

datos=pd.read_csv('precios.csv')
df=pd.DataFrame(datos)

#Guarda el nombre
producto=input('introduce tu compra: ')
#cantidad
piezas=int(input('Cuantas necesitas?: '))
#En la columna de producto si es igual al producto, darme la fila de esa columna
precio=df[df['producto']==producto]['precio']

print(pago(piezas,precio))












