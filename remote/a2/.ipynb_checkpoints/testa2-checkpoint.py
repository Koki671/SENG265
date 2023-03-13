{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "c8d1a9b9",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import yaml\n",
    "\n",
    "# Read in the YAML files\n",
    "\n",
    "def main():\n",
    "    with open('airlines.yaml', 'r') as f:\n",
    "        airlines = yaml.safe_load(f)\n",
    "    \n",
    "    with open('airports.yaml', 'r') as f:\n",
    "        airports = yaml.safe_load(f)\n",
    "    \n",
    "    with open('routes.yaml', 'r') as f:\n",
    "        routes = yaml.safe_load(f)\n",
    "\n",
    "# Convert the YAML data to pandas data frames\n",
    "    airlines_df = pd.DataFrame(airlines)\n",
    "    airports_df = pd.DataFrame(airports)\n",
    "    routes_df = pd.DataFrame(routes)\n",
    "\n",
    "# Merge the data frames\n",
    "    merged_df = pd.merge(routes_df, airports_df, left_on='route_from_aiport_id', right_on='airport_id', how='left')\n",
    "    merged_df = pd.merge(merged_df, airports_df, left_on='route_to_airport_id', right_on='airport_id', how='left', suffixes=('_from', '_to'))\n",
    "    merged_df = pd.merge(merged_df, airlines_df, left_on='route_airline_id', right_on='airline_id', how='left')\n",
    "\n",
    "    # Drop the unnecessary columns\n",
    "    merged_df = merged_df.drop(['airport_id_from', 'airport_id_to', 'airline_id'], axis=1)\n",
    "\n",
    "    # Print the final data frame\n",
    "    print(merged_df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "42546f4b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ba097bf1",
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
