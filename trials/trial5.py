import random 

n = int(input('Enter the lenght of random integers'))
li = []
for i in range(n):
    integer = random.randint(1,101)
    li.append(integer)

avg = sum(li)/n
print(max(li),min(li),avg)
    
    
li = [12,34,54,23,44]
for i in range(len(li)):
    swap = False
    for j in range(len(li)-i-1):
        if li[j]>li[j+1]:
            li[j],li[j+1] = li[j+1],li[j]
            swap = True
    if swap==False:
        break
print(li)

target = int(input("Enter the number :"))

left , right = 0 , len(li)-1
while left<=right:
    mid = left + (right-left)//2
    if li[mid]==target:
        print(target,"found at index :",mid)
        break
    elif li[mid]<target:
        left=mid+1
    else:
        right=mid-1


arr = [[12,23,34,54,56],
       [32,54,65,23,65]]

rows = len(arr)
cols = len(arr[0])
transpose = []
for i in range(cols):
    row = []
    for j in range(rows):
        row.append(arr[j][i])
    
    transpose.append(row)
print(transpose)

sum=0
for k in range(len(arr)):
    sum+=arr[k][k]
print("Sum of digonals :",sum)



a = [[1,2],
     [3,4]]
b = [[5,6,7],
     [8,9,10]]


a_rows = len(a)
a_cols = len(a[0])
b_rows = len(b)
b_cols = len(b[0])
