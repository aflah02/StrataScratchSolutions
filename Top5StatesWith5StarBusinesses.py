# Import your libraries
import pandas as pd

# Get All 5 Star Hotels
yelp_business = yelp_business[yelp_business['stars'] == 5]

# Groupby the State and Get the Counts
yelp_business = yelp_business.groupby('state').size().reset_index(name='n_businesses')

# Sort yelp_business
yelp_business = yelp_business.sort_values(by = ['n_businesses', 'state'], ascending = [False, True])

# Pick The Top 5
yelp_business.nlargest(5, ['n_businesses'], keep = 'all')

