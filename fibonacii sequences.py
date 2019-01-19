# write a python programs to print the fibonacci sequence

'''

what is fibonaci sequence?

It is just a sequence of integer like

 0,1,1, 2,3,5,8,13,21 etc

 the
 {Nth term = (Nth-1) - (Nth-2)}

 '''

nterms = int(input("Enter up to how many terms: "))

n1 = 0
n2 = 1

count = 0

# check if the numnber of terms is valid

if nterms < 0:
    print("Invalid input, please input positive integer")
elif nterms == 1:
    print("fibonacci sequences upto ", nterms, ": ")
    print(n1)
else:
    print("Fibnonacii sequences upto ", nterms, ": ")
    while count < nterms:
        print(n1, end='-')
        nth = n1 + n2
      # update value
        n1 = n2
        n2 = nth
        count += 1

    
