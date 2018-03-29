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


input_text_txt = load_txt(filename)
input_text_tokens = nltk.word_tokenize(input_text_txt)

# Pre-processing tokens
input_text_tokens_without_punctuation = [t.lower() for t in input_text_tokens if t.isalnum()]
input_text_word_stems = [nltk.PorterStemmer().stem(w) for w in input_text_tokens_without_punctuation]

print(filename, "lexical diversity: ", ttr(input_text_word_stems, input_text_tokens_without_punctuation))
