def gen(x, y):
    for i in range(1, x + 1):
        yield i + y

s = gen(2, 5)
print(s.__next__())
print(s.__next__())
print(s.__next__())