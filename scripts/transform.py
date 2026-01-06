import pandas as pd

def transform_data(product_df, transactions_df, users_df):
    product_df['currency'] = product_df['price'].str[:2]
    product_df['price'] = product_df['price'].str[3:].astype(int)
    
    transactions_df['transaction_date'] = pd.to_datetime(transactions_df['transaction_date'], format='%d/%m/%Y')
    
    users_df['email'] = users_df['email'].replace("", None)
    
    merged_df = transactions_df.merge(product_df, on='product_id', how='left') \
                                .merge(users_df, on='user_id', how='left')

    merged_df['total_transaction'] = merged_df['quantity'] * merged_df['price']
    return merged_df