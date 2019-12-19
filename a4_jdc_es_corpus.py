# IDF语料库就是 jieba 官方在大量文本的基础上，通过计算得到的一个 idf 字典，其 key 为分词之后的每个词，其 value 为 每个词的IDF数值。
# 读取文本文件，分词，去停用词，得到 all_dict 字典，字典的键是 word，字典的值是包含 word 的文档的个数。
# line 是单个文档

import pandas as pd
import pickle
# import the elasticsearch client library
from elasticsearch import Elasticsearch
import re
import string
import jieba.analyse
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer


def clean_text_round1(text):
    ''' Remove text in square brackets, remove punctuation and remove words containing numbers.'''
    text = re.sub(r'\r\n', '', text)
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub(r'\d', '', text)  # 刪數字
    return text


def clean_text_round2(text):    # 英數字及中文字
    rule = re.compile(r"[^a-zA-Z0-9\u4e00-\u9fa5]")
    text = rule.sub('', text)
    return text

domain = "35.234.21.35"
port = 9200
index_name = 'jdcyuan_dm_201910'
size = 5

def create_corpus(domain, port, index_name, size):
    try:
        # declare a client instance 'es'
        es = Elasticsearch([{'host': domain, 'port': port}])
        # info() method raises error if domain or conn is invalid print the result
        # print(json.dumps(Elasticsearch.info(es), indent=4), "\n")

    except Exception as err:
        print("Elasticsearch() ERROR:", err, "\n")
        # client is set to none if connection is invalid
        es = None

    all_docs = {}

    res = es.search(index=index_name, body={"size": size, "query": {"match_all": {}}})
    # print("Got %d Hits:" % res['hits']['total']['value'])
    i = 0
    for hit in res['hits']['hits']:
        i = i + 1
        # print(hit["_source"]["JFULL"])
        strJFull = hit["_source"]["JFULL"]
        strJFull = clean_text_round1(strJFull)
        strJFull = clean_text_round2(strJFull)
        all_docs[str(i)] = '  '.join(jieba.cut(strJFull, cut_all=False))

    # for item in all_docs.items():
    #     print(item)

    # Generate df from all_docs dict
    df = pd.DataFrame(list(all_docs.values()), columns=['JFULL'])
    # print(df)
    return df


df = create_corpus(domain, port, index_name, size)
print(df)
pickle_out = open("df_pickle", "wb")
pickle.dump(df, pickle_out)
pickle_out.close()

