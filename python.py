import random
userscore = 0
computerscore = 0
ties = 0
rounds = 0

mode = ""
while mode not in ("infinite", "best5", "computerwin"):
    mode = input("infinite or best5 or computerwin: ").lower()
    if mode not in ("infinite", "best5", "computerwin"):
        print("spatny vstup")


while True:
    if mode == "best5" and rounds >= 5:
        if userscore > computerscore:
            print("vyhravas celkove")
        elif userscore < computerscore:
            print("prohravas celkove")
        else:
            print("remiza")
        break

    print ("Score: user -", userscore, "pocitac -", computerscore)
    user = input("Enter (rock, paper, scissors) or 'quit': ")
    if user == 'quit':
        break
    if user == 'rock':
        user = 0
    elif user == 'paper':
        user = 1
    elif user == 'scissors':
        user = 2
    else:
        print("spatny vstup")
        continue

    if mode == "computerwin":
        print("prohravas")
        computerscore += 1
        rounds += 1
        continue
    computer = random.randint(0, 2)
    if user == computer:
        print("remiza")
        ties += 1

    elif (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
        print("vyhravas")
        userscore += 1
    else:
        print("prohravas")
        computerscore += 1
    rounds += 1

print("Final score: user wins -", userscore, "computer wins -", computerscore, "ties -", ties)
