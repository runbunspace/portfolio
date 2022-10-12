"""
generating a Dungeons and Dragons character
"""
import random

class Character:
    def __init__(self, race):
        print(race, 'created at level 1')
        self.race = race
        self.level = 1
        self.proficiencies = []
        self.languages = ['Common']
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
        self.abilities = abilities
        
    def generate_random(self):
        self.get_race()
        self.get_alignment()
        self.get_abilities()


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

dwarf1 = Dwarf()
dwarf1.dwarf_abilities()
    


