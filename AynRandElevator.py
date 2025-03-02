# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 01:35:17 2021

@author: mjkoenig
Based on the game "Trapped in an Elevator with Ayn Rand" by Oliver Darkshire
"""
import random

debate=0
desperation=0
violence=0
roll1=0
roll2=0

while True:
    special_rule=str(input("Do you continue to speak with Rand (yes or no)? "))
    if special_rule=="yes":
        roll1=random.randint(1,6)
        roll2=random.randint(1,6)
        if roll1 <= 3:
            if roll2==1:
                print("'This is the fault of the bolsheviks!' Debate goes up!")
                debate+=1
            if roll2==2:
                print("'Are elevators communist? Only a communist would seize up like this!' Debate goes up!")
                debate+=1
            if roll2==3:
                print("'The concept of down is anti-progress and small minded. True capitalists ever always move up!' Desperation increases.")
                desperation+=1
            if roll2==4:
                print("'If you have enough money, you can fly!' violence increases...")
                violence+=1
            if roll2==5:
                print("'This elevator is private property and therefore can NOT kill me, an individual.' Debate and violence increases...")
                debate+=1
                violence+=1
            if roll2==6:
                print("'Gravity has been co-opted by the state as part of a Communist conspiracy to Socialize Mars.' Desperation and Debate increase.")
                debate+=1
                desperation+=1
        if roll1 > 3:
            if roll2==1:
                print("'My novel is really a philosophy, actually, which is in a way a novel.' Desperation increases.")
                desperation+=1
            if roll2==2:
                print("'Many stores sell furniture like the kind I have in my home.' Violence increases...")
                violence+=1
            if roll2==3:
                print("'I just really hate homosexuals.' Violence and Debate go up...")
                violence+=1
                debate+=1
            if roll2==4:
                print("'You can tell a hero because he's attractive; unlike villains who are ugly.' Desperation and debate go up!")
                desperation+=1
                debate+=1
            if roll2==5:
                print("'When I die, make a massive dollar sign wreath out of flowers for me.' Desperation goes up.")
                desperation+=1
            if roll2==6:
                print("'If we must run out of food, I would eat you.' Violence increases.")
                violence+=1
    if special_rule=="no":
        print("I CAN'T TAKE IT ANYMORE!!!!!!!")
        roll1=random.randint(1,6)
        roll2=random.randint(1,6)
        debate+=(roll1+roll2)
        print(f"Your daring act of giving up adds {roll1+roll2} to your debate score!")
        if debate>=10:
            print("You've won! ---GAME OVER---")
        if debate<10:
            print("Rand cackles at your pathetic socialist corpse. ---GAME OVER---")
        break
    if debate==10 or violence==10 or desperation==10:
        break
if debate==10:
    print("You successfully debate Ayn Rand into jumping down the elevator shaft, but as she descends into the inky abyss you hear the sound of bat wings unfurling from her dessicated husk of a body. ---GAME OVER(?)---")
if desperation==10:
    print("You hear the elevator shout about how it can't take it anymore before it willingly unhooks itself from the cables. You all die in a smashed heap.---GAME OVER---")
if violence==10:
    print("RAND MUST ANSWER FOR HER SINS")
    roll1=random.randint(1,6)
    if roll1==1:
        print("You shoot Rand, she seems unsurprised. ---GAME OVER---")
    if roll1==2:
        print("Ayn Rand snatches the gun from you and fires, killing you.  She tells you that it's nothing personal, but you know it's a lie.")
    if roll1>2:
        print("You struggle until the gun goes off and the bullet somehow hits you both. Ayn Rand is furious as she dies- sharing a bullet is unthinkable!")
        
