import random
import Interactions
import CharacterCreation
class Combat(object) :
    def fight(self):
        Name = ["Chad", "Bully", "Stacy", "Becky", "Brad", "Chadham", "Chang","Bishal","Principle","Teacher", "Hall-Monitor"]
        intent = ["Wants to throw hands", "Saw you littering", "Saids you're late for class", "Caught you skipping", "Wants to subjugate you to a drug test!", "Wants to square up."]
        attack = ["Punch", "Kick", "Flee", "Use-inventory"]
        movements = ["Whalloped", "Ruptured", "Penetrated", "Thrusted", "Smashed", "Masticated"]
        bodyparts = ["Face","Booty","Ribs","Bones","Chest","Knees", "Pelvis"]
        comedy = ["Butter your biscuits", "Cream your corn","Debugg your face", "Pound your booty", "Bust your chops"]
        print(f"The{Name[random.randrange(10)]} {intent[random.randrange(5)]}")
