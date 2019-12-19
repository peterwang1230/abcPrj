import a4_jdc_es_corpus as escps
import pandas as pd
import pickle

domain = "35.234.21.35"
port = 9200
index_name = 'jdcyuan_dm_201910'
size = 5

pickle_in = open("df_pickle", "rb")
df1 = pickle.load(pickle_in)

print(df1)

df2 = escps.create_corpus(domain, port, index_name, size)
print(df2)

df = pd.concat([df1, df2])
# df.reset_index(inplace=True)
print(df)

pickle_out = open("df_pickle", "wb")
pickle.dump(df, pickle_out)
pickle_out.close()