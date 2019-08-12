import random
def get_number_from_user():
    while True:
        number = input('Write down the number you geuss: ')
        if number.isdigit():break
        else:print("only number")
    return (int(number))
while True:
    difficulty = input("Choose the difficulty of the game and write it down (simple, medium, difficult) or exit: ")
    if difficulty == "simple" or difficulty == "Simple":
        live = 5
        score = 0
        print("Welcom to Guess my number! You are the lucky guinea pig!\nPlease guess number from 1~5, or else. You have 5 lives to guess this right!(right = lives+2;wrong = lives-1)")
        while live>0:
            correct_answer = random.randint(1,5)
            num = get_number_from_user()
            if num == correct_answer:
                score += 1
                live += 2
                print("oh! you are right!lives:"+str(live))
            elif num > 5:
                live -= 1
                print(str(live)+" lives more!(only 1~5)")
            else:
                live -= 1
                print(str(live)+" lives more!")
        print("You have got "+str(score)+" point!")
    elif difficulty == "medium" or difficulty == "Medium":
        live = 6
        score = 0
        print("Welcom to Guess my number! You are the lucky guinea pig!\nPlease guess number from 1~10, or else. You have 6 lives to guess this right!(right = lives+2;wrong = lives-1)")
        while live>0:
            correct_answer = random.randint(1,10)
            num = get_number_from_user()
            if num == correct_answer:
                score += 1
                live += 2
                print("oh! you are right!lives:"+str(live))
            elif num > 10:
                live -= 1
                print(str(live)+" lives more!(only 1~10)")
            else:
                live -= 1
                print(str(live)+" lives more!")
        print("You have got "+str(score)+" point!")
    elif difficulty == "difficult" or difficulty == "Difficult":
        live = 8
        score = 0
        print("Welcom to Guess my number! You are the lucky guinea pig!\nPlease guess number from 1~15, or else. You have 8 lives to guess this right!(right = lives+2;wrong = lives-1)")
        while live>0:
            correct_answer = random.randint(1,15)
            num = get_number_from_user()
            if num == correct_answer:
                score += 1
                live += 2
                print("oh! you are right!lives:"+str(live))
            elif num > 15:
                live -= 1
                print(str(live)+" lives more!(only 1~15)")
            else:
                live -= 1
                print(str(live)+" lives more!")
        print("You have got "+str(score)+" point!")
    else:
        break