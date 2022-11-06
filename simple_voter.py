'''
* voting function *
1. max number of candidates will be 10
2. take inputs of candidate names, limit 10
3. take an input of number of voters
4. for each voter, take an input of a name as their vote
5. check if vote name matches a candidate name, and if so, add a tally to the candidate
6. if vote name does not match any candidate, print 'invalid selection'
7. identify and print the name(s) of the candidate(s) with the most votes
'''

class simple_voter:
    def get_candidates(self):
        candidates = {}
        for i in range(10):
            name = {input(f'candidate #{i+1}: '): 0}
            candidates.update(name)
            if i == 9: break
            if i == 0: continue
            j = input('press y to add another candidate: ')
            if j == 'y': continue
            else: break
        self.candidates = candidates
    
    def get_voters(self):
        voters = None
        while voters == None:
            voters = input('how many voters? ')
            try:
                voters = int(voters)
                if voters > 0: 
                    print(f'there are {voters} voters')
                else: 
                    print('voters must be greater than zero')
                    voters = None
            except:
                print('voters must be a whole number')
                voters = None
        self.voters = voters
    
    def get_votes(self):
        for i in range(self.voters):
            vote = input(f'vote #{i+1}: ')
            match = False
            for key in self.candidates:
                if key == vote:
                    self.candidates[key] += 1
                    match = True
            if match == False:
                print('invalid selection')
        print(self.candidates)

    def get_winner(self):
        most_votes = 0
        for key in self.candidates:
            if self.candidates[key] > most_votes:
                most_votes = self.candidates[key]
        print('winner(s):')
        for key in self.candidates:
            if self.candidates[key] == most_votes:
                print(key)

    def election_day(self):    
        self.get_candidates()
        self.get_voters()
        self.get_votes()
        self.get_winner()

test = simple_voter()
test.election_day()

