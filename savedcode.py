def __init__(self,arguments):
    self.name = arguments
def occurence(self):
    name = {
    'Anna' : Anna()
    }
    person = Events.occurence.name.get(self.name)
    person.conversation()

class Anna(object):
relationship = 0
encounter = 0
name = 0
health = CharacterCreation.self.stat[4] * 100
HitPoints = CharacterCreation.Creation().self.stat[0]
Gender = 'Female'
def conversation() :
    if encounter == 0:
        print("A girl bumps into you ... she's an african american girl with a large black afro.")
        print("She's a plump girl with a large round face, her eyes are very large and gives off an innocent aura. ")
        print("Her nose is very large, and her forehead is very broad.")
        print("OH! I'm sorry for bumping into you!")
        print("1.That's okay, don't worry about it.")
        print("2.HEY WATCH, WHERE YOU'RE GOING YOUNG BUL.")
        print("3.Punch her in the face.")
        print("4.Say nothing and walk away.")
        choices = int(input(" "))
        if choices == 1 :
            print("Thanks, my name is Anna by the way nice to meet you!")
            print("1.Nice to meet you.")
            print("2.What class you got next Anna?")
            print("3.Anna that's a nice name[flirt]")
            print("4.Gotta run now see you later.")
            answerChoice1 = int(input(" "))
            if answerChoice1 == 1 :
                print("Man Mr.Fitzgerald for this class is tough, I can't event be late or else he'll report me.")
                print("1.Dude that sounds terrible. It'd suck to be in that class --oh wait, I think I have him.")
                print("2.I wouldn't know this is my first year here.")
                print("3.Well at least you aren't gonna be late.")
                answerChoice1Sub1 = int(input(" "))
                if answerChoice1Sub1 == 1 :
                        print("HAH! Good luck ... errr what's your name?")
                        print(f"1.My name is {characterCreation.stats.name}")
                        print("2.I'd rather not say [Edgy].")
                        print("3.Shouldn't you get going?")
                        FinalChoice = int(input(" "))
                        if FinalChoice == 1 :
                            print(f"Alright ... {characterCreation.stats.name} .. I'll remember that. I have to leave now though, see you.")
                            relationship += 3
                            name += 1
                            encounter += 1
                        elif FinalChoice == 2 :
                            print("Okay ... suit yourself. I have to go now ...")
                            relationship -= 3
                            encounter += 1
                        elif FinalChoice == 3:
                            print("Shit you're right!")
                            relationship -= 3
                            encounter += 1
                elif answerChoice1Sub1 == 2 :
                        print("Oh sweet the school hasn't gotten to you yet. Enjoy it while you can, lol.")
                        print("Now I have to go see you around.")
                elif answerChoice1Sub1 == 3 :
                        print("Yeah but I'm about to be ... anyways I gotta go see you around.")
                elif answerChoice1 == 2 :
                        print("History class with Mr.Fitzgerald.")
                        print("1.Dude that sounds terrible. It'd suck to be in that class --oh wait, I think I have him.")
                        print("2.I don't know that name to be honest.")
                        print("3.Hope you aren't late.")
                answerChoice1Sub1 = int(input(" "))
                if answerChoice1Sub1 == 1 :
                        print("HAH! Good luck ... errr what's your name?")
                        print(f"1.My name is {characterCreation.stats.name}")
                        print("2.I'd rather not say [Edgy].")
                        print("3.Shouldn't you get going?")
                        FinalChoice = int(input(" "))
                        if FinalChoice == 1 :
                            print(f"Alright ... {characterCreation.stats.name} .. I'll remember that. I have to leave now though, see you.")
                            relationship += 3
                            name += 1
                            encounter += 1
                        elif FinalChoice == 2 :
                            print("Okay ... suit yourself. I have to go now ...")
                            relationship -= 3
                            encounter += 1
                        elif FinalChoice == 3:
                            print("Shit you're right!")
                            relationship -= 3
                            encounter += 1
                elif answerChoice1Sub1 == 2 :
                        print("Must be your first year here, well welcome to Casper High.")
                        print("Now I have to go see you around.")
                elif answerChoice1Sub1 == 3 :
                        print("I hope I'm not either .. see you around.")
        elif answerChoice1 == 3 :
                if(random.randrange(4)+ characterCreation.self.stat[3] > 20) :
                    print("She smiles at you with a shining look in her eyes though this was only for a moment.")
                    print("She turns away from you and strokes her hair, and then she would turn back to you.")
                    print("She takes out a small piece of paper, and a pen writing the number down and handing it to you.")
                    print("She walks away from you smiling.")
                    relationship += 10
                else :
                    print("Uhmm ... thank you for being interested but ... I have to go.")
                    print("She walks away from you hastily.")
                    relationship -= 10
        if(choices == 3) :
            fight = combat.Combat(health,hitPoints)
            fight.fight()
