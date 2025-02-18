from pydantic import BaseModel, field_validator
from typing import List, Optional

class Price(BaseModel):
    total:float

class Size(BaseModel):
    price:Price

class Item(BaseModel):
    id: int
    name: str
    brand:str
    sizes: list[Size]
    rating: int
    volume: int
    
    # @field_validator("name", mode="before")           #валидатор проверки на соотвествие тексту в поле name
    # @classmethod
    # def check_name(cls, value):
    #     my_string = "Xiaomi AX3000T"
    #     if my_string not in value:
    #         return None  # Принудительно выбрасываем исключение
    #     return value     
    @property
    def price(self) -> Optional[float]:
        return self.sizes[0].price.total/100 if self.sizes else None

class Items(BaseModel):
    products : List[Item]
   



# test = Item(**response.json()["data"]["products"][0])