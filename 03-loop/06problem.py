# Find the factorial using while loop
number = 5
factorial = number
i = 1

while(i<= number):
    factorial = factorial * (number -1)
    number = number - 1
    i+=1

print(factorial)