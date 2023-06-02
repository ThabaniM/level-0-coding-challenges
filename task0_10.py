def common_characters(word1, word2):
    final_char = ""
    if word1 == word2:
        return word1

    shorter_word = min(word1, word2, key=len)
    longer_word = max(word1, word2, key=len)

    for char in shorter_word:
        if longer_word.find(char) != -1 and final_char.count(char) <= 1:
            final_char = final_char + char + ", "
    
    if len(final_char) != 0:
        return final_char[:-2]
    else: return 'There were no common characters found'


if __name__ == "__main__":
    characters_in_common = common_characters("zzzz", "computers")
    print("Common letters:", characters_in_common)
