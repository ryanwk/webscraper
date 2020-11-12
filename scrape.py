import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# set url to target website
myurl = 'https://www.newegg.com/p/pl?d=graphics+cards'

# open up connection and then grab data from webpage
uClient = uReq(myurl)
page_html = uClient.read()
# close connection to webpage/url
uClient.close()

# use soup to parse html 
page_soup = soup(page_html, "html.parser")

# pop open any html element using this syntax
# e.g., page_soup.h1 brings up an h1 tag from the url specified

# grab everything with the specified class
containers = page_soup.findAll("div", {"class":"item-container"})

# check length of containers
# len(containers)

# grab: brand, product name, and shipping
for container in containers:
    brand = container.div.div.a.img["title"]
    
    title_container = container.findAll("a", {"class":"item-title"})
    product_name = title_container[0].text
    
    shipping_container = container.findAll("li", {"class":"price-ship"})
    shipping = shipping_container[0].text.strip()

    print("brand :" + brand)
    print("product name :" + product_name)
    print("shipping :" + shipping)
    