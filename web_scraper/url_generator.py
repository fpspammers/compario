def generateSearchUrl(searchString):
    searchUrl = "https://www.amazon.in/s?k="+searchString
    return searchUrl

def generateProductUrl(productASIN):
    productUrl = "https://www.amazon.in/dp/"+productASIN
    return productUrl
