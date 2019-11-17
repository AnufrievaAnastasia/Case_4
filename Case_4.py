"""Case-study #4 Text analysis
Developers:
Anufrieva A.(67%)
Zhuravleva A.
"""
from textblob import TextBlob, Word, Blobber
from textblob.classifiers import NaiveBayesClassifier
from textblob.taggers import NLTKTagger
from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel

import local as lc

text = input(lc.TXT_TEXT).lower()

count_sentens = text.count('.') + text.count('!') + text.count('?') + text.count('?!') + text.count('...')
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

FRE_RU = 206.835 - (1.3 * ASL) -(60.1 * ASW)
FRE_EN = 206.835 - (1.015 * ASL) - (84.6 * ASW)

text = TextBlob(text)
if text.detect_language() == 'en':
    pol = text.sentiment.polarity
    sub = text.sentiment.subjectivity
    print(lc.TXT_FRE_EN_0, FRE_EN)
    if 90 <= FRE_EN <= 100:
        print(lc.TXT_FRE_EN_1)
    elif 65 <= FRE_EN < 90:
        print(lc.TXT_FRE_EN_2)
    elif 30 <= FRE_EN < 65:
        print(lc.TXT_FRE_EN_3)
    else:
        print(lc.TXT_FRE_EN_4)
    print(lc.TXT_OBJ, (1 - sub) * 100, '%')
    print(lc.TXT_TON, pol)