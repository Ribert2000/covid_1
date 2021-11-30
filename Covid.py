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