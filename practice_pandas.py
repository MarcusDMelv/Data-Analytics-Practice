# TODO Load libs
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

class RunPandas:
    # TODO Using 'encoding =' and type method
    df_shoes = pd.read_csv('shoe_price_ranking_dataset.csv',
                           encoding='latin-1')
    '''
    Default is utf-8
    If you don't specify no error
    latin-1 can be used to decode a csv if not in plain text
    ** When loading data set try to find the metadata type and use the encoding or else trial and error
    '''
    # TODO Load CSV
    # read csv, specific index
    df_football = pd.read_csv('nd-football-2017-roster.csv',
                              index_col='Height')
    # load specific DataSeries
    df_football_height = pd.read_csv('nd-football-2017-roster.csv',
                                     index_col='Name',
                                     usecols=['Number', 'Name', 'Height'])
    print(df_football_height.head())
    # load dates, this labels the object type as a date
    df_weather = pd.read_csv('seattle_weather_2015_2016.csv',
                             parse_dates=['date'])
    # TODO What is a DataFrame
    # made up of indexes and one or more DataSeries objecs
    # load top 5 using head function
    top5 = df_football.head()
    # TODO USING SPECIFIC DataSeries
    # able to locate a specific DataSeries
    players_name = df_football['Name']
    players_number = df_football['Number']
    # use the type method to display object type
    series_type = type(players_name)
    print('Showing object type {0}'.format(players_name[0:]))
    print('Showing a dataframe: \n\t Index are the numbers labeling the DataSeries ( each column)\n{0}'.format(top5))
    # TODO display each DataSeries value with no order (rows)
    # grab data series  ' Names '
    display_players_names = players_name[:5].values
    print('Shows DataSeries values with no order:\n\t{0}'.format(display_players_names))
    # TODO run loop through specific DataSeries
    players_name = players_name[0:]
    players_number = players_number[0:]
    print('Run through a DataFrame picking out specific DataSeries:')
    loop_counter = 1
    for players in df_football[:2].values:
        players_name = players[1:2]
        players_number = players[:1]
        print('{2} Players Number and Name:{0}{1}'.format(players_number, players_name, loop_counter))
        loop_counter += 1
        time.sleep(2)
    # TODO Going deeper with DataSeries
    # use a dictionary
    # languages are indexes : string is the DataSeries
    create_series = pd.Series({
        'R': 'Not as cool',
        'Python': 'This is all me'
    })
    custom_df = pd.DataFrame(data=create_series,index=['R','Python'])
    print(custom_df)
    print('This is a custom series\n\t{0}'.format(create_series))
    print('From a custom series showing index: \n\t{0}'.format(create_series.index))
    # TODO USING INDEX******************
    # TODO sizing a DataSeries ( look at: index_label,size,type )
    series_index = df_football['Name']
    print('Looking at a DataSeries size\n\t{0}'.format(series_index.index))
    # **************************************************************
    # TODO CHANGING INDEX VALUE
    df_football.index = df_football['Number']
    print('The Data Frames index has changed to the players numbers:\n\t{0}'.format(df_football.index))
    # TODO Data Selection**************************************************************************************************
    print('Starting Data Selection customized index to say school name\n\n')
    df_coll_scoreboard = pd.read_csv('college-scorecard-data-scrubbed.csv',
                                     encoding='latin-1',
                                     index_col='institution_name')
    print(df_coll_scoreboard.head())
    # TODO picking specific DataSeries
    # locate URL DataSeries
    url_series = df_coll_scoreboard['url']
    print('Using institution name as the index. I want to see URLs:\n\t{0}'.format(url_series[:3]))
    # TODO DOES a value exist?
    # use the 'in' keyword to look for a specific value in the series
    school_exist = 'University of Notre Dame' in url_series
    print('Does a value exist in the DataSeries?:\n\t{0}'.format(school_exist))
    # TODO Value Retrieval using index
    school_url = url_series['University of Notre Dame']
    print('Since index is school name we are able to find values using school name.'
          '\n\t{0}'.format(school_url))
    # TODO view all index in a DataSeries
    print('View all index in a DataSeries:\n\t{0}'.format(url_series.keys()[:3]))
    # TODO ITERATOR ( LIST OF TUPLES) -> security
    tuple_list = list(url_series.items())[:10]
    print('Using tuples and iterates as a list:\n\t{0}'.format(
        tuple_list[::2]
    ))
    # TODO Slice using the index
    schools_between = url_series['Stanford University': 'University of Notre Dame']
    print('Able slice using index labels\n\t{0}'.format(schools_between[:5]))
    # TODO USING COMPARISON OPERATORS
    # create  series object
    sat_average_series = df_coll_scoreboard['sat_average']
    # now use comparison operator to locate specific data sets
    sat_1200_plus = sat_average_series[sat_average_series > 1200]
    my_school = 'University of Advance Technology' in sat_1200_plus
    print(
        'Using comparison operators find specific data sets: EXAMPLE\n My schools SAT score average is higher then 1200'
        '\n Data says:{1}\n\t{0}'.format(sat_1200_plus[:4], my_school))
    # TODO Using Double Comparison Operators TO FIND A RANGE
    # uses () when using a double operator!!
    sat_1400_plus = sat_average_series[(sat_average_series >= 1400) & (sat_average_series <= 1500)]
    my_school = 'Stanford University' in sat_1400_plus
    print(
        'This uses DOUBLE operators to find a specific value in a DataSeries\n is Stanford in this 1400+ SAT score list'
        '{0}\n'.format(my_school))
    time.sleep(2)
    for school in sat_1400_plus.keys()[:4]:
        print(school)
        time.sleep(2)
    # TODO RETRIEVE MULTIPLE COLUMNS AT ONCE
    # use double square brackets
    df_small_scoreboard = df_coll_scoreboard[['act_english_25', 'act_english_75']][:4]
    print('\nJust pulled specific DataSeries from the Data Frame MORE THEN ONE!\n\t{0}'.format(df_small_scoreboard))
    # TODO RETURN ROWS FROM A DATA FRAME USING CRITERIA
    # return data series with specific values in a column
    # call for df with condition inside
    idaho_schools = df_coll_scoreboard[df_coll_scoreboard['state'] == 'ID']
    print('\nAble to call specific values in a DataSeries\n\t{0}'.format(idaho_schools))
    # TODO DOUBLE CRITERIA
    # DONT FORGET THE ()
    new_york_schools = df_coll_scoreboard[
        (df_coll_scoreboard['state'] == 'NY') & (df_coll_scoreboard['predominant_degree_desc'] == 'Bachelors')]
    print('These schools must be in NY and must off Bachelors Degree\n{0}'.format(new_york_schools))
    # TODO MAKE COLUMNS ROWS AND ROWS THE COLUMNS!!
    df_flip = df_coll_scoreboard.transpose
    print('Now the columns are rows and the rows are columns: {0}'.format(df_flip))
    # TODO Data Operations
    # using numpy functions
    # load two different DataFrames
    df_coll_scoreboard = pd.read_csv('college-scorecard-data-scrubbed.csv',
                                     encoding='latin-1',
                                     index_col='OPEID6')
    df_coll_loan = pd.read_csv('college-loan-default-rates.csv',
                               index_col='opeid')
    sat_avg = df_coll_scoreboard['sat_average']
    # *******TODO handling NaN (null)******
    print('How to handle the NaN values'.format(sat_avg))
    # use a mask to get rid of nulls
    filter_avg_score = sat_avg[sat_avg > 0]
    print('I just got rid of the nulls\n\t{0}'.format(filter_avg_score))
    # TODO fill a null in pandas
    print('\nWait we can fill the nulls with a value')
    print(sat_avg.divide(10, fill_value=0)[:5])
    # TODO using numpy functions
    print('\nUsing numpy functions')
    print(np.negative(filter_avg_score))
    print(np.log2(filter_avg_score))
    print('Using Math functions TOO')
    print(filter_avg_score.divide(10)[:5])
    # TODO Grab columns between specific columns using : (between)
    # columns grab all columns between year_1 and year_1_default_rate
    year_1_data = df_coll_loan.loc[:, 'year_1':'year_1_default_rate']
    year_2_data = df_coll_loan.loc[:, 'year_2':'year_2_default_rate']
    print('Grab columns using loc:\n\t{0}\n\t{1}'.format(year_1_data.head(), year_2_data.head()))


#TODO CUSTOM DATA FRAMES
# created a custom dataframe with index
sales_2015 = pd.DataFrame([
    {'One Burger': 2.99, 'Fries': 1.99},
    {'Two Burgers': 3.75, 'Fries': 1.99}],
    # index for the Data series
    index=['Number 1', 'Number 2']
)
print('This is a custom dataframe!: \n\t{0}'.format(sales_2015))
print('')

