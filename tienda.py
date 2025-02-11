import streamlit as st
import pandas as pd

'''
# Analizador de Ventas

### Objetivo
Crear un programa en Python que analice un conjunto de **datos de ventas de una tienda**. El programa debe realizar varias operaciones de Data Science para proporcionar información valiosa sobre las ventas de la tienda.

### Consigna

1. **Lectura de Datos**: Crea un DataFrame que contenga los datos provistos en el archivo **Datos_Ventas_Tienda.csv** provisto en esta lección. El archivo incluirá información como *fecha de venta*, *categoría de producto*, *cantidad vendida* y *precio*.
2. **Fusión de Datos**: Crea un segundo DataFrame que contenga los datos del archivo **Datos_Ventas_Tienda2.csv** (también provisto en esta lección), y concaténalos para tener un solo dataFrame con toda la información.

3. **Tratamiento de Datos**: Utiliza Pandas para manipular estos datos. Deberás realizar tareas como limpieza de datos, filtrado y  transformaciones básicas.
4. **Análisis de Ventas**: Realiza análisis para responder preguntas como:
- ¿Cuál es el producto más vendido?
- ¿Cuál es el mes con más ventas?
5. **Datos Agrupados**: Agrupa los datos por categoría de producto y analiza las ventas por categoría.
6. **Guardar Resultados**: Al final, guarda el DataFrame completo (incluyendo la columna de meses) en un archivo .csv en tu ordenador.
'''

'''## Lectura y fusión de datos'''

df1 = pd.read_csv("Datos_Ventas_Tienda.csv")
df2 = pd.read_csv("Datos_Ventas_Tienda2.csv")
df = pd.concat([df1, df2], ignore_index=True)
df

code = '''
df1 = pd.read_csv("Datos_Ventas_Tienda.csv")
df2 = pd.read_csv("Datos_Ventas_Tienda2.csv")
df = pd.concat([df1, df2], ignore_index=True)
'''
st.code(code, language="python")

'''## Tratamiendo de datos
**Revisar si hay valores nulos o tipos de datos que no correspondan con su columna**'''

code = '''
df.isnull().sum()
type(df["Fecha"][0]) #Debe ser un TimeStamp
type(df["Producto"][0]) #Debe ser un str
type(df["Cantidad"][0]) #Debe ser un int
type(df["Precio Unitario"][0]) #Debe ser un int
type(df["Total Venta"][0]) #Debe ser un int
df.info()
'''

st.code(code, language="python")

'''**Convertir la columna fecha de str a TimeStamp**'''

df["Fecha"] = pd.to_datetime(df["Fecha"])
df

code='''
df["Fecha"] = pd.to_datetime(df["Fecha"])
df
'''
st.code(code, language="python")

'''**Reemplazar valores en la columna de "Producto" mal escrito**'''
df["Producto"] = df["Producto"].replace("Electrónic","Electrónicos")
df

code='''
df["Producto"] = df["Producto"].replace("Electrónic","Electrónicos")
df
'''
st.code(code, language="python")

'''**Detectar y eliminar registros duplicados en el DataFrame**'''
code='''
df.duplicated().sum() #Detecta registro duplicados
df.drop_duplicates(inplace=True) #Elimina los registros duplicados
df.duplicated().sum() #Revisa si quedaron registros duplicados
'''
st.code(code, language="python")

'''## Análisis de ventas
**¿Cuál es el producto más vendido?**'''

producto_mas_vendido = df.groupby("Producto")["Cantidad"].sum()
producto_mas_vendido = producto_mas_vendido.sort_values(ascending=False).head(1)
producto_mas_vendido

code='''
producto_mas_vendido = df.groupby("Producto")["Cantidad"].sum()
producto_mas_vendido = producto_mas_vendido.sort_values(ascending=False).head(1)
producto_mas_vendido
'''

st.code(code, language="python")

'''**¿Cuál es el mes con más ventas?**'''

meses = []
for m in df["Fecha"]:
    meses.append(m.month)

df["Mes"] = meses

mes_mayor_venta = df.groupby("Mes")["Total Venta"].sum().sort_values(ascending=False).head(1)
mes_mayor_venta

code='''
meses = []
for m in df["Fecha"]:
    meses.append(m.month)

df["Mes"] = meses

mes_mayor_venta = df.groupby("Mes")["Total Venta"].sum().sort_values(ascending=False).head(1)
mes_mayor_venta
'''

st.code(code, language="python")

'''## Datos Agrupados
**Agrupar las categorías de producto y analizar las ventas**'''
agrupar_productos = df.groupby("Producto")["Total Venta"].sum().sort_values(ascending=False)
agrupar_productos

code='''
agrupar_productos = df.groupby("Producto")["Total Venta"].sum().sort_values(ascending=False)
agrupar_productos
'''
st.code(code, language="python")