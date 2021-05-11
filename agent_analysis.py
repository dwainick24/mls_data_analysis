#this file will find all the top performing agents in a market
import pandas as pd 
from collections import Counter

def get_list_agent_count(df):
    #will find the top list agent 
    values = df.loc[:, "Listing Agent's Name"]
    agents_set = set(values)
    agents = dict.fromkeys(agents_set, 0)
    for v in values:
        #if agent exists, add one
        #add each agent to the agent list 
        #assign that list to be the keys
        for a in agents.keys():
            if a == v:
                agents[v] += 1
    #print(agents)
    return agents

def find_top_agents_dict(agent_dict, num):
    #takes in the agent_dict, then finds the one with the highest count
    #convert agent_dict to a counter object 
    top_agents_count = Counter(agent_dict)
    #finish code 
    top_agents = top_agents_count.most_common(num)
    return top_agents   

def find_top_agents(df, num):
    #uses above two functions to find the top agents in the data
    agents_dict = get_list_agent_count(df)
    top_agent = find_top_agents_dict(agents_dict, num)
    return top_agent

def top_selling_agent(df):
    #will find top selling agent for dataframe. Not sure where to find this data 
    pass 

if __name__ == "__main__":
    df = pd.read_csv('data_agents.csv')
    agents = get_list_agent_count(df)
    print(agents)
    top_agents = find_top_agents_dict(agents, 3)
    print(top_agents)
