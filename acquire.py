import pandas as pd

import env
import os
from pydataset import data

def get_titanic_data():
   
    filename = 'titanic.csv_'
    url = env.get_db_url('titanic_db')
    if os.path.exists(filename):
        print('this file exists, reading from csv')
        
        df = pd.read_csv(filename, index_col=0)
    else:
        print('this file doesnt exist, reading from sql and saving to csv')
     
        df = pd.read_sql('select * from passengers', url)

        df.to_csv(filename)
        
    return df 


def get_iris_data():
    filename = 'iris_'
    url = env.get_db_url('iris_db')
    
    if os.path.exists(filename):
        print('this file exists, reading from csv')

        df_iris = pd.read_csv(filename, index_col=0)
    else:
        print('this file doesnt exist, reading from sql and saving as csv')
        
        df_iris = pd.read_sql('''select * from species
join measurements using (species_id)''', url)
        df_iris.to_csv(filename)
        
    return df_iris


def get_telco_data():
   
    filename = 'telco.csv_'
    url = env.get_db_url('telco_churn')
    if os.path.exists(filename):
        print('this file exists, reading from csv')
        
        df = pd.read_csv(filename, index_col=0) 
    else:
        print('this file doesnt exist, reading from sql and saving to csv')
      
        df = pd.read_sql('''select * from customers
    join contract_types using (contract_type_id)
    join internet_service_types using (internet_service_type_id)
    join payment_types using (payment_type_id);''', url)

        df.to_csv(filename)
        
    return df 
