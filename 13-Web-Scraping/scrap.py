import requests
import bs4
import lxml

result = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
soup = bs4.BeautifulSoup(result.text,'lxml')

comp = soup.select('.mw-file-element')[0]

image_link = requests.get("https://upload.wikimedia.org/wikipedia/en/thumb/9/94/Symbol_support_vote.svg/19px-Symbol_support_vote.svg.png")

f =open('my_new_file_name.jpg','wb')
f.write(image_link.content)
f.close()
