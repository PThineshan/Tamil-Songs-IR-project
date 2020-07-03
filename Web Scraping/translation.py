from translate import Translator
import ast

# dictionary_string = "{'movie': '10 Enradhukulla (10 எண்றதுகுள்ள) ', 'year': '2015', 'music': 'D. Imman', 'actors': 'Vikram, Samantha', 'movie_url': 'https://www.tamilpaa.com/10-enradhukulla-songs-lyrics', 'movie_image': 'https://www.tamilpaa.com/upload/movies/10-enradhukulla.jpg', 'movie_name_tamil': '10 எண்றதுகுள்ள', 'movie_name_eng': '10 Enradhukulla', 'movie_song': [{'song_title': '\nVroom Vroom (\nபேர கேட்டா )', 'song_url': 'https://www.tamilpaa.com/3000-vroom-vroom-tamil-songs-lyrics', 'song_music': 'D. Imman', 'song_lyrics': 'Madhan Karky', 'song_singers': '', 'song_fulllyrics': 'பேர கேட்டா \xa0பேஜாரு பண்ற\nமெய்ய சொல்லு யாருடா\xa0நீ\nfees-u வாங்கி confuse-u பண்ற\nமெய்ய சொல்லு யாருடா \xa0நீ\n\nநான் பாஞ்ச bullet-u தான்\nஆபத்தே chicklet\xa0 தான்\nகார் ஓட்டும் fight jet-u நான்\nபொண்ணுங்க மாக்நெட்-உ நான்\nஎனக்குன்னு இல்ல கூண்டு\nஉன் நெஞ்சில ஏன்டா காண்டு\nஉனக்கென்ன வேணும் வேண்டு\nஎன்னோட பேரு \xa0bond-u\nBond James Bond\n\nபேர கேட்டா \xa0பேஜாரு பண்ற\nமெய்ய சொல்லு யாருடா\xa0நீ\nfees-u வாங்கி confuse-u பண்ற\nமெய்ய சொல்லு யாருடா \xa0நீ\n\nஎன் கண்ணில் அச்சம் இல்ல\nஎன் போல உச்சம் இல்ல\nஊருக்கு செல்ல புள்ள\nஎதிரிக்கி நான் தான் தொல்ல\nஎனக்குன்னு இல்ல வேலி\nநான் ஆடுற வரைக்கும் ஜாலி\nஅடிச்சா எல்லாரும் காலி\nஎன்னோட பேரு கொஹ்லி\nKohli Virat Kohli\n\nஎன் ஊரு பரமக்குடி\nநான் யாரு கண்டுபிடி\nமொத்த வித்த அத்துப்படி\nஎன் கிட்ட கத்துகடி\nபடிப்புக்கு போவல tuition\nஆனா நடிப்புல நான் ஒரு ocean\nபுதுமைகதான் என் பேஷன்\nஎன்னோட பேரு ஹாசன்\nHassan Kamal Hassam\n\nநீங்க நல்லவரா இல்ல கெட்டவரா \nரெண்டும் செந்ததுதான் நான்\ni am a hero and a villain'}, {'song_title': '\nAanaalum Indha Mayakkam (\nஆனாலும் இந்த மயக்கம் )', 'song_url': 'https://www.tamilpaa.com/3002-aanaalum-indha-mayakkam-tamil-songs-lyrics', 'song_music': 'D. Imman', 'song_lyrics': 'Madhan Karky', 'song_singers': '', 'song_fulllyrics': 'ஆனாலும் இந்த மயக்கம்\nஆகாது நெஞ்சே உனக்கு\nபோனாலும் நின்னு சிரிக்கும்\nபோகாது இந்த கிறுக்கு\nஎனக்கு புடிச்ச அது மாறி\nஉலகம் கெடக்கு அழகேறி\nமுன்னால.. ஒ…\nதர ரா தாராரரா....\n(அவளா சொல்லும் முன்ன மனமே ஏன் துள்ளுற)\nஆனாலும் இந்த மயக்கம்\nஆகாது நெஞ்சே உனக்கு\nபோனாலும் நின்னு சிரிக்கும்\nபோகாது இந்த கிறுக்கு\n\nஅருகாமையில் இருப்பேன்\nஅடடா என வியப்பேன்\nநீ சொன்னாலும் சொல்லாம நின்னாலும்\nதினமும் நல்ல சகுனம்\nபுதுசா ஒரு பயணம்\nஇந்த பாதையில் ஊர் சேரனும்\nதலைய கோதி நானும் பார்த்தேன்\nதனிமை எல்லாம் தின்னு தீக்க வந்தாயே.. ஓ..\nதர ரா தாராரரா...\n(அவளா சொல்லும் முன்ன மனமே ஏன் துள்ளுற)\nஆனாலும் இந்த மயக்கம்\nஆகாது நெஞ்சே உனக்கு\n\nசிரிக்கும் போதே முறைப்ப மழைக்குள் வெயில் அடிப்ப \nநான் போனாலும் போகாத சொல்லிட்டேன்\nமுடியும் என நெனச்சா தொடரும் என முடிப்பேன்\nநீ மாறாத நான் மாறிட்டேன்\nநிலவுக்குள்ள இல்ல நீரு\nநீரில் தூங்கும் நிலவ பாரு \n\nஆனாலும் இந்த மயக்கம்\nஆகாது நெஞ்சே உனக்கு\nபோனாலும் நின்னு சிரிக்கும்\nபோகாது இந்த கிறுக்கு\nஎனக்கு புடிச்ச அது மாறி\nஉலகம் கெடக்கு அழகேறி\nமுன்னால.. ஒ…\nதர ரா தாராரரா....\n\nஅவளா சொல்லும் முன்ன மனமே ஏன் துள்ளுற\n'}, {'song_title': '\nGaana Gaana (\nகானா கானா )', 'song_url': 'https://www.tamilpaa.com/3003-gaana-gaana-tamil-songs-lyrics', 'song_music': 'D. Imman', 'song_lyrics': 'Madhan Karky', 'song_singers': '', 'song_fulllyrics': 'வேதாளத்த தின்னு ஏப்பம் விடும் \nவிக்ரம் விக்ரம் விக்ரம் விக்ரம் \nவிக்கிரமாதித்தன் நான் அம்மா \nவண்டி ஓட்டி போகனும் டா தூரமா \nஎன் வயுறு இங்க பசிகுதட கோரம \nசீக்கிரம் எதாச்சும் கொண்ட சூட காரமா \n\nசூட காரமா சூட காரமா \nஐயோ பாவமா மாட்டிகிச்சு ஆளுமா\nவேண்டாத வேலை எல்லாம் உனக்கு எதுக்கு ராசா \nகூண்டு குள்ள காலெடுத்து வைக்கூறியே லூச \nஇப்போ கூட ஒன்னும் இல்ல ஓடி போய்டு \nஇல்ல எங்களோட சங்கத்துல மெம்பெர் ஆயிடு \n\nசூட வந்தது சூப்பர் மாமா \nகாரமா கேட்டேனே காரமா காரமா \n\nகானா கானா தெலுங்கானா \nஅட காரம் கெளப்பும் மொளக நா \nகானா கானா தெலுங்கானா \nஇங்க யாரும் மயங்கும் அழகா நா\nகண்ணால பாத்தாலே வாயெல்லாம் நீரூறும் \nவாயோட வெச்சாலே கண்ணெல்லாம் நீரூறும் \nபசங்க எல்லாருமே பீசு போன தோக்கு \nபொண்ணுங்க மென்னு துப்பும் வெத்தல பாக்கு \nஅடடா செவந்துருச்சு நாக்கு \n\nகானா கானா தெலுங்கானா \nஇவன் உங்கள அடக்கிட வந்தன \nகானா கானா தெலுங்கானா \nஇவன் எங்கள விடுவிக்க வந்தன \n\nபூட்டி மறைகிறது உங்க பொழுது போக்கு \nதொறந்து ருசிகிறது எங்களோட நாக்கு \nஅடடா ஒடஞ்சிடுச்சு லாக்கு\n\nகானா கானா தெலுங்கானா \nஇவன் தீயில் உருகும் மெழுகானா \nகானா கானா தெலுங்கானா \nஇவ அழுவும் போதும் அழகானா \n\nஎன்கிருந்து வந்தானோ \nஎதுக்காக வந்தானோ \nதிருகாணி எடுக்குறான் \nமரையாணி முடுக்குறான்\nபல்ப சக்கரம் மாட்டிவிட்டு \nகுதிரையத்தான் ஓட்டுறான் \n\nஎன்கிருந்து வந்தானோ \nஎதுக்காக வந்தானோ \nதிருகாணி எடுக்குறான் \nமரையாணி முடுக்குறான்\nபல்ப சக்கரம் மாட்டிவிட்டு \nகுதிரையத்தான் ஓட்டுறான் \n\nதோட்டாவே இல்லாம துப்பாக்கியால் தாக்குறான் \nகானா கானா தெலுங்கானா \nஇவன் ஜெயிச்சிட பொறந்த சுல்தானா \nகானா கானா தெலுங்கானா \nஎன்ன மயக்கிட வந்த மஸ்தான \nஆள தெரியாம அட்ரஸ்ச கேட்டுட்டேன்\nஆடி முடியாம ஐய்யா நா தோத்துட்டேன் \nதண்ணி காட்டுறது என் பொழுது போக்கு \nஎன்ன சாச்சிபுட்ட காலர துக்கு \nநீ தான் டவுனு குள்ள டாக்கு\n\nகானா கானா தெலுங்கானா \nஅந்த ஐகளின் ஐ அது இவன்தானா\nகானா கானா தெலுங்கானா \nஇவன் எங்கள விடுவிக்க வந்தனானா\nகானா கானா தெலுங்கானா \nஇனி ஜாலி ஜாலிலோ ஜிம்கானா \nகானா கானா தெலுங்கானா \nஅப்புறம் பஞ்சம் முந்தி அந்த மைனா\n'}]}"
# dictionary_string=dictionary_string.replace('\n','\\n')
# print(dictionary_string)
# a_dictionary = ast.literal_eval(dictionary_string)
# print(type(a_dictionary))
tamil_songs_file= open("tamil_corpus.txt",'r',encoding="utf8").read()
data = tamil_songs_file.splitlines(True)
for line in data:
    line = ''.join(line.split())
    line = line.replace('\n', '\\n').replace('\xa0', '\\xa0')
    line = ast.literal_eval(line)

    translator = Translator(from_lang="english", to_lang="tamil")
    movie_songs = line.get("movie_song")
    output = []
    for movie_song in movie_songs:
        music = translator.translate(movie_song.get("song_music"))
        lyrics = translator.translate(movie_song.get("song_lyrics"))
        singers = translator.translate(movie_song.get("song_singers"))
        actors = translator.translate(line.get("actors"))

        out = {
            "movie": line.get("movie_name_tamil"),
            "song": (movie_song.get("song_title").split('('))[1][:-3],
            "music": music,
            "lyrics": lyrics,
            "singers": singers,
            "year": line.get("year"),
            "actors": actors,
            "song_url": movie_song.get("song_url"),
            "full_lyrics": movie_song.get("song_fulllyrics")
        }
        output.append(out)
        print(output)

file = open("tamil_songs_corpus_final.txt", "a")
for song in output:
    file.write(str(song)+'\n')
