# SETUP: DO NOT CHANGE
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
plt.style.use('seaborn')

# loading data
"""
Age
Gender
state
---------
self_employed: Are you self-employed?
remote_work
work_interfere
no_employees
treatment
"""
# Scub data
survey_cleaned = pd.read_csv('survey.csv',
            # use columns
            usecols=['Age','Gender','state','self_employed','remote_work','work_interfere','no_employees','treatment'],
            # indexed column
            index_col='Age',
            # create booleans
            true_values=['Yes'],
            false_values=['No']
            )
print(survey_cleaned)
# Edit Column Headers
#fix text
fixed_columns = survey_cleaned.columns.str.title()
# add underscores
fixed_columns = fixed_columns.str.replace(' ','_')
survey_cleaned.columns = fixed_columns
print(survey_cleaned)


# handling nulls
"""
Gender - drop
State - drop
Self_Employed - False
Work_Interfere - drop
No_Employees - drop
Remote - drop
"""

#Gender
gender = survey_cleaned['Gender']
gender = gender.dropna()
#State
state = survey_cleaned['State']
state = state.dropna()
#Self_Employed
self_employed = survey_cleaned['Self_Employed']
self_employed = self_employed.dropna()
#Work_Interfere
work_interfere = survey_cleaned['Work_Interfere']
work_interfere = work_interfere.dropna()
#No_Employees
number_employees = survey_cleaned['No_Employees']
number_employees = number_employees.dropna()
#Remote
remote = survey_cleaned['Remote_Work']
remote = remote.dropna()
# Handle misspellings
# Gender-Correct spelling Male / Female
gender.replace('M','Male', inplace=True)
gender.replace('male','Male', inplace=True)
gender.replace('m','Male', inplace=True)
gender.replace('F','Female', inplace=True)
gender.replace('female','Male', inplace=True)
gender.replace('f','Female', inplace=True)
# State-ALL Caps
state.str.upper()
# Work_Interfere - Rarely/Often/Sometimes/Never
# No_Employees - One number
number_employees.replace('6-25', '25', inplace=True)
number_employees.replace('26-100', '100', inplace=True)
number_employees.replace('100-500', '500', inplace=True)
number_employees.replace('More than 1000', '1000', inplace=True)
# Remote_Work - Boolean
print('{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n'.format(gender, state, self_employed, work_interfere, number_employees, remote))

# checking if any if any letters in numeric values
mask = number_employees.str.isalpha()
print('Number of letters found:')
print(len(number_employees[mask]))

# check data types
survey_cleaned['No_Employees'] = pd.to_numeric(number_employees)
print(number_employees.dtype)