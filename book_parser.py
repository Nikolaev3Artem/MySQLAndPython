# importing all that we will work with
import requests
from bs4 import BeautifulSoup as BS
import sqlite3
from DataBase_Wrapper import DB

# initializing our db
db = DB()

# counting pages form 2 becouse on first page syntax is not simillar
pages = 2
for pages in range(2,50):
    # making get request to our page
    r = requests.get(f"https://book24.ua/ua/catalog/fantastika_fentezi/?PAGEN_1={pages}")
    # taking all html from url
    html = BS(r.content, 'html.parser')

    # make cycle to take all books in our html
    for info in html.select(".catalog_item_wrapp > .inner_wrap"):

        # taking title for our book
        title = info.select(".item-title > a > span")
        title = title[0].text
        # our price currency
        price_currency = " грн."

        # taking author of the book
        try:
            author = info.select(".item_info > .sa_block > .article_block > .font_sxs > a")
            author = author[0].text
        except:
            author = "None"

        # taking discount price of the book
        try:
            discount_price = info.select(".item_info > .cost > .price_matrix_wrapper > .prices-wrapper > .price > .values_wrapper > .price_value")
            discount_price = discount_price[0].text
        except:
            discount_price = "None"
            discount = "None"

        # taking main price of the book
        try:
            price = info.select(".item_info > .cost > .price_matrix_wrapper > .price > .values_wrapper > .price_value")
            price = price[0].text
        except:
            price = info.select(".item_info > .cost > .price_matrix_wrapper > .prices-wrapper > .discount > .values_wrapper > .price_value")
            price = price[0].text
        
        # taking procent of discout of the book
        try:
            discount = info.select(".image_wrapper_block > .stickers > div > .sticker_sovetuem")
            discount = discount[0].text
        except:
            discount = "None"

        # taking photo url of the book
        try:
            photo = info.select(".image_wrapper_block > .thumb > .section-gallery-wrapper > .section-gallery-wrapper__item > img")
            photo = "https://book24.ua" + photo[0].attrs['data-src']
        except:
            photo = "None"

        # display it in console if u need it
        # print(f'Title: {title}')
        # print(f'Author: {author}')
        # print(f'Price without discount: {price} + {price_currency}')
        # print(f'Price with discount {discount_price} + {price_currency}')
        # print(f'Photo {photo}')
        # print(f'Discount procent {discount}')
        # print('---------------------------------------------------------------------------------------------------------')

        # all our data in variable data
        data = (str(title),str(author),str(price),str(discount_price),str(discount),str(price_currency),str(photo))
        # inserting all book data in our database using function called add
        db.add(data = data)
        i += 1

