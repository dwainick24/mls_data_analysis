#this program will parse the data from the mls and will analyze that data 
from ppersqft import calc_average
from median_avg_price import median_price, mean_price
from agent_analysis import find_top_agents

import pandas as pd 

df = pd.read_csv('BCD_listed.csv')
average_ppersqft = calc_average(df, 'List Price', 'SqFt Liv Area')
median_list = median_price(df, 'List Price')
mean_list = mean_price(df, "List Price")
top_agents = find_top_agents(df, 3)

with open("data_listed.txt", "w") as file:
    file.write(f'AvgPricePerSqFt: {average_ppersqft}\n')
    file.write(f'Median List Price: {median_list}\n')
    file.write(f'Mean List Price: {mean_list}\n')
    file.write(f'Top Agents: {top_agents}')
