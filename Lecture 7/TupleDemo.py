tuple1 = ('green', 'red', 'blue')

print(tuple1)

tuple2 = ([7, 1, 2, 23, 4, 5])

print(tuple2)

print(f'length is {len(tuple2)}')
print(f'max is {max(tuple2)}')
print(f'min is {min(tuple2)}')
print(f'sum is {sum(tuple2)}')

print(f'The first element is: {tuple2[0]}')

tuple3 = 2 * tuple1 # Duplicate a tuple
print(tuple3)

print(tuple2[2:4])
print(tuple1[-1])

print(2 in tuple2)

for v in tuple1:
    print(v, end = ' ')
print()

list1 = list(tuple2)
list1.sort
tuple4 = tuple(list1)
tuple5 = tuple(list1)
print(tuple4)
print(tuple4 == tuple5)