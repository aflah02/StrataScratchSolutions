import pandas as pd

dc_bikeshare_q1_2012 = dc_bikeshare_q1_2012.sort_values(by='end_time', ascending = False)

dc_bikeshare_q1_2012 = dc_bikeshare_q1_2012.drop_duplicates(subset = ['bike_number'])

dc_bikeshare_q1_2012 = dc_bikeshare_q1_2012[['bike_number', 'end_time']]

dc_bikeshare_q1_2012.rename(columns = {'end_time': 'last_used'}, inplace = True)

dc_bikeshare_q1_2012
