# Task 0.10
# Make a function that takes two strings as input, and outputs the common characters/letters
#  that they share.

# For example, Input: ‘house’, ‘computers’ . Output: ‘Common letters: o, u, e, s’)
word1 = input('Enter word 1: ')
word2 = input('Enter word 2: ')

def common_characters(word1, word2):
    final_char = ''
    if len(word1) <= len(word2):
        for char in word1:
            print(final_char.count(char))
            if word2.find(char) != -1 and final_char.count(char) <= 1:
                final_char = final_char + char + ', ' 
    else: 
         for char in word2:
            if word1.find(char) != -1 and final_char.count(char) <= 1:
                final_char = final_char + char + ', ' 
    return final_char

ans = common_characters(word1, word2) 
print(ans[:-2]) if len(ans) != 0 else print('no matches')