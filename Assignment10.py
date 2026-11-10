import pandas as pd
import numpy as np

teams = {
    "10 or more wins": [],
    "8-9 wins": [],
    "6-7 wins": [],
    "Fewer than 6 wins": []
}
#Ask the user to choose a season
season_user = int(input("Enter a season to analyze: "))
#Read the csv file and store in into a variable
data_file = pd.read_csv("cfb.csv")
#Filter the data_file to show rows from the selected season only
#I learned that by adding the @ symbol, I can reference a Python variable that exists outside the DataFrame
data_by_season = data_file.query("Season == @season_user")
#Let the user know if the requested season is not found
while data_by_season.isnull() == True :
    season_user = int(input("Season not found. Please, try again: "))

#Loop 1: 10 or more wins
wins_10 = data_file.query("Win >= 10")
print(wins_10["Team"])
#Loop 2: 8-9 wins
wins_8_9 = data_file.query("Win <= 9 and Win >= 8")
print(wins_8_9["Team"])
#Loop 3: 6-7 wins
wins_6_7 = data_file.query("Win <= 7 and Win >= 6")
print(wins_6_7["Team"])
#Loop 4: Fewer than 6 wins
wins_6 = data_file.query("Win < 6")
print(wins_6["Team"])