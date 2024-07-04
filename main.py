import requests
import pandas as pd
from bs4 import BeautifulSoup
product_name = []
Price = []
reviews = []
description = []

for j in range(1,10):
  url = f"https://www.ebay.com/sch/i.html?_from=R40&_nkw=phone&_sacat=0&_pgn={j}"

  r = requests.get(url)
      # print(r)

  soup = BeautifulSoup(r.text,"lxml")
  # print(soup)

  names = soup.find_all("div",class_ = "s-item__title")

  # print(len(names))


  for i in names:
      name = i.text
      product_name.append(name)

  # print(len(product_name))



  prices = soup.find_all("span",class_ = "s-item__price")

  for i in prices:
      name = i.text
      Price.append(name)

  # print(len(Price))


  desc = soup.find_all("span",class_="s-item__shipping")
  for i in desc:
      name = i.text
      description.append(name)

  # print(description)

min_length = min(len(product_name), len(Price), len(description))
product_name = product_name[:min_length]
Price = Price[:min_length]
description = description[:min_length]
df = pd.DataFrame({"Product Name":product_name,"Prices":Price,"Decription":description})
print(df)


df.to_csv("Mobiles_Data.csv")