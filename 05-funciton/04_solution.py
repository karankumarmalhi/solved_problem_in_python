# Write a function that take varible number idf aurguments
def sum_all(*args):
    return sum(args)


print(sum_all(1, 2, 3))
print(sum_all(1, 2, 3, 8, 7))
print(sum_all(1, 2, 3, 8, 7, 9, 10))