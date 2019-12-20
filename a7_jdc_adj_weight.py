import pickle

pickle_in = open("jtitle_pickle", "rb")
df = pickle.load(pickle_in)
pickle_in.close()

# print(df)
define adj_weight(key):
    s_title = set([])
    for i in df['JTITLE']:
        y = i.split(' ')    # to list
        s_title.update(y)
    # print(s_title)
    if key in s_title:
        return 0.3
    else:
        return 0