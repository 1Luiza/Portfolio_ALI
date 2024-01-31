"""
В большой текстовой строке text подсчитать количество встречаемых слов и
вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.

Слова разделяются пробелами, апостроф не считается за пробел.
Такие слова как don t, it s, didn t итд (после того, как убрали знак препинания
апостроф) считать двумя словами.

Отсортируйте по убыванию значения количества повторяющихся слов.

Мой вариант:
import re
from collections import Counter

def count_words(text):
    # Replace apostrophes with spaces
    text = re.sub(r"'\s", " ", text)
    # Split text into words
    words = re.findall(r'\b[a-zA-Z]+\b', text)
    # Remove punctuation and convert to lowercase
    words = [word.lower() for word in words]
    # Count the frequency of each word
    word_counts = Counter(words)
    # Return the 10 most common words
    return word_counts.most_common(10)


# Example usage:
text = "Python is an interpreted high-level programming language for
general-purpose programming. Created by Guido van Rossum and first released
in 1991, Python's design philosophy emphasizes code readability with its
notable use of significant whitespace."
print(count_words(text))
"""

text = "Python is an interpreted high-level programming language for " \
       "general-purpose programming. Created by Guido van Rossum and first " \
       "released in 1991, Python's design philosophy emphasizes code " \
       "readability with its notable use of significant whitespace."

# Удаляем знаки препинания и приводим текст к нижнему регистру
cleaned_text = ''.join(
    char.lower() if char.isalpha() or char.isspace() else ' ' for char in text)

# Разбиваем текст на слова и считаем их количество
words = cleaned_text.split()
word_counts = {}

for word in words:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1

# Получаем 10 самых часто встречающихся слов
top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]

print(top_words)
