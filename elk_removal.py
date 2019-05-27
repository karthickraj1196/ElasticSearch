# -*- coding: utf-8 -*-
"""
Created on Fri May 24 16:25:35 2019

@author: pushparajkarthick_d
"""
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'Elasticsearch_host', 'port': 'ElasticSearch_Port'}])
#print(es.get(index='scicommon-*', id='rv2J0moByHW8pddMs9eo'))
#es.indices.delete(index='scicommon-2019.05.19')
index = es.indices.get_alias("Indices_name").keys()
list(index)
print(len(list(index)))
index = sorted(list(index))
length = len(list(index))
print(length)



#print(sorted(list_of_index.items(), key = lambda kv:(kv[1],kv[0])))
#print(list(index)[0])
#es.indices.delete(index=list(index)[0])



#length = 16 
while length > 15:
    i = 0
    index = es.indices.get_alias("qacommon-*").keys()
    list(index)
    length = len(list(index))
    index = sorted(list(index))
    print(list(index))
    print(list(index)[0])
    es.indices.delete(index=list(index)[0])
    length -= 1
    i +=1
#for i in length:
