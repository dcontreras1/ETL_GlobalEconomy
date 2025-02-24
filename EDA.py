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

#crear conexión con PostgreSQL
engine = create_engine(DATABASE_URL)

# Carga del dataset
file_path = r"C:\Users\Danie\OneDrive\Escritorio\Global Economy Indicators.csv"
df = pd.read_csv(file_path)

# Limpiar noombres de columnas (espacios y reemplazar guiones bajos)
df.columns = df.columns.str.strip().str.replace(" ", "_")

#ver info general del dataset
df.info()

#Análisis valores nulos
missing_values = df.isnull().sum().sort_values(ascending=False)
missing_percentage = (df.isnull().sum() / len(df)) * 100
missing_df = pd.DataFrame({"Missing Values": missing_values, "Percentage": missing_percentage})
print(missing_df[missing_df["Missing Values"] > 0])

#Estadísticas descriptivas
descriptive_stats = df.describe()
print(descriptive_stats)

#visualización de distribuciones
plt.figure(figsize=(12, 6))
sns.histplot(df["Gross_Domestic_Product_(GDP)"], bins=50, kde=True, color="blue")
plt.title("Distribución del PIB (GDP)")
plt.xlabel("GDP en USD")
plt.show()

plt.figure(figsize=(12, 6))
sns.histplot(df["Gross_National_Income(GNI)_in_USD"], bins=50, kde=True, color="green")
plt.title("Distribución del GNI")
plt.xlabel("GNI en USD")
plt.show()

#Matriz de correlación
plt.figure(figsize=(12, 6))
numeric_df = df.select_dtypes(include=[np.number]) #Filtrar solo columnas numéricas
sns.heatmap(numeric_df.corr(), cmap="coolwarm", annot=False, linewidths=0.5)
plt.title("Matriz de Correlación")
plt.show()

#Transformación y limpieza

#eliminar columnas con más del 15% de valores nulos
threshold = 0.15
columns_to_drop = missing_df[missing_df["Percentage"] > (threshold + 100)].index.tolist()
df_clean = df.drop(columns=columns_to_drop)

#rellenar valores nulos con la mediana
df_clean.fillna(df_clean.median(numeric_only=True), inplace=True)

#transformación logarítmica para normalizar datos
to_log_transform = ["Gross_Domestic_Product_(GDP)", "Gross_National_Income(GNI)_in_USD", "Exports_of_goods_and_services", "Imports_of_goods_and services"]
for col in to_log_transform:
    df_clean[col] = np.log1p(df_clean[col])

#Eliminar duplicados
df_clean = df_clean.drop_duplicates()

#verificar tamaño del DataFrame antes de cargar
total_rows = df_clean.shape[0]
print(f"Filas en df_clean antes de cargar; {total_rows}")
print(df_clean.head()) #Mostrar las primeras filas para verificar

#Cargar datos en PostgreSQL solo si hay filas
if total_rows > 0:
    df_clean.to_sql("economy_indicators", engine, if_exists="append", index=False, method="multi", chunksize=1000)
    print("Datos cargados exitosamente en PostgreSQL")

    #verificar si los datos se insertaron correctamente
    with engine.connect() as conn:
        result = pd.read_sql("SELECT COUNT(*) FROM economy_indicators;", conn)
        print(f"Filas en PostgreSQL después de la carga: {result.iloc[0, 0]}")
else:
    print("No hay datos para cargar en PostgreSQL")

#Visualización de toda la información del dataset
print("Mostrando todas las filas del dataset:")
print(df.to_string())