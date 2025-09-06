# Sum of even number 

given_input = int(input("Enter number:"))


sum_of_even_number = 0
for n in range(1, given_input+1):
    if(n % 2 == 0):
        sum_of_even_number += n

print(sum_of_even_number)