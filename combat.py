import random
import Interactions
import CharacterCreation

class Combat(object):
    def __init__(self, list):
        self.list = list

    def fight(self):
        health = (self.list[4] + 5) * 100
        playerHealth = self.list[4] * 100
        Name = ["Chad", "Bully", "Stacy", "Becky", "Brad", "Chadham", "Chang","Bishal","Principle","Teacher", "Hall-Monitor"]
        intent = ["Wants to throw hands", "Saw you littering", "Saids you're late for class", "Caught you skipping", "Wants to subjugate you to a drug test!", "Wants to square up."]
        attack = ["Punch", "Kick", "Flee"]
        movements = ["Whalloped", "Ruptured", "Penetrated", "Obliterated", "Smashed", "Masticated", "Tapped"]
        bodyparts = ["Face","Booty","Ribs","Bones","Chest","Knees", "Pelvis"]
        comedy = ["Butter your biscuits", "Cream your corn","Debugg your face", "Pound your booty", "Bust your chops"]
        print(f"The{Name[random.randrange(10)]} {intent[random.randrange(5)]}")
        print("What do you do?")
        for i in range(3):
            print(f"{i}.{attack[i]}")
        while health != 0:

            choice = int(input(" "))
            if(choice == 0) :
                if random.randrange(5) + self.list[2] > self.list[2] + 3 :
                    print(f"You {movements[random.randrange(5)]} them in the {bodyparts[random.randrange(5)]}")
                    health -= self.list[0] * 100
                else :
                    print(f"They {movements[random.randrange(5)]} you in the {bodyparts[random.randrange(5)]}")
                    playerHealth -= (self.list[0] + 5) * 100
            if(choice == 1):
                if random.randrange(5) + self.list[2] > self.list[2] + 3 :
                    print(f"You {movements[random.randrange(5)]} them in the {bodyparts[random.randrange(5)]}")
                    health -= self.list[0] * 100
                else :
                    print(f"They {movements[random.randrange(5)]} you in the {bodyparts[random.randrange(5)]}")
                    playerHealth -= (self.list[0] + 5) * 100
