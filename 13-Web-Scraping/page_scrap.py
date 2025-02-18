import requests
import bs4
import lxml

base_url = "http://books.toscrape.com/catalogue/page-{}.html"
resu = requests.get(base_url.format('1'))
soup = bs4.BeautifulSoup(resu.text,"lxml")

products = soup.select(".product_pod")
example = products[0]
example.select('.star-rating.Two')

two_star_title = []

for n in range (1,51):

    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text,'lxml')
    books = soup.select('.product_pod')

    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            two_star_title.append(book.select('a')[1]['title'])

print(two_star_title)

