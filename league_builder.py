import csv


if __name__ == '__main__':
    def setup_teams(team, sharks, dragons, raptors, counter):
        for kid in team:
            if counter == 1:
                sharks.append(kid)
                counter += 1
            elif counter == 2:
                dragons.append(kid)
                counter += 1
            elif counter == 3:
                raptors.append(kid)
                counter = 1


    def print_teams(team, team_name):
        with open('teams.txt', 'a') as teamsfile:
            teamsfile.write('{}\n'.format(team_name))
            for kid in team:
                teamsfile.write('{}, {}, {}, {}\n'.format(kid['Name'], kid['Height (inches)'], kid['Soccer Experience'], kid['Guardian Name(s)']))
            # add a space before the next team for easier readability
            teamsfile.write('\n')


    def welcome_letter(team, team_name):
        for kid in team:
            # create file names with firstname_lastname of the kid
            kid_file_name = '_'.join(kid['Name'].lower().split())
            with open('{}.txt'.format(kid_file_name), 'a') as kidfile:
                kidfile.write('Dear {},\n'.format(kid['Guardian Name(s)']))
                kidfile.write("Welcome to the soccer season! Here is your child's information:\n")
                kidfile.write('Soccer Player: {}\n'.format(kid['Name']))
                kidfile.write('Team: {}\n'.format(team_name))
                kidfile.write('First Practice: Oct. 5th at 5pm')


    # Open the csv of soccer players
    with open('soccer_players.csv') as csvfile:
        # Read the csv file as a dictionary
        csv_reader = csv.DictReader(csvfile)
        #put students into two groups based on their previous experience
        previous_exp = []
        no_previous_exp = []
        for row in csv_reader:
            if row['Soccer Experience'] == 'YES':
                previous_exp.append(row)
            else:
                no_previous_exp.append(row)

        # setup teams - variables
        sharks = []
        dragons = []
        raptors = []
        # pass in counter in case total students is not equally divisible into teams
        # that way we start adding kids to the next team and do not start from the top again
        counter = 1

        # setup teams - previous_exp
        setup_teams(previous_exp, sharks, dragons, raptors, counter)

        # setup teams - no_previous_exp
        setup_teams(no_previous_exp, sharks, dragons, raptors, counter)

        # write students to file
        print_teams(sharks, 'Sharks')
        print_teams(dragons, 'Dragons')
        print_teams(raptors, 'Raptors')

        # create welcome letters
        welcome_letter(sharks, 'Sharks')
        welcome_letter(dragons, 'Dragons')
        welcome_letter(raptors, 'Raptors')
