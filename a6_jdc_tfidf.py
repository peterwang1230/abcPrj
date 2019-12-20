import pandas as pd
import pickle
import a4_jdc_es_corpus as escps
import jieba.analyse

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

# jieba.set_dictionary("dict.txt.big")
jieba.load_userdict("userdict_tw.txt")

pickle_in = open("jfull_pickle", "rb")
df = pickle.load(pickle_in)
pickle_in.close()

# print(df)

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
# print(word_count_vector)
# print(word_count_vector.toarray())

# create document term matrix
dtm = pd.DataFrame(word_count_vector.toarray(), columns=cv.get_feature_names())
dtm.index = df.index
# print("\n=====dtm=====")
# print(dtm)

# TfidfTransformer to Compute Inverse Document Frequency (IDF)
# 計算 idf
tfidf_transformer = TfidfTransformer(smooth_idf=True, use_idf=True)
tfidf_transformer.fit(word_count_vector)


# Helper Functions
def sort_coo(coo_matrix):
    tuples = zip(coo_matrix.col, coo_matrix.data)
    return sorted(tuples, key=lambda x: (x[1], x[0]), reverse=True)


def extract_topn_from_vector(feature_names, sorted_items, topn=10):
    """get the feature names and tf-idf score of top n items"""

    # use only topn items from vector
    sorted_items = sorted_items[:topn]

    score_vals = []
    feature_vals = []

    # word index and corresponding tf-idf score
    for idx, score in sorted_items:
        # keep track of feature name and its corresponding score
        score_vals.append(round(score, 3))
        feature_vals.append(feature_names[idx])

    # create a tuples of feature,score
    # results = zip(feature_vals,score_vals)
    results = {}
    for idx in range(len(feature_vals)):
        results[feature_vals[idx]] = score_vals[idx]

    return results


# 讀入測試文件
# get the document that we want to extract keywords from
str1 = '案例-接案紀錄： 當事人從北屯區部子里太原路三段全家出來因攜帶毒品咖啡包被抓 \
       檢警問東西來源、有無使用 \
       東西來源是自己聯絡上手拿到的，不認識  \
       之前有在使用，但成分內容不清楚 \
       警察驗出是二級毒品 \
       在檢警回答：在網咖不認識的人問我需不需要 在全家被攔查就主動交付 \
       第一次吸食 \
       訴求要戒癮治療不要勒戒'
str1 = escps.clean_text_round1(str1)
str1 = escps.clean_text_round2(str1)

doc = '  '.join(jieba.cut(str1, cut_all=False))
# print(type(doc))
# print(doc)

# 找出關鍵字 top5
# generate tf-idf for the given document
# you only needs to do this once, this is a mapping of index to
feature_names = cv.get_feature_names()
tf_idf_vector = tfidf_transformer.transform(cv.transform([doc]))
# print(tf_idf_vector)

# sort the tf-idf vectors by descending order of scores
sorted_items = sort_coo(tf_idf_vector.tocoo())
# extract only the top n; n here is 10
keywords = extract_topn_from_vector(feature_names, sorted_items, 25)

# now print the results
print("\n===Keywords item===")
print(keywords)
# for i in keywords.items():
#     print(i)

# add a dummy breakpoint for keywords print
# print()     

