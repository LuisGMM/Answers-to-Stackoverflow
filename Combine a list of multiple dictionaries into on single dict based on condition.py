

lst = [
        {
            "Game": "Lego",
            "players": [         
            {
                "Age": "28",
                "Experience": "yes",
                "Score": [
                    {
                        "Alicia": 987
                    }
                ]
            },
                {
                    "Age": "20",
                    "Experience": "yes",
                    "Score": [
                        {
                            "Alex": 230
                        }
                    ]
                },
                {
                    "Age": "20",
                    "Experience": "yes",
                    "Score": [
                        {
                            "juana": 275
                        }
                    ]
                }
            ],
            "season": "summer"
        }
    ]

result_lst = []

for game_dict in lst:

    result_dict = {}
    result_dict['Game'] = game_dict['Game']
    result_dict['players'] = []
    result_dict['season'] = game_dict['season']

    for player_dict1 in game_dict['players']:

        starting_idx = game_dict['players'].index(player_dict1) + 1

        for player_dict2 in game_dict['players'][starting_idx:]:

            if player_dict1['Age'] == player_dict2['Age'] and player_dict1['Experience'] == player_dict2['Experience']:

                age = player_dict1['Age']
                experience = player_dict1['Experience']

                for result_player in result_dict['players']:

                    if age == result_player['Age']:

                        if player_dict1['Score'][0] not in result_player['Score']:
                            result_player['Score'].append(player_dict1['Score'][0])

                        if player_dict2['Score'][0] not in result_player['Score']:
                            result_player['Score'].append(player_dict2['Score'][0])

                        break
                
                else:

                    players_dict = {'Age': age,
                                    'Experience': experience,
                                    'Score': [player_dict1['Score'][0],
                                            player_dict2['Score'][0],
                                    ]
                    }

                    result_dict['players'].append(players_dict)
    
    in_result_dict = True

    for player_dict in game_dict['players']:
        
        for result_players in result_dict['players']:
            for result_player in result_players['Score']:
                
                if player_dict['Score'][0] == result_player:
                    in_result_dict = False
                    break

        if in_result_dict:
            result_dict['players'].append(player_dict)

    result_lst.append(result_dict)


print(result_lst)

[{'Game': 'Lego', 
  'players': [{'Age': '20', 
               'Experience': 'yes', 
               'Score': [{'Alex': 230}, {'juana': 275}]}, 
               
               {'Age': '28', 
                'Experience': 'yes', 
                'Score': [{'Alicia': 987}]}], 
  'season': 'summer'}]