#Functions to grab the median list price from a dataframe of real estate 

#will have to grab whatever row is in the middle of the data. pandras has a funtion for this 

import pandas as pd
from re import sub
from decimal import Decimal

def add_decimal_col(df, price_type):
    values = df.loc[:, price_type]
    m_list = []
    for i in values:
        if type(i) == float:
            continue
        value = Decimal(sub(r'[^\d.]', '', i))
        m_list.append(value)
    try:
        df["Price Decimal"] = m_list
    except ValueError:
        print('Not available. Try different price type')
    return df


def median_price(df, price_type):
    add_decimal_col(df, price_type)
    f_value = df.loc[:, "Price Decimal"].median()
    print(f_value)
    f_value = convert_to_dollars(f_value)
    print(f_value)
    return f_value

def mean_price(df, price_type):
    #will do same as above but with the averages
    add_decimal_col(df, price_type)
    f_value = df.loc[:, "Price Decimal"].mean()
    f_value = convert_to_dollars(f_value)
    return f_value

def diff_list_sales(df):
    #this function will show the average difference between sales and list prices
    pass 

def convert_to_dollars(value):
    #function to convert a calculation back to dollars
    f_value = "{:,}".format(value)
    f_value = f'${f_value}'
    return f_value