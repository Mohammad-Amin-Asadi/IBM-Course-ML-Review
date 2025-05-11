import pandas as pd
file_path = "./iris.csv"

#Import data (CSV = Comma Separated Values)
data =  pd.read_csv(file_path)
print(data.iloc[:5])