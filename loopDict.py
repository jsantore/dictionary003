afc_east_west_wins = {'Bills': 4,
                      'Jets': 3,
                      'Dolphins': 3,
                      'Patriots': 2,
                      'Chiefs': 3,
                      'Chargers': 3,
                      'Broncos': 2,
                      'Raiders': 1}

largest_so_far = 'Raiders'
for team_name in afc_east_west_wins.keys():
    print(f"The {team_name} have {afc_east_west_wins[team_name]} wins so far")