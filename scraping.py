import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.in/s?k=iphonex&rh=n%3A1389401031&ref=nb_sb_noss"
response = requests.get(url)

response_type = response.content
response.encoding = response_type
response_text = response.text
soup = BeautifulSoup(response_text, 'lxml')
print(soup.find("span",attrs={"data-component-type":"s-product-image"}))
