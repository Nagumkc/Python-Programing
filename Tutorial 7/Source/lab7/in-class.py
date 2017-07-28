from nltk.corpus import wordnet as w
from nltk.tokenize import word_tokenize,sent_tokenize,wordpunct_tokenize
from nltk.stem import LancasterStemmer,WordNetLemmatizer
from nltk import pos_tag,ne_chunk,ngrams
from collections import Counter
s="Sport (British English) or sports includes all forms of competitive physical activity or games which,through casual or organised participation, aim to use, maintain or improve physical ability and skills while providing enjoyment to participants, and in some cases, entertainment for spectators.Usually the contest or game is between two sides, each attempting to exceed the other. Some sports allow a tie game; others provide tie-breaking methods, to ensure one winner and one loser. A number of such two-sided contests may be arranged in a tournament producing a champion. Many sports leagues make an annual champion by arranging games in a regular sports season, followed in some cases by playoffs. Hundreds of sports exist, from those between single contestants, through to those with hundreds of simultaneous participants, either in teams or competing as individuals. In certain sports such as racing, many contestants may compete, each against each other, with one winner."

res=w.synsets("sport")
print("wordnet\n",res)
tok=[word_tokenize(t) for t in sent_tokenize(s)]
print("tok\n",tok)
ste=LancasterStemmer()
print("stem\n")
for t in tok:
    print(ste.stem(str(t)))
print("pos\n")
print(pos_tag(str(tok)))
print("lemm\n")
l=WordNetLemmatizer()
for t in tok:
    print(l.lemmatize(str(t)))
print("ner\n")
ner=ne_chunk(pos_tag(wordpunct_tokenize(str(t))))
print(ner)
print("try gram\n")
ner=ngrams(t,3)

print(Counter(ner))
