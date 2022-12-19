import requests
from bs4 import BeautifulSoup as BS
import sqlite3
from DataBase_Wrapper import DB

db = DB()
i = 2
for i in range(2,50):
    r = requests.get(f"https://book24.ua/ua/catalog/fantastika_fentezi/?PAGEN_1={i}")
    html = BS(r.content, 'html.parser')

    for info in html.select(".catalog_item_wrapp > .inner_wrap"):

        title = info.select(".item-title > a > span")
        title = title[0].text
        price_currency = " грн."

        try:
            author = info.select(".item_info > .sa_block > .article_block > .font_sxs > a")
            author = author[0].text
        except:
            author = "None"

        try:
            discount_price = info.select(".item_info > .cost > .price_matrix_wrapper > .prices-wrapper > .price > .values_wrapper > .price_value")
            discount_price = discount_price[0].text
        except:
            discount_price = "None"
            discount = "None"

        try:
            price = info.select(".item_info > .cost > .price_matrix_wrapper > .price > .values_wrapper > .price_value")
            price = price[0].text
        except:
            price = info.select(".item_info > .cost > .price_matrix_wrapper > .prices-wrapper > .discount > .values_wrapper > .price_value")
            price = price[0].text
        
        try:
            discount = info.select(".image_wrapper_block > .stickers > div > .sticker_sovetuem")
            discount = discount[0].text
        except:
            discount = "None"
        try:
            photo = info.select(".image_wrapper_block > .thumb > .section-gallery-wrapper > .section-gallery-wrapper__item > img")
            photo = "https://book24.ua" + photo[0].attrs['data-src']
        except:
            photo = "None"

        print(f'Title: {title}')
        print(f'Author: {author}')
        print(f'Price without discount: {price} + {price_currency}')
        print(f'Price with discount {discount_price} + {price_currency}')
        print(f'Photo {photo}')
        print(f'Discount procent {discount}')
        print('---------------------------------------------------------------------------------------------------------')

        data = (str(title),str(author),str(price),str(discount_price),str(discount),str(price_currency))
        db.add(data = data)
        i += 1

