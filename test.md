# hbirPrj
HBIR 海選計畫

# List 司法院判決開放資料
survey 判決書 open data files  
a0_jdc_rarfiles.py

# 網路爬蟲下載司法院判決開放資料 
a1_jdc_getrarfiles.py  
司法院 open data 從 1996/01 ~ 2019/10 計286 壓縮檔 （.rar files)

# 解壓縮司法院判決書開放資料
a2_jdc_unrarfiles.py 產生 .json files  
計 1491 萬餘筆，82.9 GB

# Google Cloud 架設 Elastic Search and Kibana 伺服器
ES: http://35.234.21.35:9200/
Kibana： http://35.234.21.35:5601/app/kibana

# 建索引
jdcyuan_index.json

# 建刑事索引資料庫 (10 月)
概念驗証刑事案件: 27087 案例  
index_name = 'jdcyuan_dm_201910'  
a3_jdc_es_indexing.py

# 調整並建立判決書中文斷詞詞庫
Kibana Client 
user_dic 

# 讀取 ES NoSQL DB，建立判決書語料庫 （Corpus)
a4_jdc_es_corpus.py  
pickle out for integration.

# 新增語料庫
a5_jdc_add_corpus  
df.reset_index(inplace=True) 計數
 
# 關鍵字擷取
stop_words_tw.txt 調校  
a6_jdc_tfidf.py 關鍵字調校 Top 10

# 調整權重
a7_jdc_adj_weight.py

