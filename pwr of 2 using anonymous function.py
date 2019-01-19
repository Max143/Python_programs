# Write a python prorgam to display power of 2 usinng anonymous function

'''

Anonymous function is also called as Lambda function

These function are without name.

It's like same as normal function because it does not use def keyword
  
         Que. How to use it?

   syntax - lambda funtion : expression

         where, this have no. or argument
          but only use single expression.

        Que. When to use it?

        Use where nameless function is required
                  when you need to define a another function under a already defined function

                  It is used where ever  functio object are required.
'''

print("Here the example")

def  double(x):
    return x*2
    double = lambda y : y*2
    

print(double(5))
print(double(6))

#while True:
   # double = lambda x : x*2
 #   print(double(int(input("Enter an integer: "))))


'''


              lambda function used with built-function
              like filter() and map()


    filter() : In python, what it does it takes a fucntion and a list as argument

    map() : In python, a function is called with all the items in the list and  a new list is returned with contains item returnd by that function for each item.
    
                


    Let's talk about filter () and map() function
    with examples.


'''

# write a program to filter out a list of number in even without using a normal function def (use anonymous function)
'''
print("write a program to filter out a list of number in even without using a normal function def (use anonymous function")

my_list1 = [1,2,3,4,5,6,7,8,9,10]

new_list1 = list(filter(lambda x : (x/2==0), my_list1))
print(new_list1)


'''


# write a program to double each item in a list using map()

my_list = [1,2,3,4,5,6,7,8,9,10]

new_list = list(map(lambda x: x*2, my_list)) 

print(new_list)

for i in (new_list):
    print(i)






















