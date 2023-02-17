#!/usr/bin/env python
import pandas as pd
def main():
    drivers_df: pd.DataFrame = pd.read_csv('drivers.csv')
    results_df: pd.DataFrame = pd.read_csv('results.csv')


if __name__=="__main__":
    main()