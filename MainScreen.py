import Common, helper_events, keyboard, datetime
from Common import ImagePath
from threading import Thread
from time import sleep
from os import remove, getenv, listdir, mkdir
from mouse import MoveEvent, WheelEvent
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from speech_recognition import Microphone, Recognizer
from kivy.factory import Factory
from auto_tasks import runMouseMouseKeyboardEvents
from kivy.config import Config
from record_task import open_new_desktop_and_come_back_to_original_and_record, just_record, close_desktop_record
from helper_events import back_to_events
from select_task import search_string_in_file
from kivymd.app import MDApp
from kivymd.uix.picker import MDTimePicker
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivy.uix.settings import SettingsPanel
from webbrowser import open as openweb
from Common import ReadOpenWindow, ReadCloseWindow, SetOpenWindow, SetCloseWindow, ctrlWinD, ctrlWinArrow, getEmail
from ctypes import *
from encrypt_files import decfile, encfile


from kivy.core.window import Window
from kivy.uix.button import Button


Window.size = (1080, 720)
app_data_path = getenv('APPDATA')
path = f"{app_data_path}/Auto Tasks"
Config.set('graphics', 'resizable', True)
Config.set('input', 'mouse', 'mouse, multitouch_on_demand')
Config.set('kivy', 'exit_on_escape', '0')
Config.write()
Common.writeInFile(rf"{path}\checkbox_for_new_desktop.txt", "True")

Main = """
<Tutorial>
    MDLabel:
        id: mainText
        text: "Welcome to Auto Tasks!\\nWe highly recommending you to\\nwatch an overview tutorial to\\nunderstand better our software"
        font_size: 26
        halign: 'left'
        pos_hint: {"center_x": 0.55, "center_y": 0.65}

    MDRaisedButton:
        text: app.WatchText
        font_size: 16
        pos_hint: {"center_x": 0.35, "center_y": 0.2}
        md_bg_color: 255/255, 165/255, 0, 1

    MDRaisedButton:
        text: "Watch now"
        font_size: 16
        pos_hint: {"center_x": 0.65, "center_y": 0.2}
        on_press: app.open_tutorial()
        md_bg_color: 255/255, 165/255, 0, 1

    Image:
        source: app.logoPng
        size_hint_y: None  # Tells the layout to ignore the size_hint in y dir
        height: dp(90)  # The fixed height you want
        pos_hint: {"center_x": 0.85, "center_y": 0.7}

<ScheduleTasks>
    BoxLayout:
        orientation: 'vertical'
        pos_hint: {"center_x": 0.53, "center_y": 0.3}
        size_hint_x: None
        size_hint_y: 1.18
        width: 350
        disabled: app.scheduleDisable
        ScrollView:
            size_hint_y: None
            BoxLayout:
                id: YourTaskName
                orientation: 'horizontal'
                size_hint_x: None
                width: self.minimum_width
        AutoCompleter:
            size_hint_y: None
            container: YourTaskName
            size_hint_y: 0.2
            size_hint_x: 0.9
            color_mode: 'accent'
            mode: "rectangle"
            font_size: 24
            disabled: app.scheduleDisable
        Widget:

    Label:
        id: a
        text: app.ScheduledLabel
        size_hint_x: None
        font_size: 20
        pos_hint: {"center_x": 0.5, "center_y": 0.86}
        opacity: 1

    MDRectangleFlatButton: #select task button
        text: "Scheduled your task"
        font_size: 16
        pos_hint: {"center_x": 0.65, "center_y": 0.15}
        opacity: app.opacityDisable
        disabled: app.scheduleDisable
        on_press:
            app.show_date_picker_via_main_screen()

    MDRectangleFlatButton: #quit button
        text: "Close"
        font_size: 16
        pos_hint: {"center_x": 0.3, "center_y": 0.15}


<delete>
    Label:
        text: "Deleted successfully"
        font_size: 22
        pos_hint: {"center_x": 0.5, "center_y": 0.82}

    Label:
        text: "the changes will appear once\\nyou restart the software"
        font_size: 14
        pos_hint: {"center_x": 0.5, "center_y": 0.52}


    MDRectangleFlatButton: #quit button
        text: "Close"
        font_size: 12
        pos_hint: {"center_x": 0.5, "center_y": 0.2}

<view>
    Label:
        id: scLabel
        text: app.scLabel
        font_size: 22
        pos_hint: {"center_x": 0.5, "center_y": 0.65}

    MDRectangleFlatButton: #quit button
        text: "Close"
        font_size: 12
        pos_hint: {"center_x": 0.5, "center_y": 0.2}

<ShortcutWord>
    MDTextField:
        mode: "rectangle"
        id: www
        hint_text: "Enter a word"
        size_hint_x: None
        width: 330
        font_size: 22
        pos_hint: {"center_x": 0.5, "center_y": 0.85}
        disabled: app.disabledShortcut

    MDRectangleFlatButton:
        text: "Press here and record key"
        size_hint_x: None
        width: 50
        font_size: 20
        pos_hint: {"center_x": 0.5, "center_y": 0.57}
        on_press: app.recordShortCut_thred()
        disabled: app.disabledShortcut

    Label:
        id: scLabel
        text: app.keysLive
        size_hint_x: None
        font_size: 21
        pos_hint: {"center_x": 0.5, "center_y": 0.43}
        disabled: app.disabledShortcut

    MDRectangleFlatButton: #quit button
        text: "Close"
        font_size: 16
        pos_hint: {"center_x": 0.35, "center_y": 0.15}

    MDRectangleFlatButton: #save button
        text: "Save"
        font_size: 16
        pos_hint: {"center_x": 0.65, "center_y": 0.15}
        on_press: app.word_short_cuts(www.text)
        disabled: app.disabledShortcut


<ShortcutsSelecter>
    BoxLayout:
        orientation: 'vertical'
        pos_hint: {"center_x": 0.52, "center_y": 0.53}
        size_hint_x: None
        size_hint_y: 1.18
        width: 350
        disabled: app.disabledShortcut
        ScrollView:
            size_hint_y: None
            BoxLayout:
                id: YourTaskName
                orientation: 'horizontal'
                size_hint_x: None
                width: self.minimum_width

        AutoCompleter:
            size_hint_y: None
            container: YourTaskName
            size_hint_y: 0.2
            size_hint_x: 0.9
            color_mode: 'accent'
            mode: "rectangle"
            font_size: 24
        Widget:

    MDRectangleFlatButton:
        text: "Press here and record key"
        size_hint_x: None
        width: 50
        font_size: 20
        pos_hint: {"center_x": 0.5, "center_y": 0.54}
        on_press: app.recordShortCut_thred()
        disabled: app.disabledShortcut

    Label:
        id: scLabel
        text: app.keysLive
        size_hint_x: None
        font_size: 21
        pos_hint: {"center_x": 0.5, "center_y": 0.38}
        disabled: app.disabledShortcut

    MDRectangleFlatButton: #quit button
        text: "Close"
        font_size: 16
        pos_hint: {"center_x": 0.35, "center_y": 0.15}

    MDRectangleFlatButton: #save button
        text: "Save"
        font_size: 16
        pos_hint: {"center_x": 0.65, "center_y": 0.15}
        on_press: app.SaveShortcut()
        disabled: app.disabledShortcut

<CloseWindow>
    Label:
        id: CloseWindowLabel
        text: app.CloseWindowLabel1
        font_size: 21
        pos_hint: {"center_x": 0.5, "center_y": 0.75}

    MDRectangleFlatButton: #youtube button
        text: "Watch a tutorial"
        font_size: 16
        on_press: app.open_url()
        pos_hint: {"center_x": 0.8, "center_y": 0.23}

    MDRectangleFlatButton: #quit button
        text: "Close"
        font_size: 16
        pos_hint: {"center_x": 0.2, "center_y": 0.23}

    MDRectangleFlatButton: #start recording
        text: "Start recording"
        font_size: 16
        pos_hint: {"center_x": 0.48, "center_y": 0.23}
        on_press: app.ChangeLabel123()
        on_release: app.record_event_of_closing_new_desktop()

<ShortCuts>
    MDRectangleFlatButton:
        text: "Press here and record key"
        size_hint_x: None
        width: 50
        font_size: 20
        pos_hint: {"center_x": 0.5, "center_y": 0.8}
        on_press: app.recordShortCut_thred()
        disabled: app.disabledShortcut

    Label:
        id: scLabel
        text: app.keysLive
        size_hint_x: None
        font_size: 21
        pos_hint: {"center_x": 0.5, "center_y": 0.58}
        disabled: app.disabledShortcut

    MDRectangleFlatButton: #quit button
        text: "Close"
        font_size: 16
        pos_hint: {"center_x": 0.35, "center_y": 0.2}

    MDRectangleFlatButton: #save button
        text: "Save"
        font_size: 16
        pos_hint: {"center_x": 0.65, "center_y": 0.2}
        on_press: app.WriteShortcut()
        disabled: app.disabledShortcut

<RunTask>
    MDTextField:
        id: loop
        text: "1"
        size_hint_x: None
        width: 48
        font_size: 18
        pos_hint: {"center_x": 0.15, "center_y": 0.63}
    MDLabel:
        text: "Number of\\n iterations"
        size_hint_x: None
        font_size: 15
        pos_hint: {"center_x": 0.17, "center_y": 0.53}
        
    MDTextField:
        id: SpeedFactor
        text: "1"
        size_hint_x: None
        width: 48
        font_size: 18
        pos_hint: {"center_x": 0.15, "center_y": 0.4}
    MDLabel:
        text: "Speed Factor"
        size_hint_x: None
        font_size: 15
        pos_hint: {"center_x": 0.17, "center_y": 0.32}



    CheckBox:
        pos_hint: {"center_x": 0.85, "center_y": 0.55}
        active: True
        on_active: app.choice_open_new_desktop(self.active)
        background_checkbox_normal: app.checkBoxImage
        background_checkbox_down: app.checkBoxImage2
        size_hint_x: None
        size_hint_y: None
        size: sp(60), sp(60)

    MDLabel:
        text: "Open new window"
        size_hint_x: None
        font_size: 14
        pos_hint: {"center_x": 0.89, "center_y": 0.45}

    CheckBox:
        pos_hint: {"center_x": 0.85, "center_y": 0.25}
        active: False
        on_active: app.check_box(self.active)
        background_checkbox_normal: app.checkBoxImage
        background_checkbox_down: app.checkBoxImage2
        size_hint_x: None
        size_hint_y: None
        size: sp(60), sp(60)
        opacity: app.opacityCheckbox
        disabled: app.disabledCheckbox

    MDLabel:
        text: "Close window\\nafter running"
        size_hint_x: None
        font_size: 14
        pos_hint: {"center_x": 0.86, "center_y": 0.14}
        opacity: app.opacityCheckbox

    BoxLayout:
        orientation: 'vertical'
        pos_hint: {"center_x": 0.52, "center_y": 0.53}
        size_hint_x: None
        size_hint_y: 1.3
        width: 350
        ScrollView:
            size_hint_y: None
            BoxLayout:
                id: YourTaskName
                orientation: 'horizontal'
                size_hint_x: None
                width: self.minimum_width
        AutoCompleter:
            size_hint_y: None
            container: YourTaskName
            size_hint_y: 0.2
            size_hint_x: 0.9
            color_mode: 'accent'
            mode: "rectangle"
            font_size: 24
        Widget:

    Label:
        id: a
        text: app.labelSelect
        size_hint_x: None
        font_size: 20
        pos_hint: {"center_x": 0.48, "center_y": 0.59}
        opacity: 1
    MDRectangleFlatButton: #select task button
        text: "Select task"
        font_size: 16
        pos_hint: {"center_x": 0.25, "center_y": 0.15}

        on_release:                
            app.selectTasksKivy(loop.text, SpeedFactor.text)

    MDRectangleFlatButton: #quit button
        text: "Close"
        font_size: 16
        pos_hint: {"center_x": 0.55, "center_y": 0.15}

<NewTaskNoMic>
    CheckBox:
        pos_hint: {"center_x": 0.8, "center_y": 0.3}
        active: False
        on_active: app.check_box(self.active)
        background_checkbox_normal: app.checkBoxImage
        background_checkbox_down: app.checkBoxImage2
        size_hint_x: None
        size_hint_y: None
        size: sp(60), sp(60)
        opacity: app.opacityCheckbox
        disabled: app.disabledCheckbox

    CheckBox:
        pos_hint: {"center_x": 0.8, "center_y": 0.6}
        active: True
        on_active: app.choice_open_new_desktop(self.active)
        background_checkbox_normal: app.checkBoxImage
        background_checkbox_down: app.checkBoxImage2
        size_hint_x: None
        size_hint_y: None
        size: sp(60), sp(60)

    MDLabel:
        text: "Close window\\nafter recording"
        size_hint_x: None
        font_size: 15
        pos_hint: {"center_x": 0.8, "center_y": 0.185}
        opacity: app.opacityCheckbox

    MDLabel:
        text: "Open new window"
        size_hint_x: None
        font_size: 15
        pos_hint: {"center_x": 0.83, "center_y": 0.495}

    MDTextField:
        mode: "rectangle"
        id: TaskName
        hint_text: "Your task name"
        size_hint_x: None
        width: 235
        font_size: 22
        pos_hint: {"center_x": 0.4, "center_y": 0.85}

    Label: #second label
        id: p
        text: app.output
        size_hint_x: None
        font_size: 20
        pos_hint: {"center_x": 0.35, "center_y": 0.55}

    MDRectangleFlatButton: #start recording button
        text: app.b3
        font_size: 16
        pos_hint: {"center_x": 0.25, "center_y": 0.2}
        on_press:
            app.changeLabel2(TaskName.text)
        on_release:
            app.start_and_save(TaskName.text)
        disabled: app.disable
        opacity: app.opacity

    MDRectangleFlatButton: #quit button
        text: "Close"
        font_size: 16
        pos_hint: {"center_x": 0.55, "center_y": 0.2}


<NewTask>
    CheckBox:
        pos_hint: {"center_x": 0.8, "center_y": 0.3}
        active: False
        on_active: app.check_box(self.active)
        background_checkbox_normal: app.checkBoxImage
        background_checkbox_down: app.checkBoxImage2
        size_hint_x: None
        size_hint_y: None
        size: sp(60), sp(60)
        opacity: app.opacityCheckbox
        disabled: app.disabledCheckbox

    CheckBox:
        pos_hint: {"center_x": 0.8, "center_y": 0.6}
        active: True
        on_active: app.choice_open_new_desktop(self.active)
        background_checkbox_normal: app.checkBoxImage
        background_checkbox_down: app.checkBoxImage2
        size_hint_x: None
        size_hint_y: None
        size: sp(60), sp(60)

    MDLabel:
        text: "Close window\\nafter recording"
        size_hint_x: None
        font_size: 15
        pos_hint: {"center_x": 0.8, "center_y": 0.185}
        opacity: app.opacityCheckbox
    MDLabel:
        text: "Open new window"
        size_hint_x: None
        font_size: 15
        pos_hint: {"center_x": 0.83, "center_y": 0.495}
    MDTextField:
        mode: "rectangle"
        id: TaskName
        hint_text: "Your task name"
        size_hint_x: None
        width: 235
        font_size: 22
        pos_hint: {"center_x": 0.4, "center_y": 0.85}
    Label: #main label
        id: recorder
        text: app.text
        size_hint_x: None
        font_size: 20
        pos_hint: {"center_x": 0.4, "center_y": 0.6}
        opacity: app.opac
    Label: #second label
        id: p
        text: app.output
        size_hint_x: None
        font_size: 20
        pos_hint: {"center_x": 0.35, "center_y": 0.55}
        opacity: app.opac2
    Image:
        source: app.micImage
        size_hint_y: None  # Tells the layout to ignore the size_hint in y dir
        height: dp(50)  # The fixed height you want
        pos_hint: {"center_x": 0.8, "center_y": 0.85}

    MDRectangleFlatButton: #audio button
        text: "Start recording"
        font_size: 16
        pos_hint: {"center_x": 0.8, "center_y": 0.85}
        disabled: app.disabLable
        opacity: 0
        on_press:
            app.change()
        on_release:
            app.startRecord(TaskName.text)

    MDRectangleFlatButton: #i cant record button
        text: app.b2
        font_size: 16
        pos_hint: {"center_x": 0.25, "center_y": 0.2}
        on_press:
            app.okay(TaskName.text, recorder.text)
        disabled: app.disabLable
        opacity: app.opac4

    MDRectangleFlatButton: #start recording button
        text: app.b3
        font_size: 16
        pos_hint: {"center_x": 0.25, "center_y": 0.2}
        on_press:
            app.changeLabel()
        on_release:
            app.start_and_save(TaskName.text)
        disabled: app.disable
        opacity: app.opac3

    MDRectangleFlatButton: #quit button
        text: "Close"
        font_size: 16
        pos_hint: {"center_x": 0.55, "center_y": 0.2}



<ContentNavigationDrawer>:
    ScrollView:
        MDList:
            TwoLineIconListItem:
                text: "Home"
                secondary_text: "Your main screen"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "Home"
                IconLeftWidget:
                    icon: "home"

            TwoLineIconListItem:
                text: "Settings"
                secondary_text: "Your settings screen"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "Settings"
                IconLeftWidget:
                    icon: "wrench"

            TwoLineIconListItem:
                text: "Task manager"
                secondary_text: "Task editor and modifier"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "Task manager"
                IconLeftWidget:
                    icon: "border-color"

            TwoLineIconListItem:
                text: "Keyboard manager"
                secondary_text: "Shortcuts manager screen"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "Keyboard manager"
                IconLeftWidget:
                    icon: "keyboard"

            TwoLineIconListItem:
                text: "Schedule manager"
                secondary_text: "Schedule manager screen"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "Schedule manager"
                IconLeftWidget:
                    icon: "alarm-check"




Screen:
    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "Auto Tasks"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
    MDNavigationLayout:
        x: toolbar.height
        ScreenManager:
            id: screen_manager

            Screen:
                name: "Home"

                MDLabel:
                    text: f"Hello {app.getName()}!"
                    halign: "center"
                    font_size: 24
                    pos_hint: {"center_x": 0.5, "center_y": 0.958}
                    bold: True
                Image:
                    source: app.micImage   
                    allow_stretch: True          
                    size_hint_y: 0.185  # Tells the layout to ignore the size_hint in y dir
                    #height: dp(125)  # The fixed height you want
                    pos_hint: {"center_x": 0.5, "center_y": 0.7}

                MDRectangleFlatButton: #audio run button
                    text: "aa"
                    font_size: 100
                    # disabled: app.isMic
                    pos_hint: {"center_x": 0.5, "center_y": 0.7}
                    on_release: app.audioRun()
                    on_press: app.change2()
                    size_hint_y: 0.2
                    size_hint_x: 0.13
                    opacity: 0

                MDLabel:
                    text: app.micLabel
                    halign: "center"
                    font_size: 28
                    pos_hint: {"center_x": 0.5, "center_y": 0.55}
                    bold: True

                MDLabel:
                    text: "Create new task"
                    halign: "center"
                    font_size: 28
                    pos_hint: {"center_x": 0.2, "center_y": 0.55}
                    bold: True
                Image:
                    source: app.plusImage
                    allow_stretch: True
                    size_hint_y: 0.185
                    #height: dp(125)
                    pos_hint: {"center_x": 0.2, "center_y": 0.7}
                MDRectangleFlatButton: #show new task dialog
                    text: "aa"
                    font_size: 100
                    pos_hint: {"center_x": 0.2, "center_y": 0.7}
                    on_press: app.Show()
                    size_hint_y: 0.2
                    size_hint_x: 0.13
                    opacity: 0


                MDLabel:
                    text: "Run your task"
                    halign: "center"
                    font_size: 28
                    pos_hint: {"center_x": 0.8, "center_y": 0.55}
                    bold: True
                MDRectangleFlatButton:
                    text: "aa"
                    font_size: 100
                    pos_hint: {"center_x": 0.8, "center_y": 0.7}
                    on_press: app.Show2()
                    size_hint_y: 0.2
                    size_hint_x: 0.13
                    opacity: 0

                Image:
                    source: app.runImage
                    allow_stretch: True
                    size_hint_y: 0.2  # Tells the layout to ignore the size_hint in y dir
                    #height: dp(130)  # The fixed height you want
                    pos_hint: {"center_x": 0.8, "center_y": 0.7}

                Image:
                    source: app.KeyboardImage
                    allow_stretch: True
                    size_hint_y: 0.2  # Tells the layout to ignore the size_hint in y dir
                    #height: dp(131)  # The fixed height you want
                    pos_hint: {"center_x": 0.8, "center_y": 0.3}
                MDLabel:
                    text: "Shortcut for task"
                    halign: "center"
                    font_size: 28
                    pos_hint: {"center_x": 0.8, "center_y": 0.15}
                    bold: True
                MDRectangleFlatButton:
                    text: "aa"
                    font_size: 100
                    pos_hint: {"center_x": 0.8, "center_y": 0.3}
                    size_hint_y: 0.2
                    size_hint_x: 0.13
                    on_press: app.ScSelecter()
                    opacity: 0


                Image:
                    source: app.GreenKeyboardImage
                    allow_stretch: True
                    size_hint_y: 0.193  # Tells the layout to ignore the size_hint in y dir
                    #height: dp(128)  # The fixed height you want
                    pos_hint: {"center_x": 0.2, "center_y": 0.3}
                MDLabel:
                    text: "Shortcut for word"
                    halign: "center"
                    font_size: 28
                    pos_hint: {"center_x": 0.2, "center_y": 0.15}
                    bold: True
                MDRectangleFlatButton:
                    text: "aa"
                    font_size: 100
                    pos_hint: {"center_x": 0.2, "center_y": 0.3}
                    on_press: app.SctWord()
                    size_hint_y: 0.2
                    size_hint_x: 0.13
                    opacity: 0

                Image:
                    source: app.ClockImage
                    allow_stretch: True
                    size_hint_y: 0.24  # Tells the layout to ignore the size_hint in y dir
                    #height: dp(160)  # The fixed height you want
                    pos_hint: {"center_x": 0.5, "center_y": 0.3}
                MDLabel:
                    text: "Schedule tasks"
                    halign: "center"
                    font_size: 28
                    pos_hint: {"center_x": 0.5, "center_y": 0.15}
                    bold: True

                MDRectangleFlatButton:
                    text: "aa"
                    font_size: 100
                    pos_hint: {"center_x": 0.5, "center_y": 0.3}
                    on_press: app.Schedule()
                    size_hint_y: 0.2
                    size_hint_x: 0.13
                    opacity: 0


            Screen:
                name: "Task manager"

                MDCard:
                    size_hint: 1, 0.905
                    #size: 1080,665
                    pos_hint: {"center_x": 0.5, "center_y": 0.46}
                    padding: 25
                    spacing: 25
                    orientation: 'vertical'
                    ScrollView:
                        MDList:
                            id: container

            Screen:
                name: "Settings"

                MDRectangleFlatButton:
                    text: "Watch a tutorial"
                    font_size: 20
                    pos_hint: {"center_x": 0.67, "center_y": 0.15}
                    on_press: app.open_tutorial()
                    #md_bg_color: 255/255, 255/255, 1, 0.8


                MDLabel:
                    text: f"Username: {app.getName()}"
                    halign: "center"
                    font_size: 24
                    pos_hint: {"center_x": 0.88, "center_y": 0.24}

                MDRectangleFlatButton:
                    text: "Log out"
                    font_size: 24
                    pos_hint: {"center_x": 0.88, "center_y": 0.15}
                    on_press: app.Logout()

                MDLabel:
                    text: "Open new desktop"
                    halign: "center"
                    font_size: 24
                    pos_hint: {"center_x": 0.62, "center_y": 0.78}
                MDLabel:
                    text: "Yes \ No"
                    halign: "center"
                    font_size: 15
                    pos_hint: {"center_x": 0.62, "center_y": 0.71}
                MDTextField:
                    id: open
                    size_hint_x: None
                    hint_text: app.getOpenDesktop()
                    color_mode: 'accent'
                    max_text_length: 3
                    width: 80
                    font_size: 18
                    pos_hint: {"center_x": 0.79, "center_y": 0.78}
                MDRectangleFlatButton:
                    text: "Save"
                    font_size: 18
                    pos_hint: {"center_x": 0.9, "center_y": 0.78}
                    on_press: app.saveOpenDesktop(open.text)

                MDLabel:
                    text: "Close new desktop"
                    halign: "center"
                    font_size: 24
                    pos_hint: {"center_x": 0.62, "center_y": 0.58}
                MDLabel:
                    text: "Yes \ No"
                    halign: "center"
                    font_size: 15
                    pos_hint: {"center_x": 0.62, "center_y": 0.51}
                MDTextField:
                    id: close
                    size_hint_x: None
                    hint_text: app.getCloseDesktop()
                    color_mode: 'accent'
                    max_text_length: 3
                    width: 80
                    font_size: 18
                    pos_hint: {"center_x": 0.79, "center_y": 0.58}
                MDRectangleFlatButton:
                    text: "Save"
                    font_size: 18
                    pos_hint: {"center_x": 0.9, "center_y": 0.58}
                    on_press: app.saveCloseDesktop(close.text)

                MDLabel:
                    text: "Maximize windows (beta)"
                    halign: "center"
                    font_size: 24
                    pos_hint: {"center_x": 0.6, "center_y": 0.4}
                MDLabel:
                    text: "Yes \ No"
                    halign: "center"
                    font_size: 15
                    pos_hint: {"center_x": 0.62, "center_y": 0.31}
                MDTextField:
                    id: close1
                    size_hint_x: None
                    hint_text: app.get_Maximized_window_choice_state()
                    color_mode: 'accent'
                    max_text_length: 3
                    width: 80
                    font_size: 18
                    pos_hint: {"center_x": 0.79, "center_y": 0.4}
                MDRectangleFlatButton:
                    text: "Save"
                    font_size: 18
                    pos_hint: {"center_x": 0.9, "center_y": 0.4}
                    on_press: app.save_Maximized_window_choice_state(close1.text)

                MDLabel:
                    text: "Operating system direction"
                    halign: "center"
                    font_size: 24
                    pos_hint: {"center_x": 0.2, "center_y": 0.8}
                MDLabel:
                    text: "Right \ Left"
                    halign: "center"
                    font_size: 17
                    pos_hint: {"center_x": 0.12, "center_y": 0.68}
                MDTextField:
                    id: Direction123
                    size_hint_x: None
                    hint_text: app.getDirection()
                    color_mode: 'accent'
                    max_text_length: 5
                    width: 80
                    font_size: 18
                    pos_hint: {"center_x": 0.25, "center_y": 0.68}
                MDRectangleFlatButton:
                    text: "Save"
                    font_size: 18
                    pos_hint: {"center_x": 0.35, "center_y": 0.68}
                    on_press: app.saveDirection(Direction123.text)

                MDSwitch:
                    active: False
                    on_active: app.darkMode()
                    pos_hint: {"center_x": 0.2, "center_y": 0.55}
                MDLabel:
                    text: "Dark mode"
                    halign: "left"
                    font_size: 24
                    pos_hint: {"center_x": 0.55, "center_y": 0.55}

                MDLabel:
                    text: "Color"
                    halign: "left"
                    font_size: 24
                    pos_hint: {"center_x": 0.55, "center_y": 0.4}

                MDRectangleFlatButton:
                    text: "Red"
                    font_size: 17
                    pos_hint: {"center_x": 0.19, "center_y": 0.4}
                    on_press: app.color("DeepOrange")
                MDRectangleFlatButton:
                    text: "Orange"
                    font_size: 17
                    pos_hint: {"center_x": 0.29, "center_y": 0.4}
                    on_press: app.color("Orange")
                MDRectangleFlatButton:
                    text: "Blue"
                    font_size: 17
                    pos_hint: {"center_x": 0.39, "center_y": 0.4}
                    on_press: app.color("Blue")

                MDLabel:
                    text: app.keyLabel
                    halign: "left"
                    font_size: 24
                    pos_hint: {"center_x": 0.55, "center_y": 0.25}
                MDLabel:
                    text: app.recordKey
                    halign: "left"
                    font_size: 21
                    pos_hint: {"center_x": 0.835, "center_y": 0.25}
                MDRectangleFlatButton:
                    text: "Record / Save"
                    font_size: 18
                    pos_hint: {"center_x": 0.49, "center_y": 0.25}
                    on_press: app.saveKey()

                MDLabel:
                    text: "Record yourself closing window"
                    halign: "left"
                    font_size: 24
                    pos_hint: {"center_x": 0.55, "center_y": 0.1}
                MDRectangleFlatButton:
                    text: "Press here"
                    font_size: 18
                    pos_hint: {"center_x": 0.48, "center_y": 0.1}
                    on_press: app.CloseWindowHelper()

            Screen:
                name: "Keyboard manager"

                MDCard:
                    size_hint: 1, 0.905
                    #size: 1080,665
                    pos_hint: {"center_x": 0.5, "center_y": 0.46}
                    padding: 25
                    spacing: 25
                    orientation: 'vertical'
                    ScrollView:
                        MDList:
                            id: container2

            Screen:
                name: "Schedule manager"

                MDCard:
                    size_hint: 1, 0.905
                    #size: 1080,665
                    pos_hint: {"center_x": 0.5, "center_y": 0.46}
                    padding: 25
                    spacing: 25
                    orientation: 'vertical'
                    ScrollView:
                        MDList:
                            id: container3


        MDNavigationDrawer:
            id: nav_drawer
            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer


"""

class Tutorial(FloatLayout):
    pass

class delete(FloatLayout): pass

class view(FloatLayout): pass

class ShortcutWord(FloatLayout): pass

class ShortcutsSelecter(FloatLayout):
    pass

class NewTask(FloatLayout):
    def Build(self):
        self.theme_cls.theme_style = "Light"

class NewTaskNoMic(FloatLayout):
    pass

class CloseWindow(FloatLayout): pass

class ScheduleTasks(FloatLayout): pass

class RunTask(FloatLayout): pass

class ShortCuts(FloatLayout): pass

class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class AutoCompleter(Factory.MDTextField):
    suggestions = Factory.ListProperty()
    container = Factory.ObjectProperty()

    def listOfNames(self):
        with open(rf"{path}/{getEmail()}/names_of_user_tasks.txt", "r") as name_of_user_tasks:
            data_from_name_of_user_tasks = name_of_user_tasks.readlines()
            name_of_user_tasks_list = []
            for task in data_from_name_of_user_tasks:
                name_of_user_tasks_list.append(task)
            return name_of_user_tasks_list

    def on_text(self, _, text):
        out = []
        DATA_SOURCE = self.listOfNames()
        for word in DATA_SOURCE:
            if text in word:
                global work_name
                work_name = text
                out.append(word)
        self.suggestions = out
        global new_work_name

        try:
            new_work_name = min(out, key=len)
            new_work_name = new_work_name[:-1]
        except:
            new_work_name = ""

    def on_suggestions(self, _, suggestions):
        container = self.container
        if not container:
            return
        container.clear_widgets()
        for word in suggestions:
            btn = Factory.MDRectangleFlatButton(text=word[:-1],
                                                on_press=self.select_word,
                                                size_hint_x=None,
                                                width=150, )
            container.add_widget(btn)

    def select_word(self, btn):
        self.text = btn.text
        self.suggestions = []
        global work_name
        work_name = self.text

class AutoTask(MDApp, object):
    def __init__(self, Password, **kwargs):
        super().__init__(**kwargs)

        try:
            with open(f"{path}/{getEmail()}_ultra_secure.txt", "r") as f:
                secure_choice = f.read()
                f.close()

            if secure_choice == "on":
                self.Password_for_enc = Password
            else:
                self.Password_for_enc = getEmail()
        except:
            self.Password_for_enc = getEmail()



    with open(rf"{path}/checkbox.txt", 'w') as f:
        f.write("on")
        f.close()
    taskToScheduled = ""
    logoPng = StringProperty(rf"{ImagePath}\logo.png")
    ScheduledLabel = StringProperty("Type your task name")
    disabledCheckbox = BooleanProperty(False)
    checkBoxImage2 = StringProperty(rf"{ImagePath}\checked.png")
    opacityCheckbox = StringProperty("1")
    plusImage = StringProperty(rf"{ImagePath}\plus.png")
    checkBoxImage = StringProperty(rf"{ImagePath}\unchecked.png")
    runImage = StringProperty(rf"{ImagePath}\run.png")
    micImage = StringProperty(rf"{ImagePath}\microphone.png")
    KeyboardImage = StringProperty(rf"{ImagePath}\keyboard_blue.png")
    ClockImage = StringProperty(rf"{ImagePath}\clock.png")
    GreenKeyboardImage = StringProperty(rf"{ImagePath}\keyboard_green.png")
    text = StringProperty("")
    bt = StringProperty("Start recording")
    b2 = StringProperty("I can't record")
    b3 = StringProperty("Start recording")
    labelSelect = StringProperty("Type your task name")
    micLabel = StringProperty("Quick audio run")
    opacity = StringProperty("1")
    opac = StringProperty("1")
    opac2 = StringProperty("0")
    opac3 = StringProperty("0")
    opac4 = StringProperty("1")
    output = StringProperty("")
    user_input = None
    name = ""
    audio = ""
    kb = ""
    mb = ""
    mm = ""
    mw = ""
    count = 0
    disable = BooleanProperty(True)
    disabLable = BooleanProperty(False)
    boo = True
    all_speech_tries = ""
    keyLabel = StringProperty("Your stop recording key")
    UserTimeChoice = ""
    UserDateChoice = ""
    keysLive = StringProperty("")
    recordshortcut = BooleanProperty(True)
    scLabel = StringProperty("")
    CloseWindowLabel1 = StringProperty("Here you can record yourself closing\na new window, if you need help press on the\ntutorial below")
    opacityDisable = StringProperty("1")
    close_tabs_helper = BooleanProperty(False)
    disabledShortcut = BooleanProperty(True)
    recordKey = StringProperty(Common.key())
    scheduleDisable = BooleanProperty(False)
    isMic = BooleanProperty(True)
    WatchText = StringProperty("No Thanks")

    def build(self):
        self.use_kivy_settings = False
        self.settings_cls = SettingsPanel
        self.settings_cls.title = "The best tool for automating your daily tasks"
        self.icon = rf"{ImagePath}\icon.png"
        self.theme_cls.theme_style = Common.GetColort()
        self.theme_cls.primary_palette = Common.Colorr()
        self.title = "Auto Tasks"
        global password_for_encrypt
        password_for_encrypt = self.Password_for_enc
        self.runShortCuts()
        self.runShortCutsWord()
        self.isMic = self.check_if_user_have_microphone()
        return Builder.load_string(Main)

    def runShortCuts(self):
        try:
            for file in listdir(f"{path}/{getEmail()}/short_cuts"):
                with open(f"{path}/{getEmail()}/short_cuts/{file}", 'r') as f:
                    x = f.read()
                    keyboard.add_hotkey(file, lambda y=x: self.selectTasksKivyManager(f"{y}a"))
        except:
            pass

    def on_start(self):
        try:
            with open(rf"{path}\{getEmail()}\first_log_in.txt", 'r') as f:
                read = f.read()
                if read == "yes":
                    self.watch()
                    with open(rf"{path}\{getEmail()}\first_log_in.txt", 'w') as f1:
                        f1.write("no")

        except:
            with open(rf"{path}\{getEmail()}\first_log_in.txt", 'w') as f1:
                f1.write("no")
                self.watch()

        try:
            mkdir(f'{path}/{getEmail()}/schedule')
        except:
            pass

        with open(f"{path}/open.txt", 'w') as f:
            f.write("True")

        list_tasks = Common.NameOfUserTasks()
        title = OneLineIconListItem(
            text="Here you can edit your task, delete them, and set a time when there gonna play")
        self.root.ids.container.add_widget(title)

        for x in range(len(list_tasks)):
            icon10 = IconLeftWidget(icon="clock")
            icon10.bind(on_press=lambda y, x=list_tasks[x]: self.show_date_picker(x))
            icon20 = IconLeftWidget(icon="delete")
            icon20.bind(on_press=lambda y, x=list_tasks[x]: self.deleteTask(x))
            icon30 = IconLeftWidget(icon="play-circle")
            icon30.bind(on_press=lambda y, x=list_tasks[x]: self.selectTasksKivyManager(x))
            icon40 = IconLeftWidget(icon="keyboard")
            icon40.bind(on_press=lambda y, x=list_tasks[x]: self.shortCuts(x))
            items = OneLineIconListItem(text="                                         " + list_tasks[x] + " task")
            items.add_widget(icon10)
            items.add_widget(icon20)
            items.add_widget(icon30)
            items.add_widget(icon40)
            self.root.ids.container.add_widget(items)


        list_sc_task = []
        for sc in listdir(f"{path}/{getEmail()}/short_cuts"):
            list_sc_task.append(sc)
        list_sc_word = []
        for sc in listdir(f"{path}/{getEmail()}/short_cuts_words"):
            list_sc_word.append(sc)

        title = OneLineIconListItem(
            text="Here you can edit your short cuts and delete them")
        self.root.ids.container2.add_widget(title)

        list_schedule = []
        for schedule in listdir(f"{path}/{getEmail()}/schedule"):
            if schedule != "['2020', '1', '1'] & ['00', '00', '00'] & system_file":
                list_schedule.append(schedule)
        title1 = OneLineIconListItem(
            text="Here you see your schedule tasks and delete them")
        self.root.ids.container3.add_widget(title1)

        for x in range(len(list_sc_task)):
            icon = IconLeftWidget(icon="delete")
            icon.bind(on_press=lambda y, x=list_sc_task[x]: self.deleteSc(x))
            icon2 = IconLeftWidget(icon="eye")
            icon2.bind(on_press=lambda y, x=list_sc_task[x]: self.View(x))
            items = OneLineIconListItem(text="              " + list_sc_task[x] + " shortcut for task")
            items.add_widget(icon)
            items.add_widget(icon2)
            self.root.ids.container2.add_widget(items)

        for x in range(len(list_sc_word)):
            icon = IconLeftWidget(icon="delete")
            icon.bind(on_press=lambda y, x=list_sc_word[x]: self.deleteSc(x))
            icon2 = IconLeftWidget(icon="eye")
            icon2.bind(on_press=lambda y, x=list_sc_word[x]: self.View(x))
            items = OneLineIconListItem(text="              " + list_sc_word[x] + " shortcut for word")
            items.add_widget(icon)
            items.add_widget(icon2)
            self.root.ids.container2.add_widget(items)

        list_year_schedule = []
        list_month_schedule = []
        list_day_schedule = []
        list_hour_schedule = []
        list_min_schedule = []
        list_name_schedule = []

        for filename in listdir(f"{path}/{getEmail()}/schedule"):

            if filename != "['2020', '1', '1'] & ['00', '00', '00'] & system_file":
                list_schedule_name = filename.split("'")

                name_schedule_task = list_schedule_name[12][2:]

                day_to_run = list_schedule_name[5]
                year_to_run = list_schedule_name[1]
                month_to_run = list_schedule_name[3]
                hour_to_run = list_schedule_name[7]
                min_to_run = list_schedule_name[9]

                list_year_schedule.append(year_to_run)
                list_month_schedule.append(month_to_run)
                list_day_schedule.append(day_to_run)
                list_hour_schedule.append(hour_to_run)

                list_min_schedule.append(min_to_run)
                list_name_schedule.append(name_schedule_task)

        for x in range(len(list_schedule)):
            icon = IconLeftWidget(icon="delete")
            icon.bind(on_press=lambda y, x=list_schedule[x]: self.delete_schedule(x))
            items1 = OneLineIconListItem(
                text="      " + list_day_schedule[x] + "/" + list_month_schedule[x] + "/" + list_year_schedule[
                    x] + "  |  " + list_hour_schedule[x] + ":" + list_min_schedule[x] + "        " +
                     list_name_schedule[x] + "    schedule task")
            items1.add_widget(icon)
            self.root.ids.container3.add_widget(items1)

        if not listdir(f"{path}/{getEmail()}/schedule"):
            pass
        else:
            schedule_thread = Thread(target=lambda: self.ScheduledTaskHelper_for_start(), daemon=True)
            schedule_thread.start()

    def deleteSc(self, name):
        try:
            remove(f"{path}/{getEmail()}/short_cuts_words/{name}")
            self.Delete()
        except:
            pass
        try:
            remove(f"{path}/{getEmail()}/short_cuts/{name}")
            self.Delete()
        except:
            pass

        try:
            keyboard.remove_all_hotkeys()
            self.runShortCuts()
            self.runShortCutsWord()

        except:
            pass

    def open_url(self):
        openweb('https://youtu.be/drcsnJp5GZY')

    def Delete(self):
        show = delete()
        but = (Button(text="close", size_hint=(None, None),
                      width=100, height=50, pos_hint={"center_x": 0.5, "center_y": 0.19}, opacity=0))
        show.add_widget(but)
        popupWindow2 = Popup(title="", content=show, size_hint=(None, None), size=(360, 220),
                             background_color=Common.LightDark(),
                             auto_dismiss=False)
        but.bind(on_press=popupWindow2.dismiss)
        popupWindow2.open()

    def View(self, name):
        count = 0
        try:
            open(f"{path}/{getEmail()}/short_cuts_words/{name}", "r")
            count = count + 1
        except:
            pass
        try:
            open(f"{path}/{getEmail()}/short_cuts/{name}", "r")
            count = count + 1
        except:
            pass

        if count == 0:
            self.Delete()
        else:
            try:
                try:
                    decfile(f"{path}/{getEmail()}/short_cuts_words/{name}", password_for_encrypt)

                    with open(f"{path}/{getEmail()}/short_cuts_words/{name}", 'r') as f:
                        self.scLabel = f.read()
                        f.close()
                    encfile(f"{path}/{getEmail()}/short_cuts_words/{name}", password_for_encrypt)

                    show = view()
                    but = (Button(text="close", size_hint=(None, None),
                                  width=100, height=50, pos_hint={"center_x": 0.5, "center_y": 0.19}, opacity=0))
                    show.add_widget(but)
                    popupWindow2 = Popup(title=name + " (shortcut for word)", content=show, size_hint=(None, None),
                                         size=(360, 220), background_color=Common.LightDark(),
                                         auto_dismiss=False)
                    but.bind(on_press=popupWindow2.dismiss)
                    popupWindow2.open()
                except:
                    with open(f"{path}/{getEmail()}/short_cuts/{name}", 'r') as f:
                        self.scLabel = f.read()
                        f.close()

                    show = view()
                    but = (Button(text="close", size_hint=(None, None),
                                  width=100, height=50, pos_hint={"center_x": 0.5, "center_y": 0.19}, opacity=0))
                    show.add_widget(but)
                    popupWindow2 = Popup(title=name + " (shortcut for task)", content=show, size_hint=(None, None),
                                         size=(340, 220), background_color=Common.LightDark(),
                                         auto_dismiss=False)
                    but.bind(on_press=popupWindow2.dismiss)
                    popupWindow2.open()
            except:
                show = view()
                self.scLabel = "Your task was deleted"
                but = (Button(text="close", size_hint=(None, None),
                              width=100, height=50, pos_hint={"center_x": 0.5, "center_y": 0.19}, opacity=0))
                show.add_widget(but)
                popupWindow2 = Popup(title=name, content=show, size_hint=(None, None), size=(340, 220),
                                     background_color=Common.LightDark(),
                                     auto_dismiss=False)
                but.bind(on_press=popupWindow2.dismiss)
                popupWindow2.open()

    def darkMode(self):
        color = Common.readFile(rf"{path}/file.txt")
        if color == "Dark":
            a = "Light"
            Common.writeInFile(rf"{path}/file.txt", a)
        else:
            a = "Dark"
            Common.writeInFile(rf"{path}/file.txt", a)
        self.theme_cls.theme_style = a
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_palette = Common.Colorr()

    def Show(self):
        statusMic = self.check_if_user_have_microphone()
        if statusMic:
            self.NoMic()
        else:
            self.Mic()

    def Mic(self):
        show = NewTask()
        but = (Button(text="close", size_hint=(None, None),
                      width=100, height=50, pos_hint={"center_x": 0.55, "center_y": 0.2}, opacity=0))
        show.add_widget(but)
        popupWindow = Popup(title="New task", content=show, size_hint=(None, None), size=(530, 380),
                            background_color=Common.LightDark(),
                            auto_dismiss=False)
        but.bind(on_press=popupWindow.dismiss)
        self.bt = "Start recording"
        self.b2 = "I can't record"
        self.b3 = "Start recording"
        self.opac = "1"
        self.opac2 = "0"
        self.opac3 = "0"
        self.opac4 = "1"
        self.output = ""
        self.close_tabs_helper = False
        self.disable = True
        self.disabLable = False
        self.disabledCheckbox = False
        self.opacityCheckbox = "1"
        popupWindow.open()

    def NoMic(self):
        show = NewTaskNoMic()
        but = (Button(text="close", size_hint=(None, None),
                      width=100, height=50, pos_hint={"center_x": 0.55, "center_y": 0.2}, opacity=0))
        show.add_widget(but)
        popupWindow = Popup(title="New task", content=show, size_hint=(None, None), size=(530, 380),
                            background_color=Common.LightDark(),
                            auto_dismiss=False)
        but.bind(on_press=popupWindow.dismiss)
        self.bt = "Start recording"
        self.b3 = "Start recording"
        self.opacity = "1"
        self.opac = "1"
        self.opac2 = "0"
        self.opac3 = "0"
        self.opac4 = "1"
        self.output = f"""We will record your motions\n once you press the button below,\n you can end the record by\n pressing your '{Common.readFile(f"{path}/key.txt")}' key."""
        self.close_tabs_helper = False
        self.disable = False
        self.disabLable = False
        self.disabledCheckbox = False
        self.opacityCheckbox = "1"
        popupWindow.open()

    def Show2(self):
        show = RunTask()
        but = (Button(text="close", size_hint=(None, None),
                      width=100, height=50, pos_hint={"center_x": 0.55, "center_y": 0.15}, opacity=0))
        show.add_widget(but)
        popupWindow2 = Popup(title="Run Task", content=show, size_hint=(None, None), size=(540, 420),
                             background_color=Common.LightDark(),
                             auto_dismiss=False)
        but.bind(on_press=popupWindow2.dismiss)
        self.close_tabs_helper = False
        self.disabledCheckbox = False
        self.opacityCheckbox = "1"
        popupWindow2.open()

    def change(self):
        self.text = "Please say your task name"
        self.opac2 = "0"

    def Logout(self):
        Common.writeInFile(rf"{path}/remember.txt", "no")
        AutoTask("").stop()

    def right_or_left(self):
        pass

    def startRecord_thred(self, name):
        self.opac = "1"
        self.opac2 = "0"
        try:
            r = Recognizer()
            with Microphone() as source:
                audio = r.listen(source, 4, 4)
                try:
                    self.user_input = r.recognize_google(audio)
                    self.bt = "Record again"
                    self.b2 = "Submit"
                    if self.user_input.lower() == name:
                        self.text = str(self.user_input).lower()
                    else:
                        self.text = str(f"{self.user_input}, record again").lower()
                except:
                    self.text = "We could not\n recognize your voice"
                    self.bt = "Record again"

            self.save_speech_error(self.user_input.lower())
            self.bt = "Record again"
            self.b2 = "Submit"
        except:
            self.text = "Something went wrong"

    def startRecord(self, name):
        s_thread = Thread(target=lambda: self.startRecord_thred(name), daemon=True)
        s_thread.start()

    def delete_schedule(self, name_s):
        try:
            remove(f"{path}/{getEmail()}/schedule/{name_s}")
            self.Delete()
        except:
            pass

    def name_of_tasks(self):
        with open(f"{path}/{getEmail()}/names_of_user_tasks.txt", "a") as f_name_tasks:
            f_name_tasks.write(self.name + '\n')
            f_name_tasks.close()

    def save_speech_error(self, word):
        self.all_speech_tries += f"{word.lower()}& "

    def okay(self, name, audio):
        try:
            open(f"{path}/{getEmail()}/file_saver/{name}_max_choice.txt", "w")
            name_is_valid = True
        except:
            name_is_valid = False
        self.name = name
        self.audio = audio
        self.text = ''
        iss = False
        for x in self.name:
            if x != " " and '"' not in x and "<" not in x and ">" not in x and "/" not in x and r"\"" not in x and "?" not in x and "*" not in x and "|" not in x and ":" not in x:
                iss = True

        if iss and name_is_valid:
            self.name_of_tasks()
            self.opac = "0"
            self.opac2 = "1"
            self.output = f"""We will record your motions\n once you press the button below,\n you can end the record by\n pressing your '{Common.readFile(f"{path}/key.txt")}' key."""
            self.opac3 = "1"
            self.opac4 = "0"
            self.disable = False
            # שומר את כל הניסיונות של המשתמש לחזור על שם המשימה בקובץ טקסט

            if not name in self.all_speech_tries:
                self.all_speech_tries += f"{name.lower()}& "
            with open(f"{path}/{getEmail()}/file_saver/{name}all_speech_tries.txt", 'w') as f:
                f.write(self.all_speech_tries)


        else:
            self.opac = "1"
            self.opac2 = "0"
            self.text = "Your task name is invalid"

    def changeLabel(self):
        if not self.boo:
            self.opac3 = "0"
            self.disable = True
        self.opac4 = "0"
        self.output = "We are recording right now."
        self.disable = (False)
        self.disabLable = (True)

    def changeLabel2(self, task_name):
        try:
            open(f"{path}/{getEmail()}/file_saver/{task_name}_max_choice.txt", "w")
            name_is_valid = True
        except:
            name_is_valid = False
        iss = False
        for x in task_name:
            if x != " " and '"' not in x and "<" not in x and ">" not in x and "/" not in x and r"\"" not in x and "?" not in x and "*" not in x and "|" not in x and ":" not in x:
                iss = True
        if iss and name_is_valid:
            self.opac3 = "0"
            self.disable = True
            self.opacity = "0"
            self.opac4 = "0"
            self.output = "We are recording right now."
            self.disable = (False)
            self.disabLable = (True)
            with open(f"{path}/{getEmail()}/file_saver/{task_name}all_speech_tries.txt", 'w') as f:
                f.write(f"{task_name.lower()}& ")
            with open(f"{path}/{getEmail()}/names_of_user_tasks.txt", "a") as f_name_tasks:
                f_name_tasks.write(task_name.lower() + '\n')
                f_name_tasks.close()

    def ChangeLabel123(self):
        self.CloseWindowLabel1 = "We are recording now"

    def record_event_of_closing_new_desktop_for_threading(self):

        keyboard.press_and_release("left windows + tab")

        mouse_events, keyboard_events = close_desktop_record()
        mouse_button = []
        mouse_wheel = []
        mouse_move = []

        # ממין את הEVENT לפי הסוג שלהם
        for event in mouse_events:
            if type(event) == MoveEvent:
                mouse_move.append(event)
            elif type(event) == WheelEvent:
                mouse_wheel.append(event)
            else:
                mouse_button.append(event)

        # reformat the lists into strings, in order to insert to database
        all_lists = helper_events.reformat_all(keyboard_events[:-1], mouse_button, mouse_wheel, mouse_move)
        # keyboard
        kb = '#'.join(all_lists[0])
        # mouse
        mb = '#'.join(all_lists[1])  # button
        mm = '#'.join(all_lists[2])  # move
        mw = '#'.join(all_lists[3])  # wheel

        # שומר את כל הפעולות בקבצים שונים לפי סוג הפעולה
        with open(f"{path}/{getEmail()}/file_saver/close_new_desktop_after_recording_system_file_kb.txt", 'w') as f:
            f.write(kb)

        with open(f"{path}/{getEmail()}/file_saver/close_new_desktop_after_recording_system_file_mb.txt", 'w') as f:
            f.write(mb)

        with open(f"{path}/{getEmail()}/file_saver/close_new_desktop_after_recording_system_file_mm.txt", 'w') as f:
            f.write(mm)

        with open(f"{path}/{getEmail()}/file_saver/close_new_desktop_after_recording_system_file_mw.txt", 'w') as f:
            f.write(mw)

        self.CloseWindowLabel1 = "Your record succecfully saved"

    def record_event_of_closing_new_desktop(self):

        record_closing_desktop_thread = Thread(
            target=lambda: self.record_event_of_closing_new_desktop_for_threading(), daemon=True)
        record_closing_desktop_thread.start()

    def run_close_new_deskstop(self):
        try:
            with open(f"{path}/{getEmail()}/file_saver/close_new_desktop_after_recording_system_file_kb.txt",
                      'r') as f1:
                data_kb = f1.read().replace('\n', '')
            kb = data_kb

            with open(f"{path}/{getEmail()}/file_saver/close_new_desktop_after_recording_system_file_mb.txt",
                      'r') as f2:
                data_mb = f2.read().replace('\n', '')
            mb = data_mb

            with open(f"{path}/{getEmail()}/file_saver/close_new_desktop_after_recording_system_file_mw.txt",
                      'r') as f3:
                data_mw = f3.read().replace('\n', '')
            mw = data_mw

            with open(f"{path}/{getEmail()}/file_saver/close_new_desktop_after_recording_system_file_mm.txt",
                      'r') as f4:
                data_mm = f4.read().replace('\n', '')
            mm = data_mm

            all_events = back_to_events(kb.split('#'), mb.split('#'), mm.split('#'), mw.split('#'))
            kb_events, mb_events, mm_events, mw_events = all_events

            all_mouse_events = mb_events + mm_events + mw_events
            all_mouse_events = sorted(all_mouse_events, key=lambda event: event.time)

            keyboard.start_recording()
            keyboard.stop_recording()

            keyboard.press_and_release("left windows + tab")

            runMouseMouseKeyboardEvents(all_mouse_events, kb_events, 1, 1)

            ctrlWinArrow()
        except:
            pass


    def start_and_save_for_threading(self, task_name):
        iss = False
        for x in task_name:
            if x != " " and '"' not in x and "<" not in x and ">" not in x and "/" not in x and r"\"" not in x and "?" not in x and "*" not in x and "|" not in x and ":" not in x:
                iss = True
        try:
            open(f"{path}/{getEmail()}/file_saver/{task_name}_max_choice.txt", "w")
            name_is_valid = True
        except:
            name_is_valid = False

        if iss and name_is_valid:
            if self.disabledCheckbox == False:
                mouse_events, keyboard_events = open_new_desktop_and_come_back_to_original_and_record()
            else:
                mouse_events, keyboard_events = just_record()

            with open(f"{path}/{getEmail()}/maximized_choice.txt", "r") as f:
                max_choice = f.read()
                f.close()

            if max_choice == "Yes":
                with open(f"{path}/{getEmail()}/file_saver/{task_name}_max_choice.txt", "w") as f:
                    f.write("Yes")
                    f.close()
            else:
                with open(f"{path}/{getEmail()}/file_saver/{task_name}_max_choice.txt", "w") as f:
                    f.write("No")
                    f.close()

            mouse_button = []
            mouse_wheel = []
            mouse_move = []

            # ממין את הEVENT לפי הסוג שלהם
            for event in mouse_events:
                if type(event) == MoveEvent:
                    mouse_move.append(event)
                elif type(event) == WheelEvent:
                    mouse_wheel.append(event)
                else:
                    mouse_button.append(event)

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
            encfile(f"{path}/{getEmail()}/file_saver/{task_name}_kb.txt", password_for_encrypt)

            with open(f"{path}/{getEmail()}/file_saver/{task_name}_mb.txt", 'w') as f:
                f.write(mb)
            encfile(f"{path}/{getEmail()}/file_saver/{task_name}_mb.txt", password_for_encrypt)

            with open(f"{path}/{getEmail()}/file_saver/{task_name}_mm.txt", 'w') as f:
                f.write(mm)
            encfile(f"{path}/{getEmail()}/file_saver/{task_name}_mm.txt", password_for_encrypt)

            with open(f"{path}/{getEmail()}/file_saver/{task_name}_mw.txt", 'w') as f:
                f.write(mw)
            encfile(f"{path}/{getEmail()}/file_saver/{task_name}_mw.txt", password_for_encrypt)

            self.output = "Your record successfully saved."
            self.opac3 = "0"
            self.disable = (True)
            self.boo = False

            if self.close_tabs_helper:
                self.run_close_new_deskstop()

            icon10 = IconLeftWidget(icon="clock")
            icon10.bind(on_press=lambda y, x=task_name: self.show_date_picker(f"{x}a"))
            icon20 = IconLeftWidget(icon="delete")
            icon20.bind(on_press=lambda y, x=task_name: self.deleteTask_before_restart(x))
            icon30 = IconLeftWidget(icon="play-circle")
            icon30.bind(on_press=lambda y, x=task_name + "a": self.selectTasksKivyManager(x))
            icon40 = IconLeftWidget(icon="keyboard")
            icon40.bind(on_press=lambda y, x=task_name + "a": self.shortCuts(x))
            items = OneLineIconListItem(text="                                         " + task_name + " task")
            items.add_widget(icon10)
            items.add_widget(icon20)
            items.add_widget(icon30)
            items.add_widget(icon40)
            self.root.ids.container.add_widget(items)

        else:
            self.output = "Your task name is invalid"

    def start_and_save(self, task_name):
        start_save_thread = Thread(target=lambda: self.start_and_save_for_threading(task_name))
        start_save_thread.start()

    def saveKey_for_thread(self):
        self.recordKey = keyboard.read_hotkey(suppress=False)
        Common.writeInFile(rf"{path}/key.txt", self.recordKey)

    def saveKey(self):
        recordkeyboard_thread = Thread(target=lambda: self.saveKey_for_thread(), daemon=True)
        if self.count == 0:
            recordkeyboard_thread.start()
            self.count = 1
        else:
            recordkeyboard_thread.start()

    def check_final_file_for_kivy(self, input):
        input = input[:-1]
        task_name_list = Common.NameOfUserTasks()

        # מפעיל את user_select_task ושומר את שם המשימה
        # עובר על הרשימה ומוצא את השם המתאים

        for name in task_name_list:
            if name != "":
                if search_string_in_file(name, input):
                    user_input_error = name
                    return user_input_error

    def maximize_window_thread_run(self):
        while True:
            if keep_maximized_run == True:
                sleep(3)
                keyboard.press("left windows")
                keyboard.press_and_release("up")
                keyboard.release("left windows")
            else:
                break

    def maximize_window_thread_run1(self, time_factor):
        while True:
            if keep_maximized_run1 == True:
                sleep(3/time_factor)
                keyboard.press("left windows")
                keyboard.press_and_release("up")
                keyboard.release("left windows")
            else:
                break

    def maximize_window_run1(self, speed_factor):
        max_run_thread1 = Thread(target=lambda: self.maximize_window_thread_run1(speed_factor), daemon=True)
        max_run_thread1.start()

    def maximize_window_run(self):
        max_run_thread = Thread(target=lambda: self.maximize_window_thread_run(), daemon=True)
        max_run_thread.start()

    def maximize_window_thread_run2(self):
        while True:
            if keep_maximized_run2 == True:
                sleep(3)
                keyboard.press("left windows")
                keyboard.press_and_release("up")
                keyboard.release("left windows")
            else:
                break

    def maximize_window_run2(self):
        max_run_thread2 = Thread(target=lambda: self.maximize_window_thread_run2(), daemon=True)
        max_run_thread2.start()

    def maximize_window_thread_run3(self):
        while True:
            if keep_maximized_run3 == True:
                sleep(3)
                keyboard.press("left windows")
                keyboard.press_and_release("up")
                keyboard.release("left windows")
            else:
                break

    def maximize_window_run3(self):
        max_run_thread3 = Thread(target=lambda: self.maximize_window_thread_run3(), daemon=True)
        max_run_thread3.start()

    def selectTasksKivyManager_for_threading(self, name):  # select the task
        global keep_maximized_run

        try:
            name = name[:-1]

            decfile(rf"{path}/{getEmail()}/file_saver/{name}_kb.txt", password_for_encrypt)
            decfile(rf"{path}/{getEmail()}/file_saver/{name}_mb.txt", password_for_encrypt)
            decfile(rf"{path}/{getEmail()}/file_saver/{name}_mw.txt", password_for_encrypt)
            decfile(rf"{path}/{getEmail()}/file_saver/{name}_mm.txt", password_for_encrypt)

            with open(f"{path}/{getEmail()}/file_saver/{name}_kb.txt", 'r') as f1:
                data_kb = f1.read()
            kb = data_kb

            with open(f"{path}/{getEmail()}/file_saver/{name}_mb.txt", 'r') as f2:
                data_mb = f2.read()
            mb = data_mb

            with open(f"{path}/{getEmail()}/file_saver/{name}_mw.txt", 'r') as f3:
                data_mw = f3.read()
            mw = data_mw

            with open(f"{path}/{getEmail()}/file_saver/{name}_mm.txt", 'r') as f4:
                data_mm = f4.read()
            mm = data_mm

            encfile(rf"{path}/{getEmail()}/file_saver/{name}_kb.txt", password_for_encrypt)
            encfile(rf"{path}/{getEmail()}/file_saver/{name}_mb.txt", password_for_encrypt)
            encfile(rf"{path}/{getEmail()}/file_saver/{name}_mw.txt", password_for_encrypt)
            encfile(rf"{path}/{getEmail()}/file_saver/{name}_mm.txt", password_for_encrypt)

            all_events = back_to_events(kb.split('#'), mb.split('#'), mm.split('#'), mw.split('#'))
            kb_events, mb_events, mm_events, mw_events = all_events

            all_mouse_events = mb_events + mm_events + mw_events
            all_mouse_events = sorted(all_mouse_events, key=lambda event: event.time)

            keyboard.start_recording()
            keyboard.stop_recording()

            if ReadOpenWindow() == "True":
                with open(f"{path}/{getEmail()}/file_saver/{name}_max_choice.txt", "r") as f:
                    max_choice = f.read()
                if max_choice == "Yes":
                    keep_maximized_run = True
                    self.maximize_window_run()
                    ctrlWinD()
                    runMouseMouseKeyboardEvents(all_mouse_events, kb_events, 1, 1)
                    ctrlWinArrow()
                    keep_maximized_run = False
                else:
                    ctrlWinD()
                    runMouseMouseKeyboardEvents(all_mouse_events, kb_events, 1, 1)
                    ctrlWinArrow()


            else:
                with open(f"{path}/{getEmail()}/file_saver/{name}_max_choice.txt", "r") as f:
                    max_choice = f.read()
                if max_choice == "Yes":
                    keep_maximized_run = True
                    self.maximize_window_run()
                    runMouseMouseKeyboardEvents(all_mouse_events, kb_events, 1, 1)
                    keep_maximized_run = False
                else:
                    runMouseMouseKeyboardEvents(all_mouse_events, kb_events, 1, 1)

            if ReadCloseWindow() == "True":
                self.run_close_new_deskstop()

        except:
            pass

    def selectTasksKivyManager(self, name):
        try:
            open(f"{path}/{getEmail()}/file_saver/{name[:-1]}_mm.txt", "r")
            selectTasksKivyManager_thread = Thread(
                target=lambda: self.selectTasksKivyManager_for_threading(name))
            selectTasksKivyManager_thread.start()
        except:
            self.Delete()

    def deleteTask(self, name):

        with open(f"{path}/{getEmail()}/names_of_user_tasks.txt", "r") as f:
            read_data = f.readlines()
            with open(f"{path}/{getEmail()}/names_of_user_tasks.txt", "w") as f1:
                for task in read_data:
                    if not task == name:
                        f1.writelines(task)
        name = name[:-1]
        try:
            remove(f"{path}/{getEmail()}/file_saver/{name}_kb.txt")
        except:
            pass
        try:
            remove(f"{path}/{getEmail()}/file_saver/{name}_mb.txt")
        except:
            pass
        try:
            remove(f"{path}/{getEmail()}/file_saver/{name}_mw.txt")
        except:
            pass
        try:
            remove(f"{path}/{getEmail()}/file_saver/{name}_mm.txt")
        except:
            pass
        try:
            remove(f"{path}/{getEmail()}/file_saver/{name}all_speech_tries.txt")
        except:
            pass
        try:
            remove(f"{path}/{getEmail()}/file_saver/{name}_max_choice.txt")
        except:
            pass
        try:
            for file in listdir(rf"{path}/{getEmail()}/short_cuts"):
                with open(rf"{path}/{getEmail()}/short_cuts/{file}", 'r') as f:
                    data = f.read()
                    f.close()
                    if data == name:
                        remove(rf"{path}/{getEmail()}/short_cuts/{file}")
        except:
            pass

        self.Delete()

    def deleteTask_before_restart(self, name):
        with open(rf"{path}/{getEmail()}/names_of_user_tasks.txt", "r") as f:
            read_data = f.readlines()
            with open(rf"{path}/{getEmail()}/names_of_user_tasks.txt", "w") as f1:
                for task in read_data:
                    if not task[:-1] == name:
                        f1.writelines(task)
        try:
            remove(f"{path}/{getEmail()}/file_saver/{name}_kb.txt")
        except:
            pass
        try:
            remove(f"{path}/{getEmail()}/file_saver/{name}_mb.txt")
        except:
            pass
        try:
            remove(f"{path}/{getEmail()}/file_saver/{name}_mw.txt")
        except:
            pass
        try:
            remove(f"{path}/{getEmail()}/file_saver/{name}_mm.txt")
        except:
            pass
        try:
            remove(f"{path}/{getEmail()}/file_saver/{name}all_speech_tries.txt")
        except:
            pass
        try:
            remove(f"{path}/{getEmail()}/file_saver/{name}all_speech_tries.txt")
        except:
            pass
        try:
            remove(f"{path}/{getEmail()}/file_saver/{name}_max_choice.txt")
        except:
            pass
        try:
            for file in listdir(rf"{path}/{getEmail()}/short_cuts"):
                with open(rf"{path}/{getEmail()}/short_cuts/{file}", 'r') as f:
                    data = f.read()
                    f.close()
                    if data == name:
                        remove(rf"{path}/{getEmail()}/short_cuts/{file}")
        except:
            pass

        self.Delete()

    def selectTasksKivy_for_threading(self, name_for_select_kivy_task, speed_factor):  # select the task
        global keep_maximized_run1
        try:
            speed_factor = float(speed_factor)
            name_for_select_kivy_task = int(name_for_select_kivy_task)
            name = new_work_name

            decfile(rf"{path}/{getEmail()}/file_saver/{name}_kb.txt", password_for_encrypt)
            decfile(rf"{path}/{getEmail()}/file_saver/{name}_mb.txt", password_for_encrypt)
            decfile(rf"{path}/{getEmail()}/file_saver/{name}_mw.txt", password_for_encrypt)
            decfile(rf"{path}/{getEmail()}/file_saver/{name}_mm.txt", password_for_encrypt)

            with open(rf"{path}/{getEmail()}/file_saver/{name}_kb.txt", 'r') as f1:
                data_kb = f1.read().replace('\n', '')
            kb = data_kb

            with open(rf"{path}/{getEmail()}/file_saver/{name}_mb.txt", 'r') as f2:
                data_mb = f2.read().replace('\n', '')
            mb = data_mb

            with open(rf"{path}/{getEmail()}/file_saver/{name}_mw.txt", 'r') as f3:
                data_mw = f3.read().replace('\n', '')
            mw = data_mw

            with open(rf"{path}/{getEmail()}/file_saver/{name}_mm.txt", 'r') as f4:
                data_mm = f4.read().replace('\n', '')
            mm = data_mm

            encfile(rf"{path}/{getEmail()}/file_saver/{name}_kb.txt", password_for_encrypt)
            encfile(rf"{path}/{getEmail()}/file_saver/{name}_mb.txt", password_for_encrypt)
            encfile(rf"{path}/{getEmail()}/file_saver/{name}_mw.txt", password_for_encrypt)
            encfile(rf"{path}/{getEmail()}/file_saver/{name}_mm.txt", password_for_encrypt)

            all_events = back_to_events(kb.split('#'), mb.split('#'), mm.split('#'), mw.split('#'))
            kb_events, mb_events, mm_events, mw_events = all_events

            all_mouse_events = mb_events + mm_events + mw_events
            all_mouse_events = sorted(all_mouse_events, key=lambda event: event.time)

            keyboard.start_recording()
            keyboard.stop_recording()

            if self.disabledCheckbox == False:
                with open(f"{path}/{getEmail()}/file_saver/{name}_max_choice.txt", "r") as f:
                    max_choice = f.read()
                if max_choice == "Yes":
                    keep_maximized_run1 = True
                    self.maximize_window_run1(speed_factor)
                    ctrlWinD()

                    if speed_factor <= 0.1:
                        speed_factor = 0.1
                    if speed_factor >= 10:
                        speed_factor = 10

                    runMouseMouseKeyboardEvents(all_mouse_events, kb_events, name_for_select_kivy_task, speed_factor)
                    ctrlWinArrow()
                    keep_maximized_run1 = False
                else:
                    ctrlWinD()
                    runMouseMouseKeyboardEvents(all_mouse_events, kb_events, name_for_select_kivy_task, speed_factor)
                    ctrlWinArrow()

            else:
                with open(f"{path}/{getEmail()}/file_saver/{name}_max_choice.txt", "r") as f:
                    max_choice = f.read()
                if max_choice == "Yes":
                    keep_maximized_run1 = True
                    self.maximize_window_run1(speed_factor)
                    runMouseMouseKeyboardEvents(all_mouse_events, kb_events, name_for_select_kivy_task, speed_factor)
                    keep_maximized_run1 = False
                else:
                    runMouseMouseKeyboardEvents(all_mouse_events, kb_events, name_for_select_kivy_task, speed_factor)

            if self.close_tabs_helper:
                self.run_close_new_deskstop()

        except:
            self.labelSelect = "Something went wrong,\ntry to enter a valid name"

    def selectTasksKivy(self, name_for_select_kivy_task, speed_factor):
        selectTasksKivy_thread = Thread(
            target=lambda: self.selectTasksKivy_for_threading(name_for_select_kivy_task, speed_factor))
        selectTasksKivy_thread.start()

    def selectTasksKivyAudio_for_threading(self, name):  # select the task
        global keep_maximized_run2

        try:
            name = name[:-1]
            decfile(rf"{path}/{getEmail()}/file_saver/{name}_kb.txt", password_for_encrypt)
            decfile(rf"{path}/{getEmail()}/file_saver/{name}_mb.txt", password_for_encrypt)
            decfile(rf"{path}/{getEmail()}/file_saver/{name}_mw.txt", password_for_encrypt)
            decfile(rf"{path}/{getEmail()}/file_saver/{name}_mm.txt", password_for_encrypt)

            with open(rf"{path}/{getEmail()}/file_saver/{name}_kb.txt", 'r') as f1:
                data_kb = f1.read()
            kb = data_kb

            with open(rf"{path}/{getEmail()}/file_saver/{name}_mb.txt", 'r') as f2:
                data_mb = f2.read()
            mb = data_mb

            with open(rf"{path}/{getEmail()}/file_saver/{name}_mw.txt", 'r') as f3:
                data_mw = f3.read()
            mw = data_mw

            with open(rf"{path}/{getEmail()}/file_saver/{name}_mm.txt", 'r') as f4:
                data_mm = f4.read()
            mm = data_mm

            encfile(rf"{path}/{getEmail()}/file_saver/{name}_kb.txt", password_for_encrypt)
            encfile(rf"{path}/{getEmail()}/file_saver/{name}_mb.txt", password_for_encrypt)
            encfile(rf"{path}/{getEmail()}/file_saver/{name}_mw.txt", password_for_encrypt)
            encfile(rf"{path}/{getEmail()}/file_saver/{name}_mm.txt", password_for_encrypt)

            all_events = back_to_events(kb.split('#'), mb.split('#'), mm.split('#'), mw.split('#'))
            kb_events, mb_events, mm_events, mw_events = all_events

            all_mouse_events = mb_events + mm_events + mw_events
            all_mouse_events = sorted(all_mouse_events, key=lambda event: event.time)

            keyboard.start_recording()
            keyboard.stop_recording()

            if ReadOpenWindow() == "True":
                with open(f"{path}/{getEmail()}/file_saver/{name}_max_choice.txt", "r") as f:
                    max_choice = f.read()
                if max_choice == "Yes":
                    keep_maximized_run2 = True
                    self.maximize_window_run2()
                    ctrlWinD()
                    runMouseMouseKeyboardEvents(all_mouse_events, kb_events, 1, 1)
                    keep_maximized_run2 = False
                    ctrlWinArrow()
                else:
                    ctrlWinD()
                    runMouseMouseKeyboardEvents(all_mouse_events, kb_events, 1, 1)
                    ctrlWinArrow()
            else:
                with open(f"{path}/{getEmail()}/file_saver/{name}_max_choice.txt", "r") as f:
                    max_choice = f.read()
                if max_choice == "Yes":
                    keep_maximized_run2 = True
                    self.maximize_window_run()
                    runMouseMouseKeyboardEvents(all_mouse_events, kb_events, 1, 1)
                    keep_maximized_run2 = False
                else:
                    runMouseMouseKeyboardEvents(all_mouse_events, kb_events, 1, 1)

            if ReadCloseWindow() == "True":
                self.run_close_new_deskstop()

        except:
            self.labelSelect = "Something went wrong,\ntry to enter a valid name"

    def selectTasksKivyAudio(self, name_for_select_kivy_task):
        selectTasksKivyAudio_thread = Thread(
            target=lambda: self.selectTasksKivyAudio_for_threading(name_for_select_kivy_task))
        selectTasksKivyAudio_thread.start()

    def color(self, color):
        self.theme_cls.primary_palette = Common.SetColor(color)

    def audioRun_thread(self):
        if self.check_if_user_have_microphone():
            self.micLabel = "We cannot detect\nan input device"
        else:
            try:
                r = Recognizer()
                with Microphone() as source:
                    audio = r.listen(source, 4, 4)
                    try:
                        user_input = r.recognize_google(audio).lower()
                        self.selectTasksKivyAudio(self.check_final_file_for_kivy(user_input))
                        self.micLabel = "Quick audio run"

                    except:
                        self.micLabel = "We could not\n recognize your voice"
            except:
                self.micLabel = "Something went wrong"

    def audioRun(self):
        audio = Thread(target=lambda: self.audioRun_thread(), daemon=True)
        audio.start()

    def change2(self):
        self.micLabel = "We are recording now"

    def check_box(self, value):
        if value:
            self.close_tabs_helper = True
            try:
                with open(rf"{path}/{getEmail()}/file_saver/close_new_desktop_after_recording_system_file_mm.txt",
                          "r") as f:
                    f.read()
            except:
                self.CloseWindowHelper()
        else:
            self.close_tabs_helper = False

    def choice_open_new_desktop(self, value):
        if value:
            self.disabledCheckbox = False
            self.opacityCheckbox = "1"
        else:
            self.disabledCheckbox = True
            self.opacityCheckbox = "0"
            self.close_tabs_helper = False

    def on_cancel(self, instance, time):
        pass

    def shortCuts(self, name):
        try:
            self.disabledShortcut = False
            self.keysLive = ""
            open(rf"{path}/{getEmail()}/file_saver/{name[:-1]}_mm.txt", "r")
            global nameForShortCuts
            nameForShortCuts = name
            show = ShortCuts()
            closeButton = (Button(text="close", size_hint=(None, None),
                                  width=105, height=53, pos_hint={"center_x": 0.35, "center_y": 0.195}, opacity=0))
            show.add_widget(closeButton)
            popupWindow3 = Popup(title="Create a short cut", content=show, size_hint=(None, None), size=(500, 360),
                                 background_color=Common.LightDark(),
                                 auto_dismiss=False)
            closeButton.bind(on_press=popupWindow3.dismiss)
            popupWindow3.open()
        except:
            self.Delete()

    def recordShortCut(self):
        self.keysLive = keyboard.read_hotkey(suppress=False)

    def recordShortCut_thred(self):
        recordkeyboard_thread = Thread(target=lambda: self.recordShortCut(), daemon=True)
        recordkeyboard_thread.start()

    def WriteShortcut(self):
        try:
            name_of_task_for_short_cut = nameForShortCuts[:-1]
            with open(rf"{path}/{getEmail()}/short_cuts/{self.keysLive}", 'w') as f:
                f.write(name_of_task_for_short_cut)
                f.close()
            self.runShortCuts()
            self.disabledShortcut = True
            icon = IconLeftWidget(icon="delete")
            icon.bind(on_press=lambda y, x=self.keysLive: self.deleteSc(x))
            icon2 = IconLeftWidget(icon="eye")
            icon2.bind(on_press=lambda y, x=self.keysLive: self.View(x))
            items = OneLineIconListItem(text="              " + self.keysLive + " shortcut for task")
            items.add_widget(icon)
            items.add_widget(icon2)
            self.root.ids.container2.add_widget(items)
        except:
            pass

    def nameOfShortCuts(self, name):
        with open(rf"{path}/{getEmail()}/names_of_short_cuts.txt", "a") as f_name_tasks:
            f_name_tasks.write(name + '\n')
            f_name_tasks.close()

    def CloseWindowHelper(self):
        show = CloseWindow()
        closeButton = (Button(text="close", size_hint=(None, None),
                              width=100, height=50, pos_hint={"center_x": 0.2, "center_y": 0.23}, opacity=0))
        show.add_widget(closeButton)
        popupWindow3 = Popup(title="Close new window", content=show, size_hint=(None, None), size=(520, 320),
                             background_color=Common.LightDark(),
                             auto_dismiss=False)
        closeButton.bind(on_press=popupWindow3.dismiss)
        popupWindow3.open()

    def ScSelecter(self):
        self.disabledShortcut = False
        self.keysLive = ""
        show = ShortcutsSelecter()
        closeButton = (Button(text="close", size_hint=(None, None),
                              width=100, height=50, pos_hint={"center_x": 0.35, "center_y": 0.15}, opacity=0))
        show.add_widget(closeButton)
        popupWindow4 = Popup(title="Create a short cuts for tasks", content=show, size_hint=(None, None),
                             background_color=Common.LightDark(),
                             size=(500, 440),
                             auto_dismiss=False)
        closeButton.bind(on_press=popupWindow4.dismiss)
        popupWindow4.open()

    def SaveShortcut(self):
        try:
            name_short_cut = new_work_name
            if self.keysLive != " " and '"' not in self.keysLive and "<" not in self.keysLive and ">" not in self.keysLive and "/" not in self.keysLive and r"\"" not in self.keysLive and "?" not in self.keysLive and "*" not in self.keysLive and "|" not in self.keysLive and ":" not in self.keysLive:
                name_is_legit = True
            else:
                name_is_legit = False

            if name_is_legit:
                open(f"{path}/{getEmail()}/file_saver/{name_short_cut}_mm.txt")
                with open(f"{path}/{getEmail()}/short_cuts/{self.keysLive}", 'w') as f:
                    f.write(name_short_cut)
                    f.close()
                self.runShortCuts()
                self.disabledShortcut = True
                icon = IconLeftWidget(icon="delete")
                icon.bind(on_press=lambda y, x=self.keysLive: self.deleteSc(x))
                icon2 = IconLeftWidget(icon="eye")
                icon2.bind(on_press=lambda y, x=self.keysLive: self.View(x))
                items = OneLineIconListItem(text="              " + self.keysLive + " shortcut for task")
                items.add_widget(icon)
                items.add_widget(icon2)
                self.root.ids.container2.add_widget(items)
            else:
                self.keysLive = 'the keys can not contain >*<"?:\/'


        except:
            self.keysLive = "Name is invalid"

    def SctWord(self):
        self.disabledShortcut = False
        self.keysLive = ""
        show = ShortcutWord()
        but = (Button(text="close", size_hint=(None, None),
                      width=100, height=50, pos_hint={"center_x": 0.35, "center_y": 0.15}, opacity=0))
        show.add_widget(but)

        popupWindow = Popup(title="Create auto complete short cut", content=show, size_hint=(None, None),
                            background_color=Common.LightDark(),
                            size=(520, 420),
                            auto_dismiss=False)
        but.bind(on_press=popupWindow.dismiss)
        popupWindow.open()

    def runShortCutsWord(self):
        try:
            for file in listdir(f"{path}/{getEmail()}/short_cuts_words"):
                decfile(f"{path}/{getEmail()}/short_cuts_words/{file}", password_for_encrypt)

                with open(f"{path}/{getEmail()}/short_cuts_words/{file}", 'r') as f:
                    x = f.read()
                keyboard.add_hotkey(file, lambda y=x: keyboard.write(y))
                encfile(f"{path}/{getEmail()}/short_cuts_words/{file}", password_for_encrypt)

        except:
            pass

    def word_short_cuts(self, word):
        try:
            with open(f"{path}/{getEmail()}/short_cuts_words/{self.keysLive}", 'w') as f:
                f.write(word)
            encfile(f"{path}/{getEmail()}/short_cuts_words/{self.keysLive}", password_for_encrypt)
            self.runShortCutsWord()
            self.disabledShortcut = True
            icon = IconLeftWidget(icon="delete")
            icon.bind(on_press=lambda y, x=self.keysLive: self.deleteSc(x))
            icon2 = IconLeftWidget(icon="eye")
            icon2.bind(on_press=lambda y, x=self.keysLive: self.View(x))
            items = OneLineIconListItem(text="              " + self.keysLive + " shortcut for word")
            items.add_widget(icon)
            items.add_widget(icon2)
            self.root.ids.container2.add_widget(items)

        except:
            pass

    def getDirection(self):
        with open(f"{path}/{getEmail()}/Direction.txt", 'r') as f:
            return f.read()

    def saveDirection(self, direction):
        left = ['l', 'left', 'no']
        right = ['r', 'right', 'yes']
        if direction.lower() in left:
            Common.Setlanguages("left")
        if direction.lower() in right:
            Common.Setlanguages("right")
        self.root.ids.Direction123.text = ""
        self.root.ids.Direction123.hint_text = self.getDirection()

    def getKey(self):
        f = open(rf"{path}/key.txt", 'r')
        MyKey = f.read()
        f.close()
        return MyKey

    def getOpenDesktop(self):
        if ReadOpenWindow() == "True":
            return "Yes"
        else:
            return "No"

    def getCloseDesktop(self):
        if ReadCloseWindow() == "True":
            return "Yes"
        else:
            return "No"

    def saveOpenDesktop(self, state):
        list = ["true", "yes", "y"]
        list2 = ["false", "no", "n"]
        if state.lower() in list:
            SetOpenWindow("True")
        elif state.lower() in list2:
            SetOpenWindow("False")
        self.root.ids.open.text = ""
        self.root.ids.open.hint_text = self.getOpenDesktop()

    def saveCloseDesktop(self, state):
        list = ["true", "yes", "y"]
        list2 = ["false", "no", "n"]
        if state.lower() in list:
            SetCloseWindow("True")
        elif state.lower() in list2:
            SetCloseWindow("False")
        self.root.ids.close.text = ""
        self.root.ids.close.hint_text = self.getCloseDesktop()

    def getName(self):
        with open(rf"{path}/{getEmail()}/name.txt", 'r') as f:
            return f.read()

    def show_time_picker(self):

        # Define default time
        now = datetime.datetime.now()

        current_time = now.strftime("%H:%M:%S")
        default_time = datetime.datetime.strptime(current_time, '%H:%M:%S').time()

        time_dialog = MDTimePicker()
        # Set default Time
        time_dialog.set_time(default_time)
        time_dialog.bind(on_save=self.on_save1, on_cancel=self.on_cancel)
        time_dialog.open()

    def on_save1(self, instance, value):
        self.UserTimeChoice = str(value)
        self.opacityDisable = "1"
        self.scheduleDisable = True
        self.ScheduledLabel = "Your task scheduled successfully"
        self.ScheduledTask()
        try:
            mkdir(rf"{path}/{getEmail()}/schedule1")
        except:
            pass

        with open(rf"{path}/{getEmail()}/schedule1/{self.taskToScheduled[:-1]}.txt", "w") as f:
            f.write(self.UserTimeChoice + "&" + self.UserDateChoice[:-1])

    def on_save(self, instance, value, date_range):
        self.UserDateChoice = str(value)
        self.show_time_picker()

    def show_date_picker(self, name):
        try:
            open(f"{path}/{getEmail()}/file_saver/{name[:-1]}_mm.txt", "r")
            self.taskToScheduled = name
            date_dialog = MDDatePicker(mode="picker")
            date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
            date_dialog.open()
        except:
            self.Delete()

    def show_date_picker_via_main_screen(self):
        try:
            self.taskToScheduled = new_work_name + "a"
            open(f"{path}/{getEmail()}/file_saver/{self.taskToScheduled[:-1]}_kb.txt").close()
            date_dialog = MDDatePicker(mode="picker")
            date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
            date_dialog.open()
        except:
            self.ScheduledLabel = "Please choose a valid name"

    def ScheduledTaskHelper_for_start(self):

        def job(name):
            global keep_maximized_run3

            decfile(rf"{path}/{getEmail()}/file_saver/{name}_kb.txt", password_for_encrypt)
            decfile(rf"{path}/{getEmail()}/file_saver/{name}_mb.txt", password_for_encrypt)
            decfile(rf"{path}/{getEmail()}/file_saver/{name}_mw.txt", password_for_encrypt)
            decfile(rf"{path}/{getEmail()}/file_saver/{name}_mm.txt", password_for_encrypt)

            with open(rf"{path}/{getEmail()}/file_saver/{name}_kb.txt", 'r') as f1:
                data_kb = f1.read().replace('\n', '')
            kb = data_kb

            with open(rf"{path}/{getEmail()}/file_saver/{name}_mb.txt", 'r') as f2:
                data_mb = f2.read().replace('\n', '')
            mb = data_mb

            with open(rf"{path}/{getEmail()}/file_saver/{name}_mw.txt", 'r') as f3:
                data_mw = f3.read().replace('\n', '')
            mw = data_mw

            with open(rf"{path}/{getEmail()}/file_saver/{name}_mm.txt", 'r') as f4:
                data_mm = f4.read().replace('\n', '')
            mm = data_mm

            encfile(rf"{path}/{getEmail()}/file_saver/{name}_kb.txt", password_for_encrypt)
            encfile(rf"{path}/{getEmail()}/file_saver/{name}_mb.txt", password_for_encrypt)
            encfile(rf"{path}/{getEmail()}/file_saver/{name}_mw.txt", password_for_encrypt)
            encfile(rf"{path}/{getEmail()}/file_saver/{name}_mm.txt", password_for_encrypt)

            all_events = back_to_events(kb.split('#'), mb.split('#'), mm.split('#'), mw.split('#'))
            kb_events, mb_events, mm_events, mw_events = all_events

            all_mouse_events = mb_events + mm_events + mw_events
            all_mouse_events = sorted(all_mouse_events, key=lambda event: event.time)

            keyboard.start_recording()
            keyboard.stop_recording()

            with open(f"{path}/{getEmail()}/file_saver/{name}_max_choice.txt", "r") as f:
                max_choice = f.read()
            if max_choice == "Yes":
                keep_maximized_run3 = True
                self.maximize_window_run3()
                ctrlWinD()
                runMouseMouseKeyboardEvents(all_mouse_events, kb_events, 1, 1)
                ctrlWinArrow()
                keep_maximized_run3 = False
            else:
                ctrlWinD()
                runMouseMouseKeyboardEvents(all_mouse_events, kb_events, 1, 1)
                ctrlWinArrow()

        while True:

            list_year_schedule = []
            list_month_schedule = []
            list_day_schedule = []
            list_hour_schedule = []
            list_min_schedule = []
            list_name_schedule = []

            for filename in listdir(f"{path}/{getEmail()}/schedule"):
                list_schedule_name = filename.split("'")

                name_schedule_task = list_schedule_name[12][2:]

                day_to_run = int(list_schedule_name[5])
                year_to_run = int(list_schedule_name[1])
                month_to_run = int(list_schedule_name[3])
                hour_to_run = int(list_schedule_name[7])
                min_to_run = int(list_schedule_name[9])

                list_year_schedule.append(year_to_run)
                list_month_schedule.append(month_to_run)
                list_day_schedule.append(day_to_run)
                list_hour_schedule.append(hour_to_run)
                list_min_schedule.append(min_to_run)
                list_name_schedule.append(name_schedule_task)

            date = datetime.datetime.now()

            for x in range(len(list_year_schedule)):
                if date.day == list_day_schedule[x] and date.month == list_month_schedule[x] and date.minute == \
                        list_min_schedule[x] and date.hour == list_hour_schedule[x] and date.year == list_year_schedule[
                    x]:
                    name_final = list_name_schedule[x]
                    job(name_final)

                    if int(list_hour_schedule[x]) < 10:
                        hour_to_remove = "0" + str(list_hour_schedule[x])
                    else:
                        hour_to_remove = list_hour_schedule[x]

                    if int(list_min_schedule[x]) < 10:
                        min_to_remove = "0" + str(list_min_schedule[x])
                    else:
                        min_to_remove = list_min_schedule[x]
                    try:
                        remove(
                            f"{path}/{getEmail()}/schedule/['{list_year_schedule[x]}', '{list_month_schedule[x]}', '{list_day_schedule[x]}']&['{hour_to_remove}', '{min_to_remove}', '00']&{name_final}")

                        # del list_day_schedule[x]
                        # del list_month_schedule[x]
                        # del list_hour_schedule[x]
                        # del list_min_schedule[x]
                        # del list_year_schedule[x]
                        # del list_name_schedule[x]
                        sleep(10)
                    except:
                        sleep(65)

                    # this breaks out of the while loop if it's the right day.
                    # break
                # else:
            sleep(1)  # wait 1 second

    def ScheduledTaskHelper(self):
        user_time_list = self.UserTimeChoice.split(":")
        UserDateList = self.UserDateChoice.split('-')
        if UserDateList[1][0] == '0':
            UserDateList[1] = UserDateList[1][1]
        if UserDateList[2][0] == '0':
            UserDateList[2] = UserDateList[2][1]

        with open(f'{path}/{getEmail()}/schedule/{UserDateList}&{user_time_list}&{self.taskToScheduled[:-1]}',
                  'w') as f:
            f.write(self.taskToScheduled[:-1])

        self.scheduleDisable = True

        icon = IconLeftWidget(icon="delete")
        task_to_delete = str(UserDateList) + "&" + str(user_time_list) + "&" + self.taskToScheduled[:-1]
        icon.bind(on_press=lambda y, x=task_to_delete: self.delete_schedule(x))
        items1 = OneLineIconListItem(
            text="      " + UserDateList[2] + "/" + UserDateList[1] + "/" + UserDateList[0] + "  |  " + user_time_list[
                0] + ":" + user_time_list[1] + "        " + self.taskToScheduled[:-1] + "    schedule task")
        items1.add_widget(icon)
        self.root.ids.container3.add_widget(items1)

    def ScheduledTask(self):
        schedule_thread = Thread(target=lambda: self.ScheduledTaskHelper(), daemon=True)
        schedule_thread.start()

    def Schedule(self):
        self.scheduleDisable = False
        show = ScheduleTasks()
        but = (Button(text="close", size_hint=(None, None),
                      width=100, height=50, pos_hint={"center_x": 0.3, "center_y": 0.15}, opacity=0))
        show.add_widget(but)
        popupWindow = Popup(title="Create a Schedule Task", content=show, size_hint=(None, None), size=(540, 420),
                            background_color=Common.LightDark(),
                            auto_dismiss=False)
        but.bind(on_press=popupWindow.dismiss)
        popupWindow.open()

    def get_Maximized_window_choice_state(self):
        try:
            with open(f"{path}/{getEmail()}/maximized_choice.txt", "r") as f:
                data = f.read()
            return data
        except:
            with open(f"{path}/{getEmail()}/maximized_choice.txt", "w") as f:
                f.write("No")
            return "No"

    def save_Maximized_window_choice_state(self, state):
        list = ["true", "yes", "y"]
        list2 = ["false", "no", "n"]
        if state.lower() in list:
            with open(f"{path}/{getEmail()}/maximized_choice.txt", "w") as f:
                f.write("Yes")
                f.close()
        elif state.lower() in list2:
            with open(f"{path}/{getEmail()}/maximized_choice.txt", "w") as f:
                f.write("No")
                f.close()

        self.root.ids.close1.text = ""
        self.root.ids.close1.hint_text = self.get_Maximized_window_choice_state()

    def check_if_user_have_microphone(self):
        winmm = windll.winmm
        if winmm.waveInGetNumDevs() == 0:
            self.micLabel = "We cannot detect\nan input device"
            return True
        else:
            return False

    def watch(self):
        show = Tutorial()
        closeButton = (Button(text="close", size_hint=(None, None),
                              width=100, height=50, pos_hint={"center_x": 0.35, "center_y": 0.2}, opacity=0))
        show.add_widget(closeButton)

        popupWindow0 = Popup(title="Welcome to Auto Tasks!", content=show, size_hint=(None, None),
                             background_color=Common.LightDark(),
                             size=(600, 350),
                             auto_dismiss=False)
        closeButton.bind(on_press=popupWindow0.dismiss)
        popupWindow0.open()

    def open_tutorial(self):
        openweb('https://www.youtube.com/watch?v=WTYO7_-7LJ4&ab_channel=AutoTasksOfficial')
        self.WatchText = ("Close")

