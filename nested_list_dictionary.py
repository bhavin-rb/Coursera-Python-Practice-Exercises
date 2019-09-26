# Question - The variable nested contains a nested list. Assign ‘snake’ to the variable output using indexing.

nested = [['dog', 'cat', 'horse'], ['frog', 'turtle', 'snake', 'gecko'], ['hamster', 'gerbil', 'rat', 'ferret']]
output = nested[1][2]
print(output)

# Question 2 - Below, a list of lists is provided. Use in and not in tests to create variables with Boolean values.
# See comments for farther instructions.

lst = [['apple', 'orange', 'banana'], [5, 6, 7, 8, 9.9, 10], ['green', 'yellow', 'purple', 'red']]

# Test to see if 'yellow' is in the third list of lst. Save to variable ``yellow``
if 'yellow' in lst[2]:
    yellow = True
else:
    yellow = False
print(yellow)  # to check if variable 'yellow' is True

# Test to see if 4 is in the second list of lst. Save to variable ``four``
if 4 in lst[1]:
    four = True
else:
    four = False
print(four)  # to check if variable "four" is False

# Test to see if 'orange' is in the first element of lst. Save to variable ``orange``
if 'orange' in lst[0]:
    orange = True
else:
    orange = False
print(orange)

# Question - Below, we’ve provided a list of lists.
# Use in statements to create variables with Boolean values - see the ActiveCode window for farther directions.

L = [[5, 8, 7], ['hello', 'hi', 'hola'], [6.6, 1.54, 3.99], ['small', 'large']]

# Test if 'hola' is in the list L. Save to variable name test1
if 'hola' in L:
    test1 = True
else:
    test1 = False
print(test1)  # to check if variable "test1" is False

# Test if [5, 8, 7] is in the list L. Save to variable name test2
if [5, 8, 7] in L:
    test2 = True
else:
    test2 = False
print(test2)

# Test if 6.6 is in the third element of list L. Save to variable name test3
if 6.6 in L[2]:
    test3 = True
else:
    test3 = False
print(test3)

# Question - Provided is a nested data structure. Follow the instructions in the comments below. Do not hard code.

nested = {'data': ['finding', 23, ['exercises', 'hangout', 34]], 'window': ['part', 'whole', [], 'sum',
                                                                            ['math', 'calculus', 'algebra', 'geometry',
                                                                             'statistics',
                                                                             ['physics', 'chemistry', 'biology']]]
          }

# Check to see if the string data is a key in nested, if it is, assign True to the variable data, otherwise assign False.
if 'data' in nested:
    data = True
else:
    data = False
print(data)

# Check to see if the integer 24 is in the value of the key data, if it is then assign to the variable twentyfour the
# value of True, otherwise False.
if 24 in nested['data']:
    twentyfour = True
else:
    twentyfour = False
print(twentyfour)

# Check to see that the string 'whole' is not in the value of the key window. If it's not, then assign to the variable whole the value of True, otherwise False.
if 'whole' not in nested['window']:
    whole = True
else:
    whole = False
print(whole)
# Check to see if the string 'physics' is a key in the dictionary nested. If it is, assign to the variable physics, the value of True, otherwise False.

if 'physics' in nested:
    physics = True
else:
    physics = False
print(physics)

# Question - The variable nested_d contains a nested dictionary with the gold medal counts for the top four
# countries in the past three Olympics. Assign the value of Great Britain’s gold medal count from the London
# Olympics to the variable london_gold. Use indexing. Do not hardcode.

nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}
london_gold = nested_d['London']['Great Britain']
print(london_gold)

# Question - Below, we have provided a nested dictionary.
# Index into the dictionary to create variables that we have listed in the ActiveCode window.

sports = {'swimming': ['butterfly', 'breaststroke', 'backstroke', 'freestyle'], 'diving': ['springboard', 'platform', 'synchronized'], 'track': ['sprint', 'distance', 'jumps', 'throws'], 'gymnastics': {'women':['vault', 'floor', 'uneven bars', 'balance beam'], 'men': ['vault', 'parallel bars', 'floor', 'rings']}}

# Assign the string 'backstroke' to the name v1
v1 = sports['swimming'][2]
print(v1)
# Assign the string 'platform' to the name v2
v2 = sports['diving'][1]
print(v2)
# Assign the list ['vault', 'floor', 'uneven bars', 'balance beam'] to the name v3
v3 = sports['gymnastics']['women']
print(v3)
# Assign the string 'rings' to the name v4
v4 = sports['gymnastics']['men'][-1]
print(v4)

# Question - Given the dictionary, nested_d, save the medal count for the USA from all three Olympics in the dictionary to the list US_count.

nested_d = {'Beijing': {'China': 51, 'USA': 36, 'Russia': 22, 'Great Britain': 19},
            'London': {'USA': 46, 'China': 38, 'Great Britain': 29, 'Russia': 22},
            'Rio': {'USA': 35, 'Great Britain': 22, 'China': 20, 'Germany': 13}
            }

US_count = []
for key, value in nested_d.items():
    if 'USA' in value.keys():
        US_count.append(value['USA'])
print(US_count)

# Question - Iterate through the contents of l_of_l and assign the third element of sublist to a new list called third.

l_of_l = [['purple', 'mauve', 'blue'], ['red', 'maroon', 'blood orange', 'crimson'], ['sea green', 'cornflower', 'lavender', 'indigo'], ['yellow', 'amarillo', 'mac n cheese', 'golden rod']]
third = []
for elem in l_of_l:
    third.append(elem[2])
print(third)

# Question - Given below is a list of lists of athletes. Create a list, t, that saves only the athlete’s name
# if it contains the letter “t”. If it does not contain the letter “t”, save the athlete name into list other.

athletes = [['Phelps', 'Lochte', 'Schooling', 'Ledecky', 'Franklin'], ['Felix', 'Bolt', 'Gardner', 'Eaton'], ['Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak', 'Dalton']]
check = 't'
t = []
other = []
for letter in athletes[0]:
    if check in letter:
        t.append(letter)
    else:
        other.append(letter)
for letter_1 in athletes[1]:
    if check in letter_1:
        t.append(letter_1)
    else:
        other.append(letter_1)
for letter_2 in athletes[2]:
    if check in letter_2:
        t.append(letter_2)
    else:
        other.append(letter_2)
print(t)
print(other)
