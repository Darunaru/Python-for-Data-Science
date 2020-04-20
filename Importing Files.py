import os
import pandas as pd

data_csv=pd.read_csv('Iris_data_sample.csv') #Used to read any file in spider
data_csv=pd.read_csv('Iris_data_sample.csv',price_col=0) #Makes the 1st column as index column

#These special characters can be changed to "nam" by passing the parameter "na_values"
data_csv=pd.read_csv('Iris_data_sample.csv',index_col=0,na_values=["??","###"])


#Reading .xlsx files
#sheet_name specifies the sheet in which the data must be read
data_xlsx=pd.read_xlsx('Iris_data_sample.xlsx',sheet_name="Iris_data")  

#Reading Text Files
#Default delimiter is (TAB - '\t') and Most used is comma and blank
data_textFile=pd.read_txt('Iris_data_sample.txt',sep=" ")
data_textFile=pd.read_txt('Iris_data_sample.txt',sep="\t")
