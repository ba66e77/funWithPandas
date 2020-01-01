import pandas as pd

data = pd.io.stata.read_stata('data/shor+mccarty+1993-2016+individual+legislator+data+May+2018+release+(Updated+July+2018).dta')

print(data.columns)
print(data.head())