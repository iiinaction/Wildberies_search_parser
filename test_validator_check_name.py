from pydantic import BaseModel, field_validator, ValidationError
import  pprint
class Item(BaseModel):
    id: int
    name: str  
    brand: str
    sizes: list[str]  # Для примера, пусть это список строк
    rating: int
    volume: int

    @field_validator("name", mode="before")
    @classmethod
    def check_name(cls, value):
        my_string = "Xiaomi AX3000T"
        if my_string not in value:
            raise ValueError("Недопустимое имя")  # Принудительно выбрасываем исключение
        return value  

""" data = [
     {"id": 1, "name": "Xiaomi AX3000T Pro", "brand": "Xiaomi", "sizes": ["S", "M"], "rating": 5, "volume": 500},
     {"id": 2, "name": "Samsung Router", "brand": "Samsung", "sizes": ["L"], "rating": 4, "volume": 400},
     {"id": 3, "name": "Xiaomi AX3000T Lite", "brand": "Xiaomi", "sizes": ["XL"], "rating": 5, "volume": 600},
"""

# valid_items = []

# for item in data:
#     try:
#         obj = Item(**item)
#         valid_items.append(obj)
#     except ValidationError:
#         pass  # Просто пропускаем запись, которая не прошла валидацию

# pprint.pprint(valid_items)  # Здесь будут только объекты с name, содержащим "Xiaomi AX3000T"