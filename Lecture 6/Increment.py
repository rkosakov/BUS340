def main():
    x = 1
    print('Before the call, x is: ', x)
    increament(x)

def increament(n):
    n += 1
    print('\tn inside the function is, ', n) 

main()