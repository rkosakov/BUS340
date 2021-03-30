def isPalidrome(s):
    
    return isPalidromeHelper(s, 0, len(s) - 1)

def isPalidromeHelper(s, low, high):
    if (high <= low):
        return True 
    elif s[low] != s[high]:
        return False
    else:
        return isPalidromeHelper(s, low + 1, high - 1)

def main():
    print('Is moon a palidrome?', isPalidrome('moon'))
    print('Is noon a palidrome?', isPalidrome('noon'))
    print('Is ab a palidrome?', isPalidrome('ab'))

main()