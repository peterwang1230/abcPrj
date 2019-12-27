import pandas as pd
import pickle
import a4_jdc_es_corpus as escps
import re
import string
import jieba.analyse

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

# jieba.set_dictionary("dict.txt.big")
jieba.load_userdict("userdict_tw.txt")

pickle_in = open("jfull_pickle", "rb")
df = pickle.load(pickle_in)
pickle_in.close()

docs = df['JFULL'].tolist()
# print(docs)

#
stpwrdpath = "stopwords_tw.txt"  # current dir
with open(stpwrdpath, 'rb') as fp:
    stopwords = fp.read().decode('utf-8-sig')  # 停用詞提取

#
stpwrdlst = stopwords.splitlines()  # 將停用詞表轉換爲list
# print(stpwrdlst)

cv = CountVectorizer(max_df=0.85, stop_words=stpwrdlst)  # 創建詞袋數據結構
word_count_vector = cv.fit_transform(docs)  # 詞頻矩陣
#print(word_count_vector)
#print(word_count_vector.toarray())

# create document term matrix
dtm = pd.DataFrame(word_count_vector.toarray(), columns=cv.get_feature_names())
dtm.index = df.index
print(dtm)
# print("\n=====dtm=====")
# for col in dtm.columns: 
#     print(col) 

# import os
# kwsFile = open('kws.txt', 'w')
# kwsFile.write('Hello world!\n')
# kwsFile.close()
