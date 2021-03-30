a = set('abracadabra')
b = set('alacazam')

print(a)
print(b)

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

a = set('abracadabra')
b = set('alacazam')

print(a-b)

print(a|b)
print(a&b)
print(a^b)

s1 = {1,2,3,4}
s2 = {1,4,2}

print(s1 == s2)
print(s1 != s2)