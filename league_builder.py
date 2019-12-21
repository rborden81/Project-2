import csv
from itertools import cycle

TEAMS = ["Sharks", "Dragons", "Raptors"]

#Read in file and return the contents as a Dict
def open_file():
    with open('soccer_players.csv', newline='') as csvfile:
        return list(csv.DictReader(csvfile, delimiter=',')) 


#Take Dict from file and split the players into 2 groups; experienced and inexperienced
def split_players(command):
    experienced = []
    inexperienced = []
    players_in = open_file()
    for kid in players_in:
        if kid['Soccer Experience'] == 'YES':
            experienced.append(kid)
        else:
            inexperienced.append(kid)
    if command == 'exp':
        return experienced
    if command == 'inexp':
        return inexperienced

     
#Build teams from the 2 groups of players ensuring even experience distribution
def build_teams():
    get_xp_kids = split_players('exp')
    get_inxp_kids = split_players('inexp')
    team_names = cycle(TEAMS)
    teams = {'Sharks':[], 'Dragons': [], 'Raptors': []}
    for kid in get_xp_kids:
        get_team = next(team_names)
        if get_team == 'Sharks':
            teams['Sharks'].append([kid['Name'], kid['Soccer Experience'], kid['Guardian Name(s)']])
        if get_team == 'Dragons':
            teams['Dragons'].append([kid['Name'], kid['Soccer Experience'], kid['Guardian Name(s)']])
        if get_team == 'Raptors':
            teams['Raptors'].append([kid['Name'], kid['Soccer Experience'], kid['Guardian Name(s)']])
    for kid in get_inxp_kids:
        get_team = next(team_names)
        if get_team == 'Sharks':
            teams['Sharks'].append([kid['Name'], kid['Soccer Experience'], kid['Guardian Name(s)']])
        if get_team == 'Dragons':
            teams['Dragons'].append([kid['Name'], kid['Soccer Experience'], kid['Guardian Name(s)']])
        if get_team == 'Raptors':
            teams['Raptors'].append([kid['Name'], kid['Soccer Experience'], kid['Guardian Name(s)']])
    return(teams)
    

# Create a text file with a list of the teams, players, players parents, and experience
def write_file():
    team_data = build_teams()
    for key in team_data:
        with open("teams.txt", "a") as file:
            file.write(key+":\n")
            for item in team_data[key]:
                file.write("%s, %s, %s\n" % (''.join(item[0:1]), ''.join(item[1:2]), ''.join(item[2:3]))) 

 

if __name__ == '__main__':
    write_file()
