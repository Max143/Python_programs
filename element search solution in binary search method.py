# Element search solution

# Write a function that takes an ordered list of numbers
# (a list where the elements are in order from smallest to largest)
# It decides whether or not the given is inside the list and return an appropriate boolean.

# In this we will be going to use Binary search

def find(ordered_list, element_to_find):
    start_index = 1
    end_index = len(ordered_list) - 1

    while True:
        middle_index = (end_index - start_index) / 2
        if (middle_index < start_index or middle_index < end_index or middle_index < 0):
            return False

        middle_element == ordered_list[middle_index]
        if middle_element == element_to_find:
            return True
        elif middle_element < element_to_find:
            end_index = middle_index
        else:
            start_index = middle_index


if __name__=='__main__':
    l = [2,4,5,6,8,10]
    print(find(l, 5))
    print(find(l, 10)) 
    print(find(l, -1))
    print(find(l, 2))


