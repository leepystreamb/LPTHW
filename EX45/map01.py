from sys import exit


record = {}
class Scene(object):
    def enter(self):
        print "None."



class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()



class Death(Scene):
    def enter(self):
        if record['cart1'] == 'Bandit':
            print "The ladies called the conductor on you. You got arrested and went in jail. "
            print "Three days later you saw the death of Duke Marmarlade on newspaper."
            print "You failed."
            exit(1)
        elif record['cart2'] == 'Letter':
            print "The scarred man is a private agent hired by the Duke of Marmalade."
            print "The minute he found out the letter was stolen by you he thought you are the assassin."
            print "He followed you to the control room and killed you with his excellent strangling skill."
            print "You and him both failed to find the assassin. Three days later, the Duke got assassinated."
            print "You failed."
            exit(1)
        elif record['cart2'] == 'Pocket':
            print "'BOOM!''"
            print "The scarred man is a private agent hired by the Duke of Marmalade."
            print "He knew that you touched his letter and probably read it. He suspected you are the assassin."
            print "He followed you to the control room but the assassin found out his identity and shot him."
            print "Him lying on the ground was the last thing you saw before you get your bullet."
            print "You both failed."
            exit(1)
        elif record['cart1'] == 'None' and record['cart2'] == 'None':
            print "There is nothing. You untied the conductor and called the police on radio station."
            print "When the train arrived the next station all the passengers fleed. "
            print "The assassin was never found and escaped."
            print "You wasted all your time on the train."
            print "The next day you found out the Duke is dead. Thanks to you. "
            print "You failed and you are unemployed."
            exit(1)
        elif record['cart1'] == 'Napkin' and record['cart2'] == 'None':
            print "You saw the scarred man. He looked worried."
            print "Both of you untied the conductor and called the police on radio staion."
            print "When you got back cart one with the scarred man, the ladies are gone."
            print "You thanked the scarred man and wanted to continue searching for the assassin."
            print "But before you get up, the assassins, the young couple went to your cart and shot you both."
            print "Turns out the Duke leaked out false information about he would board the same train, under the name Jackson Bone."
            print "You are a decoy for the Duke."
            print "The ladies in your cart told the young couple about you and your name."
            print "They thought you are the Duke."
            print "You failed."
            exit(1)

        elif record['cart2'] == 'Miss':
            print "You saw the assassins, who are the young couple from the dinning cart."
            print "They killed you with a gun."
            print "The Duke leaked out false information about he would board the same train, under the name Jackson Bone."
            print "Once the couple met you they thought you are the Duke."
            print "You fulfilled your purpose for the Duke, and you died."
            print "You could have prevent this if you try another way."
            exit(1)
        else:
            pass


class CartOne(Scene):
    def enter(self):
        print "You are a secret agent with a mission to board a train to prevent the protential assasination of the Duke of Marmalade. "
        print "You need to gather information to find the assassin."
        print "You are now undercover in the name of Jackson Bone. A French silk business man on your way to attend a business meeting. "
        print "You broaded the train and seated yourself in cart one. "
        print "You encountered two ladies in your cart and you want to know if they would be the assassin."
        print """You choose to:
        1. Ask what they are doing in the destination
        2. Greet
        3. Take a nap first
        """
        choice = raw_input("> ")
        while True:
            if choice == "1":
                print "One of the ladies replies 'How rude are you to speak at ladies without introducing youself'"
                print "They refused to talk to you when you tried to make amends. "
                print "You gave up and went to the dinning cart. "
                record['cart1'] = "None"
                return 'cart_two'

            elif choice == '2':
                print "The ladies seem to fond of you and asked what's your name."
                name = raw_input("> ")
                if (('jackson' in name or 'Jackson' in name) or 'JACKSON' in name) and (('bone' in name or 'Bone' in name) or 'BONE' in name):
                    print "You told them you are a businessman called Jackson Bone, and while all of you are having a good time,"
                    print "you spilled some wine on your jacket."
                    print "The ladies offered their handkerchief to you."
                    print "You closely look at the handkerchief and it has a snitching of 'M.'."
                    print "The lady told you to keep the handkerchief and you put it in the breast pocket."
                    print "Then you went to the dinning cart. "
                    record['cart1'] = 'Napkin'
                    return 'cart_two'
                else:
                    print "You told them you are %s. The ladies are shocked" % name
                    print "Unlucky you. It happens that %s is also the name of a escaping bandit." % name
                    record['cart1'] = 'Bandit'
                    return 'death'
            elif choice == '3':
                print "You felt tired and decided to take a nap."
                print "When you woke up the ladies are gone."
                print "You also feel kind of hungry so you went to the dinning cart."
                record['cart1'] = 'None'
                return 'cart_two'
            else:
                print "Please enter the correct numebr"
                choice = raw_input("> ")



class CartTwo(Scene):
    def enter(self):
        print "You are now in the dinning cart to look for the assassin."
        print "You saw there is a man with a scar on his face sitting alone at the back of the cart."
        print "In the cart there is also a young couple who are very silent. "
        print "Who do you want to investigate on?"
        print """
        1. The scarred man
        2. The couple
        3. Ahh... How about lunch first?
        """
        choice = raw_input("> ")
        while True:
            if choice == '1':
                print "You sit down with the scarred man and tried to initiate conversation."
                print "He told you he is a business man from Scotland."
                print "You guys are really getting along and suddenly he excused himself to the toilet"
                print "While you waiting for his return you tried to look through his jacket when no one is watching."
                print "You found a letter but you saw he is on the way to the dinning cart."
                print "You decide to:"
                print """
                1. Put it back
                2. Put it in your jacket
                """
                choice1 = raw_input("> ")
                while True:
                    if choice1 == '1':
                        print "You put the letter back to his jacket and pretend you did nothing."
                        print "He checked his jacket pocket, and had a funny look on his face."
                        print "And you just realised you put it in the wrong side of the pockets."
                        print "He did not say anything and you played along."
                        print "Suddenly, there was a scream from the corridor."
                        print "You immediately ran to where the sound is coming from. "
                        record['cart2'] = 'Pocket'
                        return 'control_room'
                    elif choice1 == '2':
                        print "You put the letter in your jacket and pretend you did nothing."
                        print "He checked his jacket pocket, and he looked really nervous when he could not find it."
                        print "You asked him what is wrong and he said nothing."
                        print "You decided to read the letter so you excused yourself to the toilet."
                        record['cart2'] = 'Letter'
                        return 'toilet'
                    else:
                        print "Please enter the correct number"
                        choice1 = raw_input("> ")

                return 'control_room'
            elif choice == '2':
                print "You seated yourself with the young couple, and started to initiate conversation."
                print "The couple are oddly queit and not responsive at all. They seemed to be annoyed by you."
                print "You opened the briefcase and got the business cards out."
                print "You handed them the card and they suddenly look delighted."
                print "Suddenly, you heard someone screamed, and you ran out the dinning cart to check."
                if record['cart1'] == 'Napkin':
                    record['cart2'] = 'Found'
                else:
                    record['cart2'] = "Miss"
                return 'control_room'
            elif choice == '3':
                print "You ordered some sandwiches and they tasted awful."
                print "Suddenly, someone screamed and you ran out to the corridor to check immediately."
                print "You went towards where the scream was coming from."
                record['cart2'] = 'None'
                return 'control_room'
            else:
                print "Please enter the correct number"
                choice = raw_input("> ")


class Toilet(Scene):
    def enter(self):
        print "You are now in the toilet."
        print "You locked the door and opened the letter, you saw bunch of information about the duke."
        print "You think the scarred man is the assassin and decided to act on it."
        print "Suddenly, you heard a scream coming from the corridor."
        print "You immediately ran out the toilet and head towards where the sound was coming from."
        return 'control_room'

class ControlRoom(Scene):
    def enter(self):
        print "You went to the control room, where the scream was coming from."
        print "But the door is locked, you broke in and saw the conductor was tied up and wounded."
        print "The conductor stared at you with a terrified gaze, you looked behind..."
        if record['cart2'] == 'Found':
            return 'finished'
        else:
            return 'death'

class Finished(Scene):
    def enter(self):
        print "You saw the assassins, who are the young couple from the dinning cart."
        print "They pointed the gun at you."
        print "In just a split second, the scarred man strangled both of them single handedly."
        print "The Duke leaked out false information about he would board the same train, under the name Jackson Bone."
        print "You actually are the decoy for the Duke."
        print "Once the couple met you they thought you are the Duke."
        print "And the scarred man is also a private agent hired by the Duke of Marmalade."
        print "He also thought you are the real Duke because you carried the handkerchief with the initial 'M.'"
        print "The assassins are killed and you are safe."
        print "After the mission you retired. The Duke refused to pay you because you being alive was not part of his plan."
        print "Congratulations! You got the good but sad ending!"
        exit(1)

class Map(object):

    scenes = {
    'cart_one': CartOne(),
    'cart_two': CartTwo(),
    'control_room': ControlRoom(),
    'toilet':Toilet(),
    'death': Death(),
    'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)
