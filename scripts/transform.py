import pandas as pd

def transform_data(product_df, transactions_df):
    product_df['currency'] = product_df['price'].str[:2]
    product_df['price'] = product_df['price'].str[3:].astype(int)
    
    transactions_df['transaction_date'] = pd.to_datetime(transactions_df['transaction_date'], format='%d/%m/%Y')
    
    return transactions_df