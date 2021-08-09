

#Author: Jared Stormer
#War Game (D-Day) is a simple text based game with a scoring system and events that are picked at random.
#Results of a choice event are not randomised, yet...
#The score starts from 5 then goes up to 100 (100 wins the game).
#If the score goes down to 0, the player loses.
#Each event/ card gives/ takes away 5 points.
#Currently there aren't many events, it gets repetitive.



import random


score = 5


def EndW():
    #Wins game.
    print ("You won? You did get off the beach and got to the town, but this is only the beginning for you.")
    int2 = input ("Restart? Press Y then Enter or close the window:  ")
    if int2 == "Y":        
        global score
        score -= 95
        Main()
        
def EndL():
    #Loses game.
    print ("You have died and done you're country proud.")
    int2 = input ("Restart? Press Y then Enter or close the window:  ")
    if int2 == "Y":        
        global score
        score += 5
        Main()


def Town():
    print ("You've made it past the sea wall, now you run towards the nearest town.")
    for x in range(50):
        #Loops 50 times, the score will decide who lives and who dies, muhahahaha!
        Choices = ["a","b","c","d","e"]
        B1 = random.choice(Choices)
        print ("----------------------------------------")
        print (B1)
        if score >= 100:
            EndW()
            return
        elif score == 0:                     
            EndL()
            return
        elif B1 == "a":
            print ("Noticing a group of allies, you run with them.", SCp())

        elif B1 == "b":
            int3 = input ("You find a motorcycle, do you take it(y), or continue sneaking through?(n):  ")
            if int3 == "y":
                print ("You fire it up, only to have the Germans take notice and start firing.", SCn())
            elif int3 == "n":
                print ("You leave it and move ahead, as silently as possible.", SCp())

        elif B1 == "c":
            int4 = input ("You find a dead German, do you take his uniform(y), or keep moving?(n):")
            if int4 == "y":
                print ("You take the uniform and put it in your pack for later use.", SCp())
            if int4 == "n":
                print ("Later on you really wished you had the uniform to blend in.", SCn())

        elif B1 == "d":
            print ("You get graised buy a bullet.", SCn())
        elif B1 == "e":
            print ("You hop onto a moving truck, making progress.", SCp())

        
def Boxes():
    print ("You've made it to the sea wall, with some luck you might avenge your brothers' deaths.")
    for x in range(50):
        #Loops 50 times, the score will decide who lives and who dies, muhahahaha!
        Choices = ["a","b","c","d","e"]
        B1 = random.choice(Choices)
        print ("----------------------------------------")
        print (B1)
        if score >= 75:
            Town()
            return
        elif score == 0:                     
            EndL()
            return
        elif B1 == "a":
            print ("Noticing a pill box straight ahead, you are able to avoid machine gun fire", SCp())

        elif B1 == "b":
            int3 = input ("You sneak up, just under a pill box, do you take it out(y), or continue sneaking by?(n):  ")
            if int3 == "y":
                print ("You find a German machine gun outside the entrance, unwatched, you use it to kill the enemy.", SCp())
            elif int3 == "n":
                print ("You succesfully sneak past, but ten in your squad get killed.", SCn())

        elif B1 == "c":
            int4 = input ("You continue moving, knowing that you were walking like a drunk earlier, do you keep doing it(y), or run strait?(n):")
            if int4 == "y":
                print ("While looking comical, you move ahead without injury.", SCp())
            if int4 == "n":
                print ("You run strait ahead and get hit multiple times, luckily none are lethal.", SCn())

        elif B1 == "d":
            print ("You get graised buy a bullet.", SCn())
        elif B1 == "e":
            print ("You hop onto a moving truck, making progress.", SCp())

def Beach():
    print ("You've survived long enough to leave the beach front, there's still lots of sand to traverse though.")
    for x in range(50):
        #Loops 50 times, the score will decide who lives and who dies, muhahahaha!
        Choices = ["a","b","c","d","e"]
        B1 = random.choice(Choices)
        print ("----------------------------------------")
        print (B1)
        if score >= 50:
            Boxes()
            return
        elif score == 0:                     
            EndL()
            return
        elif B1 == "a":
            print ("Still feeling sick from the voyage, your staggering moves are beneficial.", SCp())

        elif B1 == "b":
            int3 = input ("You see an abandoned truck, do you use it(y), or leave it?(n):  ")
            if int3 == "y":
                print ("Luckily for you, the truck works, allowing you to make progress.", SCp())
            elif int3 == "n":
                print ("Unfortunately you stopped to think about it and got hit by shrapnel.", SCn())

        elif B1 == "c":
            int4 = input ("You see a barrier that could provide protection, do you use it(y), or run ahead?(n):")
            if int4 == "y":
                print ("The barrier is a burning tank, luckily it doesn't explode, giving you time to breathe.", SCp())
            if int4 == "n":
                print ("You run ahead and your legs cramp up, leaving you exposed.", SCn())

        elif B1 == "d":
            print ("You get graised buy a bullet.", SCn())
        elif B1 == "e":
            print ("You hop onto a moving truck, making progress.", SCp())

def Boat():
    print ("Your first step is to get off the landing craft.")
    for x in range(50):
        #Loops 50 times, the score will decide who lives and who dies, muhahahaha!
        Choices = ["a","b","c","d","e"]
        B1 = random.choice(Choices)
        print ("----------------------------------------")
        print (B1)
        if score >= 25:
            Beach()
            return
        elif score == 0:                     
            EndL()
            return
        elif B1 == "a":
            print ("You stumble in the water, sickened by the voyage, the Germans can't hit you.", SCp())

        elif B1 == "b":
            int3 = input ("You see an abandoned Jeep, do you use it(y), or leave it?(n):  ")
            if int3 == "y":
                print ("Luckily for you, the Jeep works, allowing you to make progress.", SCp())
            elif int3 == "n":
                print ("Unfortunately you stopped to think about it and got hit by shrapnel.", SCn())

        elif B1 == "c":
            int4 = input ("You see a barrier that could provide protection, do you use it(y), or run ahead?(n):")
            if int4 == "y":
                print ("The barrier is a bag of chicken feed, you get burned when the bag ignights.", SCn())
            if int4 == "n":
                print ("You run ahead, spotting a moving tank, you run behind it for cover and make progress", SCp())

        elif B1 == "d":
            print ("You trip and roll your ankle.", SCn())
        elif B1 == "e":
            print ("You used a barricade as a shield.", SCp())


   
def Score():
    #Prints score when requested.
    print (score) 
    


def SCp():
    #Adds to scoreboard.
    global score
    score += 5    
    print ("^", score)
    
        
    
def SCn():
    #Subtracks from scoreboard.
    global score
    score -= 5
    print ("\/", score)


def Main():
    print ("***----------------------------------------***")
    print ("Hello, Welcome to War Game (D-Day)!")
    print ("This is a text based game using rng and events to progress.")
    print ("You need to get 25 points for each stage to progress.")
    input ("Press enter to start:   " )
    
    Boat()
Main()
