import pandas as pd

DATASET_PATH = "../../data/customers.csv"

def get_data():
    df = pd.read_csv(DATASET_PATH)

    df = df.rename(columns={'Gender': 'gender', 'Age': 'age', 'Annual Income (k$)': 'annual_income', 'Spending Score (1-100)': 'spending_score'})
    df.loc[df.gender == 'Female', 'gender'] = 0
    df.loc[df.gender == 'Male', 'gender'] = 1

    return df
