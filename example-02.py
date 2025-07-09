def short_long_words(words_list):
    long_word = max(words_list, key=len)
    short_word = min(words_list, key=len)
    return short_word, long_word

# Приклад використання
words = ["apple", "orange"]
result = short_long_words(words)
print(result)  

