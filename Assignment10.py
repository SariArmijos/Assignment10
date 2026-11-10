import pandas as pd

#Create a dictionary where values will be stored later
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
#I used AI to learn that .empty check whether the DataFrame has zero rows containing the value
while data_by_season.empty:
    season_user = int(input("Season not found. Please, try again: "))
    data_by_season = data_file.query("Season == @season_user")

#Create a loop to go through each row
for index, row in data_by_season.iterrows():
    #Loop 1: 10 or more wins
    if row["Win"] >= 10:
        teams["10 or more wins"].append(row["Team"])
    #Loop 2: 8-9 wins
    elif row["Win"] >= 8:
        teams["8-9 wins"].append(row["Team"])
    #Loop 3: 6-7 wins
    elif row["Win"] >= 6:
        teams["6-7 wins"].append(row["Team"])
    #Loop 4: Fewer than 6 wins
    elif row["Win"] < 6:
        teams["Fewer than 6 wins"].append(row["Team"])

#Create another loop to display the results
#I used AI to learn .items (access keys and values from a dictionary)
#Loop 1: access the categories (column names)
#Index: represents the column names and value contains the entire list under each category
for index, value in teams.items():
    print()
    #Print the category names
    print(index)
    print()
    #Loop 2: access individual teams
    for team in value: 
        print(team)
