# **TASK: Notice how there is more than one page, and subsequent pages look like this http://quotes.toscrape.com/page/2/. 
# Use what you know about for loops and string concatenation to loop through all the pages and get all the unique authors on the website. 
# Keep in mind there are many ways to achieve this, also note that you will need to somehow figure out how to check that your loop is on the last page with quotes. 
# For debugging purposes, I will let you know that there are only 10 pages, so the last page is http://quotes.toscrape.com/page/10/, but try to create a loop that is robust enough that it wouldn't matter to know the amount of pages beforehand, perhaps use try/except for this, its up to you!**


import requests
import bs4
import lxml

base_url = "http://quotes.toscrape.com/page/"
page = 1

pagesearch = True
all_authors = set()

while pagesearch:
    page_url = base_url + str(page)
    resu = requests.get(page_url)
    soup = bs4.BeautifulSoup(resu.text,'lxml')

    if "No quotes found!" in resu.text:
        break

    for author in soup.select('.author'):
        all_authors.add(author.text)
    
    page +=1

print(all_authors)
    