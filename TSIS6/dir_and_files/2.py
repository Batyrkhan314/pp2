'''Write a Python program to check for access to a specified path.
 Test the existence, readability, writability and executability of the specified path'''

import os 

pathway = '/Users/batyrkhan/Desktop/c++/Lab3'

print('Existence:', os.access(pathway, os.F_OK))
print('Readability:', os.access(pathway, os.R_OK))
print('Writability:', os.access(pathway, os.W_OK))
print('Executability:', os.access(pathway, os.X_OK))