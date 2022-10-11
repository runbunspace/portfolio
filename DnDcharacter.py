"""
generating a Dungeons and Dragons character
"""
import random

class Character:
    def __init__(self, name, level=1):
        self.name = name
        self.level = level
        self.proficiencies = []
        self.languages = []
        self.traits = []
    
    def get_race(self):
        """ generates random character race and associated traits """
        races = {1: 'dwarf', 2: 'elf', 3: 'halfling', 4: 'human', 5: 'gnome'}
        x = random.randint(1,5)
        self.race = races[x]
        
    def get_alignment(self):
        """ generates random alignment """
        alignment_ethics = {1: 'lawful', 2: 'neutral', 3: 'chaotic'}
        ethics = random.randint(1,3)
        ethics = alignment_ethics[ethics]
        alignment_morals = {1: 'good', 2: 'neutral', 3: 'evil'}
        morals = random.randint(1,3)
        morals = alignment_morals[morals]
        self.alignment = ethics + ' ' + morals
        
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
        
    def generate_random(self):
        self.get_race()
        print(self.name + "'s race is:", self.race, '\n')
        self.get_alignment()
        print(self.name + "'s alignment is:", self.alignment, '\n')
        self.get_abilities()
        print(self.name + "'s ability stats are:", abilities, '\n')

Siggy = Character('Sigrid')
Siggy.generate_random()

class Dwarf(Character):
    def __init__(self):
        self.race = 'dwarf'
        self.size = 'medium'
        self.speed = 25
        self.proficiencies.append('battleaxe', 'light hammer', 'warhammer', 'stonecunning')
        self.languages.append('Common', 'Dwarvish')
        self.traits.append('darkvision')
    
    def dwarf_abilities(self):
        self.get_abilities()
        abilities['constitution'] += 2
        a = input('what is your dwarven subrace? enter 1 for hill, 2 for mountain')
        if a == 1:
            self.subrace = 'hill'
            abilities['wisdom'] += 1
        elif a == 2:
            self.subrace = 'mountain'
            abilities['strength'] += 2
    


