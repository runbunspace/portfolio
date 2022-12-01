'''
TIDEMAN ELECTION
https://cs50.harvard.edu/x/2022/psets/3/tideman/
get_candidates(): 
    gets no. of candidates and candidate names from user
    stores candidate names in list
get_votes():
    gets no. of voters from user
    gets voter ranks for each candidate from user
    vote_tracker dict. is used to prevent rank duplication from voters
    ranks dict. stores ranks for each candidate
compare():
    creates pairs, a dictionary of all candidate pairs
    pairs contains nested dicts. to tally voter preferences 
    lock dict. records winner/loser of each pair and winner's margin
    pair winner(s) with largest margin are locked first
    subsequent pair winners are locked according to margin, as long as the loser of the pair is not one of the winners locked in 1st round
    once locked pairs are determined, origin candidates are determined to be those in locked pairs who are undefeated
    origin candidate(s) is/are the overall winner(s)
'''

def get_pos_int(item):
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

candidates = []
def get_candidates():
    can_count = get_pos_int('candidates')
    for i in range(can_count):
        can = None
        while can is None:
            can = input(f'Candidate #{i+1}: ')
            if can in candidates:
                print('no duplicates')
                can = None
            else:
                candidates.append(can)

ranks = {}
vote_tracker = {}
def get_votes():
    voter_count = get_pos_int('voters')
    for v in range(voter_count):
        vote_tracker[f'V{v+1}'] = []
    for i in range(len(candidates)):
        print(f'Candidate {candidates[i]}:')
        temp_ranks = []
        for j in range(voter_count):
            rank = None
            while rank is None:
                rank = input(f'Voter #{j+1} rank: ')
                try: 
                    rank = int(rank)
                    if rank < 1 or rank > len(candidates):
                        print(f'rank 1 to {len(candidates)}')
                        rank = None
                    else:
                        if rank in vote_tracker[f'V{j+1}']:
                            print('rank already assigned')
                            rank = None
                        else:
                            temp_ranks.append(rank)
                            vote_tracker[f'V{j+1}'].append(rank)
                except ValueError:
                    print(f'must be integer from 1 to {len(candidates)}')
                    rank = None
        ranks[f'{candidates[i]}'] = temp_ranks
        print(vote_tracker)

def compare():
    pairs = {}
    lock = {}
    c = candidates
    temp = 1
    for i in range(len(c)-1):
        for j in range(len(c)):
            if j <= i:
                continue
            pairs[f'P{temp}'] = {c[i]: 0, c[j]: 0}
            lock[f'{c[i]}/{c[j]}'] = {'win': 0, 'loss': 0, 'margin': 0, 'locked': False}
            for r in range(len(vote_tracker)):
                ican = ranks[c[i]]
                jcan = ranks[c[j]]
                if ican[r] < jcan[r]:
                    pairs[f'P{temp}'][c[i]] += 1
                else:
                    pairs[f'P{temp}'][c[j]] += 1
            if pairs[f'P{temp}'][c[i]] > pairs[f'P{temp}'][c[j]]:
                lock[f'{c[i]}/{c[j]}']['win'] = c[i]
                lock[f'{c[i]}/{c[j]}']['loss'] = c[j]
                lock[f'{c[i]}/{c[j]}']['margin'] = pairs[f'P{temp}'][c[i]]
            else:
                lock[f'{c[i]}/{c[j]}']['win'] = c[j]
                lock[f'{c[i]}/{c[j]}']['loss'] = c[i]
                lock[f'{c[i]}/{c[j]}']['margin'] = pairs[f'P{temp}'][c[j]]
            temp += 1
    print(pairs)
    print(lock)
    source = []
    margins = []
    for key in lock:
        if lock[key]['margin'] not in margins: 
            margins.append(lock[key]['margin'])
    margins = sorted(margins, reverse = True)
    print(margins)
    for key in lock:
        if lock[key]['margin'] == margins[0]:
            lock[key]['locked'] = True
            if lock[key]['win'] not in source:
                source.append(lock[key]['win'])
    for key in lock:
        for i in range(1, len(margins)):
            if lock[key]['margin'] == margins[i]:
                if lock[key]['loss'] not in source:
                    lock[key]['locked'] = True
    for key in lock:
        for i in range(len(margins)):
            if lock[key]['margin'] == margins[i]:
                if lock[key]['locked'] == True:
                    w = lock[key]['win']
                    l = lock[key]["loss"]
                    print(f'{w}>{l} locked')
        
    print(f'Total winners: {len(source)}')
    for s in source:
        print(s)
    

get_candidates()
print(candidates)

get_votes()
print(ranks)

compare()

                
            




