import csv, pandas

data_files= ["data/daily_sales_data_0.csv", "data/daily_sales_data_1.csv", "data/daily_sales_data_2.csv"]
df = pandas.concat((pandas.read_csv(filename) for filename in data_files))

df = df[df["product"] == "pink morsel"]
df["price"] = df["price"].str.replace('$', '').astype(float)
df["sales"] = (df["price"] * df["quantity"]).astype(int)
df = df[["sales","date","region"]]

data = df.to_csv('data/daily_sales_data_pink.csv', index=False)