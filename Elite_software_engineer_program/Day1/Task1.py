# Reverse string & palindrome
string = input("Enter the string :")
i = len(string)-1
rev=""
while i>=0:
    rev+=string[i]
    i-=1
print("Reverse string :",rev)

if string == rev:
    print(string ,"is a palindrome")
else:
    print(string ,"is not a palindrome")
    
# prime number
num = int(input("Enter the number :"))
prime = True
if num<=1:
    print(num,"is not a prime number")
else:
    for i in range(2,num):
        if num%i==0:
            prime=False
            break
            
    if prime:
        print(num,"is a prime number")
    else:
        print(num,"is not a prime number")

# fibonacci
def fibonnaci(terms):
    a,b = 0,1
    for i in range(terms):
        print(a,end=" ")
        a,b = b , a+b

terms = int(input("Enter the terms :"))
fibonnaci(terms)


# armstrong number 
def armstrong(num):
    temp = num
    count = 0
    while temp!=0:
        digit = temp%10
        temp//=10
        count+=1
    temp = num
    sum = 0
    while temp!=0:
        digit = temp%10
        sum+=digit**count
        temp//=10
    if num == sum:
        print(num,"is an armstrong number")
    else:
        print(num ,"is not an armstrong number")
        
armstrong(153)    

# factorial
def factorial(num):
    if num<=1:
        return 1
    return num*factorial(num-1)
print(factorial(5))    


#count vowels
def vowels(string):
    count = 0
    for ch in string:
        if ch in "AEIOUaeiou":
            count+=1
    return count
print(vowels("Adarsh ki jai ho"))

#remove duplicates
def duplicates(string):
    seen = []
    duplicates = []
    for ch in string:
        if ch not in seen :
            seen.append(ch)
        else:
            duplicates.append(ch)
    return seen
print(duplicates("afsadkhan"))

#frequency of chars
def freq_of_chars(li):
    freq = {}
    for ele in li:
        if ele in freq:
            freq[ele]+=1
        else:
            freq[ele]=1
    return freq
print(freq_of_chars([1,1,33,33,44,44,44]))

# Second largest element
def second_largest(li):
    li.remove(max(li))
    print(max(li))

        
second_largest([12,43,34,44,54,35])