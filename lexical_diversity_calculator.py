#!/usr/bin/python
import nltk
from nltk.corpus import stopwords
import getopt
import sys

def load_txt(file):
    with open(file) as f:
        return ' '.join(line.strip() for line in f.readlines())

def ttr(stem_tokens, all_words_tokens):
    return len(set(stem_tokens)) / len(all_words_tokens)

try:
    opts, args = getopt.getopt(sys.argv[1:], 'n:')
except getopt.GetoptError:
    print("Invalid input.")
    sys.exit(2)

filename = ""

for opt, arg in opts:
    if opt in ('-n'):
        filename = arg
        if (filename == ""):
            print("Filename required.")
            sys.exit(2)
    else:
        print("Invalid Input")
        sys.exit(2)

if (filename == ""):
    print("Filename required.")
    sys.exit(2)


song_lyrics_txt = load_txt(filename)
song_lyrics_tokens = nltk.word_tokenize(song_lyrics_txt)

# Pre-processing tokens
song_lyrics_tokens_without_punctuation = [t.lower() for t in song_lyrics_tokens if t.isalnum()]
song_lyrics_word_stems = [nltk.PorterStemmer().stem(w) for w in song_lyrics_tokens_without_punctuation]

print(filename, "lexical diversity: ", ttr(song_lyrics_word_stems, song_lyrics_tokens_without_punctuation))
