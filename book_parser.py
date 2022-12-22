# importing all that we will work with
import requests
from bs4 import BeautifulSoup as BS
from DataBase_Wrapper import DB

# initializing our db
db = DB()

# counting pages form 2 becouse on first page syntax is not simillar
genre_list = [
    {"genre":"uzhasy","pages":4},
    {"genre":"fentezi","pages":26},
    {"genre":"fantastika","pages":20},
    {"genre":"klassicheskaya-ukrlit","pages":10},
    {"genre":"sovremennaya-ukrlit","pages":24},
    {"genre":"knigi_avtorov_nezavisimoy_ukrainy","pages":7},
    {"genre":"klassicheskaya","pages":13},
    {"genre":"sovremennaya","pages":16},
    {"genre":"detektiv_","pages":39},
    {"genre":"triller","pages":11},
    {"genre":"klassicheskaya_proza","pages":68},
    {"genre":"sovremennaya_proza_nov","pages":175},
    {"genre":"lyubovnyy_roman_new","pages":26},
    {"genre":"istoricheskiy_roman_new","pages":23},
    {"genre":"priklyuchencheskiy_roman","pages":7},
    {"genre":"graficheskiy_roman","pages":17},
    {"genre":"yumor_new","pages":3},
    {"genre":"sborniki-rasskazov","pages":3},
    {"genre":"folklor","pages":4}
]
i = 0
while i <= len(genre_list):
    print(f"Genre list number:{i}")
    pages = 2
    for key,value in genre_list[i].items():
        if key == "genre":
            genre = value
        elif key == "pages":
            pages = value
        for page in range(2,pages+1):
            print(f"Page number:{page}")
        # making get request to our page
            r = requests.get(f"https://book24.ua/ua/catalog/{genre}/?PAGEN_1={page}")
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
                    try:
                        price = info.select(".item_info > .cost > .price_matrix_wrapper > .prices-wrapper > .discount > .values_wrapper > .price_value")
                        price = price[0].text
                    except:
                        try:
                            price = info.select(".item_info > .price_matrix_wrapper > .price > .values_wrapper > .price_value")
                            price = price[0].text
                        except:
                            price = "None"

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
                # print(f'Genre: {genre}')
                # print(f'Price without discount: {price} + {price_currency}')
                # print(f'Price with discount {discount_price} + {price_currency}')
                # print(f'Photo {photo}')
                # print(f'Discount procent {discount}')
                # print('---------------------------------------------------------------------------------------------------------')

                # all our data in variable data
                data = (str(title),str(author),str(genre),str(price),str(discount_price),str(discount),str(price_currency),str(photo))
                # inserting all book data in our database using function called add
                db.add(data = data)
                page += 1
    i += 1
