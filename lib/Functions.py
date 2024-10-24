import random
import time

yes = ('yes', 'y', 'okay', 'yup')
no = ('no', 'nope', 'n')

money = 500
DragonName = ""

#Enemy points
EnemyHealth = 0
EnemyDefence = 0
EnemyAttack = 0
EnemySpecial = ''
EnemySpecialDamage = 0
EnemySpecialTime = 0
EnemySpecialCount = 0

#Player points
PlayerHealth = 10
PlayerDefence = 1
PlayerAttack = 1
PlayerSpecial = ''
PlayerSpecialDamage = 0
PlayerSpecialTime = 0
PlayerSpecialCount = 0

UserAction = ''
EnemyAction = ''

#Dictionary use for special power time and damage + market item cost and strength
SpecialPowersName = {'i': 'Ice',
                     'f': 'Fire',
                     's': 'Storm',
                     'a': 'Acid',
                     'e': 'Electricity'}
SpecialPowersTime = {'Ice': 6,
                     'Fire': 3,
                     'Storm': 2,
                     'Acid': 5,
                     'Electricity': 2}
SpecialPowersDamage = {'Ice': 1,
                       'Fire': 2,
                       'Storm': 3,
                       'Acid': 1,
                       'Electricity': 4}

DefenseItemStrength = {'Iron Armour': 3,
                       'Distracting Jewels': 2,
                       '"How to defend yourself 101"': 1,
                       'Invisibility potion': 4,
                       'Super Shield': 5}
DefenseItemCost = {'Iron Armour': 300,
                   'Distracting Jewels': 200,
                   '"How to defend yourself 101"': 100,
                   'Invisibility potion': 400,
                   'Super Shield': 600}
AttackItemStrength = {'Claw Sharpener': 1,
                      'Super energy potion': 3,
                      '"Breathing fire 101"': 4,
                      'Wing spikes': 2,
                      'Iron teeth': 5}
AttackItemCost = {'Claw Sharpener': 100,
                  'Super energy potion': 300,
                  '"Breathing fire 101"': 400,
                  'Wing spikes': 200,
                  'Iron teeth': 600}

def space():
    print("----------------------------------------------")

def ShowMoney():
    print("You currently have "+str(money)+" gold bits.")  #Shows the money you have

def ShowPoints():  #Shows the points you have
    print("You have "+str(PlayerAttack)+" ATTACK points.")
    print("You have "+str(PlayerDefence)+" DEFENCE points.")

def ShowItems():   #Shows the items for sale at the market with cost and points for attack or defence
    for key in DefenseItemCost:
        print(key)
        print(str(DefenseItemStrength[key])+" points for DEFENCE.")
        print("Price:"+str(DefenseItemCost[key])+"\n")
    for key in AttackItemCost:
        print(key)
        print(str(AttackItemStrength[key])+" points for ATTACK.")
        print("Price:"+str(AttackItemCost[key])+"\n")

def Market():
    global money, PlayerAttack, PlayerDefence
    print("\nThese are the available items at the market:")
    print("Remember you will have the opportunity to go to the market again.")
    print("When you win a battle you can collect gold bits to then spend at the market.\n")
    time.sleep(5)
    ShowItems()
    ShowMoney()
    ShowPoints()
    AorD = ""
    while AorD != "EXIT":
        AorD = input("\nDo you want to buy an ATTACK(a) item or a DEFEND(d) item? (If you wish to leave type EXIT. To see the item menu type MENU.)").upper()  #asks if you want to buy an attck or defend item
        if AorD == "A":
            BuyItem(AttackItemCost, AttackItemStrength, AorD)  #if you want to buy an attack item, it sets the values of BuyItem to (AttackItemCost, AttackItemStrength, AorD) so it will only look for items in the AttackItem dictionaries
        elif AorD == "D":
            BuyItem(DefenseItemCost, DefenseItemStrength, AorD)  #if you want to buy a defence item, it sets the values of BuyItem to (DefenseItemCost, DefenseItemStrength, AorD) so it will only look for items in the DefenseItem dictionaries
        elif AorD == "MENU":
            ShowItems()
        elif AorD != "EXIT":
            print("This is not an answer.")

def BuyItem(ItemCost, ItemStrength, AorD):  #Buying an item
    global PlayerAttack, PlayerDefence, money, DefenseItemStrength, DefenseItemCost, AttackItemStrength, AttackItemCost
    itemName = input("Type the item here.>").upper()  #Player types item they want to buy
    validkey = False
    for key in ItemCost:
        if itemName == key.upper():
            validkey = True
            if ItemCost[key] > money:  #Checking if player has enough money
                print("You do not have enough money to buy this item.")
            else:
                confirm = ""
                while confirm not in yes and confirm not in no:
                    confirm = input("Are you sure you want to buy "+str(key)+" for "+str(ItemCost[key])+"?").lower() #Confirming if player wants to buy that item
                    if confirm in yes:
                        space()
                        print("\nYou have bought "+str(key))
                        money = money - ItemCost[key]
                        if AorD == "A":
                            PlayerAttack = PlayerAttack + ItemStrength[key]
                        else:
                            PlayerDefence = PlayerDefence + ItemStrength[key]
                        ShowPoints()
                        ShowMoney()
                        del ItemStrength[key]  #Deleting item from market so you can't buy an item more than once
                        del ItemCost[key]
                        return
                    elif confirm not in no:
                        print("That is not an answer.")
    if validkey == False:
        print("This is not an item")


def reward():  #When you win a battle you get a reward
    global PlayerAttack, PlayerDefence, PlayerHealth, money
    print("You have gained 1 point and 200 gold bits!\nYou can give your point to either your attack or your defence to increase its strength. ")
    money = money + 200  #You gain 200 gold bits
    PlayerHealth = 10  #Reset playerHealth to 10
    ShowPoints()
    while True:
        award = input("Do you want to award your point to attack(a) or defence(d)?")  #You can assign the point you have gained to attack or defence
        if award == "a":
            PlayerAttack = PlayerAttack + 1
            ShowPoints()
            ShowMoney()
            break
        elif award == "d":
            PlayerDefence = PlayerDefence + 1
            ShowPoints()
            ShowMoney()
            break
        else:
            print("This is not an answer.")

def ask():   #asking if you want to fight or go to the market
    while True:
        answer = input("Do you want to go to the market(m) or continue fighting(f)?")
        if answer == "m":
            Market()
        elif answer == "f":
            return
        else:
            print("This is not an answer.")

def battleEnd():
    time.sleep(1)
    reward()  #If you win, you win one point(which can be given to attack or defence) and 200 gold bits
    time.sleep(1)
    ask()  #Asks if you want to continue fightng or go to the market first

def ChooseSpecialPower():  #Choose which special power you want from the ones in the dictionary (on top)
    global PlayerSpecial, PlayerSpecialTime, PlayerSpecialDamage
    print("\nIn addition to being able to attack and defend your dragon is able to use ONE Special Power.")
    print("This Special Power can only be used when an enemy is defending, but it's effect can carry on for more turns.")
    print("If an enemy attacks while you use your special power you will recieve damage as your dragon is caught off guard while building up energy for the power.\n")
    for key in SpecialPowersDamage:
        print(str(key)+" delivers "+str(SpecialPowersDamage[key])+" damage for "+str(SpecialPowersTime[key])+" turns.")
    while True:
        answer = input("\nChoose your special power: Ice(i), Fire(f), Storm(s), Acid(a), or Electricity(e).").lower()
        if answer in SpecialPowersName:
            name = SpecialPowersName[answer]
            PlayerSpecial = name
            PlayerSpecialDamage = SpecialPowersDamage[name]
            PlayerSpecialTime = SpecialPowersTime[name]
            print("\n"+DragonName+"'s special power is "+str(PlayerSpecial)+".")
            break
        else:
            print("This is not a valid answer. Please try again.")


def CreateEnemy(w, y, h):  #Creates an enemy dragon
    global PlayerHealth, PlayerSpecialCount, EnemyHealth, EnemyDefence, EnemyAttack, EnemySpecial, EnemySpecialDamage, EnemySpecialTime, EnemySpecialCount
    EnemyHealth = h  #Sets health back to 10 for player and enemy
    PlayerHealth = 10
    EnemySpecialCount = 0  #Sets count for 0 so special powers used in last battle will not affect player
    PlayerSpecialCount = 0
    EnemyDefence = random.randint(w, y) #randomized attack+defence within a certain range
    EnemyAttack = random.randint(w, y)
    value = random.randint(0, 4)
    Powers = ('Ice', 'Fire', 'Storm', 'Acid', 'Electricity')
    EnemySpecial = Powers[value]
    EnemySpecialDamage = SpecialPowersDamage[Powers[value]]
    EnemySpecialTime = SpecialPowersTime[Powers[value]]
    print("\n \nYou have encountered an enemy dragon!")
    print("Its Health is: "+str(EnemyHealth))  #Shows the enemy's and player's stats
    print("Its Attack is: "+str(EnemyAttack))
    print("Its Defence is: "+str(EnemyDefence))
    print("Its Special Power is: "+str(EnemySpecial)+". It delivers "+str(EnemySpecialDamage)+" damage for "+str(EnemySpecialTime)+" turns. \n")
    print("Your Health is: "+str(PlayerHealth))
    print("Your Attack is: "+str(PlayerAttack))
    print("Your Defence is: "+str(PlayerDefence))
    print("Your dragon's Special Power is: "+str(PlayerSpecial)+". It delivers "+str(PlayerSpecialDamage)+" damage for "+str(PlayerSpecialTime)+" turns.")

def EnemyIsAlive(): #Checks if the enemy is still alive
    if EnemyHealth > 0:
        return True
    else:
        return False

def PlayerIsAlive():  #Checks if player is still alive
    if PlayerHealth > 0:
        return True
    else:
        return False

def GetUserAction():  #Asks what player will want to do (attack, defend, or use special power)
    global UserAction
    while True:
        space()
        action = input("\nDo you want to Attack('a'), Defend('d') or use your Special Power('p')?")
        if action == "a":
            UserAction = 'attack'
            return
        elif action == "d":
            UserAction = 'defend'
            return
        elif action == "p":
            UserAction = 'special power'
            return
        else:
            print("Please enter a valid action.")

def GetEnemyAction():  #Randomizes enemy action
    global EnemyAction
    action2 = random.randint(0,2)
    if action2 == 1:
        EnemyAction = 'attack'
    elif action2 == 0:
        EnemyAction = 'defend'
    else:
        EnemyAction = 'special power'

def ShowHealth(): #Shows enemy's and player's health
    print("Your health is: "+str(PlayerHealth))
    print("The enemy's health is: "+str(EnemyHealth))

def PlayerDamage():
    global PlayerHealth
    damage = EnemyAttack-PlayerDefence
    PlayerHealth = PlayerHealth-damage

def Fight():
    global UserAction, EnemyAction, EnemyHealth, PlayerHealth, PlayerSpecial, PlayerSpecialTime, PlayerSpecialCount, EnemySpecial, EnemySpecialTime, EnemySpecialCount
    if PlayerSpecialCount > 0:  #Checks if special power is affecting player or enemy and takes away health if it is
        print("\nYour Special Power is still affecting the enemy.")
        EnemyHealth = EnemyHealth - PlayerSpecialDamage
        print("The enemy's health is now: "+str(EnemyHealth))
        PlayerSpecialCount = PlayerSpecialCount - 1
    elif EnemySpecialCount > 0:
        print("\nThe enemy's Special Power is still affecting your dragon.")
        PlayerHealth = PlayerHealth - EnemySpecialDamage
        print("Your health is now: "+str(PlayerHealth))
        EnemySpecialCount=EnemySpecialCount-1
    else:
        EnemySpecialCount = 0
        PlayerSpecialCount = 0
    print("\nYour action is: "+UserAction)
    print("The Enemy's action is: "+EnemyAction)

    #Various concequences of different combinations of actions
    if UserAction == 'defend' and EnemyAction == 'defend':
        print("You both defend. Nothing happens.")

    elif UserAction == 'defend' and EnemyAction == 'attack' and EnemyAttack > PlayerDefence:
        damage = EnemyAttack - PlayerDefence
        PlayerHealth = PlayerHealth - damage
        print("Your defence was too weak... you receive "+str(damage)+" damage.")

    elif UserAction == 'defend' and EnemyAction == 'attack' and EnemyAttack <= PlayerDefence:
        print("The enemy's attack is weak. Your dragon manages to defend it without difficulty!")

    elif UserAction == 'attack' and EnemyAction == 'attack':
        print("Both dragons attack. You both receive damage.")
        PlayerHealth = PlayerHealth - EnemyAttack
        EnemyHealth = EnemyHealth - PlayerAttack
        print("The enemy dragon receives "+str(PlayerAttack)+" damage.")
        print("Your dragon receives "+str(EnemyAttack)+" damage.")

    elif UserAction == 'attack' and EnemyAction == 'defend' and PlayerAttack > EnemyDefence:
        enemydamage2 = PlayerAttack - EnemyDefence
        EnemyHealth = EnemyHealth - enemydamage2
        print("Your dragon's attack was very effective! The enemy's defence was too weak.")
        print("The enemy dragon receives "+str(enemydamage2)+" damage.")

    elif UserAction == 'attack' and EnemyAction == 'defend' and PlayerAttack <= EnemyDefence:
        print("Your dragon's attack was too weak. The enemy dragon defends it easily.")

    elif UserAction == 'special power' and EnemyAction == 'special power':
        print("Both dragons use their special power at the same time. This neutralizes both powers so no dragon recieves demage.")

    elif UserAction == 'special power' and EnemyAction == 'defend':
        print("Your dragon uses "+str(PlayerSpecial)+" on the enemy and it is very effective! \n The enemy dragon will recieve "+str(PlayerSpecialDamage)+" damage for "+str(PlayerSpecialTime)+" turns")
        PlayerSpecialCount = PlayerSpecialTime - 1
        EnemyHealth = EnemyHealth - PlayerSpecialDamage

    elif UserAction == 'special power' and EnemyAction == 'attack':
        print("The enemy's attack was too quick! Your dragon was caught off guard while building up energy for it's special power.")
        PlayerHealth = PlayerHealth - EnemyAttack

    elif UserAction == 'defend' and EnemyAction == 'special power':
        print("The enemy dragon uses "+str(EnemySpecial)+" on your dragon! You recieve "+str(EnemySpecialDamage)+" damage for "+str(EnemySpecialTime)+" turns.")
        EnemySpecialCount = EnemySpecialTime-1
        PlayerHealth = PlayerHealth - EnemySpecialDamage

    elif UserAction == 'attack' and EnemyAction == 'special power':
        print("Your attack was too quick for the enemy! It was caught off guard while building up energy for its special power.")
        EnemyHealth = EnemyHealth - PlayerAttack

    ShowHealth()

def Battle(min, max, health):  #Joins all of the functions to make a battle
    CreateEnemy(min, max, health)
    while EnemyIsAlive() and PlayerIsAlive():
        GetUserAction()
        GetEnemyAction()
        Fight()
    if PlayerIsAlive():
        print("\n \nCongratulations! You have defeated the dragon!\n")
    else:
        print("\n \nYou Lost...Better luck next time.")
        print("\nGAME OVER")
        exit()
