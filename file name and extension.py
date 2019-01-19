"""
Input a filename and print the extension of that

"""

filename = input("Input the Filename : ")
file_extension = filename.split(".")
print("The extension of the file is  : " + repr(file_extension[-1]))


