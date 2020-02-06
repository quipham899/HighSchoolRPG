import Hallway
import random

class Creation(object):
    def __init__(self):
        self.stat = []
    def stats(self):
        words = ["Strength", "Intelligence", "Agility","Looks", "Endurance",]
        print("You're late? On the first day? Just sign the papers and go to class okay? Stop bothering me. ")
        print("The Nurse hands you a clipboard with a stack of papers, that were hastily clipped together.")
        print("The first question? What's your name")
        name = input('>')
        newPoint = 40
        for i in range(5):
            print(f"How much {words[i]} do you have?")
            stat = int(input(">"))
            if(stat < 35 and newPoint - stat >= 0):
                self.stat.append(stat)
                newPoint = newPoint - stat
                print(f"You have this many point you have left: {newPoint}.'")
            else:
                print("That's not a valid amount of points!")
            while(i == 4 and newPoint != 0):
                print(f"You still {newPoint} point's left, you need to use up all your points!'")
                print(f"Choose which stats, you'd like to give your points too.")
                for x in range(5):
                    print(f"{x}.{words[x]}")
                choice = int(input("Which stat to alter: "))
                amount = int(input("How much do you want to put into the point? "))
                if int(choice) <= newPoint and newPoint != 0:
                    self.stat[choice] = int(self.stat[choice]) + amount
                    newPoint = newPoint - amount
                    print(newPoint)
                else:
                    print("Thank you for being a dear, and following basic instructions. That can't be said for a lot of the students here, now off you go.")
                    Hallway.Hallway(self.stat).Travel()
        print("Thank you for being a dear, and following basic instructions. That can't be said for a lot of the students here, now off you go.")
        Hallway.Hallway(self.stat).Travel()
