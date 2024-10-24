
import time
import lib.Functions as f
yes = ('yes', 'y', 'okay', 'yup', 'ok')
no = ('no', 'nope', 'n')

#Introduction (Story)
print("'Welcome to How to Train Your Dragon: Quest of the Dragon Nest!'")
time.sleep(2)
print("The viking island of Berk has been peacefully living with dragons for a long time...until...")
time.sleep(2)
print("The evil dragons have decided to attack your island!\nHiccup needs your help to defeat all the dragons from the dragon nest and bring peace to the villagers.")
input("\nPress enter to continue.")  #Even if the person writes something it will still continue because the person is still pressing enter
f.space()
print("\nHiccup gives you an abandoned dragon he found and asks you to train it.")

while True:
    ans = input("Do you want to train this dragon(yes/no)?").lower()
    if ans in yes:  #if the answer is any of the things in the list yes
        print("\nYou accept the dragon and start its training!")
        break
    elif ans in no:  #if the answer is any of the things in the list no
        print("You refuse the dragon and leave the fighting for the professionals... ")
        time.sleep(1)
        print("Unfortunately that was not enough and the evil dragons destroy the whole island including you.")
        time.sleep(2)
        print("\nYou have died.")
        print("GAME OVER")
        time.sleep(4)
        exit()
        break
    else:
        print("This is not an answer...")

#Naming your dragon
print("First you will need to name your dragon!")
f.DragonName = input("What is your dragon's name?\n")
print("Say hello to "+str(f.DragonName)+", your new dragon!")
input("\n \nPress enter to continue.")
f.space()

#Introduction to type of gameplay (How to Play)
print("\nIn this game you will have to fight many enemy dragons. You can choose to defend, attack or use your special power.")
print("Every dragon has 10 health points at the beginning of each fight and the first one to reach 0 points will lose.")
print("You have 1 attack and 1 defence point at this moment but you can strengthen them by buying items at the market. \n(This will increase your probability of winning a match.)\n")

f.ShowMoney()  #shows money that you currently have

#Going to the market where you can buy stuff to increase attack/defence points
while True:
    yesno = input("Do you want to go to the market now?").lower()
    f.space()
    if yesno in yes:
        print("\n \nYou go to the market with "+str(f.DragonName)+". It is very noisy and packed with people. \nWhile you are looking at an item on sale someone bumps into you.")
        while True:
            eep = input("What do you do?\n a)Argue\n b)Ignore\n c)Ask if the person is okay.")  #Adds story element to game (choice)
            if eep == "a":
                print("The person grumbles, pushes you backwards, and keeps on walking.")  #No reward
                input("\nPress enter to continue.\n")
                f.Market()
                break
            elif eep == "b":
                print("The person keeps on walking and is lost in the crowd.")  #No reward
                input("\nPress enter to continue.\n")
                f.Market()
                f.space()
                break
            elif eep == "c":
                print("The person thanks you kindly and you find out it's none other than Astrid the famous dragon trainer!")  #Reward for being nice
                print("She offers you a dragon energy potion to strengthen your attack by 2 points!\n \n")
                f.PlayerAttack = f.PlayerAttack+2   #2+points for attack
                f.ShowPoints()
                input("\nPress enter to continue.\n")
                f.space()
                f.Market()
                break
            else:
                print("That is not a valid action, please try again.")
        break
    elif yesno in no:
        break
    else:
        print("Please type yes or no.")

f.space()
f.ChooseSpecialPower()  #Choose your special power for battle (gives damage for a certain amount of turns), you cannot change your special power after you have chosen one
f.space()

while True:
    fight = input("Are you ready to start fighting?").lower()
    if fight in yes:
        print("\nGood! The enemy dragons are waiting in their giant dragon nest.\nYou need to reach the centre to fight the dragon leader and stop the evil dragons once and for all!")
        print("You must fight enemy dragons until you reach the centre.")
        time.sleep(2)
        break
    elif fight in no:
        print("\nToo bad. You have to fight. The enemy dragons are waiting in their giant dragon nest.\nYou need to reach the centre to fight the dragon leader and stop the evil dragons once and for all!")
        print("You must fight enemy dragons until you reach the centre.")
        time.sleep(2)
        break
    else:
        print("That isn't an answer.")

f.space()

#Fighting enemy dragon (the fight ends when one dragon reaches 0 health points)
f.Battle(1, 5, 10)
f.battleEnd()

print("\nYou continue your journey through the dragon nest until...")
time.sleep(2)

#Repeats
f.Battle(2, 7, 10)
f.battleEnd()

print("\n"+str(f.DragonName)+" can sense you are nearing the centre of the nest...")
time.sleep(2)

#Repeats
f.Battle(4, 9, 10)
time.sleep(1)
f.reward()
print("You are about to reach the centre of the dragon nest and fight the leader dragon!")
time.sleep(2)
f.ask()

f.Battle(6, 10, 20)  #Last fight (boss battle) with dragon leader (it's health is higher = 20)
