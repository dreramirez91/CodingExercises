from day_2_data import elf_games

sample_games = """Game 1: 4 red, 5 blue, 4 green; 7 red, 8 blue, 2 green; 9 blue, 6 red; 1 green, 3 red, 7 blue; 3 green, 7 red
Game 2: 20 blue, 12 green, 2 red; 1 red, 2 green, 20 blue; 1 red, 14 green, 17 blue; 7 green, 17 blue
Game 3: 3 green, 4 red; 10 red, 2 blue, 5 green; 9 red, 3 blue, 5 green
Game 4: 10 green, 1 blue, 3 red; 1 red, 12 green, 1 blue; 1 blue, 2 green; 4 green, 3 red
Game 5: 3 green, 8 red, 1 blue; 4 blue, 7 red, 3 green; 2 green, 2 blue, 13 red
"""


# def possible_games(games):
#     all_games = []
#     game_number = 0
#     for full_game in games.splitlines():
#         game_list = []
#         game_number += 1
#         game_split = full_game.split(";")
#         for each_game in game_split:
#             try:
#                 colon_index = each_game.index(":") + 1
#             except ValueError:
#                 colon_index = None
#             colors_only = each_game[colon_index:]
#             stripped_colors = colors_only.strip()
#             individual_game = stripped_colors.split(",")
#             this_game = {}
#             for e in individual_game:
#                 number = ""
#                 color = ""
#                 for char in e:
#                     if char.isdigit():
#                         number += char
#                     elif char.isalpha():
#                         color += char
#                 this_game[color] = int(number)
#             game_list.append(this_game)
#         all_games.append(game_list)
#     possible_games_id_total = 0
#     games_added = []
#     for i in range(len(all_games)):
#         game_is_possible = True
#         for game in all_games[i]:
#             if (
#                 game.get("red", 0) > 12
#                 or game.get("green", 0) > 13
#                 or game.get("blue", 0) > 14
#             ):
#                 game_is_possible = False
#         if game_is_possible and (i + 1) not in games_added:
#             possible_games_id_total += i + 1
#             games_added.append(i + 1)

#     return possible_games_id_total


# print(possible_games(elf_games))  # Expected output 8

# We have 12 red cubes, 13 green cubes, and 14 blue cubes


def possible_games(games):
    all_games = {}
    game_number = 0
    for full_game in games.splitlines():
        game_list = []
        game_number += 1
        game_split = full_game.split(";")
        for each_game in game_split:
            try:
                colon_index = each_game.index(":") + 1
            except ValueError:
                colon_index = None
            colors_only = each_game[colon_index:]
            stripped_colors = colors_only.strip()
            individual_game = stripped_colors.split(",")
            this_game = {}
            for e in individual_game:
                number = ""
                color = ""
                for char in e:
                    if char.isdigit():
                        number += char
                    elif char.isalpha():
                        color += char
                this_game[color] = int(number)
            game_list.append(this_game)
        all_games[game_number] = game_list
    possible_games_id_total = 0
    games_added = []
    for game_number, game_list in all_games.items():
        game_is_possible = True
        for game in game_list:
            if (
                game.get("red", 0) > 12
                or game.get("green", 0) > 13
                or game.get("blue", 0) > 14
            ):
                game_is_possible = False
        if game_is_possible and game_number not in games_added:
            possible_games_id_total += game_number
            games_added.append(game_number)

    return possible_games_id_total


print(possible_games(sample_games))  # Expected output 8

# We have 12 red cubes, 13 green cubes, and 14 blue cubes

# def possible_games_2(games):
#     all_games = []
#     game_number = 0
#     for full_game in games.splitlines():
#         game_list = []
#         game_number += 1
#         game_split = full_game.split(";")
#         for each_game in game_split:
#             try:
#                 colon_index = each_game.index(":") + 1
#             except ValueError:
#                 colon_index = None
#             colors_only = each_game[colon_index:]
#             stripped_colors = colors_only.strip()
#             individual_game = stripped_colors.split(",")
#             this_game = {}
#             for e in individual_game:
#                 number = ""
#                 color = ""
#                 for char in e:
#                     if char.isdigit():
#                         number += char
#                     elif char.isalpha():
#                         color += char
#                 this_game[color] = int(number)
#             game_list.append(this_game)
#         all_games.append(game_list)
#     cube = 0
#     for i in range(len(all_games)):
#         count = {"red": 0, "blue": 0, "green": 0}
#         for game in all_games[i]:
#             if game.get("red", 0) > count["red"]:
#                 count["red"] = game.get("red")
#             if game.get("green", 0) > count["green"]:
#                 count["green"] = game.get("green")
#             if game.get("blue", 0) > count["blue"]:
#                 count["blue"] = game.get("blue")
#         cube += count["red"] * count["green"] * count["blue"]
#     return cube


# print(possible_games_2(elf_games))  # Expected output = 1154
