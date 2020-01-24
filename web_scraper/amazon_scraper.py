from bs4 import BeautifulSoup
from web_scraper import url_generator

def searchResults(tagObject):
    url = url_generator.generateSearchUrl("Phones")

    responseText = session.get(url, headers=requestHeaders, verify=False)

    soup = BeautifulSoup(responseText.text, 'lxml')

    productList = []

    resultListTag = soup.find('div',attrs={"class":"s-search-results"})
    print("resultListTag",type(resultListTag))

    resultList = resultListTag.find_all('div',attrs={"class":"s-result-item"},recursive=False)
    print("resultList",type(resultList))


    for product in resultList:
        if(tagObject["data-asin"]!=""):
            productUrl = url_generator.generateProductUrl(tagObject["data-asin"])
            print(productUrl)

            imageTag = tagObject.find('img',attrs={"data-image-latency":"s-product-image"})
            imageLink = imageTag["src"]
            print(imageLink)

            productName = tagObject.find('span',attrs={"class":"a-text-normal"}).text
            print(productName)

            productPrice = tagObject.find('span',attrs={"class":"a-offscreen"}).text
            print(productPrice)

            productDict = {"name":productName,"image":imageLink,"amazonPrice":productPrice,"url":productUrl}

    productList.append(productDict)

    return productList

def productPage():
