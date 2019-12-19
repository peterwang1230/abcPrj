import math
import pandas as pd

from elasticsearch import Elasticsearch
# import Python's json library to format JSON responses
import json
import re
import string
import jieba
import jieba.analyse


def clean_text_round1(text):
    ''' Remove text in square brackets, remove punctuation and remove words containing numbers.'''
    text = re.sub(r'\r\n', '', text)
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub(r'\d', '', text) # 刪數字
    return text


def clean_text_round2(text):
    rule = re.compile(r"[^a-zA-Z0-9\u4e00-\u9fa5]")
    text = rule.sub('', text)
    return text

domain = "35.234.21.35"
port = 9200
index_name = 'jdcyuan_dm_201910'
idno = 1

try:
    # declare a client instance 'es' of the Python Elasticsearch library
    es = Elasticsearch([{'host': domain, 'port': port}])
    # info() method raises error if domain or conn is invalid
    # print(json.dumps(Elasticsearch.info(es), indent=4), "\n")

except Exception as err:
    print("Elasticsearch() ERROR:", err, "\n")
    # client is set to none if connection is invalid
    es = None

res = es.get(index=index_name, id=idno)
print(res['_source'])
print(res['_source']['JFULL'])
str_text = res["_source"]["JTITLE"] + res["_source"]["JFULL"]
str_text = clean_text_round1(str_text)
str_text = clean_text_round2(str_text)

# Jieba init files
jieba.load_userdict('userdict_tw.txt')    # 自定義詞庫
# jieba.set_dictionary('dict_tw.txt')    # 切換繁體詞庫


print("/".join(jieba.cut(str_text)))
print('總詞數 {}'.format(len(list(jieba.cut(str_text)))))

total = len(list(jieba.cut(str_text)))
get_cnt = math.ceil(total*0.1)  #向上取整
print('從 %d 中取出 %d 個詞'% (total, get_cnt))
keywords_top1 = jieba.analyse.extract_tags(str_text, withWeight=True, topK=get_cnt)
print(keywords_top1 )
# print("/".join(keywords_top1))
print('關鍵詞數 {}'.format(len(keywords_top1)))