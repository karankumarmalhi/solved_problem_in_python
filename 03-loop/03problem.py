# Print the table of up to 10 skip the fifth iteration 

table = 3

for i in range(1, 11):
    if i != 5:
        print(f"{i} x {table} = {i*table}")