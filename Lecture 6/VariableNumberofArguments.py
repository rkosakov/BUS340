def psum(*args):
    res = 0
    for i in args:
        res += i
    return res

print(psum(1,2,3,4))
print(psum(10,20))

def printValue(**kwargs):
    for(key, value) in kwargs.items:
        print(key, value)

printValue(a = 1, b = 2)
printValue(c = 5)