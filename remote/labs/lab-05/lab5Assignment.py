#!/usr/bin/env python
# coding: utf-8

# In[13]:


#!/usr/bin/env python
import pandas as pd
def main():
    drivers_df: pd.DataFrame = pd.read_csv('drivers.csv')
    results_df: pd.DataFrame = pd.read_csv('results.csv')
        
    drivers_df.drop(['driverRef', 'number', 'code', 'dob', 'url','forename','surname'], inplace=True, axis=1)
    results_df.drop(['raceId', 'constructorId', 'number', 'grid', 'position', 'positionText', 'points','laps','time', 'milliseconds', 'fastestLap',
    'rank','fastestLapTime', 'fastestLapSpeed', 'statusId'],inplace=True, axis=1)
    
    results_df = results_df[results_df['positionOrder'] == 1]
    merged_df: pd.DataFrame = results_df.merge(drivers_df, on='driverId', how='left')
    country_counts = merged_df['nationality'].value_counts()
    sorted_counts = country_counts.sort_values(ascending=False).head(10)
    print(sorted_counts)
    
    

if __name__=="__main__":
    main()
    


# In[ ]:





# In[ ]:




