def single_root_words(root_words, *other_words):
    same_words = []
    root_words = root_words.lower()
    for word in other_words:
        word = word.lower()
        if root_words in word or word in root_words:
            same_words.append(word)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
