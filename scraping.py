import requests
from bs4 import BeautifulSoup
import sys
import warnings
from requests_html import HTMLSession

url = "https://www.amazon.in/s?k=iphonex&rh=n%3A1389401031&ref=nb_sb_noss"
session = HTMLSession()

if not sys.warnoptions:
    warnings.simplefilter("ignore")

requestHeaders = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}

responseText = session.get(url, headers=requestHeaders, verify=False)

soup = BeautifulSoup(responseText.text, 'lxml')
print(soup.find("span",attrs={"data-component-type":"s-product-image"}))
