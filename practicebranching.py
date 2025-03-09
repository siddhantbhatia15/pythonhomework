print("Please enter five numbers:")

num1 = int(input("First number:"))
num2 = int(input("Second number:"))
num3 = int(input("Third number:"))
num4 = int(input("Fourth number:"))
num5 = int(input("Fifth number:"))

print("Do you want to know the sum or average of the number?")

numchoice = str(input("Enter your choice here:"))

if numchoice  == "sum":
    answer = num1 + num2 + num3 + num4 + num5
    print(answer)
elif numchoice == "average":
    answer = (num1 + num2 + num3 + num4 + num5)/5
    print(answer)
else:
    print("option not supported")
    
print("thank You")
