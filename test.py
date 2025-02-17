def check_name(value):
    my_string = "Xiaomi AX300T" # проверяем наличие слова в названии товара
    if not my_string in value:
        return None  # Вместо ошибки возвращаем None (запись будет отброшена
        #raise ValueError(f"Этот товар не содержит в названии слово {my_string}")
    return value


print(check_name("супер пупер Xiaomi AX3000T крутой роутер")) # Xiaomi AX3000T