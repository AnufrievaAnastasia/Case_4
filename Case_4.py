"""Case-study #4 Text analysis
Developers:
Anufrieva A.
Zhuravleva A.
"""
import local as lc

text = input(lc.TXT_TEXT).lower()

count_sentens = text.count('. ') + text.count('! ') + text.count('? ') + text.count('?! ') + text.count('... ')
print(lc.TXT_SENTENCES, count_sentens)

count_words = len(text.split())
print(lc.TXT_WORDS, count_words)

vowel = ['a', 'e', 'i', 'o', 'u', 'у', 'е', 'ы', 'а', 'о', 'э', 'ё', 'я', 'и', 'ю']

count_syllables = 0
for letter in text:
    if letter in vowel:
        count_syllables += 1
print(lc.TXT_SYLLABLE, count_syllables)

ASL = count_words / count_sentens
print(lc.TXT_ASL, ASL)

ASW = count_syllables / count_words
print(lc.TXT_ASW, ASW)
