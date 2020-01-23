#
# Process and combine raw data files for Resting heartrate and xnx into a single
# datafile which will be the input for subsequent work.
#
# inputs: raw data for heartrate and xnx consumption
#
# output: transformed dataset of date, hr, and xnx stored as json file
#


import pandas as pd

# load multiple xnx files, transform values into mg values, then summarize to the day

# read the files and transform boolean values to tablet counts
x05 = pd.read_json('data/raw/xnx05.json')
x05['tablets'] = x05['value'] * 0.5

x1 = pd.read_json('data/raw/xnx1.json')
x1['tablets'] = x1['value']

x2 = pd.read_json('data/raw/xnx2.json')
x2['tablets'] = x2['value'] * 2

x3 = pd.read_json('data/raw/xnx3.json')
x3['tablets'] = x3['value'] * 3

x4 = pd.read_json('data/raw/xnx4.json')
x4['tablets'] = x4['value'] * 4

combinedX = pd.concat([x05, x1, x2, x3, x4])
totalX = combinedX.groupby('date').sum()

# transform number of tablets to mg
totalX['mg'] = totalX['tablets'] * 0.5

# cleanup the dataframe by dropping unneeded columns
totalX.drop(columns=['value', 'tablets'], inplace = True)


# read heartrate data
heartrate = pd.read_json('data/raw/heartrate_resting.json')
heartrate.set_index('date', inplace = True)
heartrate.rename(columns = {'value': 'heartrate'}, inplace = True)

# combine HR and xnx
hrXnx = pd.merge(heartrate, totalX, how='outer', on='date')

hrXnx.to_json('data/hrXnx.json', orient = 'index')