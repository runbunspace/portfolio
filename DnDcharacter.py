"""
generating a Dungeons and Dragons character
"""
import random

class Character:
    def __init__(self, name, level=1):
        self.name = name
        self.level = level
    
    def get_race(self):
        """ generates random character race """
        races = {1: 'dwarf', 2: 'elf', 3: 'halfling', 4: 'human', 5: 'gnome'}
        x = random.randint(1,5)
        self.race = races[x]
        print(self.name + "'s race is:", self.race, '\n')
        
    
    def get_alignment(self):
        """ generates random alignment """
        alignment_ethics = {1: 'lawful', 2: 'neutral', 3: 'chaotic'}
        ethics = random.randint(1,3)
        ethics = alignment_ethics[ethics]
        alignment_morals = {1: 'good', 2: 'neutral', 3: 'evil'}
        morals = random.randint(1,3)
        morals = alignment_morals[morals]
        self.alignment = ethics + ' ' + morals
        print(self.name + "'s alignment is:", self.alignment, '\n')
        

    def get_abilities(self):
        """ generates random ability scores """
        abilities = {'strength': 1, 'dexterity': 1, 'constitution': 1, 'intelligence': 1, 'wisdom': 1, 'charisma': 1}
        for key in abilities:
            n = 1
            temp = []
            while n <=4:
                x = random.randint(1, 6)
                temp.append(x)
                n += 1
            temp.sort(reverse=True)
            del temp[-1]
            num = 0
            for n in temp:
                num += n
            abilities[key] = num
        print(self.name + "'s ability stats are:", abilities, '\n')
    
    def generate_random(self):
        self.get_race()
        self.get_alignment()
        self.get_abilities()

Siggy = Character('Sigrid')
Siggy.generate_random()


