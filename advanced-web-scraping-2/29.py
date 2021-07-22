import requests
import records
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urldefrag
from sqlalchemy.exc import IntegrityError


db = records.Database('sqlite:///wikipedia.db')


db.query('''CREATE TABLE IF NOT EXISTS pages (
            url text PRIMARY KEY,
            page_title text NULL,
            created_at datetime,
            visited_at datetime NULL)''')

db.query('''CREATE TABLE IF NOT EXISTS links (
            url text, url_to text,
            PRIMARY KEY (url, url_to))''')

base_url = 'https://en.wikipedia.org/wiki/'


def store_page(url):
    try:
        db.query('''INSERT INTO pages (url, created_at)
                    VALUES (:url, CURRENT_TIMESTAMP)''', url=url)
    except IntegrityError as ie:
        # This page already exists
        pass


def store_link(url, url_to):
    try:
        db.query('''INSERT INTO links (url, url_to)
                    VALUES (:url, :url_to)''', url=url, url_to=url_to)
    except IntegrityError as ie:
        # This link already exists
        pass


def set_visited(url):
    db.query('''UPDATE pages SET visited_at=CURRENT_TIMESTAMP
                WHERE url=:url''', url=url)


def set_title(url, page_title):
    db.query('UPDATE pages SET page_title=:page_title WHERE url=:url',
              url=url, page_title=page_title)


def get_random_unvisited_page():
    link = db.query('''SELECT * FROM pages
                       WHERE visited_at IS NULL
                       ORDER BY RANDOM() LIMIT 1''').first()
    return None if link is None else link.url


def visit(url):
    print('Now visiting:', url)
    html = requests.get(url).text
    html_soup = BeautifulSoup(html, 'html.parser')
    page_title = html_soup.find(id='firstHeading')
    page_title = page_title.text if page_title else ''
    print(' page title:', page_title)
    set_title(url, page_title)
    for link in html_soup.find_all("a"):
        link_url = link.get('href')
        if link_url is None:
            # No href, skip
            continue
        full_url = urljoin(base_url, link_url)
        # Remove the fragment identifier part
        full_url = urldefrag(full_url)[0]
        if not full_url.startswith(base_url):
            # This is an external link, skip
            continue
        store_link(url, full_url)
        store_page(full_url)
    set_visited(url)


store_page(base_url)
url_to_visit = get_random_unvisited_page()


while url_to_visit is not None:
    visit(url_to_visit)
    url_to_visit = get_random_unvisited_page()
