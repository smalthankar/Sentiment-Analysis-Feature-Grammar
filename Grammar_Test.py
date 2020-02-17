#from __future__ import print_function
import nltk
from nltk import grammar, parse

from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.tag import pos_tag

cp = parse.load_parser('feat_gram_project_3.fcfg', trace=1)

sent = "This is a nice book , but I loved it"

if "'s" in sent:
    sent = sent.replace("'s", " is")
if "'ve" in sent:
    sent = sent.replace("'ve", " have")
if "won't" in sent:
    sent = sent.replace("won't", "will not")

text = word_tokenize(sent)
print(nltk.pos_tag(text))


tokens = sent.split()
tokens

trees = cp.parse(tokens)

if trees:
    print("Tree Exists!")

tree_number = 1
for tree in trees:
    print('Tree ', tree_number)
    print(tree)
    tree_number+=1