#break
#Task1
'''for i in range(1,101):
    if i ==51:
        break
    print(i)
#Task2
while True:
    password=input("enter password:")
    if password=="admin123":
        print("correct password")
        break
    else:
        print("wrong password")
#Task3
names=['keerthi','sakthi','harini']
search=input("enter name:")
for name in names:
    if name in name==search:
        print("name found")
        break

#continue
#Task4
for i in range (1,51):
    if i %3==0:
        continue
    print(i)
#Task5
for i in range(1,51):
    if i %2==0:
        continue
    print(i)
    
#Task6
text=input("enter a word:")
for ch in text:
    if ch in "aeiouAEIOU":
        continue
    print(ch)
#pass
#task7
def display():
    pass
#task8
class student:
    pass
#task9
for i in range(1,6):
    if i ==3:
        pass
    print(i)


#while loop
i=1
while i <=100:
    if i ==51:
        break
    print(i)
    i+=1
while True:
    pwd = input("Enter Password: ")
    if pwd == "1234":
        print("Correct Password")
        break
names = ["jothi", "harini", "sakthi", "Keerthika"]
search = input("Enter Name: ")
i = 0
while i < len(names):
    if names[i] == search:
        print("Name Found")
        break
    i += 1
i = 1
while i <= 20:
    if i % 3 == 0:
        i += 1
        continue
    print(i)
    i += 1
i=1
while i <=50:
    if i %2==0:
        i+=1
        continue
    print(i)
    i+=1
word = input("Enter Word: ")
i = 0
while i < len(word):
    if word[i] in "aeiouAEIOU":
        i += 1
        continue
    print(word[i])
    i += 1'''
i=1
while i<=5:
    if i ==3:
        pass
    print(i)
    i+=1
