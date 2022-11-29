'''
Create a script to determine validity of credit card numbers.
American Express uses 15-digit numbers, MasterCard uses 16-digit numbers, and Visa uses 13- and 16-digit numbers. 
All American Express numbers start with 34 or 37. 
All Visa numbers start with 4.
Most MasterCard numbers start with 51, 52, 53, 54, or 55. 
Credit card numbers also have a “checksum” built into them: a mathematical relationship between at least one number and others. 
That checksum enables computers to detect typos (e.g., transpositions), if not fraudulent numbers, without having to query a database, which can be slow. 
One could certainly craft a fake number that nonetheless respects the mathematical constraint, so a database is still necessary for more rigorous checks.
Most cards use an algorithm invented by Hans Peter Luhn of IBM. 
According to Luhn’s algorithm, you can determine if a credit card number is (syntactically) valid as follows:
1. Multiply every other digit by 2, starting with the number’s second-to-last digit, and then add those products’ digits together.
2. Add the sum to the sum of the digits that weren’t multiplied by 2.
3. If the total’s last digit is 0 (or, put more formally, if the total modulo 10 is congruent to 0), the number is valid!
'''
