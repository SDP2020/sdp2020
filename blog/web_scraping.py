import requests

from re import compile
from bs4 import BeautifulSoup as bs


def nav_w3(w3_soup):
    nav = w3_soup.find_all("div", {"id": "sidenav"})
    return nav

def learn_w3(site, nav=False):
    sol = []

    w3 = requests.get(site)
    w3_soup = bs(w3.content)
    intro = set(w3_soup.find_all("div", {'class': "w3-panel w3-info intro"}))
    for intro_ in intro:
        intro_ = str(intro_).split("\n")
        for intro_s in intro_:
            if "<p>" in str(intro_s) and "</p>" in str(intro_s):
                sol.append(intro_s)
    
    if nav:
        sol.append(nav_w3(w3_soup)) # append navigation solutions to the resulsts


    return sol
    # div "sidenav"


def scrap_w3(argument, nav=False):
    print("argument is %s" %(argument))
    site = "https://www.w3schools.com"
    w3 = requests.get(site) # get the html content of the site we will be visiting
    w3_soup = bs(w3.content) # convert it into a beautifulsoup object
    w3_learn = w3_soup.find_all("a", string=compile("(L|l)earn ")) # find all links that contain lean
    w3_learn = set(w3_learn) # remove all duplicates

    for learn in w3_learn:
        if argument in str(learn):
            return learn_w3(site+learn.get_attribute_list("href")[0], nav=nav) # If we find the query continue scraping
