import nltk
from nltk.corpus import brown

file = open("words.txt", "r")
words = file.read()
words = words.upper()
words = words.split()
file.close()

freqs = nltk.FreqDist([w.lower() for w in brown.words()])
wordlist_sorted = sorted(words, key=lambda x: freqs[x.lower()], reverse=False)
print (wordlist_sorted)

file = open("newWords.txt", 'w')
for word in wordlist_sorted:
    file.write(word + "\n")

file.close()