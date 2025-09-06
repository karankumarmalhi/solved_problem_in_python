# for line in open("chai.py"):
#     print(line)


f = open("chai.py")
# print(f.__next__())

while True:
    line = f.readline()
    if not line:
        break
    print(line, end='')