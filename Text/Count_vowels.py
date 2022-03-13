'''Count Vowels - Enter a string and the program counts the number of vowels in the text. 
For added complexity have it report a sum of each vowel found.'''

def count_vowels(word):
    # empty dic for adding vowels count
    vowels_dic = {}

    vowels = ('a', 'e', 'i', 'o', 'u')

    for i in vowels:
        if i in word:
            num = word.count(i)
            vowels_dic[i] = num
    print(vowels_dic)

# count_vowels('pig dog pupooi')


    
