import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

#Cargar credenciales desde credentials.json
with open("credentials.json", "r") as file:
    creds = json.load(file)

#construir la URL de conexión
DATABASE_URL = f"postgresql://{creds['user']}:{creds['password']}@{creds['host']}:{creds['port']}/{creds['database']}"
engine = create_engine(DATABASE_URL)

# Carga del dataset
file_path = r"C:\Users\Danie\OneDrive\Escritorio\Global Economy Indicators.csv"
df = pd.read_csv(file_path)

# Limpiar nombres de columnas (espacios y reemplazar guiones bajos)
df.columns = df.columns.str.strip().str.replace(" ", "_")

#ver info general del dataset
print("Información general del dataset")
df.info()
#verificar las columnas del dataframe
print("columnas en el dataframe original:", df.columns)

#Análisis valores nulos
print("valores nulos por columna:")
missing_values = df.isnull().sum().sort_values(ascending=False)
missing_percentage = (df.isnull().sum() / len(df)) * 100
missing_df = pd.DataFrame({"Missing Values": missing_values, "Percentage": missing_percentage})
print(missing_df[missing_df["Missing Values"] > 0])

#Transformación y limpieza

#eliminar columnas con más del 15% de valores nulos
threshold = 0.15
columns_to_drop = missing_df[missing_df["Percentage"] > (threshold + 100)].index.tolist()
df_clean = df.drop(columns=columns_to_drop)

#rellenar valores nulos con la mediana
df_clean.fillna(df_clean.median(numeric_only=True), inplace=True)

#Eliminar duplicados
df_clean = df_clean.drop_duplicates()

cols_to_transform = [
    "Gross_Domestic_Product_(GDP)", 
    "Gross_National_Income(GNI)_in_USD", 
    "Exports_of_goods_and_services", 
    "Imports_of_goods_and services"
    ]
for col in cols_to_transform:
    if col in df_clean.columns:  # Asegurarse de que la columna existe
        df_clean[col] = np.log1p(df_clean[col])

# Verificar el tamaño del DataFrame limpio
print(f"\nNúmero de filas después de limpiar y transformar: {df_clean.shape[0]}")

#mostrar primeras filas del dataframe limpio
print("\nPrimeras filas del dataframe limpio")
print(df_clean.head())

#asegurarse de que las columnas coincidan con las de a db
df_clean = df_clean.rename(columns={
     "Country": "country",
     "Year": "year",
     "Gross_Domestic_Product_(GDP)": "gdp",
     "Gross_National_Income(GNI)_in_USD": "gni",
     "Exports_of_goods_and_services": "exports",
     "Imports_of_goods_and_services": "imports"
})

#verificar las columnas renombradas
print("Columnas después de renombrar:", df_clean.columns)

df_clean = df_clean.loc[:, ['country', 'year', 'gdp', 'gni', 'exports', 'imports']]

#verificar las columnas que se insertarán
print("Columnas a insertar;", df_clean.columns)

#cargar los datos limpios a la base de datos PostgreSQL si hay datos disponibles
if df_clean.shape[0] > 0:
    #insertar datos
    df_clean.to_sql("economy_indicators", engine, if_exists="append", index=False, method="multi", chunksize=1000)
    print("\nDatos cargados exitosamente en PostgreSQL")
else:
    print("\nNo hay datos para cargar en PostgreSQL")

#visualización de distribuciones
plt.figure(figsize=(12, 6))
sns.histplot(df_clean["gdp"], bins=50, kde=True, color="blue")
plt.title("Distribución del PIB (GDP) después de la limpieza")
plt.xlabel("GDP en USD (log transformado)")
plt.ylabel("Frecuencia")
plt.show()

plt.figure(figsize=(12, 6))
sns.histplot(df_clean["gni"], bins=50, kde=True, color="green")
plt.title("Distribución del GNI después de la limpieza")
plt.xlabel("GNI en USD (log transformado)")
plt.ylabel("Frecuencia")
plt.show()

#Matriz de correlación
plt.figure(figsize=(12, 6))
numeric_df = df_clean.select_dtypes(include=[np.number]) #Filtrar solo columnas numéricas
sns.heatmap(numeric_df.corr(), cmap="coolwarm", annot=False, linewidths=0.5)
plt.title("Matriz de Correlación")
plt.show()

#Visualización de toda la información del dataset
print("Mostrando todas las filas del dataset:")
print(df.to_string())