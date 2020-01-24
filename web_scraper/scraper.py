from bs4 import BeautifulSoup
from . import url_generator, session, ip_rotator
import sys
import warnings

def sendRequest(url):
    responseText = None
    requestHeaders = ip_rotator.getHeaders()
    proxy = ip_rotator.getIP()

    try:
        responseText = session.get(url, headers=requestHeaders, verify=False, proxies={"http": proxy, "https": proxy})
    except:
        print("Connection failed, Retrying...")
        sendRequest(url)

    return responseText

def amazonSearchResults(searchString):
    if not sys.warnoptions:
        warnings.simplefilter("ignore")

    url = url_generator.generateSearchUrl(searchString)

    responseText = sendRequest(url)

    soup = BeautifulSoup(responseText.text, 'lxml')

    productList = []

    resultListTag = soup.find('div',attrs={"class":"s-search-results"})
    print("resultListTag",type(resultListTag))

    resultList = resultListTag.find_all('div',attrs={"class":"s-result-item"},recursive=False)
    print("resultList",type(resultList))


    for product in resultList:
        if(product["data-asin"]!=""):
            productUrl = url_generator.generateProductUrl(product["data-asin"])
            print(productUrl)

            imageTag = product.find('img',attrs={"data-image-latency":"s-product-image"})
            imageLink = imageTag["src"]
            print(imageLink)

            productName = product.find('span',attrs={"class":"a-text-normal"}).text
            print(productName)

            try:
                productPrice = product.find('span',attrs={"class":"a-offscreen"}).text
            except:
                print("Price not found")
            print(productPrice)

            productDict = {"name":productName,"image":imageLink,"amazonPrice":productPrice,"url":productUrl}
            productList.append(productDict)

    return productList

#def amazonProductPage():
