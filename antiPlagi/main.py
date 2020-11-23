import urllib
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from web_scraper import get_links_by_query

result = get_links_by_query("Jak správně běhat")
