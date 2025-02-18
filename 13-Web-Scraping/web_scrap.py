import requests
import bs4
import lxml

result = requests.get("https://quotes.toscrape.com/")


soup = bs4.BeautifulSoup(result.text,'lxml')
span_tag = soup.select('span')[0].getText()
for item in soup.select('span'):
    print(item.text)