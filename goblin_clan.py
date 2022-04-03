# Goblin Clan

import time, random, math

# scores
measures = {"gold": 10, "reputation": 10, "followers": 10, "tech_level": 10}

# win conditions
win = {"gold": 1000000, "reputation": 1000000, "followers": 1000000, "tech_level": 1000000}

# lose conditions
lose = {"gold": 0, "reputation": 0, "followers": 0, "tech_level": 0}

# Goblin Clan attributes
attributes = {"sneaky_git": 1, "fabrikator": 1, "lucky_sod": 1}

locals = {"goblins": 1, "humans": 1.5, "dwarves": 2, "elves": 3}

def check_win_lose():
    for key in measures:
        if measures[key] >= win[key]:
            print("You win!")
            exit()
        elif measures[key] == lose[key]:
            print("You lose...")
            exit()

def mining(miners):
    mined_gold = int((miners/2)*attributes["lucky_sod"])
    print("You mined {} gold.".format(mined_gold))
    measures["gold"] += mined_gold

def raiding(raiders):
    party_strength = raiders*attributes["sneaky_git"]
    print("Your strength is {}.".format(party_strength))
    opponent = random.choice(list(locals.keys()))
    opponent_numbers = random.randint(1, 10)
    opponent_strength = locals[opponent]*opponent_numbers
    attack = input("The {} have {} warriors with a strength of {}, will you still raid?".format(opponent, opponent_numbers, opponent_strength))
    if attack == "n":
        return
    else:
        your_roll = random.randint(1, 6)
        print("You rolled {}.".format(your_roll))
        opponent_roll = random.randint(1, 6)
        print("The {} rolled {}.".format(opponent, opponent_roll))
        your_outcome = your_roll * party_strength
        opponent_outcome = opponent_roll * opponent_strength
        print("Your outcome was {} and the {}' outcome was {}.".format(your_outcome, opponent, opponent_outcome))
        if your_outcome > opponent_outcome:
            loot = int(random.randint(5, 10)*locals[opponent])
            measures["gold"] += loot
            measures["reputation"] += int(loot*0.2)
            print("You took those {} for {} gold, and gained {} reputation.".format(opponent, loot, int(loot*0.2)))
        elif your_outcome == opponent_outcome:
            loot = int(random.randint(1, 5)*locals[opponent])
            dead = int(raiders*0.2)
            rep = int(loot*0.2)
            measures["gold"] += loot
            measures["followers"] -= dead
            measures["reputation"] += rep
            print("The {} fought back, you managed to pilfer {} gold and increased your reputation by {} but you lost {} clan members.".format(opponent, loot, rep, dead))
        else:
            dead = int((raiders*0.25)*locals[opponent])
            rep = int(math.ceil(dead*0.5))
            measures["followers"] -= dead
            measures["reputation"] -= rep
            print("Disaster, the {} beat your raiding party. {} clan members are now with the Great Goblin in the sky and you lost {} reputation.".format(opponent, dead, rep))
        return

def research(scientists, gold):
    tech_growth = int((scientists + gold)/2)*attributes["fabrikator"]
    print("Your tech grew by {}.".format(str(tech_growth)))
    measures["tech_level"] += tech_growth
    measures["reputation"] += tech_growth

def follower_growth(reputation):
    follower_growth = int(reputation/10)
    print("Because of your reputation, your followers have increased by {}".format(follower_growth))
    measures["followers"] += follower_growth

def game():

    goblins = measures["followers"]

    gold = measures["gold"]

    print("You have {} goblins to command.".format(goblins))

    time.sleep(1)

    miners = int(input("How many goblins will you send to mine for gold today?"))

    if miners > goblins:
        miners = int(input("You do not have that many goblins. You have {} goblins. How many goblins will you send to mine for gold?".format(measures["followers"])))
    else:
        goblins = goblins - miners

    raiders = int(input("You have {} goblins left. How many goblins will you send to raid local villages?".format(goblins)))

    if raiders > goblins:
        raiders = int(input("You do not have that many goblins. You have {} goblins. How many goblins will you send to raid local villages?".format(goblins)))
    else:
        goblins = goblins - raiders

    scientists = goblins

    if scientists == 0:
        pass
    else:
        research_gold = int(input("You have {} gold. How much will you give to the goblins you've allowed to sit around and tinker?".format(gold)))
        measures["gold"] -= research_gold

    time.sleep(0.5)

    if miners == 0:
        pass
    else:
        mining(miners)

    time.sleep(0.5)

    if raiders == 0:
        pass
    else:
        raiding(raiders)

    time.sleep(0.5)

    if scientists == 0:
        pass
    else:
        research(scientists, research_gold)

    time.sleep(0.5)

    print("It is the end of another day in goblin paradise.")

    follower_growth(measures["reputation"])

    time.sleep(0.5)

    for key in measures:
        print("{} = {}".format(key, measures[key]))
    check_win_lose()

while True:
    game()
