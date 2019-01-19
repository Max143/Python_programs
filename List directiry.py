# list all files in a directory in python

from os import listdir
from os.path import isfile, join

file_list = [f or f in listdir('/home/students') if isfile(join('/home/students', f))]

print(files_list) 
