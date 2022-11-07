'''
survey function
'''

class simple_survey:
    def __init__(self, quest_no, *ops):
        '''
        take input to create survey question and options 
        '''
        question = {f'question {quest_no}': input('survey question: ')}
        options = {}
        for o in ops:
            options.update({o: input(f'option {o}: ')})
        question.update(options)
        self.question = question
        self.options = options
        #print(self.options)
    
    def get_answers(self):
        '''
        create a dictionary to store no. of responses for each option
        '''
        answers = {}
        for key in self.options:
            answers.update({key: 0})
        self.answers = answers
    
    def get_responses(self):
        '''
        take input of how many responses were given
        '''
        responses = None
        while responses == None:
            responses = input('how many responses? ')
            try:
                responses = int(responses)
                if responses > 0: 
                    print(f'ok')
                else: 
                    print('responses must be greater than zero')
                    responses = None
            except:
                print('responses must be a whole number')
                responses = None
        self.responses = responses
    
    def get_response(self):
        '''
        enter responses and add to tally for each option
        '''
        for i in range(self.responses):
            response = input(f'response #{i+1}: ')
            match = False
            for key in self.answers:
                if key == response:
                    self.answers[key] += 1
                    match = True
            if match == False:
                print('invalid selection')

    def get_tally(self):
        '''
        sort options by highest number of responses
        '''
        for k, v in self.question.items():
            print(f'{k}: {v}')
        rank = {k: v for k, v in sorted(self.answers.items(), key=lambda item: item[1], reverse = True)}
        self.rank = rank
        print(rank)
        most_responses = 0
        for key in self.answers:
            if self.answers[key] > most_responses:
                most_responses = self.answers[key]
        print('top response(s):')
        for key in self.answers:
            if self.answers[key] == most_responses:
                print(key)

    def run_survey(self):    
        self.get_answers()
        self.get_responses()
        self.get_response()
        self.get_tally()

test = simple_survey(1, 'A', 'B', 'C')
test.run_survey()

