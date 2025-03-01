import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

with open("credentials.json", "r") as file:
    creds = json.load(file)

DATABASE_URL = f"postgresql://{creds['user']}:{creds['password']}@{creds['host']}:{creds['port']}/{creds['database']}"
engine = create_engine(DATABASE_URL)

file_path = r"C:\Users\Danie\OneDrive\Escritorio\Global Economy Indicators.csv"
df = pd.read_csv(file_path, delimiter=";")
df.columns = df.columns.str.strip().str.replace(" ", "_")

#subir datos crudos a PostgreSQL
df.to_sql("economy_raw", engine, if_exists="replace", index=False, method="multi", chunksize=1000)
print("Datos cargados en PostgreSQL")

#recuperar datos transformados desde la base de datos
df_transformed = pd.read_sql("SELECT * FROM economy_indicators_transformed", engine)

#Visualizaciones

#gráfico 1: Evolución PIB por país
plt.figure(figsize=(12,6))
sns.lineplot(data=df_transformed, x="year", y="gdp", hue="country_name", marker="o")
plt.title("Evolución del PIB por país")
plt.xlabel("Año")
plt.ylabel("PIB (GDP)")
plt.legend(title="País", bbox_to_anchor=(1, 1))
plt.grid
plt.show()

#Gráfico 2: Comparación de tasas de cambio
plt.figure(figsize=(12,6))
df_melted = df_transformed.melt(id_vars=["country_name", "year"],
                                value_vars=["ama_exchange_rate", "imf_exchange_rate"],
                                var_name="Tipo de cambio", value_name="Valor")
sns.lineplot(data=df_melted, x="year", y="Valor", hue="Tipo de cambio", style="country_name", markers=True)
plt.title("Comparación tasas de cambio")
plt.xlabel("Año")
plt.ylabel("Valor de cambio")
plt.legend(title="Tipo de cambio", bbox_to_anchor=(1, 1))
plt.grid()
plt.show()

#Gráfico 3: relación entre población y GNI per capita
plt.figure(figsize=(10,6))
sns.scatterplot(data=df_transformed, x="population", y="per_capita_gni", hue="country_name", size="gni", sizes=(20, 200))
plt.xscale("log")
plt.title("Relación entre población y GNI per capita")
plt.xlabel("Población")
plt.ylabel("GNI per capita")
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(df_transformed["household_expenditure"], bins=30, kde=True, color="blue")
plt.title("Distribución del gasto de los hogares")
plt.xlabel("Gasto de los hogares")
plt.ylabel("Frecuencia")
plt.grid()
plt.show()