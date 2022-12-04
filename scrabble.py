'''
SCRABBLE
Scrabble class initializes:
    play, a dictionary to store a word and a score for each player
    points, a dictionary of Scrabble letter scores as keys, and a corresponding list of letters for each possible score
player_input():
    takes an input from the user of the number of players
    takes an input from the user of a word for each player
    creates a dictionary key for each player in the play dictionary
    creates a nested dictionary for each player key which stores the player's inputted word and a score, initially set to zero
score():
    loops through every character of each player's word and adds a character score to the player's total score in the play dictionary
    compares all scores in the play dictionary and determines highest score
    stores all players who achieved the highest score to a list, winners
winner():
    prints a declaration of a singular winner, or multiple tied winners
'''

class Scrabble:
    def __init__(self):
        self.play = {}
        self.points = {
            1: ['a', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't', 'u'], 
            2: ['d', 'g'], 
            3: ['b', 'c', 'm', 'p'], 
            4: ['f', 'h', 'v', 'w', 'y'], 
            5: ['k'], 
            8: ['j', 'x'], 
            10: ['q', 'z']}
    
    def player_input(self):
        player_count = self.get_pos_int('players')
        for i in range(player_count):
            temp = input(f'Player {i+1} word: ')
            self.play[f'Player {i+1}'] = {'word': temp.lower(), 'score': 0}
            
    def score(self):
        for key in self.points:
            for player in self.play:
                for char in self.play[player]['word']:
                    if char in self.points[key]:
                        self.play[player]['score'] += key
        high_score = 0
        self.winners = []
        for player in self.play:
            if self.play[player]['score'] > high_score:
                high_score = self.play[player]['score']
        for player in self.play:
            if self.play[player]['score'] == high_score:
                self.winners.append(player)
        for player in self.play:
            print(f'{player} score: {self.play[player]["score"]}')
    
    def winner(self):
        if len(self.winners) == 1:
            print(f'Winner is {self.winners[0]}!')
        else:
            print('Tie between: ', end = "")
            for w in self.winners:
                print(f'{w} ', end = "")
            print('!')
    
    def play_game(self):
        self.player_input()
        self.score()
        self.winner()
            
    def get_pos_int(self, item):
        ''' get input of only a positive integer '''
        pos_int = None
        while pos_int == None:
            pos_int = input(f'how many {item}? ')
            try:
                pos_int = int(pos_int)
                if pos_int > 0:
                    return(pos_int)
                else: 
                    print('must be greater than zero')
                    pos_int = None
            except:
                print('must be a whole number')
                pos_int = None

test = Scrabble()
test.play_game()



                    
