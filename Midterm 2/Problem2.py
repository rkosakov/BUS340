charactersCount = 0
file = open("input.txt", 'rw+')
i = 0

for line in file.readlines():

    ch = line[i]
    if not ch.isupper():
        file.write(ch)

    if not ch[i] in ('\n'):
        i += 1
    else:
        i = 0

file.close()





