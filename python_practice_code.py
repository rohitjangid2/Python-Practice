# >>> NOTE: Type hints using the typing module (int, str, float, list, tuple, dict, set).
import typing

z: int = 10
y: str = "heeeeelloooo"
x: float = 4.34546
list_1: typing.List[int] = [1,2,3,4,5,]
print(list_1)
tuple_2: typing.Tuple[int, ...] = (2,4,6,3,5)
print(tuple_2)
dict_3: typing.Dict[str,int] = {"rohit":2,"mohit":5}
print(dict_3)
set_4: typing.Set[int] = {1,2,3,4}
print(set_4)
print(z,x,y)


# >>> NOTE: Hotel cost with 80% tax added, then shared among 3 people.
#hotel coantry
hotel_rant = 500
tex = hotel_rant * 0.8
totel = hotel_rant + tex
totel_person = 3
share_per_porson = totel_person / totel
print("coantry for three person : " + str(share_per_porson))

# >>> NOTE: Printing a full name with title and suffix: string concatenation vs print() with commas.
#string spac
salutation = "Dr."
first_name = "Prisha"
middle_name = "Jai"
last_name = "Agarwal"
suffix = "Ph.D."
print(salutation + "   " + first_name + " " + middle_name + " " + last_name + " , " + suffix)

print(salutation,   first_name,   middle_name,  last_name,  ",", suffix)
# >>> NOTE: ZeroDivisionError demo: dividing a number by zero.
''''
# ZeroDivisionError
numerator = 2
denominator = 0
result = numerator / denominator
print(result)
'''
# >>> NOTE: Sorting a list and finding its max and min values.
#sorting
sorting_list = [2,34,56,78,3,1,6,98,67,67,90]
print(sorted(sorting_list))
print(max(sorting_list))
print(min(sorting_list))


# >>> NOTE: Function to find the area of a square, and the sum of two squares.
def area_sq(side):
    return side*side

a_side = area_sq(5)
b_side = area_sq(5)
sum = a_side + b_side
print("area of square a and b :",a_side,b_side)
print("sum of both square",sum)


# >>> NOTE: Convert seconds into hours, minutes and remaining seconds.
def convert_second(second):
    hours = second // 3600
    minute = (second - hours* 3600) // 60
    remaining_second = second - hours * 3600 - minute * 60
    return hours , minute , remaining_second
    
result = convert_second(6000)
print(result)

# >>> NOTE: Reusing code: lucky number from name length, first without and then with a function.
# reusing the Code
name = 'rohit'
number = len(name) * 9
print("name=",name)
print("lucky number",number)

def LN(name):
    number = len(name) * 9
    print("lucky number =" , number)
LN("rohit")
# >>> NOTE: Function to calculate the area of a circle from its radius.
# redius
def circle_r(redius):
    pi = 3.14
    area = pi * (redius ** 2)
    print ("area = ", area)
circle_r(8)

# >>> NOTE: Comparison operators (>, !=, ==) returning True/False.
# condition
print(10>1)
print ( 5 != 9)
print (5 == 6)

# >>> NOTE: if/else: function that checks whether a number is less than 1000.
# if else

def tf(number):
    if number < 1000:
     return True
    return False

res = tf(900)
print(res)

# >>> NOTE: if/elif/else: username is valid only if its length is between 3 and 15.
def user(username):
    if len(username) < 3:
        print("invalid")
    elif len(username) > 15:
     print("invalid")
    else:
       print("valid") 
user("rohit")
# >>> NOTE: Round a number to the nearest multiple of 10.
# round up to 10x value
def near(number):
   x = 10
   whole_n = number // 10
   reminder =   number % x
   if reminder >= 5:
      return x*(whole_n + 1)
   return x*whole_n
print (near(11))

# >>> NOTE: While loop: counting steps until reaching the right shop.
# code using loop to reach to shope 
shop =  0
while shop < 10:
    print("wrong shop ",shop)
    shop +=1
print("right shop ",shop)

# >>> NOTE: While loops: sum and product of numbers.
# zig zek sum of 1 to 100
x = 1
sum = 0
while x < 10:
    sum = sum + x
    x += 1 
x = 1
product = 1
while x < 10:
    product = product * x
    x = x + 1
print(sum,product)

# >>> NOTE: Countdown from a given number using a while loop.
#reverse numner count 
def reverse_count(number):
    while (number > 0):
      print(number)
      number = number - 1
    print("count down completed")

reverse_count(10) 

# >>> NOTE: Count the even numbers from 1 up to a given number.
# count of even number
def even_count(number):
    even = 1
    count = 0

    if number == 0:
        return 0

    while even <= number:
        if even % 2 == 0:
         count += 1
        even += 1

    return count
print(even_count(15))


# >>> NOTE: Print the multiplication table of a number.
# table calculater 
def tableof(number):
    multiplier = 1
    while multiplier <= 10:
        result = number * multiplier
        print(number, "x", multiplier, "=", result)
        multiplier += 1
#number = int(input("Enter a number to print its table: "))
tableof(2)

# >>> NOTE: For loop: print each city from a list.
# for loopppppppppppppppppppppppppppp
cities = ["delhi","mumbai","jaipur","pune","kolkata"]
for city in cities:
    print( "i live in", city)
# >>> NOTE: For loop: sum and average of a list of numbers.
# sum average of list
n = [56, 34, 57, 89, 98, 23, 65]
sum = 0
length = 0
for i in n:
    sum += i
    length += 1
print("sum of list is", sum , "\n" "average of list is", sum / length)

# >>> NOTE: For loop: multiply numbers in a range (factorial-style product).
num = 1
for i in range(1,10):
    num = num * i
print(num)

# >>> NOTE: Convert temperature from Fahrenheit to Celsius for a range of values.
# temperature from Fahrenheit (°F) to Celsius (°C)
def fahrenheit_to_celsius(f):
    return  (f - 32) * 5 / 9
for f in range(0, 101, 5):
   print(f, "°F =", fahrenheit_to_celsius(f), "°C")

# >>> NOTE: Nested for loops: multiply each number in a list with every other number.
# multiply all the numbers with every number in list
N = [2,3,4,5,6,7,8,9,9,8,7,6,5,4,3,2,]
for self_N in N:
   for diff_N in N:
      if self_N != diff_N:
         print(self_N,diff_N,"=",(self_N*diff_N))

# >>> NOTE: Nested loops: how inner loops restart for every outer loop value.
long_list = ["A","B","C","D"]
for element in long_list:
    print(element)
    for element1 in long_list:
        for element2 in long_list:
           print(element1,element2)

# >>> NOTE: Split a sentence into words and search for a specific word.
# string with for loop 
string = "The most important thing to understand is that when an outer loop moves to the next value, all the inner loops start again from the beginning. That is why you see the same 16 pairs printed four times"
find = "beginning."
for char in string.split(): # split() use read a string as santance and then check each word in the string
    if char == find:
        print("found",char)

# >>> NOTE: Format a phone number using string slicing.
#phone_number_format
def phone_NO(number):
   iND = "(" +"+" + number[0:2] + ")"
   first_n = number[3:6]
   last_n = number[-5:]
   return iND + " " + first_n + " " + last_n
print(phone_NO('917878782301'))

# >>> NOTE: Recursion: factorial of a number.
def fact(n):
   if n < 2 :
      return 1
   result = n * fact(n-1)
   return result
print(fact(5))

# >>> NOTE: Nested loops: print a triangle pattern.
for left in range(7):
    for right in range(left,7):
        print("[" + str(left)  + "]", end = " ")
    print()

# >>> NOTE: String methods: replace an email address if it is found.
# string
def replace_email(email,old,new):
    if old in email:
        email = email.replace(old,new)
        return email
    else:
        return "not found"
print(replace_email("rohit@gmail.com","rohit@gmail.com","vaish@gmail.com"))

# >>> NOTE: Replace only the domain part of an email address.
def replace_domain(email, old_domain, new_domain):
  if "@" + old_domain in email:
    index = email.index("@" + old_domain)
    new_email = email[:index] + "@" + new_domain
    return new_email
  return email
print(replace_domain("rohit@gmail.com","gmail.com","yoho.com"))

# >>> NOTE: input() and format(): lucky number from the length of a name.
'''#found lucky number by name 
name = input("Enter your name: ")
lucky_number = len(name) * 3
print("hello {}, your lucky number is {}".format(name, lucky_number))

name = input("Enter your name: ")
print("your lucky number is {},{}".format((len(name) * 3), name))'''

# >>> NOTE: Car bill with 18% tax using input() and formatted output.
'''# billing with tax
car_amount = float(input("Enter the car amount: "))
tax_rate = 0.18
tax_amount = car_amount * tax_rate
total_amount = car_amount + tax_amount
print("your car amount is: {:.2f}, your car amount with tax is: {:.2f}".format(car_amount, total_amount))

# >>> NOTE: Convert pounds to kilograms and kilograms to pounds.
# pounds to kilogram and kilogram to pounds
pound = float(input("Enter the weight in pounds: "))
def pound_kg(pound):
   kg = pound * 0.454
   return kg
print("{} pounds == {:5.2f} kilograms".format(pound, pound_kg(pound)))

kg = float(input("Enter the weight in kilograms: "))
def kg_pound(kg):
   pound = kg / 0.454
   return pound
print("{} kilograms == {:5.2f} pounds".format(kg, kg_pound(kg)))'''

# >>> NOTE: Swap two variables using tuple unpacking.
a = 30
b = 50
print("Before swapping: a =", a, "b =", b)
a, b = b, a
print("After swapping: a =", a, "b =", b)

# >>> NOTE: Convert a sentence to a list of words and get the nth word.
#converting string to list
def acc_eliment(santance,n):
    if n > 0:
       words = santance.split()
       if n <= len(words):
          return words[n-1]

    return "invalid input"
print(acc_eliment("The quick brown fox jumps over the lazy dog", 6))
print(acc_eliment("yo yo yo yo yoy oy oy oy yo yo yoy oy oy", 10))

# >>> NOTE: List methods: append, insert, remove, pop.
name = ["rohit", "mohit", "prisha", "vaishnavi", "sneha"]
print(name)
name.append("snehal")
print(name)
name.insert(0,"Raj")
print(name)
name.insert(25,"Riya")
print(name)
name.remove("prisha")
print(name)
name.pop(4)
print(name)
print(type(name))
name.insert(1,"monu")
print(name)

# >>> NOTE: enumerate(): print list items with index numbers.
word = ["rohit","is","good","boy"]
for index, i in enumerate(word):
    print(index + 1,"->",i)

# >>> NOTE: Build 'name <email>' strings from a list of (email, name) tuples.
def full_email(people):
    result = []
    for email,name, in people:
        result.append("{},<{}>".format(name,email))
    return result
print(full_email([("rohit@gmail.com","Rohit Jangid"),("vaish@gmail.com","Vaishnavi Choudhari")]))


# >>> NOTE: List comprehension: multiples of 7 using a loop vs comprehension.
# list comprehension
multiple = []

for x in range(1,11):
    multiple.append(x*7)
print(multiple)
multiples = [x*7 for x in range(1,11)]
print(multiples)

# >>> NOTE: List comprehension with a condition: numbers divisible by 3.
z = [x for x in range(0,101) if x % 3 == 0]
print(z)

# >>> NOTE: Count how many times each letter appears in a text using a dictionary.
def count_t(text):
 result = {}
 for latter in text:
  if latter not in result:
   result[latter] = 0
   result[latter] += 1

 return result
print(count_t("rohit jangid"))

# >>> NOTE: Classes, sets and dictionaries: track which users are currently logged in on each machine.
def get_event_data(event):
    return event.date

def current_user(events):
    events.sort(key=get_event_data)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == "login":
                machines[event.machine].add(event.user)
        elif event.type == "logout":
            machines[event.machine].remove(event.user)
    return machines

def gen_report(machines):
    for machine, users in machines.items():
     if len (users) > 0:
         user_list  = ",".join(users)
         print("{}: {}".format(machine,user_list))



class Event:
  def __init__(self,event_date,event_type,machine_name,user):
    self.date = event_date
    self.type = event_type
    self.machine = machine_name
    self.user = user

events = [
  Event('2020-01-21 12:45:46', 'login', 'myworkstation.local', 'jordan'),
  Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
  Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
  Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
  Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
  Event('2020-01-23 11:24:35', 'login', 'mailserver.local', 'chris'),
]

users = current_user(events)
print(users)

gen_report(users)  

# >>> NOTE: Sum of the multiplication table (1 to 10) of a number.
def summ_t(t):
 r = 1
 summ = 0
 for i in range(1,11):
    r = t * i
    summ = r + summ
 return summ
t = int(input())
print(summ_t(t))
# >>> NOTE: Maximum product of any three numbers from a list of inputs.
limit = int(input())
num = []
for i in range(limit):
     num.append(int(input()))

num.sort()
a=num[0]*num[1]*num[-1]
b=num[-1]*num[-2]*num[-3]
print(max(a,b))


# >>> NOTE: Marks analysis: total, average, highest, lowest and students with 60+ marks.
marks = [78, 45, 89, 32, 67, 91, 56]
total = 0
h_marks = marks[0]
l_marks = marks[0]
n_stu = 0
for i in marks:
    total += i
    if i > h_marks:
     h_marks = i

    if i < l_marks:
     l_marks = i

    if i >= 60:
     n_stu += 1
average = total/len(marks)

print("Total:", total)
print("Average:", average)
print("Highest:", h_marks)
print("Lowest:", l_marks)
print("Students >= 60:", n_stu)

# >>> NOTE: Filter salaries above 40000 and find their average.
salaries = [25000, 45000, 32000, 70000, 28000, 55000, 90000]
new_sal = []
total = 0
for i in salaries:
    if i > 40000:
        new_sal.append(i)

    for j in new_sal:
        total += j
average = total/len(new_sal)

print("salary above 40000:",new_sal)
print("average of salary:",average)


# >>> NOTE: List analysis: unique, largest, smallest, even/odd and duplicate counts.
numbers = [12, 5, 8, 12, 20, 5, 30, 8, 15, 20, 30, 30]
total = 0
unique = []
largest = numbers[0]
lowest = numbers[0]
even_n = []
odd_n = []
n_dupl = []
for n in numbers:
    total += 1

    if n not in unique:
        unique.append(n)
    if n > largest:
        largest = n
    if n < lowest:
        lowest = n
    if n % 2 == 0:
       even_n.append(n)
    if n % 2 != 0:
        odd_n.append(n)
    if n not in n_dupl:
        n_dupl.append(n)
duplicate_count = total - len(unique)

print(total)
print(unique)
print(largest)
print(lowest)
print(len(even_n))
print(len(odd_n))
print(duplicate_count)
      
# >>> NOTE: OOP: Account class with debit, credit and get_balance methods.
class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc
        # debit method
    def debit(self,amount):
            self.balance -= amount
            print("Rs:",amount,"was debited")
            print("Totel balance =",self.balance)
    def credit(self,amount):
            self.balance += amount
            print("Rs:",amount,"was credited")
            print("Totel balance =",self.balance)
    def get_balance(self):
            return self.balance
           


acc1 = Account(10000, 467294)
acc1.debit(2000)
acc1.credit(50000)
acc1.debit(10000)