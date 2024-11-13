def add_everything_up(a, b):
    try:
        print(a + b)
    except:
        print(a, b, sep='')

add_everything_up(4, 'string')
add_everything_up(2, 9)
add_everything_up('float', 3.14)
add_everything_up(3, 2.17)