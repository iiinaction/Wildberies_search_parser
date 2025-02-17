import requests
import re
import csv
from models import Items
class ParseWb:
    
    def __init__(self, url:str):
        # self.__get_brand_id = self.__get_brand_id(url) # получаем id бренда
        self.params = {
    'ab_testing': 'false',
    'appType': '1',
    'curr': 'rub',
    'dest': '12358103',
    'lang': 'ru',
    'page': '1',
    'query': 'ax3000t xiaomi роутер',
    'resultset': 'catalog',
    'sort': 'popular',
    'spp': '30',
    'suppressSpellcheck': 'false',
    'uclusters': '0',
    'uiv': '8',
    'uv': 'Poc6ZkOLPzMw_0RdOu40cD4yQG_DM0QswKK9acCvOC-_-q9gwZxFG0CVum3AQ8Qvt2bF1L_cvwS8LjijOy6yNEBpvbu-cMSxwjg1tcBvPkVEeD9mutg8_8DTvrhCd7mSwKC-T0OZwptC9j6bPZu_T716wZ-6WD6RPS69wr_KwLU_ecP8Pvy_ND5utylAcbOQrlc8DLv5QGC0pkGyPGzDbkFcvrpDVsBGQZsomTVovWI6JLwqO9kvcLiDwlLCicEaQRc6pLg-tulCRkOfNDQ4djnXPsZB7DjAMzRBKsKFOmnDskBowEE60qaOOn6-rbsFwfs1ir6rOtE-f0OBQI5BxA',
}
    
    def parse(self):
        i = 1
        self.__create_csv()
        while True:
            response = requests.get('https://search.wb.ru/exactmatch/ru/common/v9/search', params=self.params, )
            i+=1
            items_info = Items.model_validate(response.json()["data"])
            if not items_info.products:
                break
            self.__save_csv(items_info)

    def __create_csv(self):                                              # создаем csv файл
        with open('wildberries_data.csv', 'w', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)                                    # создаем объект writer
            writer.writerow(['id', 'название', 'бренд', 'цена', 'рейтинг' , 'в наличии'])    # записываем заголовки
    
    def __save_csv(self, items):                                         # создаем csv файл
        with open('wildberries_data.csv', 'a', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            
            for product in items.products:
                if product.name is not None:
                    print(product.name)
                    writer.writerow([product.id,
                                    product.name,
                                    product.brand,
                                    product.price,
                                    product.rating,
                                    product.volume,])   

if __name__ == '__main__':
    ParseWb('https://www.wildberries.ru/catalog/0/search.aspx?search=ax3000t+xiaomi+%D1%80%D0%BE%D1%83%D1%82%D0%B5%D1%80&targeturl=ST&xsearch=true').parse() # передаем ссылку на бренд



   # response = requests.get('https://search.wb.ru/exactmatch/ru/common/v9/search', params=params, headers=headers)