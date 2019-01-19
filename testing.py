list_1 = [1,2,3,4,5,6,7,8,9,45,76,23,54]

list_2 = [2,3,4,5,6,12,15,16,9,7,46,76]

# question : list of common element of both lists

new_list = []

for element in list_1:
    if element in list_2:
        new_list.append(element)

print(new_list)
