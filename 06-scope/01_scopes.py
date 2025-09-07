username = "Karan"


def func():
    # username = 'chai'
    print(username)


print(username)


x = 99
# def func2():
#     global x
#     x = 50

# func2()
# print(x)


# def f1():
#     x = 88
#     def f2():
#         print(x)
#     return f2

# result = f1()
# result()


def coder(n):
    def actual(x):
        return x **n
    return actual


f = coder(2)
g = coder(3)
ac = g(2)

print(ac)

