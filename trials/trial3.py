class Student :
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        return self.name , self.marks

st1 = Student("Rishi",34)
st2 = Student("Arnav",45)
st3 = Student("Arav",79)
print(st1.display())
print(st2.display())
print(st3.display())



num = int(input("Enter the number :"))
try:
    reciprocal = 1/num
    print(reciprocal)
except Exception :
    print("Division by zero is not allowed")
    

def factorial(num):
    if num<=1:
        return 1
    else:
        return num*factorial(num-1)
print(factorial(5))