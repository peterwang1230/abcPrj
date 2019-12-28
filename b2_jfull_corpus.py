import pandas as pd
import pickle
from gensim import corpora, models, similarities
pickle_in = open("jfull_pickle", "rb")
df = pickle.load(pickle_in)
pickle_in.close()

docs = df['JFULL'].tolist()
# print(docs)
import os
kwsFile = open('jfull.txt', 'w', encoding="utf-8")
i = 0
for doc in docs:
    i = i + 1
    if i > 10:
        break
    kwsFile.write(doc)
    kwsFile.write('\n')
kwsFile.close()

