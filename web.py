from urllib.request import urlopen as uReq
from urllib.request import Request
from bs4 import BeautifulSoup as soup
import random
import pandas as pd
from datetime import date
Date=[]
Item_Name=[]
Price=[]
UPC=[]
Page_Link=[]

base_url = 'https://www.bestbuy.com'
for x in range(1,33):
  url = 'https://www.bestbuy.com/site/laptop-computers/all-laptops/pcmcat138500050001.c?cp='+str(x)+'&id=pcmcat138500050001&intl=nosplash'
  try:
    req12 = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    page_html12 = uReq(req12).read()
    page_soup12 = soup(page_html12, "html.parser")
    containers = page_soup12.findAll("div", {"class", "sku-title"})
    for container in containers:
      links = base_url + container.h4.a['href'] + '&intl=nosplash'
      req = Request(links, headers={'User-Agent': 'Mozilla/5.0'})
      page_html = uReq(req).read()
      page_soup = soup(page_html, "html.parser")
      Page_Link.append(links)
      today = date.today()
      Date.append(today)
      Name = page_soup.findAll("h1", {"class", "heading-5 v-fw-regular"})[0].text.replace(",","|")
      Item_Name.append(Name)
      print(Name)
      try:
        price = page_soup.findAll("div", {"class", "priceView-hero-price priceView-customer-price"})[0].span.text.replace(",","")
        Price.append(price)
        print(price)
      except:
        price = 'Price for this product is not availble'
        Price.append(price)
      try:
        upc = page_soup.findAll("div", {"class", "row-value col-xs-6 v-fw-regular"})[-1:][0].text
        UPC.append(upc)
        print(upc)
      except:
        upc = 'Price for this product is not availble'
        UPC.append(upc)
  except:
    pass

data={'Date': Date, 'Item_Name': Item_Name, 'Price':Price, 'UPC':UPC, 'Page_Link':Page_Link,}
df=pd.DataFrame.from_dict(data=data, orient='index')
df1 = df.T 
df1.to_excel('laptop.xlsx', index=False)
# files.download('errorfix.csv')
#df1.to_excel("~/Desktop/books_to_scrap/laptop.xlsx", index=False)
