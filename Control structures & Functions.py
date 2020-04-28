import os
import numpy as np
import pandas as pd

"""PREVIOUS PROGRAM  

        SCROLL DOWN TO CHECK FOR CONTROL STRUCTURES & FUNCTIONS      """
        
"""*****************************************************************************************************************"""
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
print("\n \n")
# CONVERTING VARIABLE'S DATATYPES : 

cars1.MetColor=cars1.MetColor.astype('object')  # The datatype is converted to object
print(cars1.info())

print(cars1['FuelType'].nbytes)             # When Fuel type is object - memory : 11488

print("\n\n")
print(cars1['FuelType'].astype('category').nbytes)  # When Fuel type is converted from object to category - memory : 1460

#CLEANING COLUMN 'Doors'

print(np.unique(cars1.Doors))    #to get unique values

cars1['Doors'].replace('three',3,inplace=True)

cars1['Doors'].replace('four',4,inplace=True)    # to replace string to number
cars1['Doors'].replace('five',5,inplace=True)

cars1.Doors=cars1.Doors.astype('int64')    # to convert to int64 to avoid confusion
print(cars1.info())


# # TO DETECT MISSING VALUES
print("\n\n")
print(cars1.isnull().sum())  # To check the count of missing values present in each column



"""*****************************************************************************************************************"""

# operations done using for loop and if statements

# To create 3 bins from 'Price' variables

cars1.insert(10,"Price_class","")       # To insert a new COLUMN with blank values

for i in range(0,len(cars1['Price'])):    # To create three bins
    
    if cars1['Price'][i]<8450:
        cars1['Price_class'][i]="Low"
    
    elif cars1['Price'][i]>11950:
        cars1['Price_class'][i]="High"
        
    else:
        cars1['Price_class'][i]="Medium"
        

""" WHILE LOOP (SAME PROCESS USING WHILE)


i=0
while i<len(cars1['Price']):
        if cars1['Price'][i]<8450:
            cars1['Price_class'][i]="Low"
    
        elif cars1['Price'][i]>11950:
            cars1['Price_class'][i]="High"
        
        else:
            cars1['Price_class'][i]="Medium"

        i=i+1
        
"""

print("\n\n")
print(cars1.Price_class.value_counts())         # Returns series containing count of unique values
print("\n\n")

# FUNCTIONS

# To convert Age variable from months to Years

cars1.insert(11,"Age_converted",0)              # creates a new column with values 0

#commented BECAUSE TO SHOW MULTIPLE INPUT FUNCTIONS
# def converted_age(value):                       # FUnction to convert months to years    
    
    # value=value/12
    # return value

    
# cars1.Age_converted=converted_age(cars1.Age)    # passing AGE values to function
# cars1.Age_converted=round(cars1.Age_converted,1) # Roundoff



""" FUNCTION WITH MULTIPLE INPUTS AND  OUTPUTS """

""" 1) Converting the Age variable from months to years and getting kilometers(KM)
        run per month
    
    2) The converted values of kilometer will be stored in a new colum "km_per_month"
    
"""

cars1.insert(12,"km_per_month",0)    

def c_convert(val1,val2):
    new_age=val1/12
    ratio=val2/val1  # convert km runs per month
    return [new_age,ratio]


cars1.Age_converted,cars1.km_per_month=c_convert(cars1.Age,cars1.KM) 

print(cars1.head())
