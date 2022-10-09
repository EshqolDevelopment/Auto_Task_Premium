import keyboard
import mouse


def k_event_to_string(event):
    return str(event.event_type) + " " + str(event.scan_code) + " " + str(event.name) + " " + str(
        event.time) + " " + str(
        event.device) + " " + str(event.modifiers) + " " + str(event.is_keypad)



def k_string_to_event(string):
    attributes = string.split()
    if len(attributes) == 7:
        is_keypad = True if attributes[6][0] == 'T' else False
        modifiers = None
        return keyboard.KeyboardEvent(attributes[0], int(attributes[1]), attributes[2], float(attributes[3]), None,
                                      modifiers, is_keypad)
    else:
        is_keypad = True if attributes[7][0] == 'T' else False
        modifiers = None
        return keyboard.KeyboardEvent(attributes[0], int(attributes[1]), attributes[2] + " " + attributes[3],
                                      float(attributes[4]), None, modifiers, is_keypad)


def m_button_event_to_string(event):
    return str(event.event_type) + " " + str(event.button) + " " + str(event.time)


def m_button_string_to_event(string):
    attributes = string.split()
    return mouse.ButtonEvent(attributes[0], attributes[1], float(attributes[2]))


def m_move_event_to_string(event):
    return str(event.x) + " " + str(event.y) + " " + str(event.time)


def m_move_string_to_event(string):
    attributes = string.split()
    return mouse.MoveEvent(int(attributes[0]), int(attributes[1]), float(attributes[2]))


def m_wheel_event_to_string(event):
    return str(event.delta) + " " + str(event.time)


def m_wheel_string_to_event(string):
    attributes = string.split()
    return mouse.WheelEvent(float(attributes[0]), float(attributes[1]))

def reformat_all(keyboard_event, mouse_button, mouse_wheel, mouse_move):
    kb = []
    mb = []
    mm = []
    mw = []
    for event in keyboard_event:
        kb.append(k_event_to_string(event))
    for event in mouse_button:
        mb.append(m_button_event_to_string(event))
    for event in mouse_wheel:
        mw.append(m_wheel_event_to_string(event))
    for event in mouse_move:
        mm.append(m_move_event_to_string(event))

    return kb, mb, mm, mw


def back_to_events(kb, mb, mm, mw):
    kb_events = []
    mb_events = []
    mm_events = []
    mw_events = []

    if kb[0] != '':
        for event in kb:
            kb_events.append(k_string_to_event(event))

    if mb[0] != '':
        for event in mb:
            mb_events.append(m_button_string_to_event(event))

    if mw[0] != '':
        for event in mw:
            mw_events.append(m_wheel_string_to_event(event))

    if mm[0] != '':
        for event in mm:
            mm_events.append(m_move_string_to_event(event))

    return kb_events, mb_events, mm_events, mw_events