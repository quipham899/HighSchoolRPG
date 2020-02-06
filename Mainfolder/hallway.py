import random
import charactercreation
import combat
#The lunchroom class allows you to do these things relating to the lunchroom.
class Rooms(object):

    def event(self, list):
        #Function accepts argument and sets it to a attribute called self.list
        self.list = list
        #Has a list of options pre-made.
        sections = ["Sit-down", "Get-Food", "Go to the Teacher", "Exit"]
        print("You've entered the lunch-room, it's loud, busy and bustling as always ...")
        print("The Cafeteria is split up amongst five sections, which one do you want to sit at today?")
        #print the options in sentence template.
        for i in range(4) :
            print(f"{i}.{sections[i]}")
        #Ask user what they want to do then generate combat.
        seat = int(input("What would you like to do? :"))
        if seat in range(4):
            fighting = combat.Combat(self.list)
            fighting.fight()

class Hallway(object):
    #Takes stat argument from Classroom
    def __init__(self, list):
        self.list = list
    #Defines a list of functions and rooms
    rooms = {
            'Lunchroom' : Rooms(),
        }
    #Defines travel mechanism, has list of travel name that correlates to function.
    def Travel(self):
        print(self.list)
        locations = ["Lunchroom", "Math", "CA","Gym","Biology", "History","Bathroom","Exit"]
        for i in range(8):
            print(f"{i}.{locations[i]}")
        #Takes user response and sifts through dictionary for function to run.
        location = int(input("Where would you like to go?"))
        print(locations[location])
        Hallway.rooms.get(locations[location]).event(self.list)
