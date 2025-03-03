ETL Project - Global Economy Indicators

Project Description

Este proyecto implementa un proceso de ETL (Extract, Transform, Load) para analizar y visualizar indicadores económicos globales.
Se extraen los datos de un archivo CSV, se realizan transformaciones y limpieza utilizando Python y Pandas, y luego se cargan en una base de datos PostgreSQL. Finalmente, se generan visualizaciones para obtener información valiosa de los datos procesados.

Herramientas Utilizadas
Python (pandas, numpy, matplotlib, seaborn, sqlalchemy)
PostgreSQL (almacenamiento de datos)
Jupyter Notebook / Python Scripts (Análisis y visualización de datos)
Git y Github (Control de versiones y documentación)

Flujo del Proceso ETL
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
