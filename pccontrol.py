import enum
from enum import Enum
import pyautogui
from PIL import Image


class SupportedBrushesColor(enum.Enum):
    Purple = (157, 71, 222)
    White = (255, 255, 255)
    Blue = (30, 153, 255)
    Red = (227, 57, 60)
    Green = (57, 186, 42)
    Orange = (250, 110, 22)
    Black = (3, 3, 3)


class MouseActions(Enum):
    LMB_one_click = 0
    LMB_two_clicks = 1
    RMB = 2
    MWHEELUP = 3
    MWHEELDOWN = 4


user_screenshot = None
current_brush_color = SupportedBrushesColor.Purple.value


def get_current_brush_color_name():
    global current_brush_color
    match current_brush_color:
        case SupportedBrushesColor.Purple.value:
            return "🟪Фиолетовый🟪"
        case SupportedBrushesColor.Red.value:
            return "🟥Красный🟥"
        case SupportedBrushesColor.Orange.value:
            return "🟧Оранжевый🟧"
        case SupportedBrushesColor.Blue.value:
            return "🟦Синий🟦"
        case SupportedBrushesColor.Black.value:
            return "⬛Чёрный⬛"
        case SupportedBrushesColor.White.value:
            return "⬜Белый⬜"
        case SupportedBrushesColor.Green.value:
            return "🟩Зелёный🟩"


def change_brush_color(brush_color):
    global current_brush_color
    current_brush_color = brush_color


def set_user_screenshot(screenshot):
    global user_screenshot
    user_screenshot = screenshot
    print(f"user screenshot: {user_screenshot}")


def click(mouse_action):
    global current_brush_color
    point_coords = get_point_coords(current_brush_color)
    x = point_coords[0]
    y = point_coords[1]
    pyautogui.moveTo(x, y)
    match mouse_action:
        case MouseActions.LMB_one_click:
            pyautogui.leftClick()
        case MouseActions.LMB_two_clicks:
            pyautogui.click(clicks=2)
        case MouseActions.RMB:
            pyautogui.click(button="RIGHT")
        case MouseActions.MWHEELUP:
            pyautogui.vscroll(-400)
        case MouseActions.MWHEELDOWN:
            pyautogui.vscroll(400)
        case _:
            pass


def get_point_coords(pixel_to_look_for):
    global user_screenshot
    delta = 20
    image = Image.open(user_screenshot)
    width, height = image.size
    desired_pixels_coords = []
    for i in range(width):
        for j in range(height):
            current_pixel_color = image.getpixel((i, j))
            if (pixel_to_look_for[0] - delta <= current_pixel_color[0] <= pixel_to_look_for[0] + delta
            and pixel_to_look_for[1] - delta <= current_pixel_color[1] <= pixel_to_look_for[1] + delta
            and pixel_to_look_for[2] - delta <= current_pixel_color[2] <= pixel_to_look_for[2] + delta):
                x = int(i * 1.5)
                if x == 0: x = 1
                elif x == 1920: x = 1919
                y = int(j * 1.5)
                if y == 0: y = 1
                elif y == 1080: y = 1079
                desired_pixels_coords.append((x, y))
    image.close()
    #print(desired_pixels_coords)
    return desired_pixels_coords[len(desired_pixels_coords) // 2]