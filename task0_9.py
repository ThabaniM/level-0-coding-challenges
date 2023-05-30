def make_vowel(word):
    vowel = ""
    for letter in word:
        if letter in ["a", "e", "i", "o", "u"]:
            if letter not in vowel:
                vowel = vowel + letter.lower() + ", "

    return vowel[:-2] if len(vowel) != 0 else print("no matches")


if __name__ == "__main__":
    vowel_made = make_vowel("Umuzie")
    print("Vowels:", vowel_made)