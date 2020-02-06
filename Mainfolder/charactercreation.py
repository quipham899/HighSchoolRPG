import hallway
import random

class Creation(object):
    def __init__(self):
        self.stat = []
    def stats(self):
        #Gets input from user for stats
        words = ["Strength", "Intelligence", "Agility","Looks", "Endurance",]
        print("You're late? On the first day? Just sign the papers and go to class okay? Stop bothering me. ")
        print("The Nurse hands you a clipboard with a stack of papers, that were hastily clipped together.")
        print("The first question? What's your name")
        name = input('>')
        newPoint = 40
        #Ask for the stats.
        for i in range(5):
            print(f"How much {words[i]} do you have?, you have {newPoint} to distribute")
            stat = int(input(">"))
            #Checks the input to make sure the input is less than 35 and to make sure the point-pool is not 0.
            if(stat != newPoint and newPoint != 0):
                self.stat.append(stat)
                newPoint = newPoint - stat
            #Checks if the point pool is exhausted and if all the points have been filled out.
            elif(newPoint == 0 and i == 5):
                hallway.Hallway(self.stat).Travel()
            else:
                #If not then do not append to arrays.
                print("That's not a valid amount of points!")
                #While it's on the last stat and you haven't used up your points, it asks you to fill out all your points.
            while(i == 4 and newPoint != 0):
                print(f"You still {newPoint} point's left, you need to use up all your points!'")
                print(f"Choose which stats, you'd like to give your points too.")
                for x in range(5):
                    print(f"{x}.{words[x]}")
                choice = int(input("Which stat to alter: "))
                amount = int(input("How much do you want to put into the point? "))
                #If it's a valid number then add it to the array.
                if amount <= newPoint and newPoint != 0:
                    self.stat[choice] = self.stat[choice] + amount
                    newPoint = newPoint - amount
                    print(newPoint)
                elif(amount > newPoint or newPoint == 0) :
                    print("That's not a valid amount of point try again!")
                else:
                #if there is no more points to insert send you to the Hallway.
                    print("Thank you for being a dear, and following basic instructions. That can't be said for a lot of the students here, now off you go.")
                    hallway.Hallway(self.stat).Travel()
        print("Thank you for being a dear, and following basic instructions. That can't be said for a lot of the students here, now off you go.")
        hallway.Hallway(self.stat).Travel()
