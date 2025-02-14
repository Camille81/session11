from string import punctuation

import requests
from django.core.signals import request_started

link = "https://www.gutenberg.org/cache/epub/18143/pg18143.txt"
punctuation = ",.?!=-(){};"
result = requests.get(link)
print(result.text)
unique_words = {}
lines = result.text.splitlines()
for line in lines:
    for p in punctuation:
        line = line.replace(p," ")
    words = line.split()
    for word in words:
        word = word.lower()
        if len(word) > 4:
            unique_words[word] = unique_words.get(word, 0) + 1

print(unique_words["roméo"])
print(unique_words["juliette"])

freq = list(unique_words.values())
freq.sort(reverse=True)
freq = freq[:10]
print(freq)
print("the most common 10 words are: ")
for f in freq:
    for key, value in unique_words.items():
     if value == f:
        print(key)
