'''Write a Python program to delete file by specified path. 
Before deleting check for access and whether a given path exists or not.'''

import os 

pathway  = 'path_name'

if os.path.exists(pathway):
    os.remove(pathway)
