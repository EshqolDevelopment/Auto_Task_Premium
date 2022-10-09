import helper_events, keyboard
from os import getenv
from threading import Thread
from time import sleep
from auto_tasks import keyboard_and_mouse_recorder, keyboard_and_mouse_recorder_for_close_desktop
from mouse import MoveEvent, WheelEvent
from speech_recog import get_user_input
from pyautogui import keyUp, keyDown, press
from Common import getEmail
app_data_path = getenv('APPDATA')
path = f"{app_data_path}/Auto Tasks"


# הפונקציה מבקשת מהשמשתמש את שם המשימה ומחזירה את כל הניסיונות של המשתמש עד שהמשתמש מצא משימה שקיימת
def select_name_and_save_error():
    global task_name
    # מבקשת את השם של המשימה אותה הוא רוצה להקליט
    task_name = input("Enter a task name: ").lower()

    # מבקש לחזור על השם של המשימה שאותה רוצה להקליט בקולך
    task_name_from_speech = get_user_input("Say the name of your task you typed previously")

    # שומר את כל הפעמים בהם המשתמש לא חזר נכונה על השם של המשימה בקולו
    all_speech_tries = f"{task_name}&"
    all_speech_tries += f"{task_name_from_speech}&"

    # אם הtext to speech של המשתמש לא תאם לשם של המשימה הפונקציה תבקש ממנו לומר את השם של המשימה עד שמה שהוא אמר מתאים לשם של המשימה
    while task_name != task_name_from_speech:
        print("Say it again please")
        if task_name_from_speech:
            if all_speech_tries != "could not recognize your voice":
                all_speech_tries += f"{task_name_from_speech}&"
        all_speech_tries = all_speech_tries[:-1]
        task_name_from_speech = get_user_input()

    # מחזיר את שם המשימה שהמשתמש בחר ואת כל הניסיונות של המשתמש לחזור על שם המשימה בקולו
    return all_speech_tries


def maximize_window_thread():
    while True:
        keyboard.press_and_release("left windows + up")
        sleep(3)


def maximized_window():
    max_thread = Thread(target=lambda: maximize_window_thread(), daemon=True)
    max_thread.start()


def open_new_desktop_and_come_back_to_original_and_record():
    # פותח שולחן עבודה חדש
    keyboard.press_and_release("ctrl + left windows + d")

    #מקליט את המשימה
    mouse_events, keyboard_events = keyboard_and_mouse_recorder()

    # מחזיר את המשתמש לשולחן עבודה המקורי
    keyDown("ctrl")
    keyDown("winleft")
    for i in range(1, 15):
        press("right")
    keyUp("ctrl")
    keyUp("winleft")

    return mouse_events, keyboard_events


def close_desktop_record():
    mouse_events = keyboard_and_mouse_recorder_for_close_desktop()
    return mouse_events



def just_record():
    mouse_events, keyboard_events = keyboard_and_mouse_recorder()
    return mouse_events, keyboard_events


def save_events_in_file():
    # קורא לפונקציה שממקבלת את השם של המשימה ושומר את כל הניסיונות של המשתמש לחזור על השם שהוא נתן למשימה
    all_speech_tries = select_name_and_save_error()

    mouse_button = []
    mouse_wheel = []
    mouse_move = []

    mouse_events, keyboard_events = open_new_desktop_and_come_back_to_original_and_record()

    # ממין את הEVENT לפי הסוג שלהם
    for event in mouse_events:
        if type(event) == MoveEvent:
            mouse_move.append(event)
        elif type(event) == WheelEvent:
            mouse_wheel.append(event)
        else:
            mouse_button.append(event)

    # שומר את כל הניסיונות של המשתמש לחזור על שם המשימה בקובץ טקסט
    with open(f"{path}/{getEmail()}/file_saver/{task_name}all_speech_tries.txt", 'w') as f:
        f.write(all_speech_tries)

    # reformat the lists into strings, in order to insert to database
    all_lists = helper_events.reformat_all(keyboard_events[:-1], mouse_button, mouse_wheel, mouse_move)
    # keyboard
    kb = '#'.join(all_lists[0])
    # mouse
    mb = '#'.join(all_lists[1])  # button
    mm = '#'.join(all_lists[2])  # move
    mw = '#'.join(all_lists[3])  # wheel


    # שומר את כל הפעולות בקבצים שונים לפי סוג הפעולה
    with open(f"{path}/{getEmail()}/file_saver/{task_name}_kb.txt", 'w') as f:
        f.write(kb)

    with open(f"{path}/{getEmail()}/file_saver/{task_name}_mb.txt", 'w') as f:
        f.write(mb)

    with open(f"{path}/{getEmail()}/file_saver/{task_name}_mm.txt", 'w') as f:
        f.write(mm)

    with open(f"{path}/{getEmail()}/file_saver/{task_name}_mw.txt", 'w') as f:
        f.write(mw)



# הפונקציה שומרת את כל השמות של המשימות שנוצרו עד כה
def name_of_tasks():

    f_name_tasks = open(f"{path}/names_of_user_tasks.txt", "a")
    f_name_tasks.write("&" + task_name)
    f_name_tasks.close()

