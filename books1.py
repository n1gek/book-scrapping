import requests
import logging
from HELLOWORLD.webscrapping.book_scrapping.PAGES.all_books_page import AllBooksPage
# from ..book_scrapping.PAGES.all_books_page import AllBooksPage

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    filename='logs.txt',
                    level=logging.DEBUG)
logger = logging.getLogger('scraping')
logger.info('Loading books list...')

page_content = requests.get('https://books.toscrape.com').content
page = AllBooksPage(page_content)

books = page.books()

print(books)

for page_num in range(1, page.page_count()):
    url = f'https://books.toscrape.com/catalogue/page-{page_num + 1}.html'
    page_content = requests.get(url).content
    page = AllBooksPage(page_content)
    books.extend(page.books())

