import requests
import webbrowser

blocked_words = ['town', 'state', 'county', 'district', 'politic', 'player', 'ball', 'champion', 'island']
url = 'https://en.wikipedia.org/api/rest_v1/page/random/html'
url2 = 'https://en.wikipedia.org/api/rest_v1/page/random/summary'

def execute_articles():

    for i in range(0,5):
        valid = False
        while(not valid):
            response = requests.get(url2)
            json = response.json()

            summary = json['extract']
            if not any(c in summary for c in blocked_words):
                valid = True

                #get url of the random article from wikipedia

                title = json['title']

                title = "".join(i for i in title if ord(i)<128)
                searchurl = 'https://en.wikipedia.org/wiki' + title.replace(" ","_")

                #Open URL

                webbrowser.open_new_tab(searchurl)

# execute_articles()

wanted_words = ['philosophy', 'science', 'programming', 'art', 'literature', 'history', 'architecture', 'theory', 'invent',
                'invention', 'time', 'nature', 'myth']

def include_articles():

    for i in range(0,5):
        valid = False
        while(not valid):
            response = requests.get(url2)
            json = response.json()

            summary = json['extract']
            if any(c in summary for c in wanted_words):
                valid = True

                matche = [w for w in wanted_words if w in summary]
                print(matche)

                #get url of the random article from wikipedia

                title = json['title']

                title = "".join(i for i in title if ord(i)<128)
                searchurl = 'https://en.wikipedia.org/wiki' + title.replace(" ", "_")

                #Open URL

                webbrowser.open_new_tab(searchurl)

def scan_full_articles():

    for i in range(0,5):
        valid = False
        while(not valid):
            response = requests.get(url)
            html = response.text

            if any(c in html for c in wanted_words):
                valid = True

                matche = [w for w in wanted_words if w in html]
                print(matche)

                #get url of the random article from wikipedia

                title = response.url
                title = title.replace("https://en.wikipedia.org/api/rest_v1/page/random/html", "")

                searchurl = 'https://en.wikipedia.org/wiki' + title

                webbrowser.open_new_tab(searchurl)

                print(title)

scan_full_articles()