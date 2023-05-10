def common_characters(word1, word2):
    final_char = ''
    if word1 == word2:
        raise Exception('Word1 shouldn\'t be the same as word2')

    if len(word1) <= len(word2):
        for char in word1:
            if word2.find(char) != -1 and final_char.count(char) <= 1:
                final_char = final_char + char + ', ' 
    else: 
         for char in word2:
            if word1.find(char) != -1 and final_char.count(char) <= 1:
                final_char = final_char + char + ', ' 

    return final_char[:-2] if len(final_char) != 0 else print('no matches')

if __name__ ==  "__main__":
    ans = common_characters('house', 'computers') 
    print('Common letters:', ans)