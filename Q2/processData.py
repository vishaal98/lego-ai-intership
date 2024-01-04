import pandas as pd

# Reading input CSV file
input_data = pd.read_csv('input.csv')

# Grouping data by 'sno' and 'product_code' and aggregating values
output_data = input_data.groupby(['sno', 'product_code']).agg({
    'size': lambda size: '|'.join(sorted(size.unique())),
    'color': lambda color: '|'.join(color.unique()),
    'price': lambda price: '|'.join(map(str, sorted(price.unique())))
}).reset_index()

# Renaming columns
output_data.columns = ['sno', 'product_code', 'sizes', 'colors', 'prices']

print(output_data)
# Writing processed data to output CSV file
output_data.to_csv('output.csv', index=False)
