import keyboard, helper_events
from pyautogui import keyDown, keyUp, press
from helper_events import back_to_events
from auto_tasks import keyboard_and_mouse_recorder, runMouseMouseKeyboardEvents
from mouse import MoveEvent, WheelEvent
from Common import getEmail

closing_desktop_task_name = "user_name_tab"

def check_if_close_desktop_task_name_exiest():
    with open(f"file_saver_close_desktop/{closing_desktop_task_name}_kb.txt", 'r') as fc:
        data_check = fc.read().replace('\n', '')



def close_tabs_helper():
    with open(f"{getEmail()}/file_saver/close_new_desktop_after_recording_system_file_kb.txt", 'r') as f1:
        data_kb = f1.read().replace('\n', '')
    kb = data_kb

    with open(f"{getEmail()}/file_saver/close_new_desktop_after_recording_system_file_mb.txt", 'r') as f2:
        data_mb = f2.read().replace('\n', '')
    mb = data_mb

    with open(f"{getEmail()}/file_saver/close_new_desktop_after_recording_system_file_mw.txt", 'r') as f3:
        data_mw = f3.read().replace('\n', '')
    mw = data_mw

    with open(f"{getEmail()}/file_saver/close_new_desktop_after_recording_system_file_mm.txt", 'r') as f4:
        data_mm = f4.read().replace('\n', '')
    mm = data_mm

    all_events = back_to_events(kb.split('#'), mb.split('#'), mm.split('#'), mw.split('#'))
    kb_events, mb_events, mm_events, mw_events = all_events

    all_mouse_events = mb_events + mm_events + mw_events
    all_mouse_events = sorted(all_mouse_events, key=lambda event: event.time)

    keyboard.start_recording()
    keyboard.stop_recording()

    keyDown("winleft")
    press("tab")
    keyUp("winleft")

    runMouseMouseKeyboardEvents(all_mouse_events, kb_events, 1)


def record_desktop_close():
    mouse_events, keyboard_events = keyboard_and_mouse_recorder()
    mouse_button = []
    mouse_wheel = []
    mouse_move = []
    for event in mouse_events:
        if type(event) == MoveEvent:
            mouse_move.append(event)
        elif type(event) == WheelEvent:
            mouse_wheel.append(event)
        else:
            mouse_button.append(event)
    all_lists = helper_events.reformat_all(keyboard_events[:-1], mouse_button, mouse_wheel, mouse_move)
    # keyboard
    kb = '#'.join(all_lists[0])
    # mouse
    mb = '#'.join(all_lists[1])  # button
    mm = '#'.join(all_lists[2])  # move
    mw = '#'.join(all_lists[3])

    with open(f"{getEmail()}/file_saver/close_new_desktop_after_recording_system_file_kb.txt", 'w') as f:
        f.write(kb)

    with open(f"{getEmail()}/file_saver/close_new_desktop_after_recording_system_file_mb.txt", 'w') as f:
        f.write(mb)

    with open(f"{getEmail()}/file_saver/close_new_desktop_after_recording_system_file_mm.txt", 'w') as f:
        f.write(mm)

    with open(f"{getEmail()}/file_saver/close_new_desktop_after_recording_system_file_mw.txt", 'w') as f:
        f.write(mw)



#  אם המשתמש עונה שהוא חפץ לסגור את החלון החדש הפונקציה בודקת האם קיימת הקלטה של סגירת חלון חדש
def close_tabs():
    try:
        check_if_close_desktop_task_name_exiest()
        return "Found a recording of closing the new desktop"
    except:
        return "Did not find a recording of closing the new desktop"



# אם לא קיימת הקלטה של סל סגירת חלון חדש הפונקציה שואלת את המשתמש האם הוא חפץ להקליט ואם הוא עונה כן הפונקציה מתחילה להקליט את העכבר והמקלדת של המשתמש
def ask_close_tab():

    global user_answer
    # שואל את המשתמש האם הוא חפץ לסגור את החלון החדש לאחר הפתיחה
    user_answer = input(
        "Do you wish to close the new desktop after the task? (yes/no) or (y/n):  ")

    if close_tabs() == "Did not find a recording of closing the new desktop":
        user_choise = input("Do you wish to close the new desktop after the task? (yes/no) or (y/n):  ")
        if user_choise in "yes":
            record_desktop_close()



# אם קיים הקלטה של סגירת החלון החדש והמשתמש בחר לסגור אותה לאחר ההקלטה הפונקציה תבצע את ההקלטה
def close_desktop_end():
    if close_tabs() == "Found a recording of closing the new desktop" and user_answer in "yes":
        close_tabs_helper()
