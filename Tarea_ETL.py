import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Importar paqueterias

df= pd.read_csv ("c:/Users/Mitzi/Desktop/Ingeniería de datos/Tarea ETL/file_path/matricula_federativa.csv", 
                 delimiter =';',encoding = 'utf8')
# Leer el archivo de datos

print(df)
# Imprimir data frame

fig = plt.bar(df['entidad_federativa'].values, df['porcentaje_mujeres'].values) 
ax = plt.subplot()
# Grafico de barras del porcentaje de mujeres en cada entidad federativa
ax.set_xlabel('Entidad federativa')
# Coloca una etiqueta en el eje x
ax.set_ylabel('Porcentaje de mujeres')

plt.show()
# Mostrar gráfico