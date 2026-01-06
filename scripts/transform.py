import pandas as pd

def transform_data(product_df):
    product_df['currency'] = product_df['price'].str[:2]
    product_df['price'] = product_df['price'].str[3:].astype(int)
    return product_df