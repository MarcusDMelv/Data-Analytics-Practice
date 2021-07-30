# SETUP: DO NOT CHANGE
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
plt.style.use('seaborn')
# Load our college scorecard data set
# Which has a number of missing data elements
college_scorecard = pd.read_csv(
    'college-scorecard-data-scrubbed.csv',
    encoding='latin-1',
    index_col='OPEID6')
print('Showing data that is not available: \n\t {0}'.format(college_scorecard['sat_average'][:10]))

# TODO Working with  isnull()
"""
The is null method returns a boolean array indicating which elements of a *`Series`* object are `np.nan` or `None`.
"""
# Pull the 'degree_seeking_undergrads` series from
# our `college_scorecard` dataframe.
degree_seeking_undergrads = college_scorecard['degree_seeking_undergrads']
print('\nisnull() shows a boolean value. If value is null True\n\t{0}'.format(degree_seeking_undergrads))
# TODO Find the nulls
# Use this is as a mask to retrieve which colleges
# are missing data on the number of degree seeking undergrads
mask = degree_seeking_undergrads.isnull()
print('\nSeek where the Nan/null/None values are:'
      '\n\t{0}'.format(degree_seeking_undergrads[mask]))
#TODO Using  notnull()
"""
### notnull()
This method is the logical inverse of `isnull()`. Use it to return a boolean mask indicating which elements are not null.
The results of this method can be used to pull back all non-null elements of a Series (or DataFrame).
"""
mask = degree_seeking_undergrads.notnull()
print('\nUsing notnull() Get rid of the values that are Nan/null/None \n\t'
      '{0}'.format(degree_seeking_undergrads[mask]))
#TODO Using dropna()
"""
### dropna()
What we just did in the previous example is so common that the *`pandas`* developers created the convenience method 
*`dropna()`* to eliminate the need to create a mask with `notnull()` and then apply it to our object to get 
back all the non-null elements.
"""
# TODO Using how = all
"""
# Specify 'all' as the value of `how`
# To return all rows with at least one
# non-null value.
subset_scorecard.dropna(how='all')[:10]
"""
# TODO Using axis = 'columns'
"""
# Note that this will actually drop all
# of our columns, since they both have
# null values in them.
subset_scorecard.dropna(axis='columns')[:10]
"""
print('Using dropna() Just like notnull() but without creating a mask\n\t'
      '{0}'.format(degree_seeking_undergrads.dropna()))
#TODO Using fillna()
"""
### fillna()
The *`fillna()`* method is used to insert (or fill in) missing data will a value of your choosing. 
It has a few available parameters.
You can also specify a value for each column if you want. In our next example, I'll specify a different value for each 
of our columns with a dictionary. Pretty cool!
"""
#TODO specify a different value for each of our columns with a dictionary.
"""
subset_scorecard.fillna(
    {'sat_writing_midpoint': 100, 'median_student_earnings': 20000})[:10]
"""
# First let's grab the SAT Writing Midpoint series
sat_writing_midpoint = college_scorecard['sat_writing_midpoint']
print('How to Replace missing values:\n\t'
      '{0}'.format(sat_writing_midpoint[:15:2]))
# "Fill" all NaN elements as 0
print('Fill in missing values with a value (replacing NaN with 0)\n\t'
      '{0}'.format(sat_writing_midpoint.fillna(0)[:15:2]))
# TODO Replace values with the "mean" of the data
"""
# A handy trick that you might want to 
# employ fairly often is to fill in NaN values
# with the average of the series so as not 
# to throw off aggregate calculations.
"""
print('Showing the mean to use to replace NaN:\n\t'
      '{0}'.format(sat_writing_midpoint.fillna(sat_writing_midpoint.mean())[:15]))
#TODO bfill/ffill
"""
# Specifying a value of 'bfill'
# will take non-null values and then fill in
# those values going backwards.
sat_writing_midpoint.fillna(method='bfill')[:11]

"""
# TODO bfill/ffill continue
"""
# Specifying a value of 'ffill'
# will take non-null values and then fill in
# those values going forwards.
sat_writing_midpoint.fillna(method='ffill')[:11]
"""