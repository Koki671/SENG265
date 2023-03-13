{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "851b6da2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "23\n",
      "British       308\n",
      "German        179\n",
      "Brazilian     101\n",
      "French         81\n",
      "Finnish        57\n",
      "Italian        43\n",
      "Australian     43\n",
      "Austrian       41\n",
      "Argentine      38\n",
      "American       33\n",
      "Name: nationality, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "#!/usr/bin/env python\n",
    "import pandas as pd\n",
    "def main():\n",
    "    drivers_df: pd.DataFrame = pd.read_csv('drivers.csv')\n",
    "    results_df: pd.DataFrame = pd.read_csv('results.csv')\n",
    "    drivers_df.drop(['driverRef', 'number', 'code', 'dob','url','forename','surname'], inplace=True, axis=1)\n",
    "    results_df.drop(['raceId', 'constructorId', 'number', 'grid', 'position', 'positionText', 'points','laps','time',\n",
    "                     'milliseconds', 'fastestLap', 'rank','fastestLapTime', 'fastestLapSpeed', 'statusId'],inplace=True, axis=1)\n",
    "    results_df = results_df[results_df['positionOrder'] == 1]\n",
    "    merged_df: pd.DataFrame = results_df.merge(drivers_df, on='driverId', how='left')\n",
    "        #To see the number of countries I need to sort\n",
    "    print(merged_df['nationality'].nunique())\n",
    "    country_counts = merged_df['nationality'].value_counts()\n",
    "    sorted_counts = country_counts.sort_values(ascending=False).head(10)\n",
    "    print(sorted_counts)\n",
    "    sorted_df =  merged_df.sort_values(by='nationality', key=lambda x: x.map(country_counts))\n",
    "    #print(sorted_df)\n",
    "  \n",
    "   \n",
    "\n",
    "    \n",
    "    \n",
    "    \n",
    "\n",
    "if __name__==\"__main__\":\n",
    "    main()\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "abe0aeaa",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
