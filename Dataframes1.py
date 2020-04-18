# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 20:32:55 2020

@author: Dharun
"""

import os
import numpy as np
import pandas as pd

cars_data=pd.read_csv('Toyota.csv',index_col=0)

#Copying the originial data using Deep Copy
cars=cars_data.copy(deep=True)

#print(cars.index)               # To get the row lables(index) of the dataframe
print(cars.columns)             # To get the column lables of the dataframe
print(cars.size)                # To get total number of elements from the dataframe
print(cars.shape)               # To get the dimensionality of the dataframe
print(cars.memory_usage())      # To get the memory usage of each column in bytes
print(cars.ndim)                # To get the number of axis/array dimensions

#Indexing and Selecting Data
print("\n \n \n \n")
print(cars.head(7))             # The function head() returns the first n rows  from dataframe
print(cars.tail(6))             # returns last n rows of the dataframe
print(cars.at[4,'FuelType'])    # provide label based scalar lookups
print(cars.iat[5,6])            # provides integer based lookups
print(cars.loc[:,'FuelType'])   # To access a group of rows and columns by lables.locc[]