# цикл while

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0

while index < len(my_list):
    elt = my_list[index]
    if elt > 0:
        print(elt)
        index += 1
    elif elt == 0:
        index += 1