'''
GREEDY ALGORITHMS: CHANGE
find the lowest total coins to give correct change
'''

''' take an input from 1-100, as change owed in cents '''
change = None
while change is None:
    change = input('choose change amount, in cents, from 1-100: ')
    try:
        change = int(change)
        if change >= 1 and change <=100:
            print('ok')
        else:
            print("NOT IN RANGE.")
            change = None
    except:
        print("CENTS MUST BE A WHOLE NUMBER.")
        change = None
        
# print(type(change))
print(f'{change} cents in change')
print('calculating coin totals')

''' 
subtract coin values, going largest to smallest
tally totals for each type of coin 
tally total number of coins
'''
TC = 0
Q = 0
D = 0
N = 0
P = 0
while change > 0:
    temp = change - 25
    if temp >= 0:
        Q += 1
        TC += 1
        change = temp
        # print(f'quarters:{Q}, total coins:{TC}, change:{change}')
    else: 
        temp = change - 10
        if temp >= 0:
            D += 1
            TC += 1
            change = temp
            # print(f'dimes:{D}, total coins:{TC}, change:{change}')
        else: 
            temp = change - 5
            if temp >= 0:
                N += 1
                TC += 1
                change = temp
                # print(f'nickels:{N}, total coins:{TC}, change:{change}')
            else:
                temp = change - 1
                P += 1
                TC += 1
                change = temp
                # print(f'pennies:{P}, total coins:{TC}, change:{change}')
               
'''
print a statement of how many of each coin to give as change
'''
print(f'please give {Q} quarters, {D} dimes, {N} nickels, {P} pennies.')
print(f'total number of coins is {TC}')
