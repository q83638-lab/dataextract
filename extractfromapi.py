import requests as r
from yahoo_fin import stock_info as si
key = str(input("stock name"))
url = "https://www.cnbc.com/quotes/?symbol=."+ key

response = r.get(url)

print(response.json)
print(si.get_live_price("aapl"))
