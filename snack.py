"""
Simple calorie counter:
1: takes multiple input pairs from user of food and calories
2: converts calories to integer value and stores the inputs as 'food': calories in a dictionary
3: prints a list of foods and the total sum of calories
"""

snack = {}
x = 1
while x == 1:
    a = input('food name: ')
    b = input('calories: ')
    snack[a] = int(b)
    c = input('press y to add more, press enter to finish: ')
    if c == 'y': print('snack so far:', snack, '\n')
    else:
        total_calories = 0
        foods = []
        for key in snack:
            total_calories += snack[key]
            foods.append(key)
        print('your snack of', foods, 'has', total_calories, 'calories')
        x = 0
