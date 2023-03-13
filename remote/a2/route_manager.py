#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 8 14:44:33 2023
Based on: https://www.kaggle.com/datasets/arbazmohammad/world-airports-and-airlines-datasets
Sample input: --AIRLINES="airlines.yaml" --AIRPORTS="airports.yaml" --ROUTES="routes.yaml" --QUESTION="q1" --GRAPH_TYPE="bar"
@author: rivera
@author: kokiitagaki
"""
import numpy as np
import csv
import sys
import yaml
import pandas as pd
import matplotlib.pyplot as plt
import argparse



def question1(airline_df: pd.DataFrame, airports_df: pd.DataFrame, routes_df: pd.DataFrame, question: str, graph_type: str) -> None:
    '''
    This function performs data processing tasks and generates a visualization in the form of a bar or pie chart for the top 20 airlines with the greatest number of routes to Canada.
    The function saves the results to both a CSV file and a PDF file with a filename that matches the 'question' parameter.
    :param pd.DataFrame  airline_df: The dataframe which contains airlines information
    :param pd.DataFrame airport_df: The dataframe which contains airports information
    :param pd.DataFrame routes_df: The dataframe which contains routes information
    :param str question: The specific question which you would like this function to solve.
    :param str graph_type: The specific type of the graph which you would like to output into a pdf file
    :return: the program passes the final data frame to another function thus returns nothing
    '''
    airline_df = airline_df.drop(['airline_country'], axis=1)
    airports_df = airports_df.drop(['airport_name', 'airport_city', 'airport_icao_unique_code', 'airport_altitude'], axis=1)
    routes_df = routes_df.drop(['route_from_aiport_id'], axis=1)

    airports_df = airports_df[airports_df['airport_country'] == 'Canada']

    routes_df = routes_df.rename(columns={'route_airline_id': 'airline_id'})
    sol = pd.merge(routes_df, airline_df, on='airline_id', how='inner')
    sol = sol.rename(columns={'route_to_airport_id': 'airport_id'})
    sol = pd.merge(sol, airports_df, on='airport_id', how='inner')
    sol = remove_space(sol, sol.columns)
    sol = sol.groupby(['airline_name', 'airline_icao_unique_code']).size().reset_index(name='size')
    sol = sol.sort_values(by=['size', 'airline_name'], ascending=[False, True]).head(20)

    
    # Writing the data to CSV file
    with open(f"{question}.csv", mode='w') as output_csv:
        writer = csv.writer(output_csv)
        writer.writerow(['subject', 'statistic'])
        keys = []
        values = []
        for index, row in sol.iterrows():
            keys.append(f"{row['airline_name']} ({row['airline_icao_unique_code']})")
            values.append(float(row['size']))
            writer.writerow([f"{row['airline_name']} ({row['airline_icao_unique_code']})", row['size']])

    # Creating the plot
    fig, ax = plt.subplots(figsize=(10,7))
    if graph_type == 'bar':
        ax.bar(keys, values)
        ax.tick_params(axis='x', which='major', labelsize=8)
        ax.set_xticks(range(len(keys)))
        ax.set_xticklabels(keys, rotation=60, ha='right', fontsize=8)
        ax.set_xlim(-0.5, len(keys)-0.5)
        ax.set_ylim(bottom=0)
        ax.set_xlabel('Airlines')
        ax.set_ylabel('Frequency')
        ax.set_title('Top 20 Airlines With The Greatest Number Of Routes To Canada')
    else:
        ax.pie(values, labels=keys, autopct='%1.0f%%', labeldistance=1.0, pctdistance=0.5)
        ax.set_title('Top 20 Airlines With The Greatest Number Of Routes To Canada')

    # Saving the plot to PDF
    fig.savefig(f"{question}.pdf")



def question2(airline_df: pd.DataFrame, airports_df: pd.DataFrame, routes_df: pd.DataFrame, question: str, graph_type: str) -> None:
    '''
    This function performs data processing tasks and generates a visualization in the form of a bar chart or pie chart for the top 30 countries with the least appearances as a destination country.
    The function then saves the resulting dataframe to a CSV file and generates a corresponding bar chart or pie chart, based on the graph_type parameter, with the number of routes on the y-axis and the countries on the x-axis or labels of the pie chart.
    The function saves the resulting chart to a PDF file with a filename that matches the 'question' parameter.
    :param pd.DataFrame airline_df: The dataframe which contains airlines information
    :param pd.DataFrame airports_df: The dataframe which contains airports information
    :param pd.DataFrame routes_df: The dataframe which contains routes information
    :param str question: The specific question which you would like this function to solve.
    :param str graph_type: The specific type of the graph which you would like to output into a pdf file
    :return: the program passes the final data frame to another function thus returns nothing
    '''


    airports_df.drop(['airport_name', 'airport_city', 'airport_icao_unique_code', 'airport_altitude'], inplace=True, axis=1)
    routes_df.drop(['route_from_aiport_id'], inplace=True, axis=1)

    routes_df = routes_df.rename(columns={'route_to_airport_id':'airport_id'})
    sol = routes_df.merge(airports_df, on='airport_id', how='inner') 

    sol = remove_space(sol,sol.columns)
    sol = sol.groupby(['airport_country'], as_index=False).size().sort_values(by=['size', 'airport_country']).head(30)
    
        # Writing the data to CSV file
    with open(f"{question}.csv", mode='w') as output_csv:
        writer = csv.writer(output_csv)
        writer.writerow(['subject', 'statistic'])
        keys = []
        values = []
        for index, row in sol.iterrows():
            keys.append(row['airport_country'])
            values.append(float(row['size']))
            writer.writerow([row['airport_country'], row['size']])
        
        # Creating the plot
    fig, ax = plt.subplots(figsize=(10,7))
    if graph_type == 'bar':
        ax.bar(keys, values)
        ax.tick_params(axis='x', which='major', labelsize=8)
        ax.set_xticks(range(len(keys)))
        ax.set_xticklabels(keys, rotation=60)
        ax.set_xlabel('Countries')
        ax.set_ylabel('Frequency')
        ax.set_title('Top 30 Countries With The Least Appearances As A Destination Country')
        fig.subplots_adjust(top=1.0, bottom=0.1)
    else:
        ax.pie(values, labels=keys, autopct='%1.0f%%', labeldistance=1.0, pctdistance=0.5)
        ax.set_title('Top 30 Countries With The Least Appearances As A Destination Country')
        fig.subplots_adjust(left=0.1)
    # Saving the plot to PDF
    fig.savefig(f"{question}.pdf")
    



def question3(airline_df: pd.DataFrame, airports_df: pd.DataFrame, routes_df: pd.DataFrame, question: str, graph_type: str) -> None:
    '''
    This function performs data processing tasks and generates a visualization in the form of a bar chart or pie chart for the top 10 destination airports.
    The function then saves the resulting dataframe to a CSV file and generates a corresponding bar chart or pie chart, based on the graph_type parameter, with the number of routes on the y-axis and the countries on the x-axis or labels of the pie chart.
    The function saves the resulting chart to a PDF file with a filename that matches the 'question' parameter.
    :param pd.DataFrame airline_df: The dataframe which contains airlines information
    :param pd.DataFrame airports_df: The dataframe which contains airports information
    :param pd.DataFrame routes_df: The dataframe which contains routes information
    :param str question: The specific question which you would like this function to solve.
    :param str graph_type: The specific type of the graph which you would like to output into a pdf file
    :return: the program passes the final data frame to another function thus returns nothing
    '''
    airline_df = airline_df.drop(['airline_country', 'airline_name', 'airline_icao_unique_code'], axis=1)
    airports_df = airports_df.drop(['airport_altitude'], axis=1)
    routes_df = routes_df.drop(['route_from_aiport_id'], axis=1)

    routes_df = routes_df.rename(columns={'route_airline_id':'airline_id'})
    sol = pd.merge(routes_df, airline_df, on='airline_id', how='left')
    sol = sol.rename(columns={'route_to_airport_id':'airport_id'})
    sol = pd.merge(sol, airports_df, on='airport_id', how='left')
    sol = remove_space(sol, sol.columns)
    sol = sol.groupby(['airport_name', 'airport_icao_unique_code', 'airport_city', 'airport_country']).size().reset_index(name='size').sort_values(by=['size', 'airport_name'], ascending=[False, True]).head(10)

        # Writing the data to CSV file
    with open(f"{question}.csv", mode='w') as output_csv:
        writer = csv.writer(output_csv)
        writer.writerow(['subject', 'statistic'])
        for index, row in sol.iterrows():
            airport_label = f"{row['airport_name']} ({row['airport_icao_unique_code']}), {row['airport_city']}, {row['airport_country']}"
            writer.writerow([airport_label, row['size']])
    keys = [f"{row['airport_name']} ({row['airport_icao_unique_code']})" for index, row in sol.iterrows()]
    values = [float(row['size']) for index, row in sol.iterrows()]

        # Creating the plot
    fig, ax = plt.subplots(figsize=(10,7))
    if graph_type == 'bar':
        ax.bar(keys, values)
        ax.tick_params(axis='x', which='major', labelsize=8)
        ax.set_xticks(range(len(keys)))
        ax.set_xticklabels(keys, rotation=60)
        ax.set_ylim(bottom=0)
        ax.set_xlabel('Airports')
        ax.set_ylabel('Frequency')
        ax.set_title("Top 10 Destination Airports")
    else:
        labels = [f"{row['airport_name']} ({row['airport_icao_unique_code']})\n{row['airport_city']}, {row['airport_country']}" for index, row in sol.iterrows()]
        ax.pie(values, labels=labels, autopct='%1.0f%%', labeldistance=1.0, pctdistance=0.5)
        ax.set_title("Top 10 Destination Airports")

    # Saving the plot to PDF
    fig.savefig(f"{question}.pdf")






def question4(airline_df: pd.DataFrame,airports_df: pd.DataFrame, routes_df: pd.DataFrame, question: str, graph_type: str) -> None:
    '''
    This function performs data processing tasks and generates a visualization in the form of a bar chart or pie chart for the top 15 destination cities.
    The function then saves the resulting dataframe to a CSV file and generates a corresponding bar chart or pie chart, based on the graph_type parameter, with the number of routes on the y-axis and the countries on the x-axis or labels of the pie chart.
    The function saves the resulting chart to a PDF file with a filename that matches the 'question' parameter.
    :param pd.DataFrame airline_df: The dataframe which contains airlines information
    :param pd.DataFrame airports_df: The dataframe which contains airports information
    :param pd.DataFrame routes_df: The dataframe which contains routes information
    :param str question: The specific question which you would like this function to solve.
    :param str graph_type: The specific type of the graph which you would like to output into a pdf file
    :return: the program passes the final data frame to another function thus returns nothing
    ''' 
    airports_df = airports_df.drop(['airport_altitude', 'airport_icao_unique_code', 'airport_name'], axis=1)
    routes_df = routes_df.drop(['route_from_aiport_id'], axis=1)

    routes_df['route_to_airport_id'] = routes_df['route_to_airport_id'].astype(str)
    airports_df = airports_df.rename(columns={'airport_id':'route_to_airport_id'})
    sol = pd.merge(routes_df, airports_df, on='route_to_airport_id', how='inner') 
    sol = remove_space(sol, sol.columns)
    sol = sol.groupby(['airport_city', 'airport_country']).size().reset_index(name='size').sort_values(by=['size', 'airport_city'], ascending=[False, True]).head(15)
    
        # Writing the data to CSV file
    with open(f"{question}.csv", mode='w') as output_csv:
        writer = csv.writer(output_csv)
        writer.writerow(['subject', 'statistic'])
        for index, row in sol.iterrows():
            writer.writerow([f"{row['airport_city']}, {row['airport_country']}", row['size']])
    keys = [f"{row['airport_city']}, {row['airport_country']}" for index, row in sol.iterrows()]
    values = [float(row['size']) for index, row in sol.iterrows()]

    # Creating the plot
    fig, ax = plt.subplots(figsize=(10,7))
    if graph_type == 'bar':
        ax.bar(keys, values)
        ax.tick_params(axis='x', which='major', labelsize=8)
        ax.set_xticks(range(len(keys)))
        ax.set_xticklabels(keys, rotation=60, ha='right')
        ax.set_xlim(-0.5, len(keys)-0.5)
        ax.set_ylim(bottom=0)
        ax.set_xlabel('Cities')
        ax.set_ylabel('Frequency')
        ax.set_title("Top 15 Destination Cities")
    else:
        ax.pie(values, labels=keys, autopct='%1.0f%%', labeldistance=1.0, pctdistance=0.5)
        ax.set_title("Top 15 Destination Cities")

    # Saving the plot to PDF
    fig.savefig(f"{question}.pdf")
    




def question5(airline_df: pd.DataFrame, airports_df: pd.DataFrame, routes_df: pd.DataFrame, question: str, graph_type: str) -> None:
    '''
    This function performs data processing tasks and generates a visualization in the form of a bar chart or pie chart for the top 15 destination cties.
    The function then saves the resulting dataframe to a CSV file and generates a corresponding bar chart or pie chart, based on the graph_type parameter, with the number of routes on the y-axis and the countries on the x-axis or labels of the pie chart.
    The function saves the resulting chart to a PDF file with a filename that matches the 'question' parameter.
    :param pd.DataFrame airline_df: The dataframe which contains airlines information
    :param pd.DataFrame airports_df: The dataframe which contains airports information
    :param pd.DataFrame routes_df: The dataframe which contains routes information
    :param str question: The specific question which you would like this function to solve.
    :param str graph_type: The specific type of the graph which you would like to output into a pdf file
    :return: the program passes the final data frame to another function thus returns nothing
    '''
    airline_df = airline_df.drop(['airline_country', 'airline_name', 'airline_icao_unique_code'], axis=1)
    airports_df = airports_df.drop(['airport_name', 'airport_city'],axis=1)

    airports_df_canada = airports_df[airports_df['airport_country']=='Canada']
    airports_df_canada = airports_df_canada.rename(columns = {'airport_id':'route_to_airport_id'})

    sol = pd.merge(routes_df, airports_df_canada, on='route_to_airport_id', how='inner')
    sol = sol.rename(columns = {'airport_altitude':'to_airport_altitude', 'airport_icao_unique_code':'to_airport_icao_unique_code'})
    airports_df_canada = airports_df_canada.rename(columns = {'route_to_airport_id': 'route_from_aiport_id'})
    sol = pd.merge(sol, airports_df_canada, on='route_from_aiport_id', how='inner')
    sol = sol.rename(columns = {'airport_altitude':'from_airport_altitude', 'airport_icao_unique_code':'from_airport_icao_unique_code'})
     # Calculate the absolute difference in altitude between the 'to' and 'from' airports and remove any extra spaces from the dataframe
    sol['diff'] = abs(pd.to_numeric(sol['to_airport_altitude'], errors='coerce') - pd.to_numeric(sol['from_airport_altitude'], errors='coerce'))
  
    sol = remove_space(sol,sol.columns)
    sol = sol.sort_values(by=['diff', 'to_airport_icao_unique_code', 'from_airport_icao_unique_code'], ascending=[False, True, True]) 
    
     # Writing the data to CSV file
    with open(f"{question}.csv", mode='w') as output_csv:
        # Write header row
        output_csv.write("subject,statistic\n")
        keys = []
        values = []
        uniques = clear_duplicates(sol)
        for i in range(10):
            key = f"{uniques[i][0]}-{uniques[i][1]}"
            value = uniques[i][2]
            keys.append(key)
            values.append(value)
            output_csv.write(f"{key},{value}\n")

     # Create plot and adjust settings
    fig, ax = plt.subplots(figsize=(10,7))
    if graph_type == 'bar':
        ax.bar(keys, values)
        ax.tick_params(axis='x', which='major', labelsize=8)
        ax.set_xticks(range(len(keys)))
        ax.set_xticklabels(keys, rotation=60)
        ax.set_xlabel('Routes')
        ax.set_ylabel('Difference In Altitude')
        ax.set_title("Top 10 Canadian Routes With The Greatest Difference In Altitude")
        fig.subplots_adjust(top=1.0, bottom=0.1)
    else:
        ax.pie(values, labels=keys, autopct='%1.0f%%', labeldistance=1.0, pctdistance=0.5)
        ax.set_title("Top 10 Canadian Routes With The Greatest Difference In Altitude")
        fig.subplots_adjust(left=0.1)

    # Save plot to PDF file
    fig.savefig(f"{question}.pdf")



def clear_duplicates(df: pd.DataFrame) -> tuple:
    '''
    stores unique routes from the data frame as a list of tuples
    
    param df: data frame containing information about the routes used in quesiton 5
    return: a list of tuples containing only the unique routes from the data frame
    '''

    uniques: tuple = []
    for index, row in df.iterrows(): 
        tmp1: tuple = (df.loc[index,'from_airport_icao_unique_code'], df.loc[index,'to_airport_icao_unique_code'], df.loc[index,'diff']) 
        tmp2: tuple = (df.loc[index,'to_airport_icao_unique_code'], df.loc[index,'from_airport_icao_unique_code'], df.loc[index,'diff']) 
        if tmp1 not in uniques and tmp2 not in uniques:
            uniques.append(tmp1) 
        
    return uniques
        
    


def remove_space(df: pd.DataFrame, columns: str) -> pd.DataFrame: 
    '''
   Removes any whitespace characters from the beginning of the string.
    param df: The dataframe you would like this function to modify
    param columns: a list of the column names in df which is a dataframe
    return: The dataframe which the function modified  
    '''
    for column in columns:
        df[column] = df[column].apply(lambda s: s.lstrip() if isinstance(s, str) else s)
    return df



def main():

    # Creating the argument parser and adding command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--AIRLINES', type=str, required=True, help='Path to airlines YAML file')
    parser.add_argument('--AIRPORTS', type=str, required=True, help='Path to airports YAML file')
    parser.add_argument('--ROUTES', type=str, required=True, help='Path to routes YAML file')
    parser.add_argument('--QUESTION', type=str, required=True, help='Question to answer')
    parser.add_argument('--GRAPH_TYPE', type=str, required=True, help='Type of graph to use')

    args = parser.parse_args()


    #Loading each data into dataframes
    with open(args.AIRLINES) as f:
        airline_df = pd.DataFrame(yaml.safe_load(f)['airlines'])

    with open(args.AIRPORTS) as f:
        airports_df = pd.DataFrame(yaml.safe_load(f)['airports'])

    with open(args.ROUTES) as f:
        routes_df = pd.DataFrame(yaml.safe_load(f)['routes'])

    question = args.QUESTION
    graph_type = args.GRAPH_TYPE

    # Dictionary of functions for each question
    question_funcs = {
    'q1': question1,
    'q2': question2,
    'q3': question3,
    'q4': question4,
    'default': question5
}
    question_funcs.get(question, question_funcs['default'])(airline_df, airports_df, routes_df, question, graph_type)
  

if __name__ == '__main__':
    main()

