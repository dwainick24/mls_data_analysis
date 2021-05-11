#this file will have a function that holds the price per square foot calculations 

def price_per_sqft_list(df):
    #takes in dataframe and adds price per square foot to it 
    price_per_sqft = []
    for i in range(len(df)):
        price = df.iloc[i, 7].split('$')[1]
        #print(price)
        price = float(price.replace(',', ''))
        try:
            sqft = df.iloc[i, 12]
            #print(sqft)
            sqft = int(sqft.replace(',', ''))
        except ValueError:
            sqft = int(df.iloc[i, 12][1:].replace(',', ''))
        except AttributeError:
            sqft = 1
        if sqft == 0:
            sqft = 1
        price_sqft = price/sqft
    #df.iloc[i]['Price Per SqFt'] = price_sqft
    #i[1]['price per sqft'] = price_sqft
        price_per_sqft.append(price_sqft)
    return price_per_sqft

def add_to(df):
    #adds the price per sq. foot to a df 
    list_psqft = price_per_sqft_list(df)
    df['Price Per SqFt'] = list_psqftd
    return df

def calc_avg(df):
    #calculates the average price per square foot
    calc = 0 
    list_psqft = price_per_sqft_list(df)
    for i in list_psqft:
        calc += i
    calc = calc/len(list_psqft)
    return calc