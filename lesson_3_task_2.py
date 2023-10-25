# 1. Создайте файл `lesson_3_task_2.py`.
# 2. В файле объявите переменную `catalog`.
# 3. Переменная хранит в себе список (`[]`).
# 4. Наполните список пятью разными экземплярами класса `Smartphone`.
# 5. Напишите цикл, который печатает весь каталог (список) в формате `<марка> - <модель>. <номер телефона>`.

from smartphone import Smartphone 
catalog = []
our_phones = ['iphone', 'samsung', 'nokia', 'xiomi', 'lg']
our_models = ['ne', 'sa', 'ia', 'mi', 'l-34']
our_phone_nimbers = ['+7900...', '+7911...', '+7922...', '+7933...', '+7944...']

for pho, mod, num in zip(our_phones, our_models, our_phone_nimbers):
    for_input = Smartphone(pho, mod, num)
    print(f'<{for_input.marka}> - <{for_input.model}>. <{for_input.number}>')

    #другие варианты написания
    # print("<" + for_input.marka + ">")
    # print('<{} - {}>'.format(for_input.marka, for_input.model))

    #f' делит наши значения попарно строчками; Функция zip() в Python создает итератор, который объединяет элементы из нескольких источников данных





