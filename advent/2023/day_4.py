from day_4_data import advent_data

sample_data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

# Part One

# def winning_numbers(cards):
#     cards = cards.splitlines()
#     cards_value = 0
#     for card in cards:
#         card_value = 0
#         first_match = False
#         winning_numbers, your_numbers = card.split("|")
#         colon = winning_numbers.index(":") + 1
#         winning_numbers = winning_numbers[colon:].strip()
#         for number in your_numbers.split(" "):
#             print(number)
#             if first_match is False:
#                 if number in winning_numbers.split(" ") and number:
#                     card_value = 1
#                     first_match = True
#             elif first_match is True:
#                 if number in winning_numbers.split(" ") and number:
#                     card_value *= 2
#         cards_value += card_value
#     return cards_value


# print(winning_numbers(advent_data))


# Part Two


# def winning_numbers(cards):
#     cards = cards.splitlines()
#     cards_won = 0
#     i = 0
#     matches = 0
#     while i < len(cards):
#         winning_numbers, your_numbers = cards[i].split("|")
#         colon = winning_numbers.index(":") + 1
#         winning_numbers = winning_numbers[colon:].strip()
#         for number in your_numbers.split(" "):
#             if number in winning_numbers.split(" ") and number:
#                 matches += 1
#                 cards_won += 1
#         if matches:
#             if i > 1:
#                 i -= 1
#                 matches -= 1
#         print(matches)
#         # if matches:
#         #     matches -= 1
#         #     i -= 1
#         i += 1

#     return cards_won


# print(winning_numbers(sample_data))


# def winning_numbers(cards):
#     cards = cards.splitlines()
#     cards_won = 0
#     matches = 0
#     for card in cards:
#         winning_numbers, your_numbers = card.split("|")
#         colon = winning_numbers.index(":") + 1
#         winning_numbers = winning_numbers[colon:].strip()
#         for number in your_numbers.split(" "):
#             if number in winning_numbers.split(" ") and number:
#                 matches += 1
#                 cards_won += 1
#         for match in range(1, matches):
#             print(match)

#     return cards_won


# print(winning_numbers(sample_data))

# need to track original card?
# times something by two?
# higher-order function?
# repeat loops?


# def winning_numbers(cards):
#     cards = cards.splitlines()
#     cards_collected = 0
#     for card in cards:
#         matches = 0
#         winning_numbers, your_numbers = card.split("|")
#         colon = winning_numbers.index(":") + 1
#         winning_numbers = winning_numbers[colon:].strip()
#         for number in your_numbers.split(" "):
#             if number in winning_numbers.split(" ") and number:
#                 matches += 1
#         for i in range(matches):
#             for j in range(i + 1, len(cards)):
#                 print(cards[j])
#                 winning_numbers, your_numbers = cards[j].split("|")
#                 colon = winning_numbers.index(":") + 1
#                 winning_numbers = winning_numbers[colon:].strip()
#                 for number in your_numbers.split(" "):
#                     if number in winning_numbers.split(" ") and number:
#                         cards_collected += 1
#     return cards_collected


# print(winning_numbers(sample_data))
# IS TOO LOW


# def winning_numbers(cards):
#     cards = cards.splitlines()
#     cards_collected = 0
#     for card in cards:
#         matches = 0
#         winning_numbers, your_numbers = card.split("|")
#         colon = winning_numbers.index(":") + 1
#         winning_numbers = winning_numbers[colon:].strip()
#         for number in your_numbers.split(" "):
#             if number in winning_numbers.split(" ") and number:
#                 matches += 1
#         for i in range(matches):
#             for j in range(i + 1, matches + 1):
#                 winning_numbers, your_numbers = cards[j].split("|")
#                 colon = winning_numbers.index(":") + 1
#                 winning_numbers = winning_numbers[colon:].strip()
#                 for number in your_numbers.split(" "):
#                     if number in winning_numbers.split(" ") and number:
#                         cards_collected += 1
#     return cards_collected


# print(winning_numbers(sample_data))


# def winning_numbers(cards):
#     cards = cards.splitlines()
#     cards_collected = 0
#     # Matches here? Are we losing something after the first loop?
#     for i in range(len(cards)):
#         matches = 0
#         winning_numbers, your_numbers = cards[i].split("|")
#         colon = winning_numbers.index(":") + 1
#         winning_numbers = winning_numbers[colon:].strip()
#         for number in your_numbers.split(" "):
#             if number in winning_numbers.split(" ") and number:
#                 matches += 1
#         if not matches:  # why only if no matches...
#             cards_collected += 1
#             print("ayo")
#         for j in range(matches):  # for each match
#             for k in range(i + 1, i + matches + 1):
#                 print("CARDS", cards[k])
#                 winning_numbers, your_numbers = cards[k].split("|")
#                 colon = winning_numbers.index(":") + 1
#                 winning_numbers = winning_numbers[colon:].strip()
#                 for number in your_numbers.split(" "):
#                     if number in winning_numbers.split(" ") and number:
#                         cards_collected += 1
#     return cards_collected


# print(winning_numbers(sample_data))


# def winning_numbers(cards):
#     cards = cards.splitlines()
#     cards_collected = 0
#     # Matches here? Are we losing something after the first loop?
#     for i in range(len(cards)):
#         matches = 0
#         winning_numbers, your_numbers = cards[i].split("|")
#         colon = winning_numbers.index(":") + 1
#         winning_numbers = winning_numbers[colon:].strip()
#         for number in your_numbers.split(" "):
#             if number in winning_numbers.split(" ") and number:
#                 matches += 1
#         if not matches:  # why only if no matches...
#             cards_collected += 1
#         else:
#             for j in range(matches):  # for each match
#                 for k in range(i + 1, i + matches + 1):
#                     # print("CARDS", cards[k]) ... card numbers aren't matching expectation whatsoever... not sure
#                     winning_numbers, your_numbers = cards[k].split("|")
#                     colon = winning_numbers.index(":") + 1
#                     winning_numbers = winning_numbers[colon:].strip()
#                     for number in your_numbers.split(" "):
#                         if number in winning_numbers.split(" ") and number:
#                             cards_collected += 1
#     return cards_collected


# print(winning_numbers(sample_data))


def winning_numbers(cards):
    cards = cards.splitlines()
    cards_collected = 0
    # Matches here? Are we losing something after the first loop?
    count = {}
    for i in range(len(cards)):
        matches = 0
        winning_numbers, your_numbers = cards[i].split("|")
        colon = winning_numbers.index(":") + 1
        winning_numbers = winning_numbers[colon:].strip()
        for number in your_numbers.split(" "):
            if number in winning_numbers.split(" ") and number:
                matches += 1
        count[i + 1] = 1
        print(count)
        print(matches)
        while matches:
            try:
                count[i] += 1
                matches -= 1
                i += 1
            except KeyError:
                break
    return cards_collected


print(winning_numbers(sample_data))
