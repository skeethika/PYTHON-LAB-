#LIST
#task1
'''numbers = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
for i in numbers:
    if i % 2 == 0:
        print(i)
#task2
numbers = [10, 25, 5, 40, 15]
print("Largest:", max(numbers))
print("Smallest:", min(numbers))

#task 3
numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
average = total / len(numbers)
print(total)
print(average)
#task4
numbers = [1, 2, 2, 3, 4, 4, 5]
numbers = list(set(numbers))
print(numbers)
#task5
numbers = [10, 50, 30, 40, 20]
numbers.sort()
print(numbers[-2])
#task6
numbers = [1, 2, 3, 4, 5]
print(numbers[::-1])
#task7
l1 = [3, 1, 5]
l2 = [4, 2, 6]
result = l1 + l2
result.sort()
print(result)
#task8
numbers = [1, 2, 3, 2, 4, 2]
print(numbers.count(2))
#task9
numbers = [1, 2, 3, 4, 5, 6]
even = []
odd = []

for i in numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)
#task10
students = ["Keerthika", "Harini", "Sakthi","Priya"]
name = "Harini"
if name in students:
    print("Found")
else:
    print("Not Found")'''

#TUPLE
# Task 1
'''subjects = ("Math", "Science", "English", "Tamil", "Computer")
for i in subjects:
    print(i)
#Task 2
subjects = ("Math", "Science", "English", "Tamil", "Computer")
print(len(subjects))
#Task 3
t = (1, 2, 3, 2, 4, 2)
print(t.count(2))
#Task 4
t = ("a", "b", "c", "d")
print(t.index("c"))
# Task 5
t = (10, 20, 30)
l = list(t)
l.append(40)
print(l)
#Task 6
t = (20, 40, 10, 60, 30)
print(max(t))
print(min(t))
# Task 7
t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(t1 + t2)
# Task 8
t = ("Apple", "Banana", "Orange")

if "Banana" in t:
    print("Exists")
else:
    print("Not Exists")
#Task 9
marks = [80, 90, 70, 85]
t = tuple(marks)
print(sum(t) / len(t))
#Task 10
t = (10, 20, 30, 40, 50)
print(t[0])
print(t[len(t)//2])
print(t[-1])'''
# Set
#Task 1
'''set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)
#Task 2
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1 & set2)
#Task 3
set1 = {1, 2, 3}
set2 = {2, 3}
print(set1 - set2)
# Task 4
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 ^ set2)
# Task 5
numbers = [1, 2, 2, 3, 4, 4]
print(set(numbers))
#Task 6
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))
#Task 7
a = {1, 2, 3}
b = {1, 2}
print(a.issuperset(b))
#Task 8
s = {1, 2, 3}
s.add(4)
s.remove(2)
print(s)
# Task 9
class1 = {"Ram", "Priya", "Hari"}
class2 = {"Hari", "Keerthika", "Ram"}
print(class1 & class2)
#Task 10
a = {1, 2}
b = {3, 4}
print(a.isdisjoint(b))'''
# Dictionary
#Task 1
'''
student = {"Name": "Keerthika", "Age": 21, "Mark": 90}
print(student)
#Task 2
student = {"Name": "Keerthika"}
student["City"] = "Salem"
print(student)
#Task 3
student = {"Name": "Keerthika", "Mark": 80}
student["Mark"] = 95
print(student)
#Task 4
student = {"Name": "Keerthika", "Age": 21}
del student["Age"]
print(student)
#Task 5
student = {"Name": "Keerthika", "Age": 21}
print(student.keys())
#Task 6
student = {"Name": "Keerthika", "Age": 21}
print(student.values())
# Task 7
student = {"Name": "Keerthika", "Age": 21}
if "Age" in student:
    print("Exists")
else:
    print("Not Exists")
#Task 8
text = "apple"
d = {}
for i in text:
    d[i] = d.get(i, 0) + 1

print(d)
#Task 9
marks = {"Keerthi": 80, "Harini": 95, "SakthiPriya": 90}
print(max(marks, key=marks.get))
#Task 10
d1 = {"a": 1}
d2 = {"b": 2}
d1.update(d2)
print(d1)
# Scenario
#List 1
cart = ["Pen", "Book"]
cart.append("Pencil")
cart.remove("Pen")
print(cart)
# List 2
attendance = ["Ramaya", "Harini", "Priya"]
if "Hari" in attendance:
    print("Present")
else:
    print("Absent")
#Tuple 3
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
n = 3
print(days[n-1])
#Tuple 4
gps = (11.6643, 78.1460)
print(gps[0])
print(gps[1])
#Set 5
visitors = {101, 102, 103}
visitors.add(104)
print(visitors)
#Set 6
student1 = {"Python", "Java", "C"}
student2 = {"Python", "C++", "Java"}
print(student1 & student2)
#Dictionary 7
employee = {
    101: ["Ramaya", "HR", 30000],
    102: ["Harini", "IT", 40000]
}
print(employee)
#  Dictionary 8
contacts = {
    "Ramaya": 9876543210,
    "Harini": 9876501234
}
print(contacts)
# Dictionary 9
marks = {"Keethika": 80, "Harini": 90}
marks["Keerthika"] = 95
print(max(marks, key=marks.get))
print(marks)
#Dictionary 10
library = {
    1: "Python",
    2: "Java"
}

book_id = 2
print(library.get(book_id))
# Challenge
#Task 1
l = [1, 2, 3]
t = tuple(l)
s = set(t)
d = {i: i*i for i in s}
print(d)
# Task 2
numbers = [1, 2, 2, 3, 3, 3]
d = {}

for i in numbers:
    d[i] = d.get(i, 0) + 1

for k, v in d.items():
    if v > 1:
        print(k)
#Task 3
text = "apple mango apple orange"
words = text.split()
d = {}

for i in words:
    d[i] = d.get(i, 0) + 1

print(d)
# Task 4
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print(set(list1) & set(list2))'''
#Task 5
students = ["Ramaya", "Harini"]
subjects = ("Python", "Java")
present = {"Ramaya"}
marks = {"Ramaya": 90, "Harini": 80}
print(students)
print(subjects)
print(present)
print(marks)
