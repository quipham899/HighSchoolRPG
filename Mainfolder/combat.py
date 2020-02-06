import random
import charactercreation

class Combat(object):
    def __init__(self, list):
        self.list = list

    def fight(self):
        health = (self.list[4] + 5) * 100
        playerHealth = self.list[4] * 100
        #Defines player health and enemy health
        Name = ["Chad", "Bully", "Stacy", "Becky", "Brad", "Chadham", "Chang","Bishal","Principle","Teacher", "Hall-Monitor", "Normie"]
        intent = ["Wants to throw hands", "Saw you littering", "Saids you're late for class", "Caught you skipping", "Wants to subjugate you to a drug test!", "Wants to square up."]
        attack = ["Punch", "Kick", "Flee"]
        movements = ["Whalloped", "Ruptured", "Penetrated", "Obliterated", "Smashed", "Masticated", "Tapped"]
        bodyparts = ["Face","Booty","Ribs","Bones","Chest","Knees", "Pelvis", "Groin"]
        comedy = ["Butter your biscuits", "Cream your corn","Debugg your face", "Pound your booty", "Bust your chops"]
        result = ["Die", "Faint", "Bleed-out",]
        #Define lists of responses used for sentence template.
        print(f"A {Name[random.randrange(11)]} {intent[random.randrange(6)]}")
        print("What do you do?")
        #Generates enemy instance
        for i in range(3):
            print(f"{i}.{attack[i]}")
        #While enemy health and your health isn't low then allow combat to happen.
        while health != 0 and playerHealth != 0:
            choice = int(input(">"))
            if(choice == 0) :
                #Roll d5 + your agility, and an enemy's's agility plus three.
                if random.randrange(5) + self.list[2] > self.list[2] + 3 :
                    #Comment what happens to the enemy if your agility is higher, and what happens to you if their agility is higher.
                    print(f"You {movements[random.randrange(5)]} them in the {bodyparts[random.randrange(7)]}")
                    health -= self.list[0] * 100
                else :
                    print(f"They {movements[random.randrange(5)]} you in the {bodyparts[random.randrange(7)]}")
                    playerHealth -= (self.list[0] + 5) * 100
            if(choice == 1):
                if random.randrange(5) + self.list[2] > self.list[2] + 3 :
                    print(f"You {movements[random.randrange(5)]} them in the {bodyparts[random.randrange(7)]}")
                    health -= self.list[0] * 100
                else :
                    print(f"They {movements[random.randrange(5)]} you in the {bodyparts[random.randrange(7)]}")
                    playerHealth -= (self.list[0] + 5) * 100
                    #Prints death for you or your enemy.
            if(health == 0):
                print(f"You've {movements[random.randrange(5)]} the opponent in the {bodyparts[random.randrange(7)]} causing them to DIE!, get out before the authority comes!")
            elif(playerHealth == 0):
                print(f"They've {movements[random.randrange(5)]} you in the {bodyparts[random.randrange(7)]} causing you to DIE!, rest in peace.")
