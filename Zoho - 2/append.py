def manual_append(lst, element):
    new_list = [0] * (len(lst) + 1) 
    for i in range(len(lst)):
        new_list[i] = lst[i]
    new_list[len(lst)] = element
    return new_list

my_list = [1, 2, 3]
my_list = manual_append(my_list, 4)
print(my_list)