import random


print()
print("Hello, this is Matt, your personal math trainer")
student = input("Tell me your name: ")
input(f"All right {student}, type enter to start")
print()


def sum_test():
    correct = 0
    num = 1
    while correct < 5:
        a = random.randint(1, 10)
        b = random.randint(1, 10)

        print(f"{(num)}) What is {a} + {b}")
        answ = int(input("Type answer "))

        if answ == a + b:
            print("You are correct")
            correct += 1
        else:
            print("It's wrong")
            print("Try again")
        num += 1
        print()
    
    s = int( ((correct / (num - 1)) * 10000) )
    score = s / 100
    print(f"{student}, your score was {score}%")
    print()

    if score >= 70:
        print("You have passed the level")
        print("Congratulations")
    else:
        print("You had less tha 70%")
        print("Let's do it again")
    
    return score


#First stage: easy sums
print("Our first level is basic sums")
print("To pass, you need to get 5 problems correct with 70% or more accuracy")
print()

score = 0
while score < 70:
    score = sum_test()
    print()



