# Goblin Clan

import time, random

measures = {"gold": 100, "reputation": 1, "followers": 10, "tech": 1}

win = {"gold": 1000000, "reputation": 100, "followers": 1000000, "tech": 10}

lose = {"gold": 0, "reputation": 0, "followers": 0, "tech": 0}

def check_win_lose():
    for key in measures:
        if measures[key] >= win[key]:
            print("You win!")
            exit()
        elif measures[key] == lose[key]:
            print("You lose...")
            exit()

def mining(miners):
    mined_gold = (miners/2)
    print("You mined " + str(mined_gold) + "gold.")
    measures["gold"] += mined_gold

def raiding(raiders):
    loot = (raiders/2)
    rep_growth = (loot/2)
    print("You looted " + str(loot) + " gold and your reputation grows by " + str(rep_growth))
    measures["gold"] += loot
    measures["reputation"] += rep_growth
    return loot

def research(scientists):
    tech_growth = (scientists/2)
    print("Your tech grew by " + str(tech_growth))
    measures["tech"] += tech_growth
    return tech_growth

def reputation_growth(followers):
    rep_growth = (followers/ 2)
    print("Because of your followers, your reputation has increased by " + str(rep_growth))
    measures["reputation"] += rep_growth

def game():
    time.sleep(1)
    mining(2)
    raiding(6)
    research(2)
    reputation_growth(measures["followers"])
    print("One day has passed.")
    for key in measures:
        print(key + " = " + str(measures[key]))
    check_win_lose()


while True:
    game()
