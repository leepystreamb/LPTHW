items = []
itemlist = ['Apple', 'Arrows', 'Bow', 'Bread', 'Eggs', 'Shield', 'Sword']

def start_game():
    print "What's your name?"
    global name
    name = raw_input('> ')
    print "Hello,", name +". How old are you?"
    global age
    age = raw_input('> ')
    if age.isdigit() == True:
        print "OK! Let's get started!"
        intro()
    else:
        print "Hey, typing a number isn't that hard."
        print "How old are you again?"
        age = raw_input('> ')
        if age.isdigit() == True:
            print "OK! Let's get started!"
            intro()
        else:
            end_game("I think you are too dumb for this game,")

def intro():
    print """
    The Village is being attacked by the dragon!
    The great hero of the village, %s, is awaken by the panic.

    %s, here's the stuff you can find in your house:
    """ % (name, name)
    print "*********************"
    for i in range (0,7):
        print i+1, itemlist[i]
    print "*********************"
    print "You bag has capacity for 3 items. Choose wisely."
    print "Type in the number to choose."
    while True:
        choice1 = raw_input('> ')
        if choice1.isdigit():
            item1 = int(choice1)
            if item1 > 0 and item1 < 8:
                items.append(itemlist[item1-1])
                print "Now you have %s. You still have two slots in your bag." % items
                while True:
                    choice2 = raw_input('> ')
                    if choice2.isdigit():
                        item2 = int(choice2)
                        if item2 > 0 and item2< 8:
                            if item2 != item1:
                                items.append(itemlist[item2-1])
                                print "Now you have %s, You have only one slot left."% items
                                print "%s, make your last choice counts!" % name
                                while True:
                                    choice3 = raw_input('> ')
                                    if choice3.isdigit():
                                        item3 = int(choice3)
                                        if item3 > 0 and item3<8:
                                            if item3 != item1 and item3 != item2:
                                                items.append(itemlist[item3-1])
                                                print "Now you've got %s, you are good to go!" % items
                                                items.sort()
                                                level1()
                                            else:
                                                print "I don't know if you know this by now, you don't have two of these."
                                                end_game("Good luck trying to find that in your house,")
                                    else:
                                        end_game("Seriously, %s. You are making my job as a narrator difficult, or check your number lock and start again,")
                            else:
                                end_game("Dumbass, you can't choose the same thing twice.")
                        else:
                            print "You did it once and you can do it twice, how come you can't count all the sudden?"
                            end_game("%s, I think you better stay at home so you don't die.") % name
            else:
                print "Hey %s, can you count? There's only 7 things here." % name
        else:
            print "%s, just a friendly reminder: You should learn to type what I told you to from now on, or you will see the consequences."


def level1():
    global money
    print "================================================================================="
    print "On the way to fight the dragon, you saw a old lady in the marketplace."
    print "You told her to leave as it would be dangerous to stay outside."
    print "Turns out she hasn't done grocery for the week yet and have nothing to make dinner."
    if ('Apple' in items) or ('Bread' in items) or ('Eggs' in items):
        print """You have some food in your bag, do you want give it to her?
        1. Sure
        2. Hell no
        Press the number to act.
        """
        choice = raw_input('> ')
        if '1' in choice:
            if 'Apple' in items:
                print "You offered her an apple as that's the first thing you found, she gladly took it and paid you $5."
                items.remove('Apple')
                money = 5
                print "You continue your journey with $%d in your pocket." % money
                level2()
            elif 'Bread' in items:
                print "You offered her a loaf of bread as that's the first thing you found, she gladly took it and paid you $10."
                items.remove('Bread')
                money = 10
                print "You continue your journeywith $%d in your pocket." % money
                level2()
            else:
                print "You offered her some eggs as that's the first thing you found."
                print "She looked unsatisfied cause they looked odd, but she still took it and paid you $5."
                items.remove('Eggs')
                money = 5
                print "You continue your journey with $%d in your pocket." % money
                level2()
        elif '2' in choice:
            print "Hey %s, that was mean." % name
            print "But you kept on going as you hearing the sound of a crying old lady fades away."
            money = 0
            level2()
        else:
            end_game("Follow the instruction so you don't have to replay the game over and over again.")

    else:
        print "You can't convince her to leave so you continue your journey."
        money = 0
        level2()


def level2():
    global money
    print "================================================================================="
    print "You stopped by the armour shop to see if you can buy something useful."
    print """
    $$$$$$$ Menu $$$$$$$
     - Helmet
    $$$$$$$$$$$$$$$$$$$$
    """
    print """Do you want to buy a helmet?
        1. Ya!
        2. Nah.
    """
    choice = raw_input('> ')
    if '1' in choice:
        if money < 10:
            print "It costs $10, but you only have $%s." % money
            if ("Arrows" in items) or ("Bow" in items) or ("Sword" in items) or ("Shield" in items):
                print "But you can trade your weapon to get the helmet."
                print """
                Take the deal?
                1. Yes
                2. No"""
                choice1 = raw_input('> ')
                if '1' in choice1:
                    if 'Arrows' in items:
                        items.remove('Arrows')
                        items.append('Helmet')
                        print "You traded the first thing you see in bag. Arrows are gone."
                        print "You left the store with a helmet"
                        level3()
                    elif 'Bow' in items:
                        items.remove('Bow')
                        items.append('Helmet')
                        print "You traded the first thing you see in bag. Bow is gone."
                        print "You left the store with a helmet"
                        level3()
                    elif 'Sword' in items:
                        items.remove('Sword')
                        items.append('Helmet')
                        print "You traded the first thing you see in bag. Sword is gone."
                        print "You left the store with a helmet"
                        level3()
                    else:
                        items.remove('Shield')
                        items.append('Helmet')
                        print "You traded the first thing you see in bag. Shield is gone."
                        print "You left the store with a helmet"
                        level3()
                elif '2' in chioce1:
                    print "You left the store and continue your journey."
                    leve3()
                else:
                    print "Learn to follow instruction and type a goddamn number next time."
            else:
                print "Well, you stopped wasting your time here and continue."
                level3()
        elif money == 10:
            print "It costs $10, do you want to spend the money?"
            print """
            1. Yes
            2. I love my money
            """
            choice2 = raw_input('> ')
            if '1' in choice2:
                money = money - 10
                items.append('Helmet')
                print "You bought the Helmet and left the store."
                level3()
            elif '2' in choice2:
                print "Alrihgt, keep your money and get going now."
                level3()
            else:
                end_game("Please just type a number next time, %s.") % name

    elif '2' in choice:
        print "You left the store and kept on going."
        level3()
    else:
        end_game("Can you just learn how to just type a number? You are making my life difficult.")

def level3():
    print "================================================================================="
    print "When you arrived the dragon is sleeping and you tried to quietly approch it."
    if 'Eggs' and 'Helmet' in items:
        print "Who would've thought of bringing eggs? The dragon woke up as you approach it."
        print "She saw the eggs in your bag and thought that you brought her lost children back."
        print "She thanked you by giving you a pat on the head. Luckily you have a helmet on."
        print "She flied away. Villagers all chant '%s! %s! %s!'." % (name, name, name)
        print "At the age of %s, %s's legend passes on." % (age, name)
        print "%s left the village with glory, as the eggs might never hatch." % name
        end_game("You got the good ending.")
    elif 'Eggs' in items:
        print "Who would've thought of bringing eggs? The dragon woke up as you approach it."
        print "She saw the eggs in your bag and thought that you brought her lost children back."
        print "She thanked you by giving you a pat on the head. It was a strong pat."
        print "Your fragile human skull cannot take the pat and you died."
        end_game("You got the unlucky ending.")
    elif 'Arrows' or 'Bow' or 'Sword' or 'Shield' in items:
        if 'Arrows' in items:
            print "You pulled out arrows to attack the dragon. Tis but a scratch."
            print "You woke the dragon and it killed you mercilessly."
            end_game("You got the bad ending.")
        elif 'Bow' in items:
            print "You pulled out the bow to attack the dragon. Tis but a scratch."
            print "You woke the dragon and it killed you mercilessly."
            end_game("You got the bad ending.")
        elif 'Sword' in items:
            print "You pulled out the Sword to attack the dragon. Tis but a scratch."
            print "You woke the dragon and it killed you mercilessly."
            end_game("You got the bad ending.")
        else:
            print "You pulled out the Shield to attack the dragon. It was stupid."
            print "You woke the dragon and it killed you mercilessly."
            end_game("You got the bad ending.")
    else:
        print "You only got some food in your bag. You are thinking:"
        print '"Oh shiiiiiiiiiiiit."'
        print "You know it is a losing battle so you fleed."
        print "%s, at the age of %s, retired from the hero profession and left the village with shame." % (name, age)
        end_game("You got the sad ending.")


def end_game(reason):
    print reason, "bye!"
    exit(0)

start_game()
