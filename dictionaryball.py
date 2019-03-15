game_dictionary = {}

def add_team(is_home_team, team_name, colors):
    team = {}
    team['team_name'] = team_name
    team['colors'] = colors
    team['players'] = {}
    if is_home_team:
        game_dictionary['home'] = team
    else:
        game_dictionary['away'] = team

def add_player(is_home_team, name, number, shoe, points, rebounds, assists, steals, blocks, slam_dunks):
    team_key = 'away'
    if is_home_team:
        team_key = 'home'

    player = {}
    player['number'] = number
    player['shoe'] = shoe
    player['points'] = points
    player['rebounds'] = rebounds
    player['assists'] = assists
    player['steals'] = steals
    player['blocks'] = blocks
    player['slam_dunks'] = slam_dunks
    game_dictionary[team_key]['players'][name] = player

def game_dict():
    add_team(True, 'Brooklyn Nets', ['Black', 'White'])
    add_team(False, 'Charlotte Hornets', ['Turquoise', 'Purple'])

    add_player(True,'Alan Anderson',0,16,22,12,12,3,1,1)
    add_player(True,'Reggie Evans',30,14,12,12,12,12,12,7)
    add_player(True,'Brook Lopez',11,17,17,19,10,3,1,15)
    add_player(True,'Mason Plumlee',1,19,26,12,6,3,8,5)
    add_player(True,'Jason Terry',31,15,19,2,2,4,11,1)

    add_player(False,'Jeff Adrien',4,18,10,1,1,2,7,2)
    add_player(False,'Bismak Biyombo',0,16,12,4,7,7,15,10)
    add_player(False,'DeSagna Diop',2,14,24,12,12,4,5,5)
    add_player(False,'Ben Gordon',8,15,33,3,2,1,1,0)
    add_player(False,'Brendan Haywood',33,15,6,12,12,22,5,12)
    return game_dictionary

def player_stat(player_name, stat):
    points = None

    if player_name in game_dictionary['home']['players'].keys():
        points = game_dictionary['home']['players'][player_name][stat]
    elif player_name in game_dictionary['away']['players'].keys():
        points = game_dictionary['away']['players'][player_name][stat]

    return points

def num_points_scored(player_name):
    return player_stat(player_name, 'points')

def shoe_size(player_name):
    return player_stat(player_name, 'shoe')

def team_colors(team_name):
    team_colors = None

    if team_name == game_dictionary['home']['team_name']:
        team_colors = game_dictionary['home']['colors']
    elif team_name == game_dictionary['away']['team_name']:
        team_colors = game_dictionary['away']['colors']

    return team_colors

def team_names():
    names = []

    for team in game_dictionary.keys():
        names.append(game_dictionary[team]['team_name'])

    return names

def player_numbers(team_name):
    numbers = []

    if team_name == game_dictionary['home']['team_name']:
        players = game_dictionary['home']['players']
    elif team_name == game_dictionary['away']['team_name']:
        players = game_dictionary['away']['players']

    for player_stat in players.values():
        numbers.append(player_stat['number'])

    return numbers

def player_stats(player_name):
    stats = None

    if player_name in game_dictionary['home']['players'].keys():
        stats = game_dictionary['home']['players'][player_name]
    elif player_name in game_dictionary['away']['players'].keys():
        stats = game_dictionary['away']['players'][player_name]

    return stats

def big_shoe_rebounds():
    big_shoe = 0
    big_shoe_player = None

    for team in game_dictionary.keys():
        for player in game_dictionary[team]['players']:
            if game_dictionary[team]['players'][player]['shoe'] > big_shoe:
                big_shoe = game_dictionary[team]['players'][player]['shoe']
                big_shoe_player = player

    return big_shoe_player

def most_points_scored():
    most_points = 0
    most_points_player = None

    for team in game_dictionary.keys():
        for player in game_dictionary[team]['players']:
            if game_dictionary[team]['players'][player]['points'] > most_points:
                most_points = game_dictionary[team]['players'][player]['points']
                most_points_player = player

    return most_points_player

def winning_team():
    most_points = 0
    team_points = 0
    most_points_team = None

    for team in game_dictionary.keys():
        team_points = 0
        for player in game_dictionary[team]['players']:
            team_points += game_dictionary[team]['players'][player]['points']
        if team_points > most_points:
            most_points = team_points
            most_points_team = game_dictionary[team]['team_name']

    return most_points_team

def longest_name():
    longest_name = ''

    for team in game_dictionary.keys():
        for player in game_dictionary[team]['players'].keys():
            if len(player) > len(longest_name):
                longest_name = player

    return longest_name

def long_name_steals_a_ton():
    most_steals = 0
    most_steals_player = None
    steals_a_ton = False

    for team in game_dictionary.keys():
        for player in game_dictionary[team]['players']:
            if game_dictionary[team]['players'][player]['steals'] > most_steals:
                most_steals = game_dictionary[team]['players'][player]['steals']
                most_steals_player = player

    if most_steals_player == longest_name():
        steals_a_ton = True

    return steals_a_ton
