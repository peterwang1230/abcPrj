import pandas as pd

def adj_weight(dict, filename='userdict_tw.txt'):
    df = pd.read_csv(filename, header=None, encoding = 'utf8')
    s = set(df[0])  # dataframe column:0 series to set 
    for key, val in dict.items():
	    if key in s:
	        dict[key] += 0.3
    return dict

if __name__ == "__main__":
    pass