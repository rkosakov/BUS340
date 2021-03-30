fileName = input('Enter a file Name')
file = open(fileName, 'r')

dict = {}

for line in file:
    line = line.strip()
    words = line.split(' ')

    for word in words:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    
    for key in list(dict.keys()):
        print(key, ':', dict[key])
