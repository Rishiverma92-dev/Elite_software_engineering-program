num = int(input('Enter the number :'))
if num>0:
    print("positive")
elif num==0:
    print("zero")
else:
    print("negative")
    
    
marks = int(input("Enter the marks :"))
if marks>=90:
    print("A")
elif marks>=75 and marks<=89:
    print("B")
elif marks>=50 and marks<=74:
    print("C")
else:
    print("fail")
    
    
char = input("Enter the string :")
i=len(char)-1
rev =""
while i>=0:
    rev += char[i]
    i-=1
if char==rev:
    print("palindrome")
else:
    print("no palindrome")


a,b = 0,1
n = int(input("Enter the number of series :"))
for i in range(n):
    print(a,end=" ")
    a,b = b,a+b
    
n = int(input("How many numbers :"))
li = []
for i in range(n):
    num = int(input('enter the number:'))
    li+=[num]
print(sum(li),max(li),min(li))

dict = {}
char = input("Enter the string: ")
for ch in char:
    if ch in dict:
        dict[ch]+=1
    else:
        dict[ch]=1
print(dict)


rows = 5
for i in range(rows):
    for j in range(i+1):
        print("*",end="")
    print()

num = int(input("How many numbers you want in a list"))
li = []
while num>0:
    ele = int(input("Enter the elements :"))
    li.append(ele)
    num-=1
li = set(li)
print(sorted(li))
        