#file will find the price per square foot. Will be done much better than the first one
import pandas as pd 

#function will convert all sq foot and price strings to floats
def convert_all_float(df, price_type, sqfttype):
    for i in range(len(df)):
        df.loc[i, price_type] = df.loc[i, price_type].replace(',', '')
        df.loc[i, price_type] = float(df.loc[i, price_type].replace('$', ''))
        #print(type(df.loc[i, sqfttype]))
        if type(df.loc[i, sqfttype]) == str:
            df.loc[i, sqfttype] = df.loc[i, sqfttype].replace(',', '')
            df.loc[i, sqfttype]  = float(df.loc[i, sqfttype].replace('¤', ''))

    return df

def ppersqft_add(df, price_type, sqfttype):
    #grab both the price type and sqfttype columns
    new_df = df.loc[:, [price_type, sqfttype]]
    new_df = convert_all_float(new_df, price_type, sqfttype)
    for i in range(len(new_df)):
        if new_df.loc[i, sqfttype] == 0:
          new_df = new_df.drop(axis=0, index=i)
    new_df['Price Per SqFt'] = new_df[price_type]/new_df[sqfttype]
    return new_df

def calc_average(df, price_type, sqfttype):
    new_df = ppersqft_add(df, price_type, sqfttype)
    average = new_df['Price Per SqFt'].mean()
    return average

if __name__ == '__main__':
    df = pd.read_csv('BCD_listed.csv')
    price = ppersqft_add(df, 'List Price', 'SqFt Liv Area')
    price = calc_average(price)
    print(price)


