import random

articles = ('A', 'The')
nouns = ('Boy', 'Girl', 'Bat', 'Ball')
verbs = ('hit', 'saw', 'liked')
prepositions = ('with', 'by')

def sentence():
    return nounPhrase() + ' ' + verbPhrase()

def nounPhrase():
    return random.choice(articles) + ' ' + random.choice(nouns)

def verbPhrase():
    return random.choice(verbs) + ' ' + nounPhrase() + ' ' + \
        prepostionalPhrase()

def prepostionalPhrase():
    return random.choice(prepositions) + ' ' + nounPhrase()

def main():
    number = int(input('Enter the number of sentences: '))
    for count in range(number):
        print(sentence())

if __name__ == '__main__':
    main()