import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Method Chaining
def load_and_process(path):
    # Chain 1: Data loaded and missing data removed
    df1 = (
        pd.read_csv(os.path.join('..','..','data','raw','database.csv'))
            .dropna()
            .loc[lambda x: x['Victim Sex'] != 'Unknown']
            # Not removing victim age at 0 because i realized that could be a baby oops
            .loc[lambda x: x['Victim Race'] != 'Unknown']
            .reset_index(drop=True)
    )
    # Chain 2: Drop irrelevant columns, not sure if we want to add new ones?
    df2 = (
        # Currently just dropping the following:
        # Agency name, Agency Type, Victim & Perp Ethnicity (these columns are somehow different from race - but not.)
        # Dropping crime type as all these crimes are murder / manslaughter
        df1.drop(['Record ID','Agency Code', 'Agency Name', 'Crime Type', 'Victim Ethnicity', 'Perpetrator Ethnicity','Record Source'], axis=1)
            .reset_index(drop=True)
            .replace({'Month': {'January':1,'Feburary':2,'March':3,'April':4,'May':5,'June':6,
                                'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}})
    )
    return df2

def weapon_df(path):
    df = load_and_process(path)

    

