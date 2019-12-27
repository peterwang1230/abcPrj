import pandas as pd

def adj_weight(key, filename='userdict_tw.txt'):
    df = pd.read_csv(filename, header=None, encoding = 'utf8')
    s = set(df[0])  # dataframe column:0 series to set 
    val = 0
    if key in s:
        val = 0.3
    return val

if __name__ == "__main__":
    print(adj_weight("毒品危害"))   # The main function goes here.

