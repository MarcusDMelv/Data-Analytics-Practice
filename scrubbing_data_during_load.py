# SETUP: DO NOT CHANGE
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
plt.style.use('seaborn')
# TODO INTRODUCTION
"""In this tutorial we will revisit the `read_csv()` function and take a closer look at how we can prevent at least 
some bad/missing data from getting into our *`DataFrames`* in the first place by using various parameters that we 
have not yet covered. """
# load dataframe
uncleaned_college_scorecard = pd.read_csv(
    'college-scorecard-data-scrubbed.csv',
    encoding='latin-1',
    index_col='OPEID6')
# TODO Choosing columns to load
"""Often times, you will start your work with a ginormous data set that will have **way** more columns that you are 
interested in. For instance, just look at all the columns in our `uncleaned_college_scorecard` *`DataFrame`*.

To avoid that problem, you can simply pass a `list` of the columns you do want to the **`usecols`** parameter.
"""
# Let's just load the basic geographical info on all colleges
college_geographies = pd.read_csv(
    'college-scorecard-data-scrubbed.csv',
    usecols=['OPEID6', 'institution_name', 'city', 'state'],
    encoding='latin-1',
    index_col='OPEID6')
print('Picked specfic columns from a large data set\n\t'
      '{0}'.format(college_geographies.head()))
# TODO Controlling what is Considered a Missing Value
"""One of the things that has bothered me the most about our college scorecard data set up until this point is how 
some of the columns which should be numeric were being upcast to 'object' types because of an occasional string being 
inserted. In particular, this happened with the following columns because of the existence of "PrivacySuppressed" 
strings: median_student_earnings, median_student_debt. Let's use the `na_values` parameter to specify that 
"PrivacySuppressed" should be considered a missing value. """
great_data_we_could_not_use_before = pd.read_csv(
    'college-scorecard-data-scrubbed.csv',
    # Specify the columns we want
    usecols=['OPEID6', 'median_student_earnings', 'median_student_debt'],
    # Tell pandas to treat "PrivacySuppressed" as a NaN value.
    na_values=['PrivacySuppressed'],
    encoding='latin-1',
    index_col='OPEID6')
print('\nAble to make specific values Nan\n\t'
      '{0}'.format(great_data_we_could_not_use_before.head()))
# TODO Controlling what Values are Converted to Boolean Objects
"""
In a similar fashion to specifing what values should be considered missing/NaN, we can also specify what values 
should be considered as `True` or `False`. 
"""
messy_weather_date = pd.read_csv('seattle_weather_2015_2016.csv')
print('\n\nData Before Boolean Scrub\n\t{0}'.format(messy_weather_date.head()))
cleaned_weather_data = pd.read_csv(
    'seattle_weather_2015_2016.csv',
    # We pass a list to both parameters
    # since there could be multiple values
    # we would want to convert to True/False
    true_values=['Yes'],
    false_values=['No'])
print('\n\nData After Boolean Scrub\n\t{0}'.format(cleaned_weather_data.head()))
