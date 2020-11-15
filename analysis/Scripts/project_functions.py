import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Method Chaining
def load_and_process(path):
    # Chain 1: Data loaded and missing data removed
    df1 = (
        pd.read_csv(r"..\..\data\raw\database.csv")
            .dropna()
            .loc[lambda x: x['Victim Sex'] != 'Unknown']
            # Not removing victim age at 0 because i realized that could be a baby oops
            .loc[lambda x: x['Victim Race'] != 'Unknown']
            .loc[lambda x: x['Perpetrator Sex'] != 'Unknown']
            .loc[lambda x: x['Perpetrator Age'] != 0]
            .loc[lambda x: x['Perpetrator Race'] != 'Unknown']
            .loc[lambda x: x['Relationship'] != 'Unknown']
            .loc[lambda x: x['Weapon'] != 'Unknown']
            .reset_index(drop=True)
    )
    # Chain 2: Drop irrelevant columns, not sure if we want to add new ones?
    df2 = (
        # Currently just dropping the following:
        # Agency name, Agency Type, Victim & Perp Ethnicity (these columns are somehow different from race - but not.)
        # Dropping crime type as all these crimes are murder / manslaughter
        df1.drop(['Record ID','Agency Code', 'Agency Name', 'Agency Type', 'Crime Type', 'Victim Ethnicity', 'Perpetrator Ethnicity'], axis=1)
            .reset_index(drop=True)
    )
    return df2
