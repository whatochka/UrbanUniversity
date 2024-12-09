def single_root_words(root_word, *other_words):
    same_words = [right_word for right_word in other_words if (root_word.lower() in right_word.lower()
                                                               or right_word.lower() in root_word.lower())]
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
