i = 0
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5, ]

while i < len(my_list):
    if my_list[i] == 0:
        i += 1
    if my_list[i] <= -1:
            break
    print(my_list[i])
    i += 1
