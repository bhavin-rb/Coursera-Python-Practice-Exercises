# Tuple Exercises from Coursera - Foundation of Python Programming

# Question - Create a tuple called olympics with four elements: “Beijing”, “London”, “Rio”, “Tokyo”.
from typing import Tuple, List, Union

olympics = ("Beijing", "London", "Rio", "Tokyo")
print(olympics)

# Question - Create a tuple called practice that has four elements: ‘y’, ‘h’, ‘z’, and ‘x’.

practice = ("y", "h", "z", "x")
print(practice)

# Question - Create a tuple named tup1 that has three elements: ‘a’, ‘b’, and ‘c’.

tup1 = ("a", "b", "c")
print(tup1)

# Question - The list below, tuples_lst, is a list of tuples. Create a list of the second elements of each tuple and assign this
# list to the variable country.

tuples_lst = [('Beijing', 'China', 2008),
              ('London', 'England', 2012),
              ('Rio', 'Brazil', 2016, 'Current'),
              ('Tokyo', 'Japan', 2020, 'Future')]
              
country: List[Union[str, int]] = [elem[1] for elem in tuples_lst]
print(country)

# Question - Provided is a list of tuples. Create another list called t_check that contains the third element of every tuple.

lst_tups = [('Articuno', 'Moltres', 'Zaptos'), ('Beedrill', 'Metapod', 'Charizard', 'Venasaur', 'Squirtle'),
            ('Oddish', 'Poliwag', 'Diglett', 'Bellsprout'), ('Ponyta', "Farfetch'd", "Tauros", 'Dragonite'),
            ('Hoothoot', 'Chikorita', 'Lanturn', 'Flaaffy', 'Unown', 'Teddiursa', 'Phanpy'),
            ('Loudred', 'Volbeat', 'Wailord', 'Seviper', 'Sealeo')]
t_check = [elem[2] for elem in lst_tups]
print(t_check)

# Question - Below, we have provided a list of tuples. Write a for loop that saves the second element of each tuple into a list called seconds.

tups = [('a', 'b', 'c'), (8, 7, 6, 5), ('blue', 'green', 'yellow', 'orange', 'red'), (5.6, 9.99, 2.5, 8.2),
        ('squirrel', 'chipmunk')]
seconds = [elem[1] for elem in tups]
print(seconds)

# Question - With only one line of code, assign the variables city, country, and year to the values of the tuple olymp.

olymp = ('Rio', 'Brazil', 2016)
(city, country, year) = olymp
print(olymp)
print(city)
print(country)
print(year)

#  Question - With only one line of code, assign the variables water, fire, electric,
#  and grass to the values “Squirtle”, “Charmander”, “Pikachu”, and “Bulbasaur”

water, fire, electric, grass = ("Squirtle", "Charmander", "Pikachu", "Bulbasaur")

# Question - With only one line of code, assign four variables, v1, v2, v3, and v4, to the following four values: 1, 2, 3, 4.

v1, v2, v3, v4 = (1, 2, 3, 4)

# Question - Define a function called info with five parameters: name, gender, age, bday_month, and hometown.
# The function should than return a tuple with all five parameters in that order.

def info(name, gender, age, bday_month, hometown):
    return name, gender, age, bday_month, hometown

# Question - Define a function called information that takes as input, the variables name, birth_year, fav_color, and hometown.
# It should return a tuple of these variables in this order.

def information(name, birth_year, fav_color, hometown):
    return name, birth_year, fav_color, hometown

# Question - Define a function called info with the following required parameters: name, age, birth_year, year_in_college, and hometown.
# The function should return a tuple that contains all the inputted information.

def info(name, age, birth_year, year_in_college, hometown):
    return name, age, birth_year, year_in_college,hometown

# Question - Given is the dictionary, gold, which shows the country and the number of gold medals
# they have earned so far in the 2016 Olympics. Create a list, num_medals,
# that contains only the number of medals for each country.
# Note: The .items() method provides a list of tuples. Do not use .keys() method.

gold = {'USA': 31, 'Great Britain': 19, 'China': 19, 'Germany': 13, 'Russia': 12, 'Japan': 10, 'France': 8, 'Italy': 8}
num_medals = list(gold.values())
print(num_medals)

#  Question - If you remember, the .items() dictionary method produces a list of tuples.
#  Keeping this in mind, we have provided you a dictionary called pokemon.
#  For every key value pair, append the key to the list p_names, and append the value to the list p_number.
#  Do not use the .keys() or .values() methods.

pokemon = {'Rattata': 19, 'Machop': 66, 'Seel': 86, 'Volbeat': 86, 'Solrock': 126}

p_names = list()
p_number = list()

for k in pokemon.keys():
    p_names.append(k)
print(p_names)

for v in pokemon.values():
    p_number.append(v)
print(p_number)

# Question - The .items() method produces a list of key-value pair tuples.
# With this in mind, write code to create a list of keys from the dictionary track_medal_
# counts and assign the list to the variable name track_events. Do NOT use the .keys() method.

track_medal_counts = {'shot put': 1, 'long jump': 3, '100 meters': 2, '400 meters': 2, '100 meter hurdles': 3,
                      'triple jump': 3, 'steeplechase': 2, '1500 meters': 1, '5K': 0, '10K': 0, 'marathon': 0,
                      '200 meters': 0, '400 meter hurdles': 0, 'high jump': 1
                      }

track_events = list()
for k in track_medal_counts.keys():
    track_events.append(k)
print(track_events)
