import threading
from copy import deepcopy
from os import getenv
from mouse import hook, unhook, play
from time import sleep
from threading import Thread, Timer
from Common import key, getEmail
import keyboard


app_data_path = getenv('APPDATA')
path = f"{app_data_path}\Auto Tasks"
def mouse_recorder():  # save mouse events in text file
    textfile = open("mouse_file.txt", "w")

    mouse_events = []
    hook(mouse_events.append)
    keyboard.wait("esc")
    unhook(mouse_events.append)

    for element in mouse_events:
        textfile.write(str(element) + "\n")
    textfile.close()

    a_file = open("mouse_file.txt", "r")
    list_of_lists = []

    for line in a_file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        list_of_lists.append(line_list)
    a_file.close()

    event_name = deepcopy(mouse_events)

    return event_name


def keyboard_recorder():  # save keyboard events in text file
    f = 'Keyboard_Location'
    file = open(f, 'a')
    text = keyboard.record(until='esc')
    file.write(str(text))
    file.close()
    return text


def maximize_window_thread():
    while True:
        if keep_maximized == True:
            keyboard.press("left windows")
            keyboard.press_and_release("up")
            keyboard.release("left windows")
            sleep(5)
        else:
            break

def maximized_window():
    max_thread = Thread(target=lambda: maximize_window_thread(), daemon=True)
    max_thread.start()

def keyboard_and_mouse_recorder_for_close_desktop():
    mouse_events = []
    keyboard_events = []

    # Start recording

    hook(mouse_events.append)  # starting the mouse recording
    keyboard.start_recording()  # starting the keyboard recording

    keyboard.wait(key())  # Waiting for 'Esc' button to be pressed

    unhook(mouse_events.append)
    keyboard_events = keyboard.stop_recording()

    return mouse_events, keyboard_events


def keyboard_and_mouse_recorder():
    global keep_maximized

    with open(rf"{path}\{getEmail()}\maximized_choice.txt", "r") as f:
        data = f.read()

    if data == "Yes":
        keep_maximized = True
        mouse_events = []
        keyboard_events = []

        # Start recording

        hook(mouse_events.append)  # starting the mouse recording
        keyboard.start_recording()  # starting the keyboard recording

        maximized_window()

        keyboard.wait(key())  # Waiting for 'Esc' button to be pressed

        unhook(mouse_events.append)
        keyboard_events = keyboard.stop_recording()

        keep_maximized = False

        return mouse_events, keyboard_events

    else:
        mouse_events = []
        keyboard_events = []

        # Start recording

        hook(mouse_events.append)  # starting the mouse recording
        keyboard.start_recording()  # starting the keyboard recording

        keyboard.wait(key())  # Waiting for 'Esc' button to be pressed

        unhook(mouse_events.append)
        keyboard_events = keyboard.stop_recording()

        return mouse_events, keyboard_events



def runMouseMouseKeyboardEvents(mouse_events, keyboard_events, number_of_operation, speed_factor):  # Playing the recorded events at the same time


    for i in range(number_of_operation):
        try:
            time_dif = keyboard_events[0].time - mouse_events[0].time
        except:
            time_dif = 0

        if time_dif >= 0:
            target = lambda: keyboard.play(keyboard_events, speed_factor=speed_factor*0.955)
            k_thread = Timer((time_dif/speed_factor)+0.5/speed_factor, target)
            k_thread.daemon = True
            k_thread.start()
            m_thread = Thread(target=lambda: play(mouse_events, speed_factor=speed_factor), daemon=True)
            m_thread.start()

            k_thread.join()
            m_thread.join()
        else:
            k_thread = threading.Thread(target=lambda: keyboard.play(keyboard_events, speed_factor=speed_factor), daemon=True)
            k_thread.start()

            target = lambda: play(mouse_events, speed_factor=speed_factor)
            m_thread = Timer(-(time_dif/speed_factor), target)
            m_thread.daemon = True
            m_thread.start()

            k_thread.join()
            m_thread.join()


def runMouseMouseKeyboardEvents_close_new_desktop(mouse_events, keyboard_events, number_of_operation):  # Playing the recorded events at the same time

    m_thread = Thread(target=lambda: play(mouse_events), daemon=True)
    m_thread.start()

    m_thread.join()





