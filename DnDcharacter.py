# need to add class type/specials
# need to define stat adjstments based on race/class type/specials

"""
DnD character generator:
instance = character_gen() 
--> creates an instance of the class, sets character level to 1

instance.gen()
--> generates a dictionary of attributes with random values
example dictionary: 
{'name': 'Lael Brightbuckle', 'race': 'elf', 'level': 1, 'alignment': 'neutral evil', 
'strength': 8, 'dexterity': 8, 'constitution': 14, 'intelligence': 5, 'wisdom': 13, 'charisma': 12}
"""

import random

class character_gen:
    def __init__(self):
        level = {'level': 1}
        self.level = level

    def get_name(self):
        """ generates character name """
        first_names = {1: 'Helja', 2: 'Ilde', 3: 'Birael', 4: 'Thea', 
                       5: 'Milo', 6: 'Lael', 7: 'Marci', 8: 'Wrenn', 
                       9: 'Lorill', 10: 'Amaun'}
        first = random.randint(1,10)
        first = first_names[first]
        last_names = {1: 'Toruun', 2: 'Manbroek', 3: 'Naldo', 4: 'Brushfellow', 
                      5: 'Highthorne', 6: 'Navarro', 7: 'Faircloak', 8: 'Garreck', 
                      9: 'Brightbuckle', 10: 'Saluzir'}
        last = random.randint(1,10)
        last = last_names[last]
        name = {'name': first + ' ' + last}
        self.name = name

    def get_race(self):
        """ generates random character race and associated traits """
        races = {1: 'dwarf', 2: 'elf', 3: 'halfling', 4: 'human', 5: 'gnome'}
        x = random.randint(1,5)
        race = {'race': races[x]}
        self.race = race
        
    def get_alignment(self):
        """ generates random alignment """
        alignment_ethics = {1: 'lawful', 2: 'neutral', 3: 'chaotic'}
        ethics = random.randint(1,3)
        ethics = alignment_ethics[ethics]
        alignment_morals = {1: 'good', 2: 'neutral', 3: 'evil'}
        morals = random.randint(1,3)
        morals = alignment_morals[morals]
        alignment = {'alignment': ethics + ' ' + morals}
        if alignment = 'neutral neutral': alignment = 'true neutral'
        self.alignment = alignment
        
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
        self.abilities = abilities
    
    def gen(self):
        self.get_name()
        self.get_race()
        self.get_alignment()
        self.get_abilities()
        stats = {}
        stats.update(self.name)
        stats.update(self.race)
        stats.update(self.level)
        stats.update(self.alignment)
        stats.update(self.abilities)
        self.stats = stats



player1 = character_gen()
player1.gen()

# this section under construction
class Dwarf(Character):
    def __init__(self):
        super().__init__('dwarf')
        self.size = 'medium'
        self.speed = 25
        self.proficiencies.extend(['battleaxe', 'light hammer', 'warhammer', 'stonecunning'])
        self.languages.append('Dwarvish')
        self.traits.append('darkvision')
        self.subrace = input('enter subrace -- hill or mountain: ')
        while self.subrace != 'hill' and self.subrace != 'mountain':
            print('invalid entry')
            self.subrace = input('enter subrace -- hill or mountain: ')
        if self.subrace == 'mountain':
            self.proficiencies.extend(['light armor', 'medium armor'])
            print('the brawn of mountain dwarves grants proficiency with light and medium armor')
        
    
    def dwarf_abilities(self):
        self.get_abilities()
        print('generating ability scores...')
        print(self.abilities)
        self.abilities['constitution'] += 2
        print('your dwarven hardiness grants +2 to your constitution')
        if self.subrace == 'hill':
            self.abilities['wisdom'] += 1
            print('the deep intuition of hill dwarves grants +1 to your wisdom')
        elif self.subrace == 'mountain':
            self.abilities['strength'] += 2
            print('the brawn of mountain dwarves grants +2 to your strength')
        print('abilities are:', self.abilities)

    


