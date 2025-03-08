# Project ETL - Global Economy Indicators

# Project Description

This project implements an Extract, Transform, Load (ETL) process to analyze and visualize global economic indicators. The data is extracted from a CSV file, loaded into a PostgreSQL database, transformed and cleaned using PSQL queries, and then used to generate visualizations in Python and Power BI. Finally, the visualizations provide valuable insights into the processed data.

# Tools

Python (pandas, numpy, matplotlib, seaborn, sqlalchemy)
PostgreSQL (data storage)
Jupyter Notebook / Python Scripts (data analysis and visualization)
Git and Github (version control and documentation)
Power BI

# ETL Process Flow

Extraction: The CSV file (Global Economy Indicators.csv) is loaded using Pandas.

Transformation:
Column names are cleaned.
Null values are handled (filled with median or deleted if necessary).
Duplicates are removed.
Logarithmic transformations are applied to normalize data.

Load:
The cleaned data is stored in a PostgreSQL database.
Data insertion is verified.

Analysis and Visualization:
Descriptive statistics.
Histograms of key variables.

# Installation and Configuration
```bash
git clone https://github.com/dcontreras1/ETL_GlobalEconomy.git
cd ETL_GlobalEconomy
```

```bash
python -m venv ETLGE-env
ETLGE-env\Scripts\activate
```

# Instal Dependencies
```bash
pip install -r requirements.txt
```

# PostgreSQL Database Configuration
```sql
CREATE DATABASE ETL_GlobalEconomy;
```

# Running the Project

1 Run the ETL pipeline
```bash
python script/ETL_GlobalEconomy.py
```

```bash
jupyter notebook Notebook/ETLGlobalEconomy.ipynb
```

# Economic Indicators Analyzed
GDP (Gross Domestic Product),
GNI (Gross National Income) per capita,
Exchange Rate,
Population,
Imports,
Household Expenditure.

# Conclusions
1. GDP growth is different across countries.

Some countries have grown fast in recent years, while others have stayed the same or grown slowly.
This shows that some nations have found better ways to improve their economies, possibly through trade, investments, or government policies.

2. Most people spend similar amounts, but a few spend much more.

Household spending is mostly low, with only a few cases of very high expenses.
This suggests that wealth is not spread evenly, and only a small group has much higher purchasing power.

3. Exchange rates are very different between countries.

Some countries have big differences between the AMA and IMF exchange rates, which may show economic instability or different ways of calculating them.
Nations with unstable economies often show larger changes in exchange rates.

4. Population size affects income per person.

Countries with fewer people usually have a higher income per person, while larger countries have more mixed results.
This means that income depends not only on how many people live in a country but also on things like jobs, businesses, and government decisions.