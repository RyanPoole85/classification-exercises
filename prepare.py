import pandas as pd
import numpy as np
import env
import os
from pydataset import data
import acquire
from sklearn.model_selection import train_test_split


# iris functions

def prep_iris(df):
    """accepts the untransformed iris data, and returns 
    the data with the transformations applied"""
    
    #removed columns 'species_id' and 'measurement_id'
    df = df.drop(columns= ['species_id','measurement_id'])
    
    #renamed column 'species_name' to 'species'
    df = df.rename(columns = {'species_name':'species'})
    
    return df

def split_iris(df):
    """function to split iris data"""
    
    #first
    train, validate_test = train_test_split(df, 
                 train_size=0.60, 
                random_state=123, 
                 stratify=df_iris.species
                )
    #second
    validate, test = train_test_split(validate_test,
                test_size=0.50, 
                 random_state=123, 
                 stratify=validate_test.species
                )
    
    return train, validate, test

def prep_iris_data(df):
    '''
    function to train, validate, and test iris data
    '''
    
    #calling my clean function
    df = prep_iris(df)
    
    #calling my split function
    train, validate, test = split_iris(df)

    return train, validate, test

# telco functions

def prep_telco(df):
    """accepts the raw telco data, and returns the data with the transformations applied"""
    
    #dropped duplicate 'id' columns and left corresponding columns with name values.
    df = df.drop(columns= ['payment_type_id','internet_service_type_id', 'contract_type_id'])
    
    #filled null values without an internet service type with "No Internet" in place of null values.
    df.internet_service_type = df.internet_service_type.fillna('No Internet')
    
    return df

def split_telco(df):
    """function to split telco data"""
    df_telco = acquire.get_telco_data()
    #first
    train, validate_test = train_test_split(df_telco, 
                 train_size=0.60, 
                random_state=123, 
                 stratify=df_telco.churn 
                )
    #second
    validate, test = train_test_split(validate_test,
                test_size=0.50, 
                 random_state=123, 
                 stratify=validate_test.churn 
                )
    
    return train, validate, test


def prep_telco_data(df):
    '''
    function to train, validate, and test telco data
    '''
    
    #calling my clean function
    df = prep_telco(df)
    
    #calling my split function
    train, validate, test = split_telco(df)

    return train, validate, test

# titanic functions    

def clean_titanic(df):
    """
    function to clean titanic data
    """
    #drop unncessary columns
    df = df.drop(columns=['embarked', 'age','deck', 'class'])
    
    #made this a string so its categorical
    df.pclass = df.pclass.astype(object)
    
    #filled nas with the mode
    df.embark_town = df.embark_town.fillna('Southampton')
    
    return df

def split_titanic(df):
    '''
    function to split titanic data
    '''
    df_titanic = acquire.get_titanic_data()
    #first split
    train, validate_test = train_test_split(df, 
                 train_size=0.60, 
                random_state=123, 
                 stratify=df.survived 
                )
    
    #second split
    validate, test = train_test_split(validate_test, 
                test_size=0.50, 
                 random_state=123, 
                 stratify=validate_test.survived 
                )
    
    return train, validate, test

def prep_titanic_data(df):
    '''
    function combining cleaning titanic data 
    and splitting titanic data
    '''
    
    #calling my clean function
    df = clean_titanic(df)
    
    #calling my split function
    train, validate, test = split_titanic(df)

    return train, validate, test

# generic functions

def splitting_data(df, col):
    """function to split data when given a dataframe and column"""
    
    #first
    train, validate_test = train_test_split(df, 
                 train_size=0.60, 
                random_state=123, 
                 stratify=df[col]
                )
    #second
    validate, test = train_test_split(validate_test,
                test_size=0.50, 
                 random_state=123, 
                 stratify=validate_test[col]
                )
    
    return train, validate, test
