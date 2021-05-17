import pandas as pd 

from ppersqft import calc_average, calc_avg
from median_avg_price import median_price, mean_price
from agent_analysis import find_top_agents


df = pd.read_csv('BCD_sales.csv')
average_ppersqft = calc_average(df)
median_sales = median_price(df, 'Sale Price')
mean_sales = mean_price(df, "Sale Price")
top_agents = find_top_agents(df, 3)

with open("data.txt", "w") as file:
    file.write(f'AvgPricePerSqFt: {average_ppersqft}\n')
    file.write(f'Median Sales Price: {median_sales}\n')
    file.write(f'Mean Sales Price: {mean_sales}\n')
    file.write(f'Top Agents: {top_agents}')

