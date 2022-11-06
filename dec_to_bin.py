'''
* convert decimal to binary *
1. take an integer as input
2. divide by 2, store the remainder in a list
3. divide the quotient from previous step by 2, store the remainder
4. continue dividing by 2 and storing remainder until quotient is 1
5. store 1 as final entry in list
6. reverse the list to get binary value
7. convert list to string for nice output
8. if decimal integer is negative, print '-' in front of output
9. else print output of binary number
'''
import math as m

DEC = None
while DEC is None:
    DEC = input('choose an integer to convert to binary: ')
    try: 
        DEC = int(DEC)
        print('ok')
    except: 
        print('NOT AN INTEGER')
        DEC = None

if DEC == 0: print('binary of 0 is 0')
else:
    BIN = []        
    q = abs(m.trunc(DEC/2))
    r = abs(DEC%2)
    while q != 1:
        BIN.append(r)
        r = q%2
        q = m.trunc(q/2)
    BIN.append(r)
    BIN.append(1)
    BIN.reverse()
    bin = int(''.join(str(x) for x in BIN))
    print(f'{DEC} in binary is: ')
    if DEC < 0: print(-bin)
    else: print(bin)

