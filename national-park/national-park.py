# analyzing national park visitor data from 2016

import numpy as np
import pandas as pd

# read in data using pandas
parks = pd.read_table('csv/parks.txt')

# filter for single column from pandas data frame
parks_visits = parks.filter(['Value'])
print(parks_visits)

# store the visits column as a numpy array so we can use numpy functions
parks_visits_array = parks_visits.values
print(parks_visits_array)

# find mean of visits using numpy
parks_visits_mean = np.mean(parks_visits_array)
print(parks_visits_mean)

# find mean of parks with more than 5 million visits
parks_top = parks_visits_array[parks_visits_array > 5000000]
parks_top_mean = np.mean(parks_top)
print(parks_top_mean)




#---this works, but load whole array into numpy
# nps_vals = nps.values
# print(nps_vals)

# nps_mean = np.mean(nps_vals[:,2])
#----




#---
# npsmean = nps["Value"].mean()

# nps = np.loadtxt('csv/parks.txt', dtype={"ParkName":str,"Rank":int,"Value":int,"PercentOfTotal":float})
# nps = np.loadtxt('csv/parks1.txt', dtype={'names': ('ParkName', 'Rank', 'Value', 'PercentOfTotal'), 'formats': ('S1', 'i4', 'i4', 'f4')})

