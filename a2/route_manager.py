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


