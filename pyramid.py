'''
PYRAMID of HASHES
'''

height = None
while height is None:
    height = input('choose integer 1-8 for pyramid height: ')
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
        
print(f'pyramid is {height} rows high')
# print(type(height))

r = 0
while r < height:
    print(' ' * (height - r) + '#' * (r+1) + '  ' + '#' * (r+1))
    r += 1
