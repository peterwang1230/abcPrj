import a4_jdc_es_corpus as escps
import pandas as pd
import pickle

domain = "35.234.21.35"
port = 9200
index_name = 'jdcyuan_dm_201910'
size = 5

pickle_in = open("jfull_pickle", "rb")
df_jfull = pickle.load(pickle_in)
pickle_in.close()

print(df_jfull)

# Add new corpus
df_new = escps.create_corpus(domain, port, index_name, "JFULL", size)
print(df_new)

df = pd.concat([df_jfull, df_new])
# df.reset_index(inplace=True)
print(df)

pickle_out = open("jfull_pickle", "wb")
pickle.dump(df, pickle_out)
pickle_out.close()