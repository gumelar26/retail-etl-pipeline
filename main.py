from config.setting import PRODUCTS_PATH, TRANSACTIONS_PATH, USERS_PATH
from scripts.extract import extract_csv, extract_json
from scripts.transform import transform_data

# Extract
product_df = extract_csv(PRODUCTS_PATH)
transactions_df = extract_csv(TRANSACTIONS_PATH)
users_df = extract_json(USERS_PATH)

# Transfrom
df = transform_data(product_df, transactions_df, users_df)
print(df)