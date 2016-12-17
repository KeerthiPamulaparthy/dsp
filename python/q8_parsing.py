# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.
import pandas as pd
df = pd.read_csv('football.csv')
df_goals = df[['Team', 'Goals', 'Goals Allowed']]
df_goals.columns = ['Team', 'Goals', 'Goals_Allowed']
df_goals['Difference'] = df_goals.Goals - df_goals.Goals_Allowed
df_goals['Difference'] = df_goals.Difference.abs()
df_goals = df_goals.sort_values(['Difference'])
print "Team with smallest difference: %s" %df_goals['Team'].loc[0]
