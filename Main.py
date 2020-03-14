import pandas as pd
from matplotlib import pyplot
path = "datasets\COVID19_line_list_data.csv"
data = pd.read_csv(path)
print("INFO DATASET CORONA")
print(data)
print(data.describe())
print(data.info())
print("RATA-RATA SEMUA KOLOM")
print(data.mean())
print("TAMPIL HISTOGRAM")
data.hist()
pyplot.show()