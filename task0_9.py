def make_vowel(word):
    vowel = ''
    for letter in word:
        letter = letter.lower()
        if letter == 'a' or letter == 'o' or letter == 'u' or letter == 'i':
            if letter not in vowel:
                vowel = vowel + letter.lower() + ', '

    return vowel

ans = make_vowel('Thabani') 

print(ans[:-2]) if len(ans) != 0 else print('no matches')