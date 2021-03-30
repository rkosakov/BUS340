fileName = input('Enter a filename: ')
file = open(fileName, 'r')

words = []
for line in file:
    for word in line.split():
        words.append(word.upper())

dict = {}
for word in words:
    number = dict.get(word, None)
    if number == None:
        dict[word] = 1

maximum = max(dict.values())
for key in dict:
    if dict[key] == max:
        print('The mode is: ', key)
        break