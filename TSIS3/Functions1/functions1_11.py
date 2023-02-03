'''11. Write a Python function that checks whether a word or phrase is palindrome or not.
 Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam
'''


def checker(s):
    if s == s[::-1]:
        return True
    
    return False

string = input()
print(checker(string))