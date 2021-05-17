This program is for parsing through statistics from the MLS. It was written to help gather data for realtors and investors and possibly retail real estate consumers. 

It currently consists of two different modules:
    main.py
    median_avg_price.py

    Main.py 
        consists of taking in a csv or dataframe, then using the other modules to do some calculations. Eventually, if it wasn't expensive, this could be done with an api call directly from the MLS


    Median_avg_price.py

    All the functions necessary to calculate the median and average List and Sales prices

    add_decimal_col
        takes in a dataframe and the price type 
        outputs a dataframe with the selected price type as a new row called "Price Decimal"
        This is necessary because the datatypes are strings and those cannot be used for math calculations 
    
    median_price
        Takes in a dataframe and the price type
        outputs the median price for selected price type 
    
    mean_price 
        Takes in a dataframe and the price type 
        Outputs the mean price for selected price type 
    
    diff_list_sales
        Takes in a dataframe 
        Outputs the average difference between the sales and list prices 
    
    convert_to_dollars
        takes in a value 
        converts value back to dollars 
    
    agent_analysis.py
    
    This file holds all the necessary functions to take in a dataset and find who are the top performing listing agents in a given dataset

    get_list_agent_count(df)
        takes in a pandas dataframe 
        outputs a dictionary with all the agents and how many properties they have listed or sold according to the data 
    
    find_top_agents_dict
        takes in the dictionary created by the function above, along with a number that determines how many top agents one would like to find 
        Outputs the top agents
    
    find_top_agents
        takes in a dataframe and a number 
        outputs the top agents using the functions above it 