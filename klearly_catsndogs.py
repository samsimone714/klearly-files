# Sam Simone
# Klearly Coding Excersize

def catsndogs(n):
    '''for every number from 1 to n print print 'dog' for every multiple of 3,
    print 'cat' for every multiple of 5, and print 'dogcat' for multiples of both.
    otherwise merely print the number'''

    for i in range(1,n+1):
        if i%3 == 0: 
            if i%5 == 0: 
                print('dogcat')
            else: print('dog')
        elif i%5 == 0: print('cat')
        else: print(i)
