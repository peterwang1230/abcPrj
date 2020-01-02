from elasticsearch import Elasticsearch

def make_query(keywords):
    qry_str = ""
    lst = keywords.keys()
    qry_str = ' OR '.join([ elem for elem in lst]) 
    return qry_str

def get_query(es, index_name, field, size, qry_str):
    res = es.search(index=index_name, body={
        "size": size, 
        "query": {
            "match": { 
                field : {
                    "query": qry_str
                }
            }
        }
    })   
    return res

if __name__ == "__main__":
    # make query and get result
    keywords = {
        '網咖': 0.494, 
        '咖啡包': 0.494, 
        '上手': 0.489, 
        '戒癮治療': 0.46299999999999997, 
        '二級毒品': 0.394
    }
    # qry_str = make_query(keywords)cls
    # print(qry_str)
    domain = "35.234.21.35"
    port = 9200
    index_name = 'jdcyuan_dm_201910'
    field = "JFULL"
    size = 0
    es = Elasticsearch([{'host': domain, 'port': port}])
    qry_str = make_query(keywords)
    res = get_query(es, index_name, field, size, qry_str)

    print(res)