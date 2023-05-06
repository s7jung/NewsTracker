import requests
from bs4 import BeautifulSoup

keyword = "bank market"
url = "https://www.cnn.com/search?q=" + keyword

res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')

articles = soup.find_all('div', {'class': 'cnn-search__result-headline'})
for article in articles[:30]:
    title = article.find('a', {'class': 'cnn-search__result-headline-link'})
    print(title.text.strip())
    print("Link:", title['href'])
    print("-" * 50)