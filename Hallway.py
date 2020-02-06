import random
import CharacterCreation

class Rooms(object):
    def event(self):
        sections = ["Sit-down", "Get-Food", "Go to the Teacher", "Exit"]
        print("You've entered the lunch-room, it's loud, busy and bustling as always ...")
        print("The Cafeteria is split up amongst five sections, which one do you want to sit at today?")
        for i in range(4) :
            print(f"{i}.{sections[i]}")
        seat = input("What would you like to do? :")


class Hallway(object):
    def __init__(self, list):
        self.list = list
    rooms = {
            'Lunchroom' : Rooms(),
        }

    def Travel(self):
        print(self.list)
        print(CharacterCreation.Creation().stat)
        locations = ["Lunchroom", "Math", "CA","Gym","Biology", "History","Bathroom","Exit"]
        for i in range(8):
            print(f"{i}.{locations[i]}")
        location = int(input("Where would you like to go?"))
        print(locations[location])
        Hallway.rooms.get(locations[location]).event()
        fighting = CharacterCreation.Creation()
        fighting.fight()
