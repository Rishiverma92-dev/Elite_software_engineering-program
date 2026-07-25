char = input("Enter the string :")
with open("output.txt","w")as f:
    f.write(char)

with open("output.txt","r") as f:
    print(f.read())
