import pandas as pd
import pickle
from pprint import pprint

# Gensim
import gensim
import gensim.corpora as corpora
# from gensim import corpora, models, similarities

pickle_in = open("jtitle_pickle", "rb")
df = pickle.load(pickle_in)
pickle_in.close()

docs = df['JTITLE'].tolist()
# print(docs)

# using set to generate unique elements 
# s_title = set([])
# for i in df['JTITLE']:
#     y = i.split()    # to list
#     s_title.update(y)
# print(s_title)

# remove common words and tokenize
stoplist = set('等 罪 因 其 案'.split())
texts = [[word for word in doc.split() if word not in stoplist]
          for doc in docs]

# print(texts)


# Create Dictionary
id2word = corpora.Dictionary(texts)
for keys,values in id2word.items():
    print(keys, values)


dictionary = corpora.Dictionary(texts)
# Human readable format of corpus (term-frequency)

dict_out = open("corpus_raw.dict", "wb")
dictionary.save('dict_out') # store the dictionary, for future reference
dict_out.close()
# print(dictionary)
for keys,values in dictionary.items():
    print(keys, values)

# print(dictionary.token2id)

# corpus = [dictionary.doc2bow(text) for text in texts]
# corpora.MmCorpus.serialize('dict_out.mm', corpus) # store to disk, for later use
# print(corpus)


# # Build LDA model
# lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
#                                            id2word=id2word,
#                                            num_topics=3, 
#                                            random_state=100,
#                                            update_every=1,
#                                            chunksize=100,
#                                            passes=10,
#                                            alpha='auto',
#                                            per_word_topics=True)

# # lda_model = gensim.models.ldamodel.LdaModel(corpus, id2word=id2word, num_topics=10)
# pprint(lda_model.print_topics())

# # Plotting tools
# import pyLDAvis
# import pyLDAvis.gensim  # don't skip this
# import matplotlib.pyplot as plt
# # Visualize the topics
# # pyLDAvis.enable_notebook()
# vis = pyLDAvis.gensim.prepare(lda_model, corpus, id2word)

# 土# vis
