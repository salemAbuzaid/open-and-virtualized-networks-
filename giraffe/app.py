from math import *  # this line to import a library of math
import numpy
import pandas as pd
import matplotlib.pyplot as plt
import useful_tools
from student import student
from question import question
from chinese_chef import chinese_chef
from list_t import list_t
from generateBinn import generate_binary


def main():
    list = [0] * 3
    generate_binary(0, 2, list)


if __name__ == "__main__":
    main()

character_name = "George"
age = "50.54"
is_male = False
print("there once was a man named " + character_name + ",")
print("he was " + age + " years old.")

character_name = "mike"
print("he\ really liked the name " + character_name + ",")
print("but didn't like being " + age + ".")
name = "SALEM"
adg = " is cool"
print(adg.upper())
print(name.isupper())
print(adg.isupper())
print(len(adg))
print(name[0])
print(name.index("SALEM"))
print(name.replace("SALEM", "MOHAMED"))

my_num = -10
my_num = abs(my_num)
print(name + " likes number " + str(my_num))
print(pow(my_num, 2))
print(max(70, 59, 3))
print(min(70, 3))
print(round(3.6))
print(30 % 4)
print(int(30 / 4))
# the usage of math library startes from here

print("the flour is:" + str(floor(7.6)))
print(ceil(7.6))
print(sqrt(30))
'''
#getting inputs from users
name =input("Enter your name: ")
age =input("Enter your age: ")
print("hello "+ name +" you are " + age + " years old")

#creating a calulator
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
result = float(num1) + float(num2)
print(result)

# mad libs game
color = input("Enter a color:")
plural_noun = input("Enter a plural noun:")
celebrity  = input("Enter a celebrity")
print("roses are "+ color )
print(plural_noun +" are blu")
print("I love "+ celebrity)
'''

# lists
freinds = ["shebl", "khater", "jim", 32, True, "ahmed"]
print(freinds[4])
print(freinds[-1])
print(freinds[3])
print(freinds[-2])
freinds[2] = "maher"
print(freinds[1:])

lucky_number = [42, 4, 8, 15, 16, 23, 1]
freinds.extend(lucky_number)  # add two lists in one of them
print(freinds)
freinds.append("creed")  # append one more element
print(freinds)
freinds.insert(1, "kelly")  # insert an element at index 1
print(freinds)
freinds.remove(freinds[6])  # removing ahmed  from the list
print(freinds)
# freinds.clear()             # clear the list
print(freinds)
x = freinds.pop()  # it pops the last element out of the list and stores it in x, we can choose the element by insiting its index in the parenthesis
print(freinds)
print("the index", freinds.index("khater"))

print("the sum  ", 1 + freinds.index("khater"))
print(freinds.count("shebl"))  # to count how many times this element appears
lucky_number.sort()  # to sort thee array
print(lucky_number)
lucky_number.reverse()
print(lucky_number)
freinds2 = freinds.copy()
print(freinds2)

###    tuples is a kind of structure that are usually used for data that are not gonna change
coordinats = (4, 5)  # it was at 1:19 minits of the vedio
print("tuples ", coordinats[0])
# coordinats[1] = 4                   # this is an error because tuples are immutable
list_tuple = [(1, 3), (1, 3, 4)]
print(list_tuple[1])


# creating functions
def say_hi(name, age):
    print("Hello " + name + " you are " + str(age))


print("top")
say_hi("salem", 24)


# using the return statement on python functions
def cube(num):
    x = pow(num, 3)
    return (x)


print(cube(50))

### if statement
is_male = True
is_tall = False
if is_male or is_tall:
    print("you are a male or tall or both ")
else:
    print('you are neither a male nor tall')

if is_male and is_tall:
    print('you are a male and tall')
elif is_male and not (is_tall):
    print("you are a short male")
else:
    print("you are either not male or not tall or both")


# comparision statements
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return (num1)
    elif num2 >= num3 and num2 >= num3:
        return (num2)
    else:
        return (num3)


print(max_num(1, 2, 3))

# getting values from the user and add them
'''
num1 = float(input("Enter the first number:"))
op = input("Enter the operator :")
num2 = float(input("Enter the second number:"))
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
else:
    print("invalid operater")
'''

# dictionaries in python
month_conversions = {
    "jan": "january",
    # key    element
    "feb": "february",
    "mar": "march",
    "E": 10
}
print(month_conversions["jan"])
print(month_conversions["E"])
print(month_conversions.get("jan"))
print(month_conversions.get("feb", "not a valid key "))


def fact(n):
    if n == 1 or n == 0:
        return (1)
    return (n * fact(n - 1))


print(fact(10))

# while loop______________
i = 1
while i <= 5:
    print(i)
    i += 1
print("done with loop")

# building a guessing game

secrert_word = "giraffe"
guess = ""
guess_cnt = 0
guess_limit = 3
out_of_guesses = False
while guess != secrert_word and not (out_of_guesses):
    if guess_cnt < guess_limit:
        # guess = input("enter the guess:  ")
        guess_cnt += 1
    else:
        out_of_guesses = True
if (out_of_guesses):
    print("you lose ")
else:
    print("you win!")

# for loops______________

for letter in "giraffe academy":
    print(letter)

for freind in freinds:
    print(freind)

for i in range(5):
    print(i)

for i in range(2, 5):
    print(i)

for i in range(len(freinds)):
    print(freinds[i])

print("2 ^ 4 = " + str(2 ** 4))


# exponent function
def raise_to_power(base, pow):
    result = 1
    for index in range(pow):
        result = result * base
    return (result)


print("the power  : " + str(raise_to_power(5, 3)))

# 2D lists and for loops ________

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print(number_grid[0][0])

for row in number_grid:
    for col in row:
        print(col)


# build a translator___________
# vowel -> g
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return (translation)


print(translate("Asalem"))

# comments ______________

'''
salem starts to learn pyhton multiple line comment 
now he is with comments 
comments are fun 
'''

# try except bloc __________
try:
    # number = int (input ("enter a number "))
    # print(number)
    val = 1 / 0
except ZeroDivisionError:
    print("Divided by zero")
except ValueError as err:
    print(err)

# reading an external file _______

employee_file = open("empolyee.txt", "r")
list_file = employee_file.read()
# print(list_file)
print(list_file[0:])
print(employee_file.readable())
# print(employee_file.read())
# employ = employee_file.readline()
# print(employee_file.readline())
'''
for employ in employee_file.readlines():
    print(employ)
'''
# print("the employ zero: ", employ[0:])
# print(employee_file.readlines()[1])
# print(employee_file.readlines())
employee_file.close()

# writting and appending onto a file
employee_file = open("empolyee.txt", "a")
# employee_file.write("\nToby - Human resources")
employee_file.close()

# create a new file for writing _________
html_file = open("index.html", "w")
html_file.write("<p>This is HTML </p>")
html_file.close()

# modules and pip _________________
print("____________________________")
print(useful_tools.roll_dice(7))
print(useful_tools.get_file_ext("employee.txt"))
print("____________________________")

# classes and objects __________________

student1 = student("jim", "business", 3.1, False)  # student object is defined in the imported student file
student2 = student("pam", "ART", 3.2, True)
print(student2.name + " " + str(student1.gpa))
print(student2.ay7aga)
print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,")

# building a multiple choice quiz ____________________

question_prompt = [
    "what color are apples?\n(a) red/green \n(b) purple\n(c) orange\n\n",
    "what color are bananas?\n(a) teal\n(b) magenta\n(c) yellow\n\n",
    "what color are strawberries?\n(a) yellow\n(b) red\n(c) blue\n\n"
]

questions = [
    question(question_prompt[0], "a"),
    question(question_prompt[1], "c"),
    question(question_prompt[2], "b")
]
'''
def run_test(questions):
    score = 0
    for question in questions :
        answer = input(question.prompt)
        if answer[0] == question.answer:
            score += 1
    print("You got "+ str(score) +"/" + str(len(questions)) + " correct")

run_test(questions)
'''
new_list = list_t(freinds)
new_list.print_list()

# object functions  _____________
student1 = student("oscar", "accounting", 3.1, False)
student2 = student("phyllis", "business", 3.8, True)

print(student2.on_honor_roll())

# inheritance __________________
'''
is basically to have a class that have all the functionalities of another class
'''
my_chef = chinese_chef()
my_chef.make_chicken()
my_chef.make_fried_rice()


def to_binary(x):
    list = []
    base = 2
    while int(x / base) > 0 or (x % base) != 0:
        list.append(x % 2)
        x = int(x / base)
    # list.append(x % 2)

    list.reverse()
    print("the binary conversion is : " + str(list))


to_binary(300)


def to_decimal(x):
    res = 0
    i = 0
    while int(x / 10) > 0 or (x % 10) != 0:
        res = res + ((x % 10) * 2 ** i)
        x = int(x / 10)
        i += 1
    print("the decimal conversion is : " + str(res))


to_decimal(11000000)

'''
def generate_binary(index, base, list):
    if index >= len(list):
        print(list)
        return
    for i in range(base):
        list[index] = i
        generate_binary(index+1, base, list)
    return
list = [0, 0, 0]
generate_binary(0, 2, list)
'''
s1 = "salem "
s2 = "mohamed"
s3 = s1 + s2
print(s3)
s4 = s1[:3] + " aaaaa " + s1[3:]
print(s4)
word = s4.split()
print("word is", word)
print("the number of aaaa is ", s4.count("aaaa"))
L = [0] * 10  ########____________GREAAAAAAAAAT DISCOVERY___________
print(L)

df = pd.read_csv('sales_data.csv')
profitList = df['total_profit'].tolist()
monthList = df['month_number'].tolist()
plt.plot(monthList, profitList, label='Month - wise Profit data of last year')
plt.xlabel('Month number')
plt.ylabel('Profit in dollar')
plt.xticks(monthList)
plt.title('Company profit per month')
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.show()
