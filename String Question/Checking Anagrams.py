'''
python program to check whether the entered strings are anagrams or not

anagrams means

exmple: listen == silent

'''

s1 = input("Enter the First string: ")

s2 = input("Enter the second string: ")


if sorted(s1) == sorted(s2):
    print("Anagrams")
else:
    print("Not Anagrams")
