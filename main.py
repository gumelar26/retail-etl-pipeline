from config.setting import PRODUCTS_PATH, TRANSACTIONS_PATH
from scripts.extract import extract_csv
from scripts.transform import transform_data

# Extract
product_df = extract_csv(PRODUCTS_PATH)
transactions_df = extract_csv(TRANSACTIONS_PATH)

# Transfrom
df = transform_data(product_df, transactions_df)
print(df)