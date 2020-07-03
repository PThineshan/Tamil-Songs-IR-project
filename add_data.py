from elasticsearch import Elasticsearch

es = Elasticsearch(
    ['localhost'],
    port=9200
)


tamil_songs_file= open("tamil_songs_collection.txt",'r',encoding="utf8").read()
data = tamil_songs_file.splitlines(True)
i = 0
docs = {}
for line in data:
    line = ''.join(line.split())
    docs[i] = str(line)
    print(docs[i])
    es.index(index='song_index', doc_type='song', id=i, body=docs[i])
    i = i+1
