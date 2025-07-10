import requests

query = input("What type of news are you intrested in today? ")
api= "Your API Key"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-05-15&sortBy=publishedAt&apiKey=802f953791d34df39daecc46c30a31ae"

print(url)
r= requests.get(url)

data = r.json()
articles= data["articles"]

for index, article in enumerate(articles) :
    print(index + 1, article["title"], article["url"])
    print("\n********************************************\n")
    
