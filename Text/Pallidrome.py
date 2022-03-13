'''Check if Palindrome - Checks if the string entered by the user is a palindrome. 
That is that it reads the same forwards as backwards like “racecar” '''

def ispallidrome(word):
    if ' ' in word:
        word = word.replace(' ', '')
    
    # condition check 
    if word == word[::-1]:
        print(f'{word} is pallidrome')
    else:
        print(f'{word} is not pallidrome')

# ispallidrome("race car")