import os
import numpy as np
import pandas as pd

# DATASET 1

cars_data=pd.read_csv('Toyota.csv',index_col=0)

#Copying the originial data using Deep Copy
cars=cars_data.copy(deep=True)

print(cars.info())

print("\n \n")
# DATASET 2

cars_data1=pd.read_csv('Toyota.csv',index_col=0,na_values=["??","????"])

#Copying the originial data using Deep Copy
cars1=cars_data1.copy(deep=True)
print(cars1.info())

"""
SUMMARY BEFORE REPLACING SPECIAL CHARACTERS WITH NAN

<class 'pandas.core.frame.DataFrame'>
Int64Index: 1436 entries, 0 to 1435
Data columns (total 10 columns):
Price        1436 non-null int64
Age          1336 non-null float64
KM           1436 non-null object <-------------
FuelType     1336 non-null object
HP           1436 non-null object <-------------
MetColor     1286 non-null float64
Automatic    1436 non-null int64
CC           1436 non-null int64
Doors        1436 non-null object
Weight       1436 non-null int64
dtypes: float64(2), int64(4), object(4)
memory usage: 123.4+ KB
None

 
SUMMARY AFTER REPLACING SPECIAL CHARACTERS WITH NAN

<class 'pandas.core.frame.DataFrame'>
Int64Index: 1436 entries, 0 to 1435
Data columns (total 10 columns):
Price        1436 non-null int64
Age          1336 non-null float64 
KM           1421 non-null float64 <-------------
FuelType     1336 non-null object
HP           1430 non-null float64 <-------------
MetColor     1286 non-null float64
Automatic    1436 non-null int64
CC           1436 non-null int64
Doors        1436 non-null object
Weight       1436 non-null int64
dtypes: float64(4), int64(4), object(2)
memory usage: 123.4+ KB
None


KM and HP have different datatypes as we have negelected ?? in the seconnd read file.
1st code is incorrect as it is not object datatype

"""
