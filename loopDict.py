afc_east_west_wins = {'Bills': 4,
                      'Jets': 3,
                      'Dolphins': 3,
                      'Patriots': 2,
                      'Chiefs': 3,
                      'Chargers': 3,
                      'Broncos': 2,
                      'Raiders': 1,
                      'Your Fantasy Team': 9}

largest_so_far = 'Raiders'
for team_name in afc_east_west_wins.keys():
    if afc_east_west_wins[team_name] > afc_east_west_wins[largest_so_far]:
        largest_so_far = team_name
print(f"The team: {largest_so_far} has the most wins with {afc_east_west_wins[largest_so_far]} wins")