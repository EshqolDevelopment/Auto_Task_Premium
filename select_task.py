import Common, keyboard
from os import getenv
from helper_events import back_to_events
from auto_tasks import runMouseMouseKeyboardEvents
from speech_recog import get_user_input
from close_tabs_helper import ask_close_tab, close_desktop_end
from Common import getEmail

app_data_path = getenv('APPDATA')
path = f"{app_data_path}/Auto Tasks"


# הפונקציה שואלת את המשתמש איזה משימה הוא רוצה להפעיל עד שהמשתמש נותן משימה ששמה קיים
def user_select_task():
    while True:
        global user_input
        user_input = get_user_input("Say the name of your task").lower()
        print(user_input)
        while user_input == "could not recognize your voice":
            user_input = get_user_input("enter the name of your task").lower()
        try:
            open(rf"{path}/{getEmail()}/file_saver/{user_input}_kb.txt", 'r')
        except:
            pass

        # מחזיר את שם המשימה
        return user_input


def user_select_task1(x):
    global user_input1
    user_input1 = x

    # מחזיר את שם המשימה
    return user_input1


# הפונקציה פותחת את קובץ הטקסט בו שמור כל שמות המשימות ובודקת אם הניסיון השגוי של המשתמש מקושר לאחד משמות המשימות
def search_string_in_file(task_name_search, string_to_search):
    task_name_search = task_name_search[:-1]
    with open(rf"{path}/{getEmail()}/file_saver/{task_name_search}all_speech_tries.txt", 'r') as f:
        # בודק אם הניסיון השגוי מקושר לאחד משמות המשימות
        if string_to_search in f.read():
            return True
        else:
            return False


# הפונקציה בודקת האם הניסיון השגוי של המשתמש מקושר לאחד המשימות ואם כן היא מחזירה את השם של המשימה אליה הניסיון השגוי מקושר
def check_final_file():
    while True:
        # פותח את הקובץ בו שמור כל שמות המשימות
        names_task_file = open(rf'{path}/{getEmail()}/names_of_user_tasks.txt', 'r')
        content = names_task_file.read()

        # מפצל את השמות בקובץ לרשימה
        global task_name_list
        task_name_list = content.split("&")

        # מפעיל את user_select_task ושומר את שם המשימה
        user_input = user_select_task()

        # עובר על הרשימה ומוצא את השם המתאים

        for name in task_name_list:
            if search_string_in_file(name, user_input):
                user_input_error = name
                print(user_input_error)
                return user_input_error
            # אם אין שם מתאים ומבקש מהשמשתמש שיחזור על שם המשימה


# הפונקציה בודקת האם הניסיון השגוי של המשתמש מקושר לאחד המשימות ואם כן היא מחזירה את השם של המשימה אליה הניסיון השגוי מקושר
def check_final_file1():
    while True:
        # פותח את הקובץ בו שמור כל שמות המשימות
        names_task_file = open(rf'{path}/{getEmail()}/names_of_user_tasks.txt', 'r')
        content = names_task_file.read()

        # מפצל את השמות בקובץ לרשימה
        global task_name_list
        task_name_list = content.split("&")

        # מפעיל את user_select_task ושומר את שם המשימה
        user_input = user_select_task1("google")

        # עובר על הרשימה ומוצא את השם המתאים

        for name in task_name_list:
            if search_string_in_file(name, user_input):
                user_input_error = name
                print(user_input_error)
                return user_input_error
            # אם אין שם מתאים ומבקש מהשמשתמש שיחזור על שם המשימה


# הפונקציה פותחת את הקבצים מההקלטה וממיינת אותם לפי הזמנים
def read_files_from_record_task():
    user_input_error = check_final_file()

    with open(f"{path}/{getEmail()}/file_saver/{user_input_error}_kb.txt", 'r') as f1:
        data_kb = f1.read().replace('\n', '')
    kb = data_kb

    with open(f"{path}/{getEmail()}/file_saver/{user_input_error}_mb.txt", 'r') as f2:
        data_mb = f2.read().replace('\n', '')
    mb = data_mb

    with open(f"{path}/{getEmail()}/file_saver/{user_input_error}_mw.txt", 'r') as f3:
        data_mw = f3.read().replace('\n', '')
    mw = data_mw

    with open(f"{path}/{getEmail()}/file_saver/{user_input_error}_mm.txt", 'r') as f4:
        data_mm = f4.read().replace('\n', '')
    mm = data_mm

    # מפריד את הפעולות לרשימה
    all_events = back_to_events(kb.split('#'), mb.split('#'), mm.split('#'), mw.split('#'))

    # סוכם את הפעולות לפעולה אחת שכוללת את כל האירועים
    kb_events, mb_events, mm_events, mw_events = all_events
    all_mouse_events = mb_events + mm_events + mw_events

    # הפונקציה ממינת את הפעולות לפי הזמן
    all_mouse_events = sorted(all_mouse_events, key=lambda event: event.time)

    return all_mouse_events, kb_events


# הפונקציה מפעילה את המשימה
def playing_the_task():
    all_mouse_events, kb_events = read_files_from_record_task()

    keyboard.start_recording()
    keyboard.stop_recording()

    Common.ctrlWinD()

    runMouseMouseKeyboardEvents(all_mouse_events, kb_events, 1, 1)

    Common.ctrlWinArrow()


# פה הכל רץ
if __name__ == '__main__':
    ask_close_tab()
    playing_the_task()
    close_desktop_end()
