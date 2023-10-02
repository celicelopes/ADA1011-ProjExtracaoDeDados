import pandas as pd

def saveData(data):
    df = pd.DataFrame(data)
    df.to_parquet("./data/data.parquet", index=False)

def printData():
    parquet_df = pd.read_parquet("./data/data.parquet")
    print(parquet_df)