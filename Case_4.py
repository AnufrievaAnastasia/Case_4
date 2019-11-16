"""Case-study #4 Анализ текста
Разработчики:
Ануфриева А.
Журавлева А.
"""

text = input("Введите текст:").lower()

count_sentens = text.count('. ') + text.count('! ') + text.count('? ') + text.count('?! ') + text.count('... ')
print('Предложений:', count_sentens)

count_words = len(text.split())
print('Слов:', count_words)

vowel = ['a', 'e', 'i', 'o', 'u', 'у', 'е', 'ы', 'а', 'о', 'э', 'ё', 'я', 'и', 'ю']

count_syllables = 0
for letter in text:
    if letter in vowel:
        count_syllables += 1
print('Слогов:', count_syllables)

ASL = count_words / count_sentens
print('Средняя длина предложения в словах:', ASL)

ASW = count_syllables / count_words
print('Средняя длина слова в слогах:', ASW)
