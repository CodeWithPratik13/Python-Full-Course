import requests
from datetime import datetime, timedelta

query = input("What type of news are you interested in today? ")
api = "your_api_key_here"

past_date = (datetime.today() - timedelta(days=7)).strftime('%Y-%m-%d')

url = f"https://newsapi.org/v2/everything?q={query}&from={past_date}&sortBy=publishedAt&pageSize=5&apiKey={api}"

r = requests.get(url)
data = r.json()

# Debug: Print full response
print(data)

if r.status_code == 200:
    articles = data.get("articles", [])
    if articles:
        for index, article in enumerate(articles):
            print(f"{index + 1}. {article['title']}")
            print(article['url'])
            print("\n********************************************\n")
    else:
        print("No articles found for your query.")
else:
    print("Error:", data.get("message", "Unknown error occurred."))
