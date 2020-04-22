# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 22:12:58 2020

@author: Dharun
"""
import os
import numpy as np
import pandas as pd

cars_data=pd.read_csv('Toyota.csv',index_col=0)

#Copying the originial data using Deep Copy
cars=cars_data.copy(deep=True)
print("\n")
print(cars.dtypes) 
print("\n")                 # Returns  a series with datatype of each column
print(cars.dtypes.value_counts())      # Returns counts of UNIQUE datatypes in dataframe

# Selecting data based on datatypes
print("\n")
# Returns subset of the column from dataframe based on column dtypes
print(cars.select_dtypes(exclude=[object]))  # Returns subset of the column from dataframe based on column dtypes which excludes object

print("\n")
print(cars.info())              # Returns concise summary of dataframe

print("\n")
print(np.unique(cars['KM']))    # Used to find unique elements in a column

print("\n")
print(np.unique(cars['HP']))    # Used to find unique elements in a column


