import requests
from bs4 import BeautifulSoup

keyword = "market"
url = "https://www.cnn.com/search?q=" + keyword

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
# a list storing the news articles containing the keyword
contains_keyword = []

articles = soup.find_all('h3', {'class': 'container__headline __headline'})
print(f"Number of articles found: {len(articles)}")

for article in articles:
    print(len(contains_keyword))
    if keyword in article.get_text().lower():
        contains_keyword.append(article)
        print(article.get_text().strip()) # for testing 
    if len(contains_keyword) == 30: # max number of articles to find
        break
