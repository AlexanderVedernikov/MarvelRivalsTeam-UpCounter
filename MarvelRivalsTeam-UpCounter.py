from itertools import combinations

def function():
    
    character_dict = {"Captain America": [],
    "Doctor Strange": [],
    "Groot": ["Jeff the Land Shark", "Rocket Raccoon"],
    "Hulk": ["Doctor Strange", "Iron Man"],
    "Magneto": [],
    "Peni Parker": ["Venom"],
    "The Thing": [],
    "Thor":["Captain America", "Storm"],
    "Venom":["Peni Parker", "Spider-Man"],
    "Black Panther":[],
    "Black Widow":[],
    "Hawkeye":["Black Widow"],
    "Hela":["Loki", "Thor"],
    "Human Torch":["Storm"],
    "Iron Fist":["Luna Snow"],
    "Iron Man":[],
    "Magik":["Black Panther", "Psylocke"],
    "Mister Fantastic":[],
    "Moon Knight":[],
    "Namor":[],
    "Psylocke":[],
    "Scarlet Witch":["Magneto"],
    "Spider-Man":["Squirrel Girl"],
    "Squirrel Girl":[],
    "Star-Lord":[],
    "Storm":[],
    "The Punisher":[],
    "Winter Soldier":[],
    "Wolverine":["Hulk", "The Thing"],
    "Adam Warlock":["Mantis", "Star-Lord"],
    "Cloak & Dagger":["Moon Knight"],
    "Invisible Woman":["Mister Fantastic"],
    "Jeff the Land Shark":[],
    "Loki":[],
    "Luna Snow":["Jeff the Land Shark", "Namor"],
    "Mantis":[],
    "Rocket Raccoon":["The Punisher", "Winter Soldier"],
    }

    numberOfPlayers = 6

    characterCombinations = list(combinations(character_dict, numberOfPlayers))

    totalCombinations = 0
    totalTeamUpTeams = 0
    totalNoTeamUpTeams = 0
    found = False

    #Iterates through every possible team combinations
    for teamCombination in range(len(characterCombinations)):

        #Iterates through every character in a team
        for character in characterCombinations[teamCombination]:
            teamUps = character_dict[character]
            found = False
            #Iterates through every team-up for a specific character
            for individualTeamUp in teamUps:
                
                #Iterates through every
                for characterAgain in characterCombinations[teamCombination]:
                    
                    if individualTeamUp == characterAgain:
                        totalTeamUpTeams += 1
                        found = True
                        #If a team-up is found, stop looking and check the next team
                        break
                if (found):
                    break
            if (found):
                break
        if not found:
            totalNoTeamUpTeams += 1
        totalCombinations +=1

    print("For a team of " + str(numberOfPlayers) + ":")
    print("Total Combinations:")
    print(totalCombinations)
    print("Total Team-Ups:")
    print(totalTeamUpTeams)
    print("Total Without Team-Ups:")
    print(totalNoTeamUpTeams)
    print("No Team-Up Ratio:")
    print(totalNoTeamUpTeams / totalCombinations)

    return True

function()