import requests
from bs4 import BeautifulSoup

URL = "https://www.instagram.com/{}/"

def scrape(username):
    full_url = URL.format(username)     #Making full url
    r = requests.get(full_url)      #Sending get request
    s = BeautifulSoup(r.text, "lxml")       #Making soup object

    tag = s.find("meta", attrs={"name":"description"})
    text = tag.attrs['content']
    main_text = text.split("-")[0]

    return main_text

username = input("Enter the username: ")
data = scrape(username)
print(data)