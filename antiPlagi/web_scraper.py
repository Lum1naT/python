import urllib
import requests
from bs4 import BeautifulSoup


def get_links_by_query(query):
    """
    docstring
    """
    query = query.replace(' ', '+')

    URL = f"https://google.com/search?q={query}"

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
                results.append(link)
    return(results)
