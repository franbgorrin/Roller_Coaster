#!/usr/bin/env python
# coding: utf-8

# # Roller Coaster

# #### Overview

# This project is slightly different than others you have encountered thus far. Instead of a step-by-step tutorial, this project contains a series of open-ended requirements which describe the project you'll be building. There are many possible ways to correctly fulfill these requirements, and you should expect to use the internet, Codecademy, and other resources when you encounter a problem that you cannot easily solve.

# #### Project Goals

# You will work to create several data visualizations that will give you insight into the world of roller coasters.

# ## Prerequisites

# In order to complete this project, you should have completed the first two lessons in the [Data Analysis with Pandas Course](https://www.codecademy.com/learn/data-processing-pandas) and the first two lessons in the [Data Visualization in Python course](https://www.codecademy.com/learn/data-visualization-python). This content is also covered in the [Data Scientist Career Path](https://www.codecademy.com/learn/paths/data-science/).

# ## Project Requirements

# 1. Roller coasters are thrilling amusement park rides designed to make you squeal and scream! They take you up high, drop you to the ground quickly, and sometimes even spin you upside down before returning to a stop. Today you will be taking control back from the roller coasters and visualizing data covering international roller coaster rankings and roller coaster statistics.
#
#    Roller coasters are often split into two main categories based on their construction material: **wood** or **steel**. Rankings for the best wood and steel roller coasters from the 2013 to 2018 [Golden Ticket Awards](http://goldenticketawards.com) are provded in `'Golden_Ticket_Award_Winners_Wood.csv'` and `'Golden_Ticket_Award_Winners_Steel.csv'`, respectively. Load each csv into a DataFrame and inspect it to gain familiarity with the data.


# 1
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# load rankings data
wood = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
steel = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')

# load rankings data
print(wood.head())
print(steel.head())
print(len(wood.index))


# 2. Write a function that will plot the ranking of a given roller coaster over time as a line. Your function should take a roller coaster's name and a ranking DataFrame as arguments. Make sure to include informative labels that describe your visualization.
#
#    Call your function with `"El Toro"` as the roller coaster name and the wood ranking DataFrame. What issue do you notice? Update your function with an additional argument to alleviate the problem, and retest your function.

# In[2]:


# 2
# Create a function to plot rankings over time for 1 roller coaster
def ranking(roller_name, roller_park, ranking_df):
    roller_ranking = ranking_df[(ranking_df['Name'] == roller_name) & (ranking_df['Park'] == roller_park)]
    fig, ax = plt.subplots()
    ax.plot(roller_ranking['Year of Rank'], roller_ranking['Rank'])
    ax.set_yticks(roller_ranking['Rank'].values)
    ax.set_xticks(roller_ranking['Year of Rank'].values)
    ax.invert_yaxis()
    plt.title("{} Rankings".format(roller_name))
    plt.xlabel('Year')
    plt.ylabel('Ranking')
    plt.show()
    plt.close()


# Create a plot of El Toro ranking over time
ranking('El Toro', 'Six Flags Great Adventure', wood)


# 3. Write a function that will plot the ranking of two given roller coasters over time as lines. Your function should take both roller coasters' names and a ranking DataFrame as arguments. Make sure to include informative labels that describe your visualization.
#
#    Call your function with `"El Toro"` as one roller coaster name, `"Boulder Dash"` as the other roller coaster name, and the wood ranking DataFrame. What issue do you notice? Update your function with two additional arguments to alleviate the problem, and retest your function.

# In[13]:


# 3
# Create a function to plot rankings over time for 2 roller coasters
def ranking_2(roller_name_1, roller_park_1, roller_name_2, roller_park_2, ranking_df):
    roller_ranking_1 = ranking_df[(ranking_df['Name'] == roller_name_1) & (ranking_df['Park'] == roller_park_1)]
    roller_ranking_2 = ranking_df[(ranking_df['Name'] == roller_name_2) & (ranking_df['Park'] == roller_park_2)]
    fig, ax = plt.subplots()
    ax.plot(roller_ranking_1['Year of Rank'], roller_ranking_1['Rank'], color='yellow', label=roller_name_1)
    ax.plot(roller_ranking_2['Year of Rank'], roller_ranking_2['Rank'], color='brown', label=roller_name_2)
    ax.set_yticks(roller_ranking_1['Rank'].values)
    ax.set_xticks(roller_ranking_2['Year of Rank'].values)
    ax.set_yticks(roller_ranking_1['Rank'].values)
    ax.set_xticks(roller_ranking_2['Year of Rank'].values)
    ax.invert_yaxis()
    plt.title("{} & {} Rankings".format(roller_name_1, roller_name_2))
    plt.xlabel('Year')
    plt.ylabel('Ranking')
    plt.legend()
    plt.show()
    plt.close()


# Create a plot of El Toro and Boulder Dash roller coasters
ranking_2('El Toro', 'Six Flags Great Adventure', "Boulder Dash", 'Lake Compounce', wood)
plt.clf()


# 4. Write a function that will plot the ranking of the top `n` ranked roller coasters over time as lines. Your function should take a number `n` and a ranking DataFrame as arguments. Make sure to include informative labels that describe your visualization.
#
#    For example, if `n == 5`, your function should plot a line for each roller coaster that has a rank of `5` or lower.
#
#    Call your function with a value of `n` and either the wood ranking or steel ranking DataFrame.

# In[11]:


# 4
# Create a function to plot top n rankings over time
def plot_n(rankings_df, n):
    top_n_rankings = rankings_df[rankings_df['Rank'] <= n]
    fig, ax = plt.subplots(figsize=(10, 10))
    for coaster in set(top_n_rankings['Name']):
        coaster_rankings = top_n_rankings[top_n_rankings['Name'] == coaster]
        ax.plot(coaster_rankings['Year of Rank'], coaster_rankings['Rank'], label=coaster)
    ax.set_yticks([i for i in range(1, 6)])
    ax.invert_yaxis()
    plt.title("Top 10 Rankings")
    plt.xlabel('Year')
    plt.ylabel('Ranking')
    plt.legend(loc=4)
    plt.show()
    plt.close()


# Create a plot of top n rankings over time
plot_n(wood, 5)
plt.clf()

# 5. Now that you've visualized rankings over time, let's dive into the actual statistics of roller coasters themselves. [Captain Coaster](https://captaincoaster.com/en/) is a popular site for recording roller coaster information. Data on all roller coasters documented on Captain Coaster has been accessed through its API and stored in `roller_coasters.csv`. Load the data from the csv into a DataFrame and inspect it to gain familiarity with the data.

# In[5]:


# 5
# load roller coaster data
data_coaster = pd.read_csv('roller_coasters.csv')
print(data_coaster.head())


# 6. Write a function that plots a histogram of any numeric column of the roller coaster DataFrame. Your function should take a DataFrame and a column name for which a histogram should be constructed as arguments. Make sure to include informative labels that describe your visualization.
#
#    Call your function with the roller coaster DataFrame and one of the column names.

# In[6]:


# 6
# Create a function to plot histogram of column values

def hist_values(df, roller_values):
    plt.hist(df[roller_values].dropna())
    plt.title('Histogram of {}'.format(roller_values))
    plt.xlabel(roller_values)
    plt.ylabel('Count')
    plt.show()
    plt.close()


# Create histogram of roller coaster speed

hist_values(data_coaster, 'speed')

# Create histogram of roller coaster length

hist_values(data_coaster, 'length')

# Create histogram of roller coaster number of inversions

hist_values(data_coaster, 'num_inversions')


# Create a function to plot histogram of height values

def height_values(df):
    heigths = df[df['height'] <= 140]['height'].dropna()
    plt.hist(heigths)
    plt.title('Heigth of data')
    plt.show()
    plt.close()


# Create a histogram of roller coaster height

height_values(data_coaster)


# 7. Write a function that creates a bar chart showing the number of inversions for each roller coaster at an amusement park. Your function should take the roller coaster DataFrame and an amusement park name as arguments. Make sure to include informative labels that describe your visualization.
#
#    Call your function with the roller coaster DataFrame and amusement park name.

# In[7]:


# 7
# Create a function to plot inversions by coaster at park
def inv_df(df, park_roller):
    park_roller = df[df['park'] == park_roller]
    inversions = park_roller['num_inversions']
    name = park_roller['name']
    plt.bar(range(len(inversions)), inversions)
    ax = plt.subplot()
    ax.set_xticks(range(len(name)))
    ax.set_xticklabels(name, rotation=90)
    plt.title('Inversions by coaster at park')
    plt.ylabel('Nº of inversions')
    plt.xlabel('Roaller Coaster')
    plt.show()


# Create barplot of inversions by roller coasters
inv_df(data_coaster, 'Six Flags Great Adventure')


# 8. Write a function that creates a pie chart that compares the number of operating roller coasters (`'status.operating'`) to the number of closed roller coasters (`'status.closed.definitely'`). Your function should take the roller coaster DataFrame as an argument. Make sure to include informative labels that describe your visualization.
#
#    Call your function with the roller coaster DataFrame.

# In[8]:


# 8
# Create a function to plot a pie chart of status.operating
def compare_data(df):
    compare_roller_open = df[df['status'] == 'status.operating']
    compare_roller_close = df[df['status'] == 'status.closed.definitely']
    num_roller_open = len(compare_roller_open)
    num_roller_closed = len(compare_roller_close)
    total_roller = [num_roller_open, num_roller_closed]

    plt.pie(total_roller, autopct='%.1f%%', labels=['Open', 'Close'])
    plt.title('Comparing Status operating roller coasters')
    plt.show()


# Create pie chart of roller coasters
compare_data(data_coaster)