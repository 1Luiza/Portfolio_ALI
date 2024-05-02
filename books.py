import requests
from bs4 import BeautifulSoup
import json

url = "https://books.toscrape.com/catalogue/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
page_number = 1
session = requests.session()

all_books = []
while True:
    response = session.get(url + 'page-' + str(page_number) + '.html',
                           headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all('li', {'class': 'col-xs-6'})
    if not books:
        break

    for book in books:
        book_info = {}
        name_info = book.find('h3')
        book_url = url + name_info.find('a')['href']
        book_info['name'] = name_info.find('a')['title']
        price = book.find('p', {'class': 'price_color'}).text.strip()
        book_info['price'] = float(
            ''.join(filter(lambda x: x.isdigit() or x == '.', price)))

        response_double = session.get(book_url, headers=headers)
        soup = BeautifulSoup(response_double.text, "html.parser")
        book_info['stock'] = soup.find('p', {
            'class': 'instock availability'}).text.strip()

        all_books.append(book_info)
    print(f'Обработана {page_number} страница')
    page_number += 1

json_data = json.dumps(all_books, ensure_ascii=False, indent=4)
with open('books_data.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_data)
print(len(all_books))
