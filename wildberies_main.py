import requests
import re
import csv
from models import Items
import json


class ParseWb:
    BASE_URL = 'https://search.wb.ru/exactmatch/ru/common/v9/search'  
    
    def __init__(self, query, params=None ):                             # инициализирируем атрибуты(ссылку) класса с параметрами
        # self.__get_brand_id = self.__get_brand_id(url) # получаем id бренда
        default_params ={
    'ab_testing': 'false',
    'appType': '1',
    'curr': 'rub',
    'dest': '12358103',
    'lang': 'ru',
    'page': '1',
    'query': 'свитер вязанный',
    'resultset': 'catalog',
    'sort': 'popular',
    'spp': '30',
    'suppressSpellcheck': 'false',
    'uclusters': '0',
    'uiv': '8',
    'uv': 'Poc6ZkOLPzMw_0RdOu40cD4yQG_DM0QswKK9acCvOC-_-q9gwZxFG0CVum3AQ8Qvt2bF1L_cvwS8LjijOy6yNEBpvbu-cMSxwjg1tcBvPkVEeD9mutg8_8DTvrhCd7mSwKC-T0OZwptC9j6bPZu_T716wZ-6WD6RPS69wr_KwLU_ecP8Pvy_ND5utylAcbOQrlc8DLv5QGC0pkGyPGzDbkFcvrpDVsBGQZsomTVovWI6JLwqO9kvcLiDwlLCicEaQRc6pLg-tulCRkOfNDQ4djnXPsZB7DjAMzRBKsKFOmnDskBowEE60qaOOn6-rbsFwfs1ir6rOtE-f0OBQI5BxA',
}
        self.params = {**default_params, **(params or {}), 'query':query} # объединяем словари
    
    def parse(self):
        i = 1
        self.__create_csv()
        while True:
            response = requests.get(self.BASE_URL, params=self.params, )
            i+=1
            items_info = Items.model_validate(response.json()["data"])
            
            # DEBAG BLOCK!!!
            # with open('wildberries_data.json', 'w', encoding="utf-8") as file:
            #     json.dump(items_info.json(), file, indent=4, ensure_ascii=False)
            # Items(products=[Item(id=1, name='Xiaomi AX3000T', brand='Xiaomi'), 
            #    Item(id=2, name='Samsung Router', brand='Samsung')])

            if not items_info.products:
                break
            if i == 3:
                break
            self.__save_csv(items_info, csv_search)

    def __create_csv(self):                                              # создаем csv файл
        with open('wildberries_data.csv', 'w', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)                                    
            writer.writerow(['id', 'название', 'бренд', 'цена', 'рейтинг' , 'в наличии'])   
    
    def __save_csv(self, items, csv_search):                              # сохраняем csv файл по столбцам полученным из parse
        with open('wildberries_data.csv', 'a', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            my_string = csv_search.lower()
            print(my_string)                                  # добавим свой строгий поиск по названию товара при добавлении в таблицу
            for product in items.products:
                if my_string in product.name.lower():
                    print(product.name)
                    writer.writerow([product.id,
                                    product.name,
                                    product.brand,
                                    product.price,
                                    product.rating,
                                    product.volume,])


if __name__ == '__main__':
    brand_query = "роутеры Xiaomi"                                        # запрос в поисковике 
    csv_search = "AX3000T"                                                # ключевые слова на строгий поиск в csv файле
    ParseWb(brand_query).parse()
