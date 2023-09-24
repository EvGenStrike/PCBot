import pcactions
import subprocess
import webbrowser


def launch_google():
    # subprocess.Popen(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
    open_website("https://www.google.com/")
    # time.sleep(5.0)
    # for i in range(0, 3):
    #     pyautogui.press("tab")
    # pyautogui.press("esc")


def open_website(site_url):
    webbrowser.open(site_url)


def close_google():
    process_name = "chrome.exe"
    while pcactions.check_if_process_running(process_name):
        subprocess.call(["taskkill", "/F", "/IM", process_name])

