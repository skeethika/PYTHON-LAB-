#Print your name 5 times
'''for i in range(5):
    print("Keerthika")

#Print numbers from 1 to 20
for i in range(1,21):
    print(i)

#Print numbers from 20 to 1
for i in range(20, 0, -1):
    print(i)
#print numbers from 1 to 50
for i in range (2,51,2):
    print(i)
#print all odd numbers 1 to 50
for i in range(1,51,2):
    print(i)
#sum of numbers from 1 to 10
sum=0
for i in range(1,11):
    sum=sum+i
print("sum=",sum)
#multiplication table
num=int(input("enter number :"))
for i in range(1,11):
    print(num,"X",i,"=",num*i)
#count how many letters in your name
name=input("enter your name:")
count=0
for i in name:
    count=count+1
print("letters=",count)

#print each character of a word on a new line
word = input("enter a word:")
for i in word:
    print(i)
#Count the number of vowels in a word
word = input("Enter a word: ")
count = 0
for i in word:
    if i in "aeiouAEIOU":
        count = count + 1
print("Vowels =", count)
#Print Cross Pattern
n = 5
for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
#Print Right Angle Triangle
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()'''
#cross pattern using alphabets
word = "rotator"
for i in range(7):
    for j in range(7):
        if i == j or i + j == 6:
            print(word[j], end=" ")
        else:
            print(" ", end=" ")
    print()
    
