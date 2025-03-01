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

#subir datos crudos a PostgreSQL
df.to_sql("economy_raw", engine, if_exists="replace", index=False, method="multi", chunksize=1000)
print("Datos cargados en PostgreSQL")