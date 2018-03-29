# HLT

### lexical_diversity_calculator.py

Uses [type/token ratio](http://www.lexically.net/downloads/version6/HTML/type_token_ratio_proc.htm) to calculate lexical diversity.

Pre-processing includes tokenising input, removing stopwords and using nltk's [Porter Stemmer](http://www.nltk.org/_modules/nltk/stem/porter.html) to obtain word stems.

Run:

> python3 lexical_diversity_calculator.py -n SampleTexts/EdSheeranLyrics.txt

Output

> EdSheeranLyrics.txt lexical diversity:  0.2112

### word_proportions.py

Finds proportions of adjectives, verbs, nouns and adjectives in a text. Categorises remaining types as 'other'.

Preprocessing involves tokenisation of input and removal of stopwords.

Uses nltk's part of speech (POS) tagger to assign parts of speech to input text tokens. Given that nltk's POS tagger was trained using the Treebank Corpus it uses the [Treebank tag set](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html). This script will map the Treebank tags to [WordNet tags](http://www.nltk.org/_modules/nltk/corpus/reader/wordnet.html) before giving the proportions as output.

Run:

>python3 word_proportions.py -n SampleTexts/GulliversTravels.txt

Output:

>Adjectives:  7.75 %  
Verbs: 17.18 %  
Nouns:  22.76 %  
Adverbs:  5.6 %  
Other:  46.7 %
