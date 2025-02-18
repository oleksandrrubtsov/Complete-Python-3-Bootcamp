import requests
import bs4
import lxml

# result = requests.get("https://quotes.toscrape.com/")
# soup = bs4.BeautifulSoup(result.text,'lxml')
# print(soup)

# **TASK: Get the names of all the authors on the first page.**
# result = requests.get("https://quotes.toscrape.com/")
# soup = bs4.BeautifulSoup(result.text,'lxml')

# authors = soup.select('.author')
# for item in soup.select('.author'):
#     print(item.text)

# **TASK: Create a list of all the quotes on the first page.**
# result = requests.get("https://quotes.toscrape.com/")
# soup = bs4.BeautifulSoup(result.text,'lxml')

# write_quotes = []
# quotes = soup.select('.text')
# for quote in quotes:
#     write_quotes.append(quote.text)

# print(write_quotes)

# **TASK: Inspect the site and use Beautiful Soup to extract the top ten tags from the requests text shown on the top right from the home page (e.g Love,Inspirational,Life, etc...). 
# HINT: Keep in mind there are also tags underneath each quote, try to find a class only present in the top right tags, perhaps check the span.**
# result = requests.get("https://quotes.toscrape.com/")
# soup = bs4.BeautifulSoup(result.text,'lxml')

# tags = soup.select('.tag-item')
# for tag in tags:
#     print(tag.text)


# **TASK: Notice how there is more than one page, and subsequent pages look like this http://quotes.toscrape.com/page/2/. 
# Use what you know about for loops and string concatenation to loop through all the pages and get all the unique authors on the website. 
# Keep in mind there are many ways to achieve this, also note that you will need to somehow figure out how to check that your loop is on the last page with quotes. 
# For debugging purposes, I will let you know that there are only 10 pages, so the last page is http://quotes.toscrape.com/page/10/, but try to create a loop that is robust enough that it wouldn't matter to know the amount of pages beforehand, perhaps use try/except for this, its up to you!**

base_url = "https://quotes.toscrape.com/page/"
page= 1

pagesearch = True
all_authors = set()

while pagesearch:
    
    page_url = base_url + str(page)
    resu = requests.get(page_url)
    soup = bs4.BeautifulSoup(resu.text,'lxml')

    if 'No quotes found!' in resu.text:
        break
    
    

    for author in soup.select('.author'):
        all_authors.add(author.text)
  
    page += 1
    
print(all_authors)


