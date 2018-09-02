



import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.amazon.in/Apple-iPhone-Space-Grey-64GB/dp/B072LPF91D/ref=sr_1_1?s=electronics&ie=UTF8&qid=1535889359&sr=1-1&keywords=iphone+x")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"id": "priceblock_ourprice", "class": "a-size-medium a-color-price"})
string_price = element.text.strip() # 91,666.00

price_without_symbol = string_price.replace(",", "")

final_price = float(price_without_symbol)

if final_price > 80000:
    print("can't buy it")
else:
    print("You can Buy it")





