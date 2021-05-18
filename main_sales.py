import pandas as pd 

from ppersqft import calc_average
from median_avg_price import median_price, mean_price, diff_list_sales_avg
from agent_analysis import find_top_agents


df = pd.read_csv('BCD_sales.csv')
average_ppersqft = calc_average(df, 'Sale Price', 'SqFt Liv Area')
median_sales = median_price(df, 'Sale Price')
mean_sales = mean_price(df, "Sale Price")
top_agents = find_top_agents(df, 3)
diff_list_sales = diff_list_sales_avg(df)

with open("data.txt", "w") as file:
    file.write(f'AvgPricePerSqFt: {average_ppersqft}\n')
    file.write(f'Median Sales Price: {median_sales}\n')
    file.write(f'Mean Sales Price: {mean_sales}\n')
    file.write(f'Top Agents: {top_agents}\n')
    file.write(f'Diff List Sales: {diff_list_sales}')

