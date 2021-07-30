import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

# TODO UPLOAD SPECIFIC COLUMN FROM CSV
# upload column from data set
player_heights = np.array(pd.read_csv
                            ('nd-football-2017-roster.csv')['Height'])
print('Players height: {0} '.format(player_heights))
# TODO SORT THE DATA
sort_data = np.sort(player_heights)
print('Players height is now sorted: {0}'.format(player_heights))
