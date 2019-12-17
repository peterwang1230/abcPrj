import pandas as pd

url = 'http://data.judicial.gov.tw/'    # starting url
lst = pd.read_html(url)  # get list of tables
# print(len(lst))

df = lst[1]  # get the archive table
print(df)
