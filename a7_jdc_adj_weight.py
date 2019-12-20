import pickle

pickle_in = open("jtitle_pickle", "rb")
df = pickle.load(pickle_in)
pickle_in.close()

# print(df)
def adj_weight(key, df):
    s_title = set([])
    for i in df['JTITLE']:
        y = i.split(' ')    # to list
        s_title.update(y)
    # print(s_title)
    val = 0
    if key in s_title:
        val = 0.3
    return val

if __name__ == "__main__":
    print(adj_weight("毒品危害", df))   # The main function goes here.

