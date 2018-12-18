"""
Created on Thu Aug 16 13:06:56 2018
@author: diego
This Lil Code was created as a joke and learning experience
with Python. It is intended for fun, and not to be used in a 
offensive way of any kind.
Input validation still relies on recursion and shall be updated
on future versions.
"""

def nameInput(name):
    def invalidInput(name):
        """Calls itself over and over
        until arriving at a valid input.
        Use only with nameInput(name)
        fuction."""
        name = name.lower()
        for char in name:
            if char not in validChars:
                print('The name contains an invalid character. Please retry.'+'\n'+'\n')
                name = invalidInput(str(input("Write here the damned name: ")))
        return name
    name = name.lower()
    validChars='abcdefghijklmnopqrstuvwxyz '
    for char in name:
        if char not in validChars:
            print('The name contains an invalid character. Please retry.'+'\n'+'\n')
            name = invalidInput(str(input("Write here the damned name: ")))
            break
    return name

def roastDIS(tempList):
    """
    This function randomly selects an
    insult from the list associated with
    the name character on roastDict{}
    """
    roastRand = random.randint(0, (len(tempList)-1))
    daRoast = str(tempList[roastRand])
    return daRoast.capitalize()

import random
roastDict={
        'a':['abominable', 'absurd', 'asinine', 'ape', 'awful'],
        'b':['banal', 'barren', 'bigot', 'blight', 'bothersome', 'brainless', 'birdbrain', 'bitter', 'bizarre', 'bogus', 'burden', 'busybody'],
        'c':['careless', 'crazy', 'cretin', 'cheap', 'childish', 'corrupt'],
        'd':['daft', 'deadbeat', 'deadweight', 'deceiving', 'demented', 'deleterious', 'delirious', 'delusional', 'degenerate', 'deranged', 'despicable', 'dim', 'dimwitted', 'disgraceful', 'dishonest', 'disgusting', 'dopey', 'dull', 'dumbo', 'dunce'],
        'e':['eejit', 'empty', 'empty-headed', 'execrable'],
        'f':['fake', 'false', 'farcical', 'featherbrained', 'feeble', 'fiend', 'filthy', 'frivolous', 'foolish', 'fopdoodle', 'foul', 'freak'],
        'g':['gobermouch', 'goon', 'goop', 'grisly', 'gross', 'grotesque', 'gruesome'],
        'h':['hag', 'half-witted', 'harebrained', 'heedless', 'heinous', 'hideous', 'horrible', 'horrid'],
        'i':['ignoble', 'imbecilic', 'importunate', 'impotent', 'imprudent', 'incautious', 'incompetent', 'inconsiderate', 'indiscreet', 'inferior', 'irrational', 'irresponsible', 'irritating', 'insane'],
        'j':['joke', 'joshing', 'junkie'],
        'k':['kecker', 'keech', 'kickmaleerie', 'knackering', 'knob'],
        'l':['lame', 'laughable', 'liar', 'litter', 'loathsome', 'loiter-sack', 'loser', 'ludicrous', 'lunatic'],
        'm':['mad', 'malicious', 'malodorous', 'maniac', 'meaningless', 'mental', 'mindless', 'mischievous', 'miserable', 'monotonous', 'moocher', 'moron'],
        'n':['nasty', 'nauseating', 'negligent', 'no-good', 'nonsensical', 'noxious', 'nutty'],
        'o':['oaf', 'oblivious', 'obnoxious', 'obscene', 'odd', 'ordinary', 'outrageous'],
        'p':['parasite', 'pathetic', 'patsy', 'perjurer', 'pernicious', 'pestilent', 'piteous', 'poignant', 'pointless', 'preposterous', 'prick', 'profane', 'puny'],
        'q':['quaint', 'queer', 'questionable', 'quisby'],
        'r':['ragamuffin', 'rat', 'rattlebrained', 'repulsive', 'repugnant', 'ridiculous', 'risible', 'rotten', 'rubbish', 'rude'],
        's':['sad', 'scatterbrained', 'scandalous', 'scourge', 'senseless', 'sickening', 'silly', 'slow', 'sordid', 'spurious', 'stale', 'stupid', 'swine'],
        't':['tedious', 'tiresome', 'trickster', 'trivial', 'trite', 'troublesome'],
        'u':['ugly', 'unbearable', 'unintelligible', 'unpleasant', 'unreasonable', 'unstable', 'unsteady','unthinking', 'unwise'],
        'v':['vague', 'vapid', 'vile', 'vulgar'],
        'w':['wacky', 'waste', 'wastrel', 'weak', 'wearisome', 'weird', 'whelp', 'wretched'],
        'x':['xenophobe'],
        'y':['yaldson', 'yokel', 'yuppie'],
        'z':['zanny', 'zestless'],
        }

#Introduction to the user
print('Greetings and salutations, sir(es) and/or madam(s).', '\n'
      'Welcome to Ye Olde Roaster.', '\n', '\n',
      'Your acquaintance with this humble little program infers that there is a person, ' +
      'or people, previous acquaintances of yours that offended or acted in such manner that ' +
      'there is need to placate the now established grudge among you.', '\n', '\n'
      'No matter.'+'\n'+'\n'
      "Yours is a simple program that shall find your antagonists' flaws very names!"+'\n'+
      'Not only that, it will list these in a organized way, by spelling their names and'+
      ' paring each character with a corresponding flaw.'+'\n'+'\n'
      'You need only to type their names below, one at a time, and the program will justify your righteous '+
      "grudge, spelling to all your foe's true nature."+'\n'+'\n'
      'Plase refrain from typing number and special characters, as they are '+'\n'+
      'not worthy of them.')

nameOutput = nameInput(str(input("Write here the damned name: ")))
spellList = list(nameOutput)
pop_List = []
for a in range(len(spellList)-1):
    if spellList[a] == ' ':
        pop_List.append(a)

popIndex_var = len(pop_List)-1 #This is a variable to use in removing empty spaces on spellList at the correct indexes
while popIndex_var >= 0:
    spellList.pop(int(pop_List[popIndex_var]))
    popIndex_var -= 1

aComma = ", " #Used to join list into string on the line below
print("Your foe's name is spelled as "+str(aComma.join(spellList))+"\n"+"\n")

ROASTED = ''
for b in range(len(spellList)):
    tempList = list(roastDict.get(spellList[b]))
    roastVal = roastDIS(tempList)
    ROASTED = ROASTED + str("The letter " + str(spellList[b]).upper()+
                            " is for " + str(roastVal)+"."+"\n")
print(ROASTED)
