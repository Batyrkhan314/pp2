'''Write a Python program to test whether a given path exists or not.
 If the path exist find the filename and directory portion of the given path. '''

import os

pathway = '/Users/batyrkhan/Desktop/c++/Lab3'

if(os.path.exists(pathway)):
    print(os.path.basename(pathway))
    print(os.path.dirname(pathway))
else:
    print('Does not exist')
