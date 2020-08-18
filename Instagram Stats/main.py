from bs4 import BeautifulSoup
import requests

URL = "https://www.instagram.com/{}/"

def parse_data(s):
    data = {}
    s = s.split("-")[0]
    s = s.split(" ")
    data['Followers'] = s[0]
    data['Following'] = s[2]
    data['Posts'] = s[4]
    return data

def scrape_data(username):
    r = requests.get(URL.format(username))
    s = BeautifulSoup(r.text, "html.parser")
    meta = s.find("meta", property="og:description")
    return parse_data(meta.attrs['content'])

if __name__=="__main__":
    username = input("Enter your username: ")
    data = scrape_data(username)
    print("This account has {} followers".format(data["Followers"]))
    print("This account has {} following".format(data["Following"]))
    print("This account has {} posts".format(data["Posts"]))