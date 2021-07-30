# SETUP: DO NOT CHANGE
import inline
import matplotlib
import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

## Introduction
'''
In this tutorial we are going to learn how to create simple line plots with Matplotlib.

Before we dive in, let's cover a few introductory matters.
'''

# TODO ### Importing Matplotlib Just as we use the ``np`` shorthand for NumPy, we will use some standard shorthands
#  for Matplotlib imports. Same disclaimer goes for these aliases as the others.

import matplotlib as mpl
import matplotlib.pyplot as plt

# TODO Setting Styles While we will get into adjusting individual pieces of our plots appearances, you can change
#  many of the properties at once by selecting a style. You can see the available styles like so See what they look
#  like here (warning, bad HTML design): https://matplotlib.org/examples/style_sheets/style_sheets_reference.html
#  ?highlight=style%20sheets%20reference
graph_style = plt.style.available

# Select a style, it will affect all subsequent plots.
plt.style.use('seaborn')

# How to Display Your Plots in Jupyter NotebooksYour textbook has information about how to display plots in a
# variety of environments, but we are only interested in how to display them in your Jupyter notebooks.
# Add this after your imports to configure Jupyter to ",
# display your plots",


#TODO import Data
football_roster = pd.read_csv('nd-football-2017-roster.csv',index_col= 'Number')
print('Football graph')
print(football_roster.head())
'''
### MATLAB-Style vs. Object Oriented Interface One of the reason that Matplotlib can be confusing to beginners (or 
anyone who isn't constantly using it) is that it presents to different interfaces. Your textbook opts for relying on 
the MATLAB style interface, but we will not do so. We will stick with the object-oriented approach, which is more 
consistent with the language as a whole and gives you more control over your plots. 

### The Anatomy of a Plot
Before we go any farther, let's define some terms Matplotlib terms:
* Every plot/chart is made of one **`figure`** object and 1 or more **`axes`** objects
* The **`figure`** object is more or less just a container
* Each **`axes`** object is a graphical representation of data that exists inside the figure.
* Most often, a *`figure`* will contain only one *`axes`* but that is not always the case as we will learn in later tutorials.


'''
print('\n plotting a graph')
# TODO In order to create a plot, we have to have the two essential components mentioned above - a **`figure`**
#  object and a **`axes`** object. You can get them like this
figure, axes = plt.subplots()
# Use the `plot()` method to "write" data on your axes.
# The first argument is used as the x-axis
# The second is used for the y-axis
# Get the objects
#figure, axes = plt.subplots()

# Use the `plot()` method to "write" data on your axes.
# The first argument is used as the x-axis
# The second is used for the y-axis
axes.plot(football_roster.index, football_roster['Height'])
plt.show()