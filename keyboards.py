from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def job_keyboard_test():
    """
    Тестовая клавиатура которая выводит подходящие вакансии
    Для корректной пагинации вакансий, нужно добавить обработчик действий 
    и динамические кнопки. Например сделать клави-ру через InlineKeyboardBuilder
    """

    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Работа 1", callback_data="job_1")],
                                                     [InlineKeyboardButton(text="Работа 2", callback_data="job_2")],
                                                     [InlineKeyboardButton(text="Работа 3", callback_data="job_3")],
                                                     [InlineKeyboardButton(text="<<<", callback_data="perv_page"), 
                                                      InlineKeyboardButton(text=">>>", callback_data="next_page")]])
    return keyboard