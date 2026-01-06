import pandas as pd

def transform_data(product_df, transactions_df, users_df):
    product_df['currency'] = product_df['price'].str[:2]
    product_df['price'] = product_df['price'].str[3:].astype(int)
    
    transactions_df['transaction_date'] = pd.to_datetime(transactions_df['transaction_date'], format='%d/%m/%Y')
    
    users_df['email'] = users_df['email'].replace("", None)
    return users_df