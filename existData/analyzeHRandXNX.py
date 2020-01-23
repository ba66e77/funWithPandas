import pandas as pd
from scipy import stats
from matplotlib import pyplot

data = pd.read_json('data/hrXnx.json', orient = 'index')

data['mg-zscore'] = stats.zscore(data.mg)
data['hr-zscore'] = stats.zscore(data.heartrate, nan_policy='omit')

reduced = data.dropna()

# Pearson
corr = reduced.corr()
corr.drop(index = ['heartrate', 'mg'], columns = ['heartrate', 'mg'], inplace=True)
print('Pearson')
print(corr)

# Spearman
corr = reduced.corr(method = 'spearman')
corr.drop(index = ['heartrate', 'mg'], columns = ['heartrate', 'mg'], inplace=True)
print("Spearman")
print(corr)

# Without this, pyplot displays warning when using data as x-axis label
# FutureWarning: Using an implicitly registered datetime converter for a matplotlib plotting method. The converter was registered by pandas on import. Future versions of pandas will require you to explicitly register matplotlib converters.
pd.plotting.register_matplotlib_converters()

pyplot.plot(reduced['mg-zscore'], label = 'mg of Xanax', color='r')
pyplot.plot(reduced['hr-zscore'], label = 'Resting heart rate', color='b')
pyplot.xlabel('Date')
pyplot.ylabel('Z-Score')
pyplot.title('Correlation of Xanax to Resting Heart Rate')
pyplot.legend()

pyplot.savefig('xnx_hr.png')
pyplot.show()