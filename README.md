# Tamil-Songs-Search-Engine
## Description
There are nearly about 4000 Tamil songs collected from 'https://www.tamilpaa.com/tamil-movies-list'. These collected songs are included tamil_corpus.txt. These songs have 9 meta data such as movie, song, music, lyrics, singers, year, actors, song_url and full_lyrics. Randomly selected nearly 1000 songs data are fully translated to Tamil using python translate library. There is a search engine developed by using Elastic Search and Kibana.

## Sample Movie Song JSON format
```json
{
  "movie": "காலா", 
  "song": "செம Weight", 
  "music": "சந்தோஷ் நாராயணன்", 
  "lyrics": "அருண்ராஜா காமராஜ், டோபடெலிக்ஸ்", 
  "singers": "ஹரிஹராசுதன், சந்தோஷ் நாராயணன்",    
  "year": "2018", 
  "actors": "ரஜினிகாந்த், நானா படேகர், ஹுமா குரேஷி, ஈஸ்வரி ராவ்",  
  "song_url": "https://www.tamilpaa.com/3436-semma-weightu-tamil-songs-lyrics", 
  "full_lyrics": "\nசெம்ம வெயிட்டு\nசெம்ம வெயிட்டு\nஅடங்க மறுப்பவன்\nவெளிச்சம் கொடுப்பவன்\nகவலை கலைக்கிறவன்\nவாருன்னுதான் காட்டு\nமனச தொடவில்லை\nமனுஷன் விடவில்லை\nகருப்ப பூசிக்கிட்டு\n........."
}
```
## Queries for ElasticSearch search engine
```
*** Match query ***
GET /song_index/_search
{
   "query":{
      "match" : {
         "music":"ஏ.ஆர்.ரஹ்மான்"
      }
   }
}

*** Query String Query ***
GET /song_index/_search
{
   "query":{
      "query_string":{
         "query":"போனமாசம்பார்த்தநிலா"
      }
   }
}

*** Term Level Queries ***
GET /song_index/_search
{
   "query":{
      "term":{"movie":"கண்ணுக்குள்நிலவு"}
   }
}

*** Range queries ***
GET /song_index/_search
{
   "query":{
      "range":{
         "year":{
            "gte":2000,
            "lte":2005
         }
      }
   }
}

*** get songs music by AR Rahuman and year 2007 (AND Operator)***
GET /song_index/_search
{
  "query": {
    "bool": {
      "should": [
        {
          "bool": {
            "must": [
              { "match": { "music":"ஏ.ஆர்.ரஹ்மான்" } },
              { "match": { "year":"2007" }}
            ]
          }
        }
      ]
    }
  }
}

*** get song music by: AR Rahuman or music by : IIayaraja (OR Operator)***
GET /song_index/_search
{
  "query": {
    "bool": {
      "should": [
        {
          "bool": {
            "must": [
              { "match": { "music":"இளையராஜா" } }
            ]
          }
        },
        {
          "bool": {
            "must": [
              { "match": { "music":"யுவன்சங்கர்ராஜா" } }
            ]
          }
        }
      ]
    }
  }
}

*** delete data from index ***
POST /song_index/_delete_by_query
{
 "query": {
   "bool": {
      "must": [
        { "match": { "movie":"நீதானேஎன்பொன்வசந்தம்" } },
        { "match": { "song":"சற்றுமுன்புபார்த்" }}
      ]
    }
  }
}

*** update data from index ***
POST /song_index/_update_by_query
{
  "script": {
    "source": "ctx._source.movie = 'துளிவிசம்'",
    "lang": "painless"
  },
  "query": {
    "bool": {
      "must": [
        { "match": { "year":"1955" } }
      ]
    }
  }
}

POST /song_index/_update/0
{
   "script" : {
      "source": "ctx._source.movie = params.movie",
      "lang": "painless",
      "params" : {
         "movie" : "empty"
      }
   }
 }

*** top 10 songs from 2000 to 2005 filter output ***
GET /song_index/_search
{
  "size" : 10,
  "sort" : [
       { "movie.keyword": {"order" : "desc"}}
   ],
  "query": {
       "range" : {
           "year" : {
               "gte" : "2000",
               "lte" :  "2005"
           }
       }
   }
}

*** stop words and stemming ***
PUT /songs_db/
{
       "settings": {
           "analysis": {
               "analyzer": {
                   "my_analyzer": {
                       "tokenizer": "standard",
                       "filter": ["custom_stopper","custom_stems"]
                   }
               },
               "filter": {
                   "custom_stopper": {
                       "type": "stop",
                       "stopwords_path": "stopwords.txt"
                   }
               }
           }
       }
}

*** search a lyrics line from song's full_lyrics field in song_index ***
GET /song_index/_search
{
   "query":{
      "multi_match": {
         "query":"போனமாசம்பார்த்தநிலா",
         "fields": ["full_lyrics"]
      }
   }
}

*** Get songs sing by AR Rahuman and not music by AR Rahuman ***
GET /song_index/_search
{
   "query": {
    "bool": {
      "must": [
        {"match": {"singers": "ஏ.ஆர்.ரஹ்மான்"}}

      ] ,
	  "must_not": [
        {"match": {"music": "ஏ.ஆர்.ரஹ்மான்"}}

      ]
    }
}}
```
