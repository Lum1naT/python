import urllib
import requests
from bs4 import BeautifulSoup

query = "Jak správně běhat"
query = query.replace(' ', '+')

URL = f"https://google.com/search?q={query}"

MOBILE_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"
DESKTOP_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"

headers = {"user-agent": DESKTOP_AGENT}

response = requests.get(URL, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    results = []

    results = []
    for g in soup.find_all('div', class_='rc'):
        anchors = g.find_all('a')
        if anchors:
            link = anchors[0]['href']
            title = g.find('h3').text
            item = {
                "title": title,
                "link": link
            }
            results.append(item)
    print(results)
