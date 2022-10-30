'''
RIGHT-ALIGNED STAIRCASE of HASHES
'''

height = None
while height is None:
    height = input('choose integer 1-8 for staircare height: ')
    try:
        height = int(height)
        if height >= 1 and height <=8:
            print('ok')
        else:
            print("NOT IN RANGE.")
            height = None
    except:
        print("NOT AN INTEGER.")
        height = None
        
print(f'staircase is {height} steps high')
# print(type(height))

r = 0
while r < height:
    print(' ' * (height - r) + '#' * (r+1))
    r += 1
    
