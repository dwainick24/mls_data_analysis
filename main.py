#this program will parse the data from the mls and will analyze that data 
from price_per_sqft import calc_avg
from median_avg_price import median_price, mean_price
from agent_analysis import find_top_agents

import pandas as pd 

df = pd.read_csv('data_agents.csv')
average_ppersqft = calc_avg(df)
median_list = median_price(df, 'List Price')
median_sales = median_price(df, 'Sale Price')
mean_list = mean_price(df, "List Price")
mean_sales = mean_price(df, "Sale Price")
top_agents = find_top_agents(df, 3)

with open("data.txt", "w") as file:
    file.write(f'AvgPricePerSqFt: {average_ppersqft}\n')
    file.write(f'Median: {median_list}\n')
    file.write(f'Median Sales Price: {median_sales}\n')
    file.write(f'Mean List Price: {mean_list}\n')
    file.write(f'Mean Sales Price: {mean_sales}\n')
    file.write(f'Top Agents: {top_agents}')
