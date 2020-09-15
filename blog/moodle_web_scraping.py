# imporying libraries
from bs4 import BeautifulSoup as bs4
from collections import deque
from requests import session as request_session

# Course class
class Course:
    def __init__(self, name, address, soup):
        self.name = name # Course name
        self.address = address # Web address
        self.soup = soup # Beautiful soup object
    

    # How to identify each object
    def __str__(self):
        return self.name

    
    def set_content(self, content):
        self.content = content # Course contents


def init_web_scrap(username, password):

    #Setting up session information
    URL = "https://courses.ms.wits.ac.za"
    HEADERS = {"Cache-Control":"no-cache",
            "Connection":"keep-alive",
            "User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0",
            "Referer": "https://courses.ms.wits.ac.za/moodle/login/index.php",
            "Origin": URL,
            }
    session = request_session()
    post = {"anchor":"","username":username,"password":password}

    #Connecting to the website
    moodle_session = session.get(URL)
    login = session.post("https://courses.ms.wits.ac.za/moodle/login/index.php", headers=HEADERS, data=post)
    login.status_code

    # web scrapping
    soup = bs4(session.get("https://courses.ms.wits.ac.za/moodle/my/").text, "html.parser")

    # Find a list of all courses
    courses = soup.find("li", {"class":"type_system depth_2 contains_branch"}).find_all("a")
    courses = list(set(courses)) # Remove duplicate entries

    # Iterate through courses and get relevant information
    courses_list = deque() # A deque to store all the courses
    for course in courses:
        course_ = str(course).split(" ")
        name = course_[-1].split(">")[1].split("<")[0] # Course name
        address = course_[1][6:-1] # Web address location
        course_soup = bs4(session.get(address).text, "html.parser") # Beautiful soup object
        courses_list.append(Course(name, address, course_soup)) # Append object to the course_list deque

    for course in courses_list:
        soup = course.soup # get soup object
        course.set_content(soup.find_all("div", {"class":"activityinstance"})) # Retrieve and set course contents

    print("hello world")
    results = {}
    for course in courses_list:
        results[str(course.name)] = str(course.content)

    return results

