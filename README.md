Proyecto ETL - Global Economy Indicators

# Descripción de proyecto

Este proyecto implementa un proceso de ETL (Extract, Transform, Load) para analizar y visualizar indicadores económicos globales.
Se extraen los datos de un archivo CSV, se cargan los datos crudos a la base de datos PostgreSQL, después se realizan transformaciones y limpieza a través de consultas PSQL, y luego se trae la información de la tabla transformada para generar las visualizaciones en python y Power BI. Finalmente, se generan visualizaciones para obtener información valiosa de los datos procesados.

# Herramientas Utilizadas

Python (pandas, numpy, matplotlib, seaborn, sqlalchemy)
PostgreSQL (almacenamiento de datos)
Jupyter Notebook / Python Scripts (Análisis y visualización de datos)
Git y Github (Control de versiones y documentación)
Power BI

# Flujo del Proceso ETL

1 Extracción: Se carga el archivo CSV (Global Economy Indicators.csv) con Pandas.

2 Transformación: 
Se limpian los nombres de columnas.
Se manejan valores nulos (relleno con mediana o eliminación si es necesario).
se eliminan duplicados.
se aplican transformaciones logarítmicas para normalizar datos.

3 Carga:
Se almacenan los datos limpios en una base de datos PostgreSQL.
Se verifica la inserción de datos.

4 Análisis y Visualización:
Estadísticas descriptivas.
Histogramas de variables clave.
Matriz de correlación.

# Instalación y Configuración
```bash
git clone https://github.com/dcontreras1/ETL_GlobalEconomy.git
cd ETL_GlobalEconomy
```

```bash
python -m venv ETLGE-env
ETLGE-env\Scripts\activate
```

# Instalar dependencias
```bash
pip install -r requirements.txt
```

# Configuración a la base de datos PostgreSQL
```sql
CREATE DATABASE ETL_GlobalEconomy;
```

# Ejecución del proyecto

1 Ejecutar el pipeline ETL
```bash
python script/ETL_GlobalEconomy.py
```

```bash
jupyter notebook Notebook/ETLGlobalEconomy.ipynb
```

# Indicadores económicos analizados
GDP (Gross Domestic Product),
GNI (Gross National Income) per capita,
Exchange Rate,
Population,
Imports,
Household Expenditure.