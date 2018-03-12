#!/usr/bin/python
import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
import getopt
import sys

TREE_BANK_ADJECTIVE_TAG_PREFIX = 'J'
TREE_BANK_VERB_TAG_PREFIX = 'V'
TREE_BANK_NOUN_TAG_PREFIX = 'N'
TREE_BANK_ADVERB_TAG_PREFIX = 'R'
OTHER = "other"
NUMBER_OF_DECIMAL_PLACES = 2

def load_txt(file):
    with open(file) as f:
        return ' '.join(line.strip() for line in f.readlines())

def map_treebank_tag_to_wordnet_tag(treebank_tag):
    if treebank_tag[1][0] == TREE_BANK_ADJECTIVE_TAG_PREFIX:
        return wordnet.ADJ;
    elif treebank_tag[1][0] == TREE_BANK_VERB_TAG_PREFIX:
        return wordnet.VERB
    elif treebank_tag[1][0] == TREE_BANK_NOUN_TAG_PREFIX:
        return wordnet.NOUN
    elif treebank_tag[1][0] == TREE_BANK_ADVERB_TAG_PREFIX:
        return wordnet.ADV
    else:
        return OTHER

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

text = load_txt(filename)

text_tokens = nltk.word_tokenize(text)
text_tokens_without_punctuation = [t.lower() for t in text_tokens if t.isalnum()]
pos_tagged_tokens_without_punctuation = nltk.pos_tag(text_tokens_without_punctuation)

pos_counts = {wordnet.ADJ: 0, wordnet.VERB: 0, wordnet.NOUN: 0, wordnet.ADV: 0, OTHER: 0}

for i in range (0, len(pos_tagged_tokens_without_punctuation)):
    pos_counts[map_treebank_tag_to_wordnet_tag(pos_tagged_tokens_without_punctuation[i])] + 1

for t in pos_tagged_tokens_without_punctuation:
    pos_counts[map_treebank_tag_to_wordnet_tag(t)] += 1

total = len(text_tokens_without_punctuation)

print("Adjectives: ", round((pos_counts[wordnet.ADJ] / total) * 100, NUMBER_OF_DECIMAL_PLACES), "%")
print("Verbs:", round((pos_counts[wordnet.VERB] / total) * 100, NUMBER_OF_DECIMAL_PLACES), "%")
print("Nouns: ", round((pos_counts[wordnet.NOUN] / total) * 100, NUMBER_OF_DECIMAL_PLACES), "%")
print("Adverbs: ", round((pos_counts[wordnet.ADV] / total) * 100, NUMBER_OF_DECIMAL_PLACES), "%")
print("Other: ", round((pos_counts[OTHER] / total) * 100, NUMBER_OF_DECIMAL_PLACES), "%")
