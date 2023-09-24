import time
import pyautogui
import datetime
import os
import subprocess
import psutil
import wallpaperchange
import cv2
import pathlib
import shutil
import pygetwindow
import googleactions
from pywinauto.mouse import *
from pywinauto.keyboard import send_keys


bot_path = pathlib.Path(__file__).parent.resolve()
wallpaper_path = fr"{bot_path}\wallpaperPhotos"
max_photos_in_one_folder = 5

forbidden_tabs = [
        "Диспетчер задач",
        "Microsoft Text Input Application0",
        "NVIDIA GeForce Overlay",
        "Program Manager",
    ]

open_specific_tab_flag = False


def turn_pc_off():
    print("turning off...")
    os.system("shutdown /s /t 1")


def take_screenshot():
    screenshot_directory = fr"{bot_path}\screenshots"
    screenshot_path = fr"{screenshot_directory}\Screenshot {get_current_time()}.png"

    current_screenshot = pyautogui.screenshot()
    current_screenshot.save(screenshot_path)

    clear_excess_photos(screenshot_directory)

    return screenshot_path


def clear_excess_photos(path):
    photo_path_directory = path
    all_screenshots = os.listdir(photo_path_directory)

    while len(all_screenshots) > max_photos_in_one_folder:
        os.remove(fr"{photo_path_directory}\{all_screenshots[0]}")
        all_screenshots.pop(0)


def minimize_all_tabs():
    windows_titles = get_all_tabs(None)
    for window_title in windows_titles:
        pygetwindow.getWindowsWithTitle(window_title)[0].minimize()


def close_all_tabs():
    global forbidden_tabs
    windows_titles = get_all_tabs(None)
    for window_title in windows_titles:
        if window_title in forbidden_tabs:
            continue
        pygetwindow.getWindowsWithTitle(window_title)[0].close()


def close_specific_tab(window_name):
    global forbidden_tabs
    windows_titles = get_all_tabs(None)
    for window_title in windows_titles:
        if window_title in forbidden_tabs:
            continue
        if window_title != window_name:
            continue
        pygetwindow.getWindowsWithTitle(window_title)[0].close()


def get_all_tabs(closed_tab = None):
    closed_tabs = [closed_tab] + forbidden_tabs
    # filter removes "" from the list
    windows_titles = list(filter(None, pygetwindow.getAllTitles()))
    windows_titles = [element for element in windows_titles if element not in closed_tabs]
    return windows_titles


def get_current_tab():
    return pygetwindow.getActiveWindowTitle()


def open_specific_tab(window_name):
    window = pygetwindow.getWindowsWithTitle(window_name)[0]
    window.maximize()
    window.activate()
    print("windows maximized")


def manage_specific_tab(window_name):
    global open_specific_tab_flag
    if open_specific_tab_flag:
        open_specific_tab(window_name)
    else:
        close_specific_tab(window_name)


def launch_wallpaper_engine():
    process_name = "wallpaper64.exe"
    subprocess.Popen(fr"{wallpaperchange.wallpaper_engine_path}\{process_name}")
    time.sleep(0.5)


def launch_process(process_path):
    subprocess.Popen(process_path)


def close_wallpaper_engine():
    if check_if_process_running("wallpaper32.exe"):
        subprocess.call(["taskkill", "/F", "/IM", "wallpaper32.exe"])
    if check_if_process_running("wallpaper64.exe"):
        subprocess.call(["taskkill", "/F", "/IM", "wallpaper64.exe"])
    directory = os.listdir(wallpaper_path)
    photo_index = min(len(directory) - 1, max_photos_in_one_folder - 1)
    change_wallpaper(fr"{wallpaper_path}\{directory[photo_index]}")


def change_wallpaper(path):
    wallpaperchange.change_wallpaper(path)


def exit_bot():
    proces_name = "python.exe"
    while check_if_process_running(proces_name):
        subprocess.call(["taskkill", "/F", "/IM", proces_name])

    # this message should never be printed
    print("Bot have been terminated")


def take_camera_photo():
    cam_port = 1
    cam = cv2.VideoCapture(cam_port, cv2.CAP_DSHOW)
    result, image = cam.read()

    current_time = get_current_time()
    camera_photo_path = fr"{bot_path}\camera_photos\Camera {current_time}.png"
    camera_photo_directory = fr"{bot_path}\camera_photos"

    # this directory should not contain russian letters
    camera_directory = fr"D:\cameraPhotos\Camera {current_time}.png"

    if result:
        cv2.imwrite(camera_photo_path, image)
    else:
        print("No image detected. Please, try again!")

    #shutil.move(camera_directory, camera_photo_path)
    clear_excess_photos(camera_photo_directory)
    return camera_photo_path


def launch_google():
    googleactions.launch_google()


def open_website(site_url):
    googleactions.open_website(site_url)


def close_google():
    googleactions.close_google()


def get_current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")


def check_if_process_running(process_name):
    # Check if there is any running process that contains the given name process_name.
    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if process_name.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def get_amount_of_processes_running(process_name):
    # Check if there is any running process that contains the given name process_name.
    # Iterate over the all the running process
    count = 0
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if process_name.lower() in proc.name().lower():
                count += 1
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return count


def epilepsy_joke():
    open_website("https://www.youtube.com/watch?v=EkXdjnX6TmE")

    while True:
        logo = pyautogui.locateOnScreen(fr"D:\cameraPhotos\logo.png")
        if logo is not None:
            break

    print(logo)
    send_keys("{f}")
    #pyautogui.press("f")
