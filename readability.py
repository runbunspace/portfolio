'''
READABILITY
take input of a string of text from the user
determine the number of letters in the string
determine the number of words in the string
determine the number of sentences in the string
determine reading grade level of the text using the Coleman-Liau index:
    L = number of letters per 100 words
    S = number of sentences per 100 words
    index = 0.0588 * L - 0.296 * S - 15.8
'''

class reading_grade:
    def __init__(self):
        text = input('Text: ')
        self.text = text.lower()
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.punctuation = ['.', '!', '?']
    
    def get_letters(self):
        self.letter_count = 0
        for char in self.text:
            if char in self.letters:
                self.letter_count += 1
    
    def get_words(self):
        word_list = self.text.split()
        self.word_count = len(word_list)
    
    def get_sentences(self):
        self.sentence_count = 0
        for char in self.text:
            if char in self.punctuation:
                self.sentence_count += 1
    
    def calculate_index(self):
        L = (self.letter_count / self.word_count) * 100
        S = (self.sentence_count / self.word_count) * 100
        index = (0.0588 * L) - (0.296 * S) - 15.8
        self.index = int(round(index))
    
    def result(self):
        self.get_letters()
        self.get_words()
        self.get_sentences()
        self.calculate_index()
        if self.index < 1:
            print('Before Grade 1')
        elif self.index >= 16:
            print('Grade 16+')
        else:
            print(f'Grade {self.index}')

test = reading_grade()
test.result()


