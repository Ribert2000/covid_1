# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 16:42:27 2021

@author: riber
"""

import pandas as pd

url = 'cov_22.csv'
data = pd.read_csv(url)

data['Nombre departamento'].replace('BOGOTA','CUNDINAMARCA', inplace=True)
data['Nombre departamento'].replace('BARRANQUILLA','ATLANTICO', inplace=True)
data['Ubicación del caso'].replace('CASA','Casa', inplace=True)
data['Ubicación del caso'].replace('casa','Casa', inplace=True)
data['Recuperado'].replace('fallecido','Fallecido', inplace=True)
data['Sexo'].replace('f','F', inplace=True)
data['Sexo'].replace('m','M', inplace=True)

#1. Número de casos de Contagiados en el País.
data[(data.Recuperado == 'Activo')].shape[0]

#2. Número de Municipios Afectados
data[(data.Recuperado != ' ')].groupby(['Nombre municipio']).size().shape[0]

#3. Liste los municipios afectados (sin repetirlos)
data[(data.Recuperado != ' ')].groupby(['Nombre municipio']).size()

#4. Número de personas que se encuentran en atención en casa
data[data['Ubicación del caso']=='Casa'].shape[0]

#5. Número de personas que se encuentran recuperados
data[data['Recuperado']=='Recuperado'].shape[0]

#6. Número de personas que ha fallecido
data[data['Recuperado']=='Fallecido'].shape[0]

#7. Ordenar de Mayor a menor por tipo de caso (Importado, en estudio, Relacionado)
data.groupby(['Tipo de contagio']).size().sort_values(ascending=False)

#8. Número de departamentos afectados
data[(data.Recuperado != ' ')].groupby(['Nombre departamento']).size().shape[0]

#9. Liste los departamentos afectados(sin repetirlos)
data[(data.Recuperado != ' ')].groupby(['Nombre departamento']).size()

#10. Ordene de mayor a menor por tipo de atención
data[(data.Recuperado != ' ')].groupby(['Ubicación del caso']).size().sort_values(ascending=False)

#11. Liste de mayor a menor los 10 departamentos con mas casos de contagiados
data['Nombre departamento'].value_counts().head(10)

#12. Liste de mayor a menor los 10 departamentos con mas casos de fallecidos
data[(data.Recuperado == 'Fallecido')]['Nombre departamento'].value_counts().head(10)

#13. Liste de mayor a menor los 10 departamentos con mas casos de recuperados
data[(data.Recuperado == 'Recuperado')]['Nombre departamento'].value_counts().head(10)

#14. Liste de mayor a menor los 10 municipios con mas casos de contagiados
data[(data.Recuperado == 'Activo')]['Nombre municipio'].value_counts().head(10)

#15. Liste de mayor a menor los 10 municipios con mas casos de fallecidos
data[(data.Recuperado == 'Fallecido')]['Nombre municipio'].value_counts().head(10)

#16. Liste de mayor a menor los 10 municipios con mas casos de recuperados
data[(data.Recuperado == 'Recuperado')]['Nombre municipio'].value_counts().head(10)

#17. Liste agrupado por departamento y en orden de Mayor a menor las ciudades con mas casos de contagiados
agrupamiento = data.groupby(['Nombre departamento', 'Nombre municipio'])
ordenamiento = agrupamiento.size().sort_values(ascending=False)
print("{}".format(ordenamiento))

#18. Número de Mujeres y hombres contagiados por ciudad por departamento
data[(data.Recuperado == 'Activo')].groupby(['Nombre municipio','Nombre departamento', 'Sexo']).size()

#19. Liste el promedio de edad de contagiados por hombre y mujeres por ciudad por departamento
dat = data.groupby(['Nombre departamento', 'Nombre municipio', 'Sexo'])
cantidad = dat.Edad.mean()
print("{}".format(cantidad))