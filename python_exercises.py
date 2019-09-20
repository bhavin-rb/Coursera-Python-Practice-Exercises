#Python Practice Questions from Coursera - Foundations of Python Programming

# Question - Assign the last element of lst to the variable end_elem. Do this so that it works no matter how long lst is.

lst = ["hi" , "goodbye" , "python" , "106" , "506" , 91 , ['all' , 'Paul' , 'Jackie' , "UMSI" , 1 , "Stephen" , 4.5] ,
    109 , "chair" , "pizza" , "wolverine" , 2017 , 3.92 , 1817 , "account" , "readings" , "papers" , 12 , "facebook" ,
    "twitter" , 193.2 , "snapchat" , "leaders and the best" , "social" , "1986" , 9 , 29 , "holiday" ,
    ["women" , "olympics" , "gold" , "rio" , 21 , "2016" , "men"] , "26trombones"]
    
end_elem = lst[-1]
print(end_elem)

# Question  - What is printed by the following statements?

L = [0.34, '6', 'SI106', 'Python', -2]
print(len(L[1:-1]))   #Answer is 3. index 1 is 6, index 2 is 'ST106' and index 3 is 'Python'. -2 is excluded.

# Question - Assign the number of elements in lst to the variable output.

lst = ["hi" , "morning" , "dog" , "506" , "caterpillar" , "balloons" , 106 , "yo-yo" , "python" , "moon" , "water" ,
       "sleepy" , "daffy" , 45 , "donald" , "whiteboard" , "glasses" , "markers" , "couches" , "butterfly" , "100" ,
       "magazine" , "door" , "picture" , "window" , ["Olympics" , "handle"] , "chair" , "pages" , "readings" ,
       "burger" , "juggle" , "craft" , ["store" , "poster" , "board"] , "laptop" , "computer" , "plates" , "hotdog" ,
       "salad" , "backpack" , "zipper" , "ring" , "watch" , "finger" , "bags" , "boxes" , "pods" , "peas" , "apples" ,
       "horse" , "guinea pig" , "bowl" , "EECS"]

output = len(lst)  # use len function to check the number of elements in the list.
print(output)

# Question - Create a variable output and assign it to a list whose elements are the words in the string str1.

str1 = "OH THE PLACES YOU'LL GO"
output = list(str1.split())
print(output)

# Question - Write one for loop to print out each element of the list several_things.
# Then, write another for loop to print out the TYPE of each element of the list several_things.
# To complete this problem you should have written two different for loops, each of which iterates
# over the list several_things, but each of those 2 for loops should have a different result.

several_things = ["hello", 2, 4, 6.0, 7.5, 234352354, "the end", "", 99]

for element in several_things:
    print(element)
    
for type_1 in several_things:
    print(type(type_1))
    
# Question - Count the number of characters in string str1. Do not use len(). Save the number in variable numbs.

str1 = "I like nonsense, it wakes up the brain cells. Fantasy is a necessary ingredient in living."

numbs = 0
for char in str1:
    numbs += 1
print(numbs)   # check the answer by using len fuinction as well and it should have same value of 90, print(len(str1)).

# Question - Assign the number of elements in lst to the variable num_lst.

lst = ["hi" , "goodbye" , "python" , "106" , "506" , 91 , ['all' , 'Paul' , 'Jackie' , "UMSI" , 1 , "Stephen" , 4.5] ,
       109 , "chair" , "pizza" , "wolverine" , 2017 , 3.92 , 1817 , "account" , "readings" , "papers" , 12 ,
       "facebook" ,
       "twitter" , 193.2 , "snapchat" , "leaders and the best" , "social" , "1986" , 9 , 29 , "holiday" ,
       ["women" , "olympics" , "gold" , "rio" , 21 , "2016" , "men"] , "26trombones"]
       
num_lst = len(lst)
print(num_lst)

# Question - What is the length of each element in list?

str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]

element = 0
for elem in str_list:
    element = len(elem)
    print(element)
    
# Question - How many times will the for loop iterate in the following statements?

p = [3, 4, "Me", 3, [], "Why", 0, "Tell", 9.3]
for ch in p:
   print(ch)   # Answer is 9 times as there are 9 items in a list.
   
# Question - Write code to create a list of numbers from 0 to 67 and assign that list to the variable nums. Do not hard code the list. 

nums = range(0,68)
print(nums)

# Question - What is printed by the following statements? (Dictionaries question)

mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
answer = mydict.get("cat")//mydict.get("dog")
print(answer) # Answer is 12//6 which gives 2.

# Question - What is printed by the following statements?

mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
print("dog" in mydict)  # is "dog" in dictionary mydict? Answer is Yes.

# Question -  What is printed by the following statements?

mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
print(23 in mydict) # Answer is False as 23 is a value and not a key in dictionary mydict.

# Question - What is printed by the following statements?

total = 0
mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
for akey in mydict:
   if len(akey) > 3:
      total = total + mydict[akey]
print(total)

# Question - The dictionary travel contains the number of countries within each continent that
# Jackie has traveled to. Find the total number of countries that Jackie has been to,
# and save this number to the variable name total. Do not hard code this!

travel = {"North America": 2, "Europe": 8, "South America": 3, "Asia": 4, "Africa":1, "Antarctica": 0, "Australia": 1}

total = 0
for continent in travel:
    total = total + travel[continent]
print(total)

# Question - schedule is a dictionary where a class name is a key and its value is how many
# credits it was worth. Go through and accumulate the total number of credits that
# have been earned so far and assign that to the variable total_credits. Do not hardcode.

total_credits = 0
for credit in schedule:
    total_credits = total_credits + schedule[credit]
print(total_credits)

# Question - Create a new list of the 6th through 13th elements of lst (eight items in all) and assign it to the variable output.

lst = ["swimming", 2, "water bottle", 44, "lollipop", "shine", "marsh", "winter", "donkey", "rain", ["Rio", "Beijing", "London"], [1,2,3], "gold", "bronze", "silver", "mathematician", "scientist", "actor", "actress", "win", "cell phone", "leg", "running", "horse", "socket", "plug", ["Phelps", "le Clos", "Lochte"], "drink", 22, "happyfeet", "penguins"]
output = lst[5:13]
print(output)

# Question - Write one for loop to print out each character of the string my_str on a separate line.

my_str = "MICHIGAN"
for c in my_str:
    print(c)
    
 # Question -  addition_str is a string with a list of numbers separated by the + sign.
 # Write code that uses the accumulation pattern to take the sum of all of the numbers
 # and assigns it to sum_val (an integer).
 # (You should use the .split("+") function to split by "+" and int() to cast to an integer).
 
 addition_str = "2+5+10+20"
 
addition_str_new = addition_str.split("+")
print(addition_str_new)  # for checking purpose only
sum_val = 0
for num in addition_str_new:
    num=int(num)
    sum_val = sum_val + num
print(sum_val)

# Question - What does the following code print?

if (4 + 5 == 10):
    print("TRUE")
else:
    print("FALSE")   # since 9 is not equal to 10, it will print FALSE first
print("TRUE")  # this will be printed regardless of anything. TRUE will be printed in the second line

# Question - What is printed by the following statements?

s = "We are learning!"
x = 0
for i in s:
    if i in ['a', 'b', 'c', 'd', 'e']:   # 'e' appears 3 times and 'a' appears 2 times
        x += 1
print(x)   # 3 + 2 = 5

# Question - Write code that uses slicing to get rid of the the second 8 so that here are only two 8’s in the list bound to the variable nums.

nums = [4, 2, 8, 23.4, 8, 9, 545, 9, 1, 234.001, 5, 49, 8, 9 , 34, 52, 1, -2, 9.1, 4]
nums = nums[0:4] + nums[5:]
print(nums)

# Question - What is printed by the following statements?

s = "python rocks"
print(s.count("o") + s.count("p")) # it will print 3. 'p' appears once and 'o' appears twice

# Question - Write code to count the number of characters in original_str using the
# accumulation pattern and assign the answer to a variable num_chars.
# Do NOT use the len function to solve the problem
# (if you use it while you are working on this problem, comment it out afterward!)

original_str = "The quick brown rhino jumped over the extremely lazy fox."

num_chars = 0
for char in original_str:
    num_chars = num_chars + 1
print(num_chars)

# Question - Provided is a list of tuples. Create another list called t_check that contains the third element of every tuple.

lst_tups = [('Articuno', 'Moltres', 'Zaptos'), ('Beedrill', 'Metapod', 'Charizard', 'Venasaur', 'Squirtle'), ('Oddish', 'Poliwag', 'Diglett', 'Bellsprout'), ('Ponyta', "Farfetch'd", "Tauros", 'Dragonite'), ('Hoothoot', 'Chikorita', 'Lanturn', 'Flaaffy', 'Unown', 'Teddiursa', 'Phanpy'), ('Loudred', 'Volbeat', 'Wailord', 'Seviper', 'Sealeo')]
t_check = [elem[2] for elem in lst_tups]
print(t_check)

# Question - Below, we have provided a list of tuples. Write a for loop that saves the second element of each tuple into a list called seconds.

tups = [('a', 'b', 'c'), (8, 7, 6, 5), ('blue', 'green', 'yellow', 'orange', 'red'), (5.6, 9.99, 2.5, 8.2), ('squirrel', 'chipmunk')]
seconds = [elem[1] for elem in tups]
print(seconds)

# Question - Write code to assign the number of characters in the string rv to a variable num_chars.

rv = """Once upon a midnight dreary, while I pondered, weak and weary,
    Over many a quaint and curious volume of forgotten lore,
    While I nodded, nearly napping, suddenly there came a tapping,
    As of some one gently rapping, rapping at my chamber door.
    'Tis some visitor, I muttered, tapping at my chamber door;
    Only this and nothing more."""

num_chars = len(rv)
print(num_chars)

# Questuion - Assign the value of the 23rd element of l to the variable checking.

l = (
"hi" , "goodbye" , "python" , "106" , "506" , 91 , ['all' , 'Paul' , 'Jackie' , "UMSI" , 1 , "Stephen" , 4.5] , 109 ,
"chair" , "pizza" , "wolverine" , 2017 , 3.92 , 1817 , "account" , "readings" , "papers" , 12 , "facebook" , "twitter" ,
193.2 , "snapchat" , "leaders and the best" , "social" , "1986" , 9 , 29 , "holiday" ,
["women" , "olympics" , "gold" , "rio" , 21 , "2016" , "men"] , "26trombones")

checking = l[22]
print(checking)

# Question - Write a program that extracts the last three items in the list sports and assigns it to the variable last.

sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
last = sports[-3:]
print(last)

# Question - week_temps_f is a string with a list of fahrenheit temperatures separated by the , sign.
# Write code that uses the accumulation pattern to compute the average (sum divided by number of items) and assigns it to avg_temp.
# Do not hard code you're answer (i.e., make you're code compute both the sum or the number of items in week_temps_f)
# (You should use the .split(",") function to split by "," and float() to cast to a float).

week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"

items = 0
sum = 0
for  i in week_temps_f.split(","):
    items = items + 1
print(items)
for c in week_temps_f.split(","):
    sum = sum + float(c)
print(sum)
avg_temp = sum/items
print(avg_temp)

# Question - Create a list of numbers 0 through 40 and assign this list to the variable numbers.
# Than, accumulate the total of the list’s values and assign that sum to the variable sum1.

numbers = range(0,41)
sum1 = 0
for tot in numbers:
    sum1 = tot + sum1
print(sum1)

# Question - Create a variable, b, and assign it the value of 15.
# Than, write code to see if the value b is greater then that of a.
# If it is, a’s value should be multiplied by 2.
# If the value of b is less then or equal to a, nothing should happen.
# Finally, create variable c and assign it the value of the sum of a and b.

a,b = 20,15
if b > a:
    a * 2
c = a + b
print(c)

# Question - Write code that combines the following variables so that the sentence
# “You are doing a great job, keep it up!” is assigned to the variable message.
# Do not edit the values assigned to by, az, io, or qy.

by = "You are"
az = "doing a great "
io = "job"
qy = "keep it up!"

message = by + " " + az + "" + io + ", " + qy
print(message)

# more practice questions will be added later
