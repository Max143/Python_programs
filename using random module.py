# python programs related to random module

print("Write a program to generate random number.")

import random
count = 0
while count < 10:
    print(random.randint(0,9))
    count += 1

# write a program for randrange()

print("write a program for randrange()")
print(random.randrange(100, 1000, 3))


# write a prorgam for randint()

print("write a program for randint.")

iter = 0
while iter < 20 :
    #get random numbers in range 0 through 9
    r = random.randint(0,9)
    print(r)
    iter += 1

# write a prorgam for choice()


# generate a random string from the list of string
print("Using choice() function")

my_list = ['Python', 'Java', 'C++', 'GO', 'swift']

print(random.choice(my_list))




# generate a random number from the list

print(random.choice(['1', '234', '3324', '75344']))




      
# generate a random number from a uniformely distributed type

print(random.choice((1.1, -5, 6, 7, 4)))



# write program for shuffle function


from random import shuffle

my_list = ['11', '4', '232', '54334', '53']

shuffle(my_list)
print(my_list)


mylist = ['20', '16', '10', '5']
random.shuffle(mylist)
print(mylist)







# Write a python program for random.sample(collection, Random list, length)

print("Write a python program for random.sample(collection, Random list, length.)")


from random import sample

# select three character from a string
print(sample("Python", 3))

# randomly select a list of three elements from a base tuple

my_tuple = (32,443,443,34343,5344,3443,343,34434)
print(sample(my_tuple, 3))

# randomly select a list of three elements from a base list

my_list = ['Mansi', 'Manish', 'Ashi', 'Mak', 'Jessica', 'Aaron']    
print(my_list)
print(sample(my_list, 4))

# randomly select a subet of size three from a given set of numberes

my_sets = {111,3343,3434,3434,34334,53433,34434}
print(my_sets)
print(sample(my_sets, 4))

# randomly select a subset fo size three from a given set of string
my_string = {'Manish', 'Mansi', 'Mak', 'Ashi', 'Jessica'}
print(my_string)
print(sample(my_string, 4))










# Python program random.random() function

print(random.random())



''''

# python program for random.uniform() function

l = 111; u= 999

guess = random.uniform(l,u)
print(guess)


lower = 1.0; upper = 2.0, fixed_per = 2

new_guess = random.uniform(lower, upper)
print(new_guess, fixed_per)

'''






























































