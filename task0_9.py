def make_vowel(word):
    vowel = ""
    lowered_word = word.lower()
    print(lowered_word)
    for letter in word:
        if letter in ["a", "e", "i", "o", "u"]:
            if letter not in vowel:
                vowel = vowel + letter.lower() + ", "

    return vowel[:-2] if len(vowel) != 0 else print("no matches")


ans = make_vowel("Umuzie")

print("Vowels:", ans)
