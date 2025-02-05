# exercise: Checking for duplicates in list:

some_list = {'a', 'b', 'c', 'b', 'd', 'm', 'n', 'n'}
some_list_2 = []

for i in some_list:
    if i not in some_list_2:
        some_list_2.append(i)
    else:
        print(i,end="")


for value in some_list:
    if some_list.count(value) > 1:
        if value not in some_list_2:
            some_list_2.append(value)

print(some_list_2)

