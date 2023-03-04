'''Write a Python program to list only directories, files and all directories, files in a specified path. '''

import os

path = '/Users/batyrkhan/Desktop/c++'

print("Directories:")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("\nFiles:")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print("\nAll :")
print([ name for name in os.listdir(path)])