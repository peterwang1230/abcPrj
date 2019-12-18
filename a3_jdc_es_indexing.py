import os
from os import listdir
from os.path import expanduser
from os.path import isfile, join
import json
import pprint
from elasticsearch import Elasticsearch

def get_json(srcDir, filename):
    json_file = open(srcDir + '/' + filename, "r", encoding="utf-8")
    dict = json.load(json_file)
    json_file.close()
    return dict

def insert_dir_rc(srcDir):
    i = 0
    str_target = '刑事'
    for folderName, subfolders, filenames in os.walk(srcDir):
        for filename in filenames:
            if folderName.find(str_target) != -1:
                i = i + 1
                print(str(i) + ' FILE INSIDE ' + folderName + ': ' + filename)
                if filename.endswith(".json"):
                    json_file = open(folderName + '/' + filename, "r", encoding="utf-8")
                    dict = json.load(json_file)
                    json_file.close()
                    # pp = pprint.PrettyPrinter(indent=4)
                    # pp.pprint(dict)

                    res = es.index(index=index_name, id=i, body=dict)
                print('')

    print(i)

# Connect to the elastic cluster
# es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
es = Elasticsearch([{'host': '35.234.21.35', 'port': 9200}])
print(es)

home = expanduser("~")
srcDir = home + '/' + 'JDCYuan/201910/'
idxDir = home + '/' + 'JDCYuan/utility'
pp = pprint.PrettyPrinter(indent=4)

# Create index
index_name = 'jdcyuan_dm_201910'
print("creating {} index...".format(index_name))
dict = get_json(idxDir, 'jdcyuan_index.json')
# pp.pprint(dict)
es.indices.create(index=index_name, body=dict)
insert_dir_rc(srcDir)