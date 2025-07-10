import requests
from datetime import datetime

query = input("What type of news are you interested in today? ")
api = "your_api_key_here"

today = datetime.today().strftime('%Y-%m-%d')
url = f"https://newsapi.org/v2/everything?q={query}&from={today}&sortBy=publishedAt&apiKey={api}&pageSize=10"

r = requests.get(url)

if r.status_code == 200:
    data = r.json()
    articles = data.get("articles", [])
    if articles:
        for index, article in enumerate(articles):
            print(index + 1, article["title"])
            print(article["url"])
            print("\n********************************************\n")
    else:
        print("No articles found for your query.")
else:
    print("Failed to fetch news:", r.status_code)
