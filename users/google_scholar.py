import requests

from collections import deque
from re import compile
from bs4 import BeautifulSoup as bs4

class Result:
    def __init__(self, name, content):
        self.name = name
        # self.citations = citations
        # self.related_articles = related_articles
        # self.versions = versions
        self.content = content
    
    
    def __str__(self):
        return str(self.name)
        
    def find_other_Versions():
#             iterate throught the other version link and return that
        pass

def google_scholar(query="Complex Equations"):
    search_results = {}
    #Setting up session information
    URL = "https://scholar.google.com/scholar"
    HEADERS = {"Cache-Control":"no-cache",
            "Connection":"keep-alive",
            "User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0",
            "Referer": "https://courses.ms.wits.ac.za/moodle/login/index.php",
            "Origin": URL,
            }
    session = requests.session()
    google_session = session.get(URL + "?hl=en&as_sdt=0%2C5&q=" + str(query) + "&btnG=")
    soup = bs4(google_session.text, "html.parser")

    div = soup.find_all("div", {"class": "gs_ri"})

    results = deque()
    for div_ in div:
        div_soup = div_.find_all("a")
        results.append(Result(div_soup[0], div_))
    
    for result in results:
        search_results[str(result)] = str(result.content)
    
    return search_results