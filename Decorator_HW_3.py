import os
from datetime import datetime
from Decorator_HW_2 import logger

cook_book={'Омлет': [
    {'ingridient_name': 'Яйцо', 'quantity': '2', 'measure': 'шт'}, 
    {'ingridient_name': 'Молоко', 'quantity': '100', 'measure': 'мл'}, 
    {'ingridient_name': 'Помидор', 'quantity': '2', 'measure': 'шт'}], 
'Утка по-пекински': [
    {'ingridient_name': 'Утка', 'quantity': '1', 'measure': 'шт'}, 
    {'ingridient_name': 'Вода', 'quantity': '2', 'measure': 'л'}, 
    {'ingridient_name': 'Мед', 'quantity': '3', 'measure': 'ст.л'}, 
    {'ingridient_name': 'Соевый соус', 'quantity': '60', 'measure': 'мл'}], 
'Запеченный картофель': [{
    'ingridient_name': 'Картофель', 'quantity': '1', 'measure': 'кг'}, 
    {'ingridient_name': 'Чеснок', 'quantity': '3', 'measure': 'зубч'}, 
    {'ingridient_name': 'Сыр гауда', 'quantity': '100', 'measure': 'г'}], 
'Фахитос': [
    {'ingridient_name': 'Говядина', 'quantity': '500', 'measure': 'г'},
     {'ingridient_name': 'Перец сладкий', 'quantity': '1', 'measure': 'шт'}, 
     {'ingridient_name': 'Лаваш', 'quantity': '2', 'measure': 'шт'},
      {'ingridient_name': 'Винный уксус', 'quantity': '1', 'measure': 'ст.л'}, 
      {'ingridient_name': 'Помидор', 'quantity': '2', 'measure': 'шт'}]}

path= 'log.txt'

@logger(path)
def get_shop_list_by_dishes(cook_book, dishes, person_count):
    shop_list={}
    # dish=[]
    # dish.append(dishes)
    for el in dishes:
        for dish, ingridients in cook_book.items():
            if el == dish:
                for ingridient in ingridients:
                    for key, value in ingridient.items():
                    # break
                        shop_list[ingridient['ingridient_name']]={'measure':ingridient['measure'],
                    'quantity':(int(ingridient['quantity'])*person_count)}
                    
    print(dishes)                
    print(shop_list)
get_shop_list_by_dishes(cook_book, ['Запеченный картофель', 'Омлет'], 2)


