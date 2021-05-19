#finds the average days on market for a dataframe
import pandas as pd 

#finds the days on market mean
def mean_dom(df):
    for i in range(len(df)):
        #convert all
        if type(df.loc[i, 'CDOM (Days on Market)']) == str:
            df.loc[i, 'CDOM (Days on Market)'] = int(df.loc[i, 'CDOM (Days on Market)'].replace(',', ''))
        elif type(df.loc[i, 'CDOM (Days on Market)']) == float:
            df = df.drop(axis=0, index=i)

    mean = df['CDOM (Days on Market)'].mean()
    return mean

#finds the median days on market
def median_dom(df):
    #TODO convert both this and the other to integers instead of strings
    for i in range(len(df)):
        if type(df.loc[i, 'CDOM (Days on Market)']) == str:
            df.loc[i, 'CDOM (Days on Market)'] = int(df.loc[i, 'CDOM (Days on Market)'].replace(',', ''))
        elif type(df.loc[i, 'CDOM (Days on Market)']) == float:
            df = df.drop(axis=0, index=i)

    median = df['CDOM (Days on Market)'].median()
    return median

if __name__ == '__main__':
    df = pd.read_csv('BCD_sales_DOM.csv')
    mean = mean_dom(df)
    median = median_dom(df)
    print(mean)
    print(median)
