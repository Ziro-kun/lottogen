import random

def generate_lotto():
    lotto = []

    while len(lotto) < 6:
        num = random.randint(1, 45)
        if num not in lotto:
            lotto.append(num)

    lotto.sort()
    return lotto


def generate_games(game_count):
    return [generate_lotto() for _ in range(game_count)]


def check_winning(game, winning_numbers, bonus_number):
    match_count = 0
    for num in game:
        if num in winning_numbers:
            match_count += 1

    if match_count == 6:
        return "1등"
    elif match_count == 5:
        if bonus_number in game:
            return "2등"
        else:
            return "3등"
    elif match_count == 4:
        return "4등"
    elif match_count == 3:
        return "5등"
    else:
        return "꽝"
