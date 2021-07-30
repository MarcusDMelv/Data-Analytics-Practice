# SETUP: DO NOT CHANGE
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
plt.style.use('seaborn')

# TODO INTRODUCTION
"""
In this tutorial we will cover how to manipulate strings (`str`) inside of `Series` objects. The ability to do so opens 
up a significant number of data cleaning possibilities.
"""
# For this tutorial, I've create a 'messy' version
# of your college loan defaults data set.
# load csv
messy_college_loan_defaults = pd.read_csv(
    'college-loan-default-rates-messy.csv', encoding='latin-1')


"""At the very beginning of our course, we talked about how Python objects have attributes (pieces of information) 
and methods (things they can do). What we didn't talk about at the time is that an object's attributes are really 
objects themselves! Which means that they are capable of having methods of their own. The str attribute (not to be 
confused with the str data type) of Series and their index objects are two examples of such a case. On these objects, 
the str attribute (itself an object) provides an interface to a large number of methods. Here is a list of the 
available methods: 
"""
print('Here is a list of the available str attribute methods:\n\t:'
      '{0}'.format([method for method in dir(pd.Series.str) if not method.startswith('_')]))
# EXTRA HELP
# help(pd.Series.str.isupper)
# TODO ## Cleaning Up our DataFrame Column Headers
print('\nAll the column names in csv\n\t'
      '{0}'.format(messy_college_loan_defaults.columns))
print('\nWe could use the upper(), title(), or lower() methods to get consistent casing\n\t'
      '{0}\n{1}\n{2}'.format(messy_college_loan_defaults.columns.str.upper(),
                             messy_college_loan_defaults.columns.str.lower(),
                             messy_college_loan_defaults.columns.str.title()))
# The replace() method takes two arguments.
# What you want to search for, and what you want
# to replace it with.

# Let's get rid of the dashes and stick with
# underscores.
fixed_case_index = messy_college_loan_defaults.columns.str.upper()
fixed_index = fixed_case_index.str.replace('-', '_')
# You just assign your fixed index to the `columns`
# attribute of messy_college_loan_defaults!
# PYTHON IS AWESOME!
messy_college_loan_defaults.columns = fixed_index
print('\n\nFixed the column names and replaced it with my own customization\n\t'
      '{0}'.format(messy_college_loan_defaults.head()))

# TODO ## Cleaning Up Bad Data in a Series
"""Now let's try our hand at cleaning up bad data inside of a `Series` object. In this section, we are going to clean 
up a couple of columns with bad data. We will use a different approach for each column. """
# The first series we are going to look into
# is the STATE column. Notice how we now reference
# the series we wantby the corrected index name.
messy_states_series = messy_college_loan_defaults['STATE']
print('\nUpdating String Values in a Series{0}'.format(messy_states_series))
# The `str.startswith()` method can give us a mask
# to retrieve all the elements in our series that start with T
mask = messy_states_series.str.startswith('T')
print('\nStates start with a T \n\t{0}'.format(messy_states_series[mask][:10]))
# Just like before, this method will create a boolean series
# that we can use as a mask.
mask = messy_states_series.str.contains(pat='TEX')
print('\nReplacing Values\n\t{0}'.format(messy_states_series[mask]))
# TODO Replacing values
# You can use str.replace to exchange one
# string for anther in a DataFrame or Series
# Specify `inplace=True` to change the existing series
# rather than creating a new version with fixed data.
#TODO Replacing value
messy_states_series.replace('TEX', 'TX', inplace=True)
# And just to verify that everything worked as expected
# let's perform our search for 'TEX' again.
mask = messy_states_series.str.contains(pat='TEX')
# pat stands for pattern
#TODO ### Getting Rid of Bad String Data in a Series
"""
Now let's turn our attention to a slightly different use case - getting rid of bad string data. 

In this case we are going to look at the `YEAR_1_BORROWERS_IN_REPAY` series/column which should be a numeric column, but occasionally has the string `NAFD` which was someone's way of marking a null value.

In tutorial 6.2 we covered how you prevent these rows from getti### Getting Rid of Bad String Data in a Series
ng into your data set in the first place. In this section, we will cover how to get rid of them if they are already present.
"""
# Grab the Series
messy_series = messy_college_loan_defaults['YEAR_1_BORROWERS_IN_REPAY']
print('Start null value NAFD \n\t')
print(messy_series[:27])
"""
As we did previously, let's discover how many problem elements we have on our hands. 

While we could use the `str.startswith()` method, in this case we will use the `str.isalpha()` method which returns a boolean series indicating which elements of `messy_series` are comprised only of letters.

It is a quick and efficient way of separating numberic entries from letter-based entries.

We can then use this as a mask to pull out all the entries of `messy_series` that are not numeric.
"""
# TODO TESTING USING isalpha
# Create the boolean mask with `str.isalpha()`
# isalpha (if contains a alphabetic character = true )

mask = messy_series.str.isalpha()
print('\nUsing isalpha method: \n\t{0}'.format(messy_series[mask]))
"""
Another approach we could have taken with a similar result would have been to use the `str.contains()` method which we used previously. 

I didn't mention it before, but you can use regular expressions with this and a number of other `str` attribute methods (see page 181 of your textbook).

I'll use this approach now:
"""
regex_mask = messy_series.str.contains(r'^NAFD$')
print('\nUsing another method besides isalpha: \n\t{0}'.format(messy_series[regex_mask]))

# TODO REPLACE NAFD WITH FALSE
# We'll tell Pandas replace all NaN values encountered with `False`
fixed_regex_mask = messy_series.str.contains(r'^NAFD$', na=False)
# Check out index 26, NaN has been replaced with False
print('\nReplace NAFD with FALSE\n\t{0}'.format(fixed_regex_mask[20:27]))
# TODO USING TO_NUMERIC
"""What we have to do now is use the `pd.to_numeric()` function. This function will attempt to 'downcast' a `Series` 
with an 'object' datatype to a numeric type. It will fail (with the default parameters) if there is anything in the 
`Series` other than NaN and string representations of numbers. """

print('\nChange data type to actual floats:\n\t')
"""
Awesome. You can see that the `dtype` has change to a `float64` numeric type.

Unlike some of the other methods we've looked at in this tutorial, there is no `inplace` parameter that we can use 
here, so we have manually assign the result of `pd.to_numeric()` back to the `YEAR_1_BORROWERS_IN_REPAY` series of 
our original `dataframe` variable. This has the effect of replacing the existing series with the modified one. """

messy_college_loan_defaults['YEAR_1_BORROWERS_IN_REPAY'] = pd.to_numeric(messy_series)

print('Now check check the dtypes of `messy_college_loan_defaults` and you\'ll see that the '
      '\'YEAR_1_BORROWERS_IN_REPAY\' `series` has successfully been changed to a \'float64\' type.'
      '\n\t{0}'.format(messy_college_loan_defaults.dtypes))
#TODO And you can now perform calculations on it!
print(messy_college_loan_defaults['YEAR_1_BORROWERS_IN_REPAY'].describe())