from telebot import types
# import database as db


# Кнопка для отправки номера
def num_bt():
    # Создаём пространство
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Создаём сами кнопки
    number = types.KeyboardButton("Отправить номер", request_contact=True)
    # Добавляем кнопки в пространство
    kb.add(number)
    return kb


# Кнопка для отправки локации
def loc_bt():
    # Создаём пространство
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Создаём сами кнопки
    location = types.KeyboardButton("Отправить локацию", request_location=True)
    # Добавляем кнопки в пространство
    kb.add(location)
    return kb


# Кнопки выбора товара
def main_menu_buttons(prods_from_db):
    # Создаём пространство для кнопок
    kb = types.InlineKeyboardMarkup(row_width=2)
    # Создаём сами кнопки
    cart = types.InlineKeyboardButton(text="Корзина", callback_data="cart")
    # Создание кнопки для каждого продукта
    all_products = [types.InlineKeyboardButton(text=f'{i[1]}',
                                               callback_data=f'{i[0]}') for i in prods_from_db if i[2] > 0]
    # for prod in prods_from_db:
    #     all_products = types.InlineKeyboardButton(text=prod[1], callback_data=str(prod[0]))
    #
    #     # Добавляем кнопки в пространство
    kb.add(*all_products)
    kb.row(cart)
    return kb


# Кнопка выбора количества
def choose_pr_count(amount=1, plus_or_minus=""):
    # Создаём пространство
    kb = types.InlineKeyboardMarkup(row_width=3)
    # Создаём кнопки
    back = types.InlineKeyboardButton(text="Назад", callback_data="back")
    to_cart = types.InlineKeyboardButton(text="Добавить в корзину", callback_data="to_cart")
    plus = types.InlineKeyboardButton(text="+", callback_data="increment")
    minus = types.InlineKeyboardButton(text="-", callback_data="decrement")
    count = types.InlineKeyboardButton(text=str(amount), callback_data=str(amount))
    # Алгоритм добавления и удаления кол-ва товара
    if plus_or_minus == "increment":
        new_amount = int(amount) + 1
        count = types.InlineKeyboardButton(text=str(new_amount), callback_data=str(new_amount))
    elif plus_or_minus == "decrement":
        if amount > 1:
            new_amount = int(amount) - 1
            count = types.InlineKeyboardButton(text=str(new_amount), callback_data=str(new_amount))
    # Добавляем кнопки в пространство
    kb.add(minus, count, plus)
    kb.row(back, to_cart)
    return kb


# Кнопки для админки
# Меню админки
def admin_menu():
    # Создаём пространство
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Создаём кнопки
    but1 = types.KeyboardButton("Добавить продукт")
    but2 = types.KeyboardButton("Удалить продукт")
    but3 = types.KeyboardButton("Изменить продукт")
    but4 = types.KeyboardButton("Перейти в меню")
    # Добавляем кнопки в пространство
    kb.add(but1, but2, but3)
    kb.row(but4)
    return kb


# Кнопки подтверждения
def confirm():
    # Создаём пространство
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Создаём кнопки
    but1 = types.KeyboardButton("Да")
    but2 = types.KeyboardButton("Нет")
    # Добавляем кнопки в пространство
    kb.add(but1, but2)
    return kb


# Кнопки для корзины
def cart_buttons():
    # Создаём пространство длякнопок
    kb = types.InlineKeyboardMarkup(row_width=2)
    # Создаём сами кнопки
    order = types.InlineKeyboardButton(text='Оформить заказ', callback_data='order')
    clear = types.InlineKeyboardButton(text='Очистить корзину', callback_data='clear')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    # Добавляем кнопки в пространство
    kb.add(order, clear)
    kb.row(back)
    return kb
