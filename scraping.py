import requests
from bs4 import BeautifulSoup
import sys
import warnings
from requests_html import HTMLSession

url = "https://www.amazon.in/s?k=Balls"
session = HTMLSession()

if not sys.warnoptions:
    warnings.simplefilter("ignore")

userAgentList = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A"]

requestHeaders = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}

responseText = session.get(url, headers=requestHeaders, verify=False)

soup = BeautifulSoup(responseText.text, 'lxml')

resultListTag = soup.find('span',attrs={"data-component-type":"s-search-results"})
resultList = resultListTag.contents

#for item in resultListTag.children:
    #imageTag = item.find('img',attrs={"data-image-latency":"s-product-image"})
    #imageLink = imageTag["src"]

print(resultList[0])
