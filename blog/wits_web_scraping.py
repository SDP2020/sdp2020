# imporying libraries
from bs4 import BeautifulSoup as bs4
from collections import deque
from requests import session as request_session


global course_list # glaobal course_list variable to store Course objects
course_list = deque()

# TODO make Course a model
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


def moodle(username, password):
    course_list = deque()
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
    try:
        courses = soup.find("li", {"class":"type_system depth_2 contains_branch"}).find_all("a")
        courses = list(set(courses)) # Remove duplicate entries
    except AttributeError:
        return {"Error": "Please confirm your login details and try again"}
    # Iterate through courses and get relevant information
    for course in courses:
        course_ = str(course).split(" ")
        name = course_[-1].split(">")[1].split("<")[0] # Course name
        address = course_[1][6:-1] # Web address location
        course_soup = bs4(session.get(address).text, "html.parser") # Beautiful soup object
        course_list.append(Course(name, address, course_soup)) # Append object to the course_list deque

    for course in course_list:
        soup = course.soup # get soup object
        course.set_content(soup.find_all("div", {"class":"activityinstance"})) # Retrieve and set course contents

    return course_list

def sakai(username, password):
    #Setting up session information
    URL = "https://wits-e.wits.ac.za/portal"
    HEADERS = {"Accept-Encoding": "gzip, deflate, br",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Cache-Control":"no-cache",
            "Connection":"keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Host": "wits-e.wits.ac.za",
            "Pragma": "no-cache",
            "TE": "Trailers",
            "User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0",
            "Referer": "https://wits-e.wits.ac.za/portal",
            "Origin": URL,
            }
    session = request_session()
    # Please enter your usename and password when prompted
    post = {"eid":username,"pw":password,"submit":"Log+In"}

    #Connecting to the website
    moodle_session = session.get(URL)
    login = session.post(URL + "/xlogin", headers=HEADERS, data=post)
    login.status_code

    # web scrapping
    soup = bs4(session.get(URL).text, "html.parser")

    # Filter out courses according to year
    courses = deque()
    try:
        courses_soup = soup.find("div", {"id": "otherSitesCategorWrap", "class":"tab-box"}).find_all("a")
    
    except AttributeError:
        return {"Error": "Please confirm your login details and try again"}
    
    for course in courses_soup:
        if "2020" in str(course) and "fullTitle" in str(course):
            courses.append(course)
    courses = deque(set(courses))

    # Add current year coursess to the course_list as well as create a Course object
    course_list = deque()
    for course in courses:
        course_ = str(course).split(" ")
        address = course_[1][6:-1]
        name = course_[-1][18:-12]
        course_soup = bs4(session.get(address).text, "html.parser")
        course_list.append(Course(name, address, course_soup))

    # Get the resource table from sakai
    for course in course_list:
        resources = course.soup.find_all("a", {"class": "Mrphs-toolsNav__menuitem--link", "title": "Resources - For posting documents, URLs to other websites, etc."})
        resource_soup = bs4(session.get(str(resources[0]).split(" ")[2][6:-1]).text, "html.parser").find_all(
            "table", {"class": "table table-striped table-hover resourcesList" })
        # TODO at the moment you only have the bs4 object, you haven't iterated through to table to get each individual resource
        course.set_content(resource_soup)

    return course_list


def init_web_scrap(username, password):
    global course_list # global course_list variable

    course_list.extend(moodle(username, password)) # scrap moodle
    course_list.extend(sakai(username, password)) # scrap sakai

    results = {} # map that keeps all the results returned by the server

    for course in course_list:
        try:
            results[str(course.name)] = str(course.content) # map course name to course contents
        except AttributeError:
            return {"Error": "Failed To Get Your Courses Please Refresh the page and double check your password \n alternatively please make sure your username is registered with wits"}
    return results

