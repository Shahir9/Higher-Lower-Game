from game_data import data
from art import logo
from art import vs
import random
import os 

score = 0
end = False
# print(data)

#Starter declaration




randomA =random.choice(data)
randomB = random.choice(data)




while end == False:
    


#compare Value
 



    print(logo)
    print(f"Compare A: {randomA['name']},  a {randomA['description']}, from {randomA['country']}")
    
    print(vs)
    print(f"Against B: {randomB['name']},  a {randomB['description']}, from {randomA['country']}")



    followerA=randomA['follower_count']
    followerB=randomB['follower_count']




    #Alternative Condition
    higherA = False
    higherB = False

    #imput
    userGuess = input("Who has more follower? A/B")
    if userGuess == "A":
        if followerA > followerB:
            higherA = True
            score += 1
        else:
            end = True
            print(f"Your score is {score}")

    elif userGuess == "B":
        if followerB > followerA:
            higherB = True
            score +=1

        else:
            end = True
            print(f"Your score is {score}")

    #NEW value
    randomA = randomB
    randomB = random.choice(data)
    





#Guess
# def guess():
#     if guess == "higher":

#     if guess == "lower":

#     if randomB["follower_count"] > randomA["follower_count"]:

#     print("youre wrong,Game Over")



#Swap Process
# 
# guess()

