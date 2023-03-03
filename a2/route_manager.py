#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 8 14:44:33 2023
Based on: https://www.kaggle.com/datasets/arbazmohammad/world-airports-and-airlines-datasets
Sample input: --AIRLINES="airlines.yaml" --AIRPORTS="airports.yaml" --ROUTES="routes.yaml" --QUESTION="q1" --GRAPH_TYPE="bar"
@author: rivera
@author: STUDENT_ID
"""
import yaml






#def sample_function(input: str) -> str:
#    """Sample function (removable) that illustrations good use of documentation.
#            Parameters
#            ----------
#                input : str, required
#                    The input message.
#
#
 #           Returns
#            -------
#                str
#                    The text returned.
#    """
#    return input.upper()


import pandas as pd
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 8 14:44:33 2023
Based on: https://www.kaggle.com/datasets/arbazmohammad/world-airports-and-airlines-datasets
Sample input: --AIRLINES="airlines.yaml" --AIRPORTS="airports.yaml" --ROUTES="routes.yaml" --QUESTION="q1" --GRAPH_TYPE="bar"
@author: rivera
@author: 
""" 
import sys
import yaml
import pandas as pd
import matplotlib.pyplot as plt
#!/usr/bin/env python
# coding: utf-8

# In[5]:


import sys
import yaml
import pandas as pd
import matplotlib.pyplot as plt

def question1(airline_df: pd.DataFrame, airports_df: pd.DataFrame, routes_df: pd.DataFrame, question: str, graph_type: str) -> None:

    airline_df.drop(['airline_country'], inplace=True, axis=1)
    airports_df.drop(['airport_name', 'airport_city', 'airport_icao_unique_code', 'airport_altitude'], inplace=True, axis=1)
    routes_df.drop(['route_from_aiport_id'], inplace=True, axis=1)

    airports_df = airports_df[airports_df['airport_country']=='Canada']

    routes_df = routes_df.rename(columns={'route_airline_id':'airline_id'})
    answer: pd.DataFrame = routes_df.merge(airline_df, on='airline_id', how='inner') 


    answer = answer.rename(columns={'route_to_airport_id':'airport_id'})
    answer = answer.merge(airports_df, on='airport_id', how='inner')  

    answer = df_lstrip(answer,answer.columns)
    answer = answer.groupby(['airline_name', 'airline_icao_unique_code'], as_index=False).size().sort_values(by=['size', 'airline_name'], ascending=[False, True]).head(20) 
    process_data(answer, question, graph_type) 


def question2(airline_df: pd.DataFrame, airports_df: pd.DataFrame, routes_df: pd.DataFrame, question: str, graph_type: str) -> None:
  
    airline_df.drop(['airline_country', 'airline_name', 'airline_icao_unique_code'], inplace=True, axis=1)
    airports_df.drop(['airport_name', 'airport_city', 'airport_icao_unique_code', 'airport_altitude'], inplace=True, axis=1)
    routes_df.drop(['route_from_aiport_id'], inplace=True, axis=1)

    routes_df = routes_df.rename(columns={'route_to_airport_id':'airport_id'})
    answer = routes_df.merge(airports_df, on='airport_id', how='inner') 

    answer = df_lstrip(answer,answer.columns)
    answer = answer.groupby(['airport_country'], as_index=False).size().sort_values(by=['size', 'airport_country']).head(30)
    process_data(answer, question, graph_type) 
     

def question3(airline_df: pd.DataFrame, airports_df: pd.DataFrame, routes_df: pd.DataFrame, question: str, graph_type: str) -> None:
   
  
    airline_df.drop(['airline_country', 'airline_name', 'airline_icao_unique_code'], inplace=True, axis=1)
    airports_df.drop(['airport_altitude'], inplace=True, axis=1)
    routes_df.drop(['route_from_aiport_id'], inplace=True, axis=1)
    
    routes_df = routes_df.rename(columns={'route_airline_id':'airline_id'})
    answer: pd.DataFrame = routes_df.merge(airline_df, on='airline_id', how='left') 
    answer = answer.rename(columns={'route_to_airport_id':'airport_id'})
    answer = answer.merge(airports_df, on='airport_id', how='left') 
    
    answer = df_lstrip(answer,answer.columns)
    answer = answer.groupby(['airport_name', 'airport_icao_unique_code', 'airport_city', 'airport_country'], as_index=False).size().sort_values(by=['size', 'airport_name'], ascending=[False, True]).head(10) 
    process_data(answer, question, graph_type) 

def question4(airports_df: pd.DataFrame, routes_df: pd.DataFrame, question: str, graph_type: str) -> None:

   
    airports_df.drop(['airport_altitude', 'airport_icao_unique_code', 'airport_name'], inplace=True, axis=1)
    routes_df.drop(['route_from_aiport_id'], inplace=True, axis=1)

    airports_df = airports_df.rename(columns={'airport_id':'route_to_airport_id'})
    answer: pd.DataFrame = routes_df.merge(airports_df, on='route_to_airport_id', how='inner') 
    
    answer = df_lstrip(answer,answer.columns)
    answer = answer.groupby(['airport_city', 'airport_country'], as_index=False).size().sort_values(by=['size', 'airport_city'], ascending=[False, True]).head(15) 
    process_data(answer, question, graph_type) 

def question5(airline_df: pd.DataFrame, airports_df: pd.DataFrame, routes_df: pd.DataFrame, question: str, graph_type: str) -> None:
 

   

    airline_df.drop(['airline_country', 'airline_name', 'airline_icao_unique_code'], inplace=True, axis=1)
    airports_df.drop(['airport_name', 'airport_city'], inplace=True, axis=1)
    
    airports_df = airports_df[airports_df['airport_country']=='Canada']

    airports_df = airports_df.rename(columns = {'airport_id':'route_to_airport_id'})
    answer: pd.DataFrame = routes_df.merge(airports_df, on='route_to_airport_id', how='inner')
    answer = answer.rename(columns = {'airport_altitude':'to_airport_altitude', 'airport_icao_unique_code':'to_airport_icao_unique_code'})

    airports_df = airports_df.rename(columns = {'route_to_airport_id': 'route_from_aiport_id'})
    answer = answer.merge(airports_df, on='route_from_aiport_id', how='inner')
    answer = answer.rename(columns = {'airport_altitude':'from_airport_altitude', 'airport_icao_unique_code':'from_airport_icao_unique_code'})

    answer['diff'] = -1.0               # creating a new column to store the difference and initializing it to -1 since the calculated difference >= 0
    answer = column_diff(answer, 'to_airport_altitude', 'from_airport_altitude', 'diff')
    answer = df_lstrip(answer,answer.columns)
    answer = answer.sort_values(by=['diff', 'to_airport_icao_unique_code', 'from_airport_icao_unique_code'], ascending=[False, True, True]) 
    process_data(answer, question, graph_type) 

def clear_duplicates(df: pd.DataFrame) -> tuple:
    

   

    uniques: tuple = []
    for index, row in df.iterrows(): 
        tmp1: tuple = (df.loc[index,'from_airport_icao_unique_code'], df.loc[index,'to_airport_icao_unique_code'], df.loc[index,'diff']) 
        tmp2: tuple = (df.loc[index,'to_airport_icao_unique_code'], df.loc[index,'from_airport_icao_unique_code'], df.loc[index,'diff']) 
        if tmp1 not in uniques and tmp2 not in uniques:
            uniques.append(tmp1) 
        
    return uniques
        
    
def column_diff(df: pd.DataFrame, in1: str, in2: str, out: str) -> pd.DataFrame:
    

  

    uniques: tuple = []
    for index, row in df.iterrows(): 
        df.loc[index,out] = abs(float(row[in1]) - float(row[in2]))   
    return df

    
def df_lstrip(df: pd.DataFrame, columns: str) -> pd.DataFrame: 
    

   

    for index, row in df.iterrows(): 
        for column in columns:
            if type(df.loc[index,column]) == str:
                df.loc[index,column] = df.loc[index,column].lstrip()
    return df

def process_data(answer: pd.DataFrame, question: str, graph_type: str) -> None:
    

   

    output_csv: file = open(f"{question}.csv",'w')
    keys: str = []
    values: int = [] 
    
    output_csv.write("subject,statistic\n")                     # writing to the csv file based on the question
    for index, row in answer.iterrows():
        if question == 'q1':
            keys.append(row['airline_name'])
            values.append(float(row['size']))
            output_csv.write(f"{row['airline_name']} ({row['airline_icao_unique_code']}),{row['size']}\n")
            
        elif question == 'q2':
            keys.append(row['airport_country'])
            values.append(float(row['size']))
            output_csv.write(f"{row['airport_country']},{row['size']}\n")

        elif question == 'q3':
            keys.append(f"{row['airport_name']} ({row['airport_icao_unique_code']})")
            values.append(float(row['size']))
            output_csv.write(f"\"{row['airport_name']} ({row['airport_icao_unique_code']}), {row['airport_city']}, {row['airport_country']}\",{row['size']}\n")

        elif question == 'q4':
            keys.append(f"{row['airport_city']}, {row['airport_country']}")
            values.append(float(row['size']))
            output_csv.write(f"\"{row['airport_city']}, {row['airport_country']}\",{row['size']}\n")

    if question == 'q5':                                      
        uniques = clear_duplicates(answer)                  # q5 is implemented differently than q1-q4 so it has its on individual case
        for i in range(10):
            keys.append(f"{uniques[i][0]}-{uniques[i][1]}")
            values.append(uniques[i][2])
            output_csv.write(f"{uniques[i][0]}-{uniques[i][1]},{uniques[i][2]}\n")
            
    f = plt.figure(figsize=(10,7))                          # creating the pie or bar chart based on the graph_type and saving it as a pdf file
    if graph_type == 'bar':
        plt.bar(keys, values)
        plt.tick_params(axis='x', which='major', labelsize=8)
        plt.xticks(rotation=60)
        plt.subplots_adjust(top=0.9, bottom=0.3)

    else:
        plt.pie(values, labels=keys, autopct='%1.0f%%', labeldistance=1.2, pctdistance=0.7)
        plt.subplots_adjust(left=0.1)

    if question == 'q1':
        plt.title("Top 20 Airlines With The Greatest Number Of Routes To Canada")
        if graph_type == 'bar':
            plt.xlabel("Airlines")
            plt.ylabel("Frequency")

    elif question == 'q2':
        plt.title("Top 30 Countries With The Least Appearances As A Destination Country")
        if graph_type == 'bar':
            plt.xlabel("Countries")
            plt.ylabel("Frequency")

    elif question == 'q3':
        plt.title("Top 10 Destination Airports")
        if graph_type == 'bar':
            plt.xlabel("Airports")
            plt.ylabel("Frequency")
        
    elif question == 'q4':
        plt.title("Top 15 Destination Cities")
        if graph_type == 'bar':
            plt.xlabel("Cities")
            plt.ylabel("Frequency")
        
    else:
        plt.title("Top 10 Canadian Routes With The Greatest Difference In Altitude")
        if graph_type == 'bar':
            plt.xlabel("Routes")
            plt.ylabel("Difference In Altitude")
        
    f.savefig(f"{question}.pdf")
    output_csv.close()

   
    
def main():
    print(sys.argv)
    #str airline = sys.argv[1].split('=')
     
    airline: str = sys.argv[1].split('=')[1]                # extracting the command line arguments
    airports: str = sys.argv[2].split('=')[1]        
    routes: str = sys.argv[3].split('=')[1]
    question: str = sys.argv[4].split('=')[1]
    graph_type: str = sys.argv[5].split('=')[1]
    
    with open(airline) as f:                                                # creating dataframes for the respective files
        airline_df: pd.DataFrame = pd.DataFrame(yaml.safe_load(f)['airlines'])

    with open(airports) as f:
        airports_df: pd.DataFrame = pd.DataFrame(yaml.safe_load(f)['airports'])

    with open(routes) as f:
        routes_df: pd.DataFrame = pd.DataFrame(yaml.safe_load(f)['routes'])
    
    if question == 'q1':
        question1(airline_df, airports_df, routes_df, question, graph_type)
        

    elif question == 'q2':
        question2(airline_df, airports_df, routes_df, question, graph_type)

    elif question == 'q3':
        question3(airline_df, airports_df, routes_df, question, graph_type)

    elif question == 'q4':
        question4(airports_df, routes_df, question, graph_type)

    else:
        question5(airline_df, airports_df, routes_df, question, graph_type)
        
        

if __name__ == '__main__':
    main()

#def main():
#    with open('airlines.yaml', 'r') as f:
   
#        airlines_data = yaml.safe_load(f)
#        airlines_df = pd.DataFrame(airlines_data)
      
       
#    with open('airports.yaml', 'r') as f:
#        airports_data = yaml.safe_load(f)
#        airports_df = pd.DataFrame(airports_data)

#    with open('routes.yaml', 'r') as f:
#        routes_data = yaml.safe_load(f)
#        routes_data = pd.DataFrame(f)
    
#    airlines_df.drop(['airline_country'], inplace=True, axis=1)
#    airports_df.drop(['airport_name', 'airport_city', 'airport_icao_unique_code', 'airport_altitude'], inplace=True, axis=1)
#    routes_df.drop(['route_from_aiport_id'], inplace=True, axis=1)


#    airports_df = airports_df[airports_df['airport_country']=='Canada']

 #   routes_df = routes_df.rename(columns={'route_airline_id':'airline_id'})
#    answer: pd.DataFrame = routes_df.merge(airlines_df, on='airline_id', how='inner') 
#    answer = answer.rename(columns={'route_to_airport_id':'airport_id'})
#    answer = answer.merge(airports_df, on='airport_id', how='inner') 

    #answer = df_lstrip(answer,answer.columns)
    #answer = answer.groupby(['airline_name', 'airline_icao_unique_code'], as_index=False).size().sort_values(by=['size', 'airline_name'], ascending=[False, True]).head(20) 
    #process_data(answer, question, graph_type) 

    
    # Merge airlines_df and airports_df on the 'country' column
#    airlines_airports_df = pd.merge(airlines_df, airports_df, on='airline_name')
    # Merge airlines_airports_df and routes_df on the 'airline' column
#    merged_df = pd.merge(airlines_airports_df, routes_df, on='airline')
#    print(merged_df)

#if __name__ == '__main__':
#    main()







if __name__ == '__main__':
    main()

#def main():
#    with open('airlines.yaml', 'r') as f:
   
#        airlines_data = yaml.safe_load(f)
#        airlines_df = pd.DataFrame(airlines_data)
      
       
#    with open('airports.yaml', 'r') as f:
#        airports_data = yaml.safe_load(f)
#        airports_df = pd.DataFrame(airports_data)

#    with open('routes.yaml', 'r') as f:
#        routes_data = yaml.safe_load(f)
#        routes_data = pd.DataFrame(f)
    
#    airlines_df.drop(['airline_country'], inplace=True, axis=1)
#    airports_df.drop(['airport_name', 'airport_city', 'airport_icao_unique_code', 'airport_altitude'], inplace=True, axis=1)
#    routes_df.drop(['route_from_aiport_id'], inplace=True, axis=1)


#    airports_df = airports_df[airports_df['airport_country']=='Canada']

 #   routes_df = routes_df.rename(columns={'route_airline_id':'airline_id'})
#    answer: pd.DataFrame = routes_df.merge(airlines_df, on='airline_id', how='inner') 
#    answer = answer.rename(columns={'route_to_airport_id':'airport_id'})
#    answer = answer.merge(airports_df, on='airport_id', how='inner') 

    #answer = df_lstrip(answer,answer.columns)
    #answer = answer.groupby(['airline_name', 'airline_icao_unique_code'], as_index=False).size().sort_values(by=['size', 'airline_name'], ascending=[False, True]).head(20) 
    #process_data(answer, question, graph_type) 

    
    # Merge airlines_df and airports_df on the 'country' column
#    airlines_airports_df = pd.merge(airlines_df, airports_df, on='airline_name')
    # Merge airlines_airports_df and routes_df on the 'airline' column
#    merged_df = pd.merge(airlines_airports_df, routes_df, on='airline')
#    print(merged_df)

#if __name__ == '__main__':
#    main()

'''
with open('airlines.yaml', 'r') as f:
        airlines_data = yaml.safe_load(f)['airlines']
        airlines_df = pd.DataFrame(airlines_data)
      
       
    with open('airports.yaml', 'r') as f:
        airports_data = yaml.safe_load(f)
        airports_df = pd.DataFrame(airports_data)

    with open('routes.yaml', 'r') as f:
        routes_data = yaml.safe_load(f)
        routes_data = pd.DataFrame(f)
        '''