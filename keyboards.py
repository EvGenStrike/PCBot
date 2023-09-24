import pcactions
from telebot import types


def generate_keyboard(items):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    for item in items:
        markup.add(types.KeyboardButton(item))

    return markup


def start_keyboard():
    items = [
        "Действия с ПК",
        "Взаимодействовать с ПК",
        "Действия с Google Chrome",
        "Приколы",
        "Выключить бота"
    ]
    return generate_keyboard(items)


def pc_keyboard():
    items = [
        "Выключить ПК",
        "Сделать скриншот",
        "Сделать фото с камеры",
        "Сделать скриншот и фото с камеры",
        "Свернуть все вкладки",
        "Закрыть все вкладки",
        "Открыть отдельную вкладку",
        "Закрыть отдельную вкладку",
        "Закрыть текущую вкладку",
        "Режим параноика",
        "Запустить Wallpaper Engine",
        "Закрыть Wallpaper Engine",
        "Поставить свои обои",

        "Назад"
    ]
    return generate_keyboard(items)


def control_pc_keyboard():
    items = [
        "ЛКМ 1 раз",
        "ЛКМ 2 раза",
        "ПКМ",
        "Прокрутить колесо вверх",
        "Прокрутить колесо вниз",
        "Обновить позицию мышки",
        "Отобразить текущее изображение на ПК",

        "Назад"
    ]
    return generate_keyboard(items)


def change_brush_keyboard():
    items = [
        "🟪Фиолетовый🟪",
        "⬜Белый⬜",
        "🟦Синий🟦",
        "🟩Зелёный🟩",
        "🟧Оранжевый🟧",
        "🟥Красный🟥",
        "⬛Чёрный⬛",

        "Назад"
    ]
    return generate_keyboard(items)


def opened_tabs_keyboard(tab_to_exclude):
    items = list(set(pcactions.get_all_tabs(tab_to_exclude)))
    items.append("Обновить")
    items.append("Назад")
    return generate_keyboard(items)


def google_keyboard():
    items = [
        "Открыть Google",
        "Закрыть Google",

        "Назад"
    ]
    return generate_keyboard(items)


def confirmation_for_turning_off_pc_keyboard():
    items = [
        "Да, я хочу выключить компьютер",
        "Нет, я не хочу выключать компьютер"
    ]
    return generate_keyboard(items)


def jokes_keyboard():
    items = [
        "Прикол с быстрой сменой цветов",

        "Назад"
    ]
    return generate_keyboard(items)


def wait_for_send_screenshot_with_mouse_position_keyboard():
    items = [
        "Поменять цвет маркера",

        "Назад"
    ]
    return generate_keyboard(items)


def wait_for_send_wallpaper_keyboard():
    items = [
        "Назад"
    ]
    return generate_keyboard(items)
