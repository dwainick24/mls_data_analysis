This program is for parsing through data on the MLS. It was written to help gather data for realtors and investors and possibly retail real estate consumers. 

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