import sys
from kivy.uix.floatlayout import FloatLayout
import encrypt_files
from Common import *

splash_screen().run()
try:
    import MainScreen
except:
    sys.exit(0)
import login_password_algoritem
from re import fullmatch
from urllib.request import urlopen
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.properties import StringProperty
from kivy.core.window import Window
from secrets import randbelow
from os import path as pathos
from string import Template
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.settings import ContentPanel

loginKV = """
Screen:
    name: "login"  
    MDLabel:
        id: welcome_label
        text: "Auto Tasks"
        font_size: 36
        halign: 'center'
        size_hint_y: None
        height: self.texture_size[1]
        pos_hint: {"center_x": 0.5, "center_y": 0.85}
        padding_y: 15

    MDTextField:
        id: email
        text: app.return_remember_user_name()
        hint_text: "email"
        icon_right: "account"
        size_hint_x: None
        width: 340
        font_size: 22
        pos_hint: {"center_x": 0.5, "center_y": 0.63}

    MDTextField:
        id: password
        text: app.return_remember_passowrd()
        hint_text: "password"
        icon_right: "eye-off"
        size_hint_x: None
        width: 340
        font_size: 22
        pos_hint: {"center_x": 0.5, "center_y": 0.52}
        password: True
        max_text_length: 15
        
    MDIconButton:
        icon: "eye"
        on_press: app.show_password3()
        pos_hint: {"center_x": 0.86, "center_y": 0.535}
        opacity: 0

    MDRectangleFlatButton:
        id: login
        text: "Log in"
        font_size: 16
        pos_hint: {"center_x": 0.5, "center_y": 0.37}
        on_press: app.logger()
        #focus: True

    Image:
        source: app.state
        size_hint_y: None
        height: dp(30)
        pos_hint: {"center_x": 0.82, "center_y": 0.37}

    MDRectangleFlatButton:
        text: " "
        font_size: 20
        pos_hint: {"center_x": 0.82, "center_y": 0.37}
        on_press: app.checkbox()
        opacity: 0

    MDRectangleFlatButton:
        text: "Register"
        font_size: 16
        pos_hint: {"center_x": 0.5, "center_y": 0.24}
        on_press: app.register()

    MDLabel:
        text: "Keep me\\nlogged in"
        #width: 50
        font_size: 15
        pos_hint: {"center_x": 1.25, "center_y": 0.3}

    MDRectangleFlatButton:
        text: "Forgot your password?"
        font_size: 16
        pos_hint: {"center_x": 0.5, "center_y": 0.11}
        on_press: app.forgot()

"""
forgotKV = """
Screen:
    MDCard:
        size_hint: None, None
        size: 420,600
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        elevation: 10
        padding: 25
        spacing: 25
        orientation: 'vertical'

        MDLabel:
            id: welcome_label
            text: "Enter your email below"
            font_size: 36
            halign: 'center'
            size_hint_y: None
            height: self.texture_size[1]
            padding_y: 15

        Widget:
            size_hint_y: None
            height: 30

        MDTextField:
            id: email
            hint_text: "email"
            icon_right: "account"
            size_hint_x: None
            width: 340
            font_size: 22
            pos_hint: {"center_x": 0.5}
            on_text_validate:

        Widget:
            size_hint_y: None
            height: 50

        MDRectangleFlatButton:
            text: "Submit email"
            font_size: 18
            pos_hint: {"center_x": 0.5}
            on_press: app.enter_email()


        MDRectangleFlatButton:
            text: "Go back"
            font_size: 18
            pos_hint: {"center_x": 0.5}
            on_press: app.login()

        Widget:
            size_hint_y: None
            height: 50
"""
registerKV = """
Screen:
    MDLabel:
        id: welcome_label
        text: "Auto Tasks"
        font_size: 34
        halign: 'center'
        size_hint_y: None
        height: self.texture_size[1]
        pos_hint: {"center_x": 0.5, "center_y": 0.85}

    MDTextField:
        id: name
        hint_text: "name"
        icon_right: "face"
        size_hint_x: None
        width: 340
        font_size: 22
        pos_hint: {"center_x": 0.5, "center_y": 0.66}

    MDTextField:
        id: email
        hint_text: "email"
        icon_right: "account"
        size_hint_x: None
        width: 340
        font_size: 22
        pos_hint: {"center_x": 0.5, "center_y": 0.54}

    MDTextField:
        id: password
        hint_text: "password"
        icon_right: "eye-off"
        size_hint_x: None
        width: 340
        font_size: 22
        pos_hint: {"center_x": 0.5, "center_y": 0.42}
        password: True
        max_text_length: 15
    MDIconButton:
        icon: "eye"
        on_press: app.show_password1()
        pos_hint: {"center_x": 0.86, "center_y": 0.43}
        opacity: 0

    MDTextField:
        id: password2
        hint_text: "confirm your password"
        icon_right: "eye-off"
        size_hint_x: None
        width: 340
        font_size: 22
        pos_hint: {"center_x": 0.5, "center_y": 0.30}
        password: True
        max_text_length: 15
    MDIconButton:
        icon: "eye"
        on_press: app.show_password2()
        pos_hint: {"center_x": 0.86, "center_y": 0.31}
        opacity: 0

    MDRectangleFlatButton:
        text: "Register"
        font_size: 16
        pos_hint: {"center_x": 0.7, "center_y": 0.15}
        on_press: app.ChecKill()
        focus: True

    MDRectangleFlatButton:
        text: "Login"
        font_size: 16
        pos_hint: {"center_x": 0.3, "center_y": 0.15}
        on_press: app.login()

"""
validEmail = """
<Info>
    Label:
        text: 'The ultra secured option make\\nall your account data a lot more\\nsecured, but if you forgot your\\npassword all your tasks and shortcuts\\ndata will be inaccessible'
        size_hint_x: None
        size_hint_y: None
        font_size: 20
        pos_hint: {"center_x": 0.5, "center_y": 0.69}

    MDRectangleFlatButton:
        text: "Okay"
        font_size: 18
        pos_hint: {'center_x':0.5, 'center_y':0.16}
        
Screen:
    MDLabel:
        id: codeLabel
        text: app.codeLabel
        font_size: 26
        halign: 'center'
        size_hint_y: None
        pos_hint: {"center_x": 0.5, "center_y": 0.8}

    MDTextField:
        id: code
        hint_text: "code"
        icon_right: "email"
        size_hint_x: None
        width: 340
        font_size: 22
        pos_hint: {"center_x": 0.5}
        max_text_length: 6
        pos_hint: {"center_x": 0.5, "center_y": 0.55}

    MDRectangleFlatButton:
        text: "Submit"
        font_size: 16
        pos_hint: {"center_x": 0.33, "center_y": 0.15}
        on_press: app.submit()

    MDRectangleFlatButton:
        text: "Go back"
        font_size: 16
        pos_hint: {"center_x": 0.67, "center_y": 0.15}
        on_press: app.register()

    MDLabel:
        text: "Ultra secured"
        font_size: 23
        size_hint_y: None
        halign: 'center'
        size_hint_y: None
        pos_hint: {"center_x": 0.35, "center_y": 0.3}
        
    MDIconButton:
        icon: "information"
        user_font_size: "32sp"
        on_press: app.info()
        pos_hint: {"center_x": 0.8, "center_y": 0.3}
        
    CheckBox:
        pos_hint: {"center_x": 0.65, "center_y": 0.3}
        active: False
        on_active: app.ultra(self.active)
        background_checkbox_normal: app.checkBoxImage
        background_checkbox_down: app.checkBoxImage2
        size_hint_x: None
        size_hint_y: None
        size: sp(60), sp(60)
"""
enterPass = """
Screen:
    MDCard:
        size_hint: None, None
        size: 420,600
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        elevation: 10
        padding: 25
        spacing: 25
        orientation: 'vertical'

        MDLabel:
            id: codeLabel
            text: app.Label
            font_size: 23
            halign: 'center'
            size_hint_y: None
            height: self.texture_size[1]
            padding_y: 15

        Widget:
            size_hint_y: None
            height: 60

        MDTextField:
            id: code
            hint_text: "code"
            icon_right: "email"
            size_hint_x: None
            width: 340
            font_size: 22
            pos_hint: {"center_x": 0.5}
            max_text_length: 6

        Widget:
            size_hint_y: None
            height: 20

        MDRectangleFlatButton:
            text: "Submit"
            font_size: 16
            pos_hint: {"center_x": 0.5}
            on_press: app.newPass()


        Widget:
            size_hint_y: None
            height: 30
"""
newPassword = """
Screen:
    MDCard:
        size_hint: None, None
        size: 420,600
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        elevation: 10
        padding: 25
        spacing: 25
        orientation: 'vertical'

        Widget:
            size_hint_y: None
            height: 20

        MDLabel:
            id: welcome_label
            text: "Enter a new password"
            font_size: 40
            halign: 'center'
            size_hint_y: None
            height: self.texture_size[1]
            padding_y: 15

        Widget:
            size_hint_y: None
            height: 20

        MDTextField:
            id: password
            hint_text: "new password"
            icon_right: "eye-off"
            size_hint_x: None
            width: 340
            font_size: 22
            pos_hint: {"center_x": 0.5}
            password: True
            max_text_length: 15


        MDTextField:
            id: password2
            hint_text: "new password"
            icon_right: "eye-off"
            size_hint_x: None
            width: 340
            font_size: 22
            pos_hint: {"center_x": 0.5}
            password: True
            max_text_length: 15
        # MDIconButton:
        #     icon: "eye"
        #     on_press: app.show_password5()
        #     pos_hint: {"center_x": 0.5, "center_y": 0.43}
        #     opacity: 1


        Widget:
            size_hint_y: None
            height: 20

        MDRectangleFlatButton:
            id: submit
            text: "Submit"
            font_size: 16
            pos_hint: {"center_x": 0.5}
            on_press: app.checkIfPasswordMatch()

        Widget:
            size_hint_y: None
            height: 10
"""

Theme = GetColort()

class LoginScreen(MDApp):
    unchecked = StringProperty(rf"{ImagePath}\unchecked.png")
    checked = StringProperty(rf"{ImagePath}\checked.png")
    spa = StringProperty(rf"{ImagePath}\splash_image.png")
    state = unchecked
    count = 0

    def show_password3(self):
        if self.root.ids.password.password == True:
            self.root.ids.password.password = False
            self.root.ids.password.icon_right = "eye"
        else:
            self.root.ids.password.password = True
            self.root.ids.password.icon_right = "eye-off"

    def build(self):
        Window.size = (420, 600)
        self.icon = rf"{ImagePath}\icon.png"
        self.title = "Auto Tasks"
        self.theme_cls.theme_style = Theme
        self.theme_cls.primary_palette = Colorr()
        self.state = self.unchecked
        self.use_kivy_settings = False
        self.settings_cls = ContentPanel
        Window.bind(on_key_down=self._on_keyboard_down)
        return Builder.load_string(loginKV)

    def _on_keyboard_down(self, instance, keyboard, keycode, text, modifiers):
        if keycode == 40 and self.count != -1:  # 40 - Enter key pressed
            self.logger()

    def login(self, Password, Email):
        LoginScreen.get_running_app().stop()
        with open(rf"{path}/emailNow.txt", 'w') as emailNow:
            emailNow.write(Email)
            emailNow.close()
        Window.size = (1080, 720)
        self.count = -1
        MainScreen.AutoTask(Password).run()

    def logger(self):
        Email = self.root.ids.email.text
        Password = self.root.ids.password.text

        try:
            with open(f'{path}/{getEmail()}/password.txt') as f:
                code_to_encrypt_with = f.read()
        except:
            code_to_encrypt_with = ""

        global password_for_encrypt
        try:
            password_for_encrypt = getEmail() + code_to_encrypt_with
        except:
            password_for_encrypt = ""

        if login_password_algoritem.user_sign_in(Password, Email):
            self.login(Password, Email)
            with open(rf"{path}/remember.txt", "r") as f:
                data = f.read()

            if data == "yes":
                with open(rf"{path}/username_remember.txt", "w") as f:
                    f.write(Email)
                with open(rf"{path}/password_remember.txt", "w") as f:
                    f.write(Password)

                encrypt_files.encfile(rf"{path}/password_remember.txt", password_for_encrypt)

            else:
                with open(rf"{path}/username_remember.txt", "w") as f:
                    f.write("")
                    f.close()
                with open(rf"{path}/password_remember.txt", "w") as f:
                    f.write("")
                    f.close()

        else:
            self.root.ids.welcome_label.text = "Incorrect email or\npassword"
            self.root.ids.password.text = ""
            self.root.ids.email.text = ""

    def return_remember_passowrd(self):
        try:
            with open(f'{path}/{getEmail()}/password.txt') as f:
                code_to_encrypt_with1 = f.read()
            password_for_encrypt2 = getEmail() + code_to_encrypt_with1

            with open(rf"{path}/remember.txt", "r") as f:
                choise_remember = f.read()
            if choise_remember == "yes":
                encrypt_files.decfile(rf"{path}/password_remember.txt", password_for_encrypt2)
                with open(rf"{path}/password_remember.txt", "r") as f:
                    password_remember = f.read()
                encrypt_files.encfile(rf"{path}/password_remember.txt", password_for_encrypt2)

            else:
                password_remember = ""
            return password_remember
        except:
            password_remember = ""
            return password_remember

    def return_remember_user_name(self):
        with open(rf"{path}/remember.txt", "r") as f:
            choise_remember = f.read()
        if choise_remember == "yes":
            with open(rf"{path}/username_remember.txt", "r") as f:
                user_name_remember = f.read()
        else:
            user_name_remember = ""
        return user_name_remember

    def register(self):
        LoginScreen.get_running_app().stop()
        RegisterScreen().run()

    def forgot(self):
        LoginScreen.get_running_app().stop()
        forgot_password().run()

    def checkbox(self):
        Email = self.root.ids.email.text
        Password = self.root.ids.password.text
        if self.state == rf"{ImagePath}\unchecked.png":
            self.state = rf"{ImagePath}\checked.png"
            writeInFile(f"{path}/remember.txt", "yes")

        else:
            self.state = rf"{ImagePath}\unchecked.png"

            writeInFile(rf"{path}/remember.txt", "no")

class RegisterScreen(MDApp):

    def show_password1(self):
        if self.root.ids.password.password == True:
            self.root.ids.password.password = False
            self.root.ids.password.icon_right = "eye"
        else:
            self.root.ids.password.password = True
            self.root.ids.password.icon_right = "eye-off"

    def show_password2(self):
        if self.root.ids.password2.password == True:
            self.root.ids.password2.password = False
            self.root.ids.password2.icon_right = "eye"
        else:
            self.root.ids.password2.password = True
            self.root.ids.password2.icon_right = "eye-off"

    def build(self):
        self.title = "Auto Tasks"
        self.theme_cls.theme_style = Theme
        self.theme_cls.primary_palette = Colorr()
        return Builder.load_string(registerKV)

    def ChecKill(self):
        lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        z = False
        for x in self.root.ids.password.text:
            if x not in lst:
                z = True

        if z:
            self.root.ids.welcome_label.text = "Password can only contain:\na-z, A-Z, 0-9"
            self.root.ids.password.text = ""
            self.root.ids.password2.text = ""

        elif len(self.root.ids.password.text) > 15 or len(self.root.ids.password2.text) > 15:
            self.root.ids.welcome_label.text = "Passwords are too long"
            self.root.ids.password.text = ""
            self.root.ids.password2.text = ""

        elif not self.root.ids.password.text == self.root.ids.password2.text:
            self.root.ids.welcome_label.text = "Passwords are not match"
            self.root.ids.password.text = ""
            self.root.ids.password2.text = ""

        elif self.root.ids.password.text == "" or self.root.ids.password2.text == "":
            self.root.ids.welcome_label.text = "Please enter a valid password"
            self.root.ids.password.text = ""
            self.root.ids.password2.text = ""

        else:
            self.Commit()

    def validEmail1(self):
        self.root.ids.email.text = ""
        self.root.ids.welcome_label.text = "Email is invalid"

    def Commit(self):
        global userEmail
        userEmail = self.root.ids.email.text
        global userPassword
        userPassword = self.root.ids.password.text
        global userName
        userName = self.root.ids.name.text

        if pathos.isdir(rf"{path}\{userEmail}") == True:
            self.root.ids.welcome_label.text = "Email is already in use"
            self.root.ids.email.text = ""

        else:
            self.sendEmail()

    def check_internet(self):
        try:
            urlopen("https://www.google.com")
            return True
        except:
            return False

    def check_email_laws(self, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if (fullmatch(regex, email)):
            return True
        else:
            return False

    def 
    
    Email(self):
        if self.check_internet():
            if self.check_email_laws(userEmail):
                try:
                    simple_num = 100000
                    random_number_for_autacation = randbelow(899999)
                    global final_number
                    final_number = random_number_for_autacation + simple_num

                    html_verison = """\
                                    <html>
                                        <head>
                                            <title></title>
                                            <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
                                            <meta name="viewport" content="width=device-width, initial-scale=1">
                                            <meta http-equiv="X-UA-Compatible" content="IE=edge" />
                                            <style type="text/css">
                                                @media screen {
                                                    @font-face {
                                                        font-family: 'Lato';
                                                        font-style: normal;
                                                        font-weight: 400;
                                                        src: local('Lato Regular'), local('Lato-Regular'), url(https://fonts.gstatic.com/s/lato/v11/qIIYRU-oROkIk8vfvxw6QvesZW2xOQ-xsNqO47m55DA.woff) format('woff');
                                                    }

                                                    @font-face {
                                                        font-family: 'Lato';
                                                        font-style: normal;
                                                        font-weight: 700;
                                                        src: local('Lato Bold'), local('Lato-Bold'), url(https://fonts.gstatic.com/s/lato/v11/qdgUG4U09HnJwhYI-uK18wLUuEpTyoUstqEm5AMlJo4.woff) format('woff');
                                                    }

                                                    @font-face {
                                                        font-family: 'Lato';
                                                        font-style: italic;
                                                        font-weight: 400;
                                                        src: local('Lato Italic'), local('Lato-Italic'), url(https://fonts.gstatic.com/s/lato/v11/RYyZNoeFgb0l7W3Vu1aSWOvvDin1pK8aKteLpeZ5c0A.woff) format('woff');
                                                    }

                                                    @font-face {
                                                        font-family: 'Lato';
                                                        font-style: italic;
                                                        font-weight: 700;
                                                        src: local('Lato Bold Italic'), local('Lato-BoldItalic'), url(https://fonts.gstatic.com/s/lato/v11/HkF_qI1x_noxlxhrhMQYELO3LdcAZYWl9Si6vvxL-qU.woff) format('woff');
                                                    }
                                                }

                                                /* CLIENT-SPECIFIC STYLES */
                                                body,
                                                table,
                                                td,
                                                a {
                                                    -webkit-text-size-adjust: 100%;
                                                    -ms-text-size-adjust: 100%;
                                                }

                                                table,
                                                td {
                                                    mso-table-lspace: 0pt;
                                                    mso-table-rspace: 0pt;
                                                }

                                                img {
                                                    -ms-interpolation-mode: bicubic;
                                                }

                                                #logo {
                                                    height: 20%;
                                                    width: 20%;
                                                    margin-top: 2%;
                                                }

                                                /* RESET STYLES */
                                                img {
                                                    border: 0;
                                                    height: auto;
                                                    line-height: 100%;
                                                    outline: none;
                                                    text-decoration: none;
                                                }

                                                table {
                                                    border-collapse: collapse !important;
                                                }

                                                body {
                                                    height: 100% !important;
                                                    margin: 0 !important;
                                                    padding: 0 !important;
                                                    width: 100% !important;
                                                }

                                                /* iOS BLUE LINKS */
                                                a[x-apple-data-detectors] {
                                                    color: inherit !important;
                                                    text-decoration: none !important;
                                                    font-size: inherit !important;
                                                    font-family: inherit !important;
                                                    font-weight: inherit !important;
                                                    line-height: inherit !important;
                                                }

                                                /* MOBILE STYLES */
                                                @media screen and (max-width:600px) {
                                                    h1 {
                                                        font-size: 32px !important;
                                                        line-height: 32px !important;
                                                    }
                                                }

                                                /* ANDROID CENTER FIX */
                                                div[style*="margin: 16px 0;"] {
                                                    margin: 0 !important;
                                                }
                                                a {
                                                    background-color: #1368ba;
                                                    cursor: pointer;
                                                }
                                            </style>
                                            <script type="text/javascript">
                                                function copyToClipboard() {
                                                    var copyText = document.getElementById("number-code");
                                                    navigator.clipboard.writeText(copyText.innerHTML);
                                                    document.getElementById("copied?").innerHTML = "Copied!"
                                                }
                                            </script>
                                        </head>

                                        <body style="background-color: #f4f4f4; margin: 0 !important; padding: 0 !important;">
                                            <!-- HIDDEN PREHEADER TEXT -->
                                            <div style="display: none; font-size: 1px; color: #fefefe; line-height: 1px; font-family: 'Lato', Helvetica, Arial, sans-serif; max-height: 0px; max-width: 0px; opacity: 0; overflow: hidden;"> We're thrilled to have you here! Get ready to dive into your new account. </div>
                                            <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                                <!-- LOGO -->
                                                <tr>
                                                    <td bgcolor="#1368ba" align="center">
                                                        <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">
                                                            <tr>
                                                                <td align="center" valign="top" style="padding: 40px 10px 40px 10px;"> </td>
                                                            </tr>
                                                        </table>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td bgcolor="#1368ba" align="center" style="padding: 0px 10px 0px 10px;">
                                                        <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">
                                                            <tr>
                                                                <td bgcolor="#ffffff" align="center" valign="top" style="padding: 40px 20px 20px 20px; border-radius: 4px 4px 0px 0px; color: #111111; font-family: 'Lato', Helvetica, Arial, sans-serif; font-size: 48px; font-weight: 400; letter-spacing: 4px; line-height: 48px;">
                                                                    <h1 style="font-size: 45px; font-weight: 400; margin: 2; margin-bottom: 3%;">Welcome , $code !</h1> <img src=" https://img.icons8.com/clouds/100/000000/handshake.png" width="125" height="120" style="display: block; border: 0px; margin-bottom: -2%;" />
                                                                </td>
                                                            </tr>
                                                        </table>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td bgcolor="#f4f4f4" align="center" style="padding: 0px 10px 0px 10px;">
                                                        <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">
                                                            <tr>
                                                                <td bgcolor="#ffffff" align="left" style="padding: 20px 30px 40px 30px; color: #666666; font-family: 'Lato', Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; line-height: 25px;">
                                                                    <p style="margin: 0; text-align: center; font-size: 20px;">Enter the number below in the AutoTasks application.</p>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td bgcolor="#ffffff" align="left">
                                                                    <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                                                        <tr>
                                                                            <td bgcolor="#ffffff" align="center" style="padding: 20px 30px 60px 30px;">
                                                                                <table border="0" cellspacing="0" cellpadding="0">
                                                                                    <tr>
                                                                                        <td align="center" style="border-radius: 3px;" bgcolor="#1368ba"><a onclick="copyToClipboard()" id="number-code" style="font-size: 20px; font-family: Helvetica, Arial, sans-serif; color: #ffffff; text-decoration: none; color: #ffffff; text-decoration: none; padding: 15px 25px; border-radius: 2px; border: 1px solid #1368ba; display: inline-block;">$code1</a>
                                                                                        </td>

                                                                                    </tr>
                                                                                </table>
                                                                                <p id="copied?" style="font-size: 18px; font-family: 'Lato', Helvetica, Arial, sans-serif; color: #747474;">&nbsp;</p>
                                                                            </td>
                                                                        </tr>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td bgcolor="#ffffff" align="left" style="padding: 0px 30px 0px 30px; color: #666666; font-family: 'Lato', Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; line-height: 25px;">
                                                                    <p style="margin: 0; margin-bottom: 3%; font-size: 15px; text-align: center;">If you have any questions, just reply to this email. We'll be happy to serve you :)</p>
                                                                </td>
                                                            </tr> <!-- COPY -->
                                                        </table>
                                                    </td>
                                                </tr>
                                                <tr>
                                                <tr>
                                                    <td bgcolor="#f4f4f4" align="center" style="padding: 0px 10px 0px 10px;">
                                                        <img id="logo" src="https://www.mediafire.com/file/0lx3rwggkr17nez/i01_WhatsApp_Image_2021-09-29_at_19.36.09_auto_x2_light_ai_2_%25281%2529.jpg/file">
                                                    </td>
                                                </tr>

                                            </table>
                                        </body>

                                    </html>

                                """

                    # userName = "nadav"
                    s = Template(html_verison).safe_substitute(code=str(userName))

                    final_number_new = final_number
                    s1 = Template(s).safe_substitute(code1=str(final_number_new))

                    message = Mail(
                        from_email='auto.tasks.service@gmail.com',
                        to_emails=userEmail,
                        subject='AutoTasks | Your Verification Code',
                        html_content=s1)
                    sg = SendGridAPIClient(env["sendgrid_api_key"])
                    sg.send(message)

                    RegisterScreen.get_running_app().stop()
                    validEmailKV().run()

                except:
                    login_password_algoritem.savePassword(userPassword, userEmail, userName)
                    self.login1(userEmail)

            else:
                self.root.ids.welcome_label.text = ""
                self.root.ids.welcome_label.text = "Your email address is not valid"

        else:
            self.root.ids.welcome_label.text = ""
            self.root.ids.welcome_label.text = "You dont have internet connection"

    def login1(self, Email):
        validEmailKV.get_running_app().stop()
        with open(rf"{path}/emailNow.txt", 'w') as emailNow:
            emailNow.write(Email)
            emailNow.close()
        Window.size = (1080, 720)
        self.count = -1
        MainScreen.AutoTask(userPassword).run()

    def login(self):
        RegisterScreen.get_running_app().stop()
        LoginScreen().run()

class validEmailKV(MDApp):
    checkBoxImage = StringProperty(rf"{ImagePath}\unchecked.png")
    checkBoxImage2 = StringProperty(rf"{ImagePath}\checked.png")
    codeLabel = StringProperty(f"We sent a verification code\n to your email")
    count = 0

    def build(self):
        self.title = "Auto Tasks"
        self.theme_cls.theme_style = Theme
        self.theme_cls.primary_palette = Colorr()
        Window.bind(on_key_down=self._on_keyboard_down)
        self.codeLabel = f"We sent a verification code\n to: {userEmail}"
        return Builder.load_string(validEmail)

    def _on_keyboard_down(self, instance, keyboard, keycode, text, modifiers):
        if keycode == 40 and self.count != -1:  # 40 - Enter key pressed
            self.submit()

    def ultra(self, value):
        try:
            if value:
                with open(rf"{path}/{userEmail}_ultra_secure.txt", "w") as f:
                    f.write("on")
                    f.close()
            else:
                with open(rf"{path}/{userEmail}_ultra_secure.txt", "w") as f:
                    f.write("off")
                    f.close()
        except:
            pass

    def info(self):
        show = Info()
        but = (Button(text="Okay", size_hint=(None, None),
                      width=100, height=50, pos_hint={"center_x": 0.5, "center_y": 0.16}, opacity=0))
        show.add_widget(but)
        popupWindow = Popup(title="What is ultra secured?", content=show, size_hint=(None, None),
                            size=(375, 320), auto_dismiss=False)
        but.bind(on_press=popupWindow.dismiss)
        popupWindow.open()

    def submit(self):
        userCode = self.root.ids.code.text
        if userCode == str(final_number):
            login_password_algoritem.savePassword(userPassword, userEmail, userName)

            self.login(userEmail)
        else:
            self.codeLabel = "try again"

    def login(self, Email):
        validEmailKV.get_running_app().stop()
        with open(rf"{path}/emailNow.txt", 'w') as emailNow:
            emailNow.write(Email)
            emailNow.close()
        Window.size = (1080, 720)
        self.count = -1
        MainScreen.AutoTask(userPassword).run()

    def register(self):
        validEmailKV.get_running_app().stop()
        RegisterScreen().run()

class forgot_password(MDApp):
    num_enter = 0

    def build(self):
        self.title = "Auto Tasks"
        self.theme_cls.theme_style = Theme
        self.theme_cls.primary_palette = Colorr()

        Window.bind(on_key_down=self._on_keyboard_down)

        return Builder.load_string(forgotKV)

    def _on_keyboard_down(self, instance, keyboard, keycode, text, modifiers):
        if keycode == 40 and self.num_enter == 0:  # 40 - Enter key pressed
            self.num_enter = 1
            self.enter_email()

    def login(self):
        forgot_password.get_running_app().stop()
        LoginScreen().run()

    def submit(self):
        forgot_password.get_running_app().stop()
        EnterNewPassword().run()

    # def check_if_username_ultra_secure(self):
    #     with open(rf"{path}/{userEmail}_ultra_secure.txt", "r") as f:
    #         ultra_mode = f.read()
    #
    #     if ultra_mode == "on":
    #         return True
    #     else:
    #         return False
# "Your account is in ultra secure mode if you reset your password all your account data will be inaccessible if you want to continue enter submit again"

    def enter_email(self):
        userEmail = self.root.ids.email.text
        if pathos.isdir(f"{path}/{userEmail}"):
            try:
                global Email123
                Email123 = userEmail
                simple_num = 100000
                random_number_for_autacation = randbelow(899999)
                global final_number
                final_number = random_number_for_autacation + simple_num

                html_verison = """\
                                <html>
                                    <head>
                                        <title></title>
                                        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
                                        <meta name="viewport" content="width=device-width, initial-scale=1">
                                        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
                                        <style type="text/css">
                                            @media screen {
                                                @font-face {
                                                    font-family: 'Lato';
                                                    font-style: normal;
                                                    font-weight: 400;
                                                    src: local('Lato Regular'), local('Lato-Regular'), url(https://fonts.gstatic.com/s/lato/v11/qIIYRU-oROkIk8vfvxw6QvesZW2xOQ-xsNqO47m55DA.woff) format('woff');
                                                }

                                                @font-face {
                                                    font-family: 'Lato';
                                                    font-style: normal;
                                                    font-weight: 700;
                                                    src: local('Lato Bold'), local('Lato-Bold'), url(https://fonts.gstatic.com/s/lato/v11/qdgUG4U09HnJwhYI-uK18wLUuEpTyoUstqEm5AMlJo4.woff) format('woff');
                                                }

                                                @font-face {
                                                    font-family: 'Lato';
                                                    font-style: italic;
                                                    font-weight: 400;
                                                    src: local('Lato Italic'), local('Lato-Italic'), url(https://fonts.gstatic.com/s/lato/v11/RYyZNoeFgb0l7W3Vu1aSWOvvDin1pK8aKteLpeZ5c0A.woff) format('woff');
                                                }

                                                @font-face {
                                                    font-family: 'Lato';
                                                    font-style: italic;
                                                    font-weight: 700;
                                                    src: local('Lato Bold Italic'), local('Lato-BoldItalic'), url(https://fonts.gstatic.com/s/lato/v11/HkF_qI1x_noxlxhrhMQYELO3LdcAZYWl9Si6vvxL-qU.woff) format('woff');
                                                }
                                            }

                                            /* CLIENT-SPECIFIC STYLES */
                                            body,
                                            table,
                                            td,
                                            a {
                                                -webkit-text-size-adjust: 100%;
                                                -ms-text-size-adjust: 100%;
                                            }

                                            table,
                                            td {
                                                mso-table-lspace: 0pt;
                                                mso-table-rspace: 0pt;
                                            }

                                            img {
                                                -ms-interpolation-mode: bicubic;
                                            }

                                            #logo {
                                                height: 20%;
                                                width: 20%;
                                                margin-top: 2%;
                                            }

                                            /* RESET STYLES */
                                            img {
                                                border: 0;
                                                height: auto;
                                                line-height: 100%;
                                                outline: none;
                                                text-decoration: none;
                                            }

                                            table {
                                                border-collapse: collapse !important;
                                            }

                                            body {
                                                height: 100% !important;
                                                margin: 0 !important;
                                                padding: 0 !important;
                                                width: 100% !important;
                                            }

                                            /* iOS BLUE LINKS */
                                            a[x-apple-data-detectors] {
                                                color: inherit !important;
                                                text-decoration: none !important;
                                                font-size: inherit !important;
                                                font-family: inherit !important;
                                                font-weight: inherit !important;
                                                line-height: inherit !important;
                                            }

                                            /* MOBILE STYLES */
                                            @media screen and (max-width:600px) {
                                                h1 {
                                                    font-size: 32px !important;
                                                    line-height: 32px !important;
                                                }
                                            }

                                            /* ANDROID CENTER FIX */
                                            div[style*="margin: 16px 0;"] {
                                                margin: 0 !important;
                                            }
                                            a {
                                                background-color: #1368ba;
                                                cursor: pointer;
                                            }
                                        </style>
                                        <script type="text/javascript">
                                            function copyToClipboard() {
                                                var copyText = document.getElementById("number-code");
                                                navigator.clipboard.writeText(copyText.innerHTML);
                                                document.getElementById("copied?").innerHTML = "Copied!"
                                            }
                                        </script>
                                    </head>

                                    <body style="background-color: #f4f4f4; margin: 0 !important; padding: 0 !important;">
                                        <!-- HIDDEN PREHEADER TEXT -->
                                        <div style="display: none; font-size: 1px; color: #fefefe; line-height: 1px; font-family: 'Lato', Helvetica, Arial, sans-serif; max-height: 0px; max-width: 0px; opacity: 0; overflow: hidden;"> We're thrilled to have you here! Get ready to dive into your new account. </div>
                                        <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                            <!-- LOGO -->
                                            <tr>
                                                <td bgcolor="#1368ba" align="center">
                                                    <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">
                                                        <tr>
                                                            <td align="center" valign="top" style="padding: 40px 10px 40px 10px;"> </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                            <tr>
                                                <td bgcolor="#1368ba" align="center" style="padding: 0px 10px 0px 10px;">
                                                    <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">
                                                        <tr>
                                                            <td bgcolor="#ffffff" align="center" valign="top" style="padding: 40px 20px 20px 20px; border-radius: 4px 4px 0px 0px; color: #111111; font-family: 'Lato', Helvetica, Arial, sans-serif; font-size: 48px; font-weight: 400; letter-spacing: 4px; line-height: 48px;">
                                                                <h1 style="font-size: 45px; font-weight: 400; margin: 2; margin-bottom: 3%;">Welcome </h1> <img src=" https://img.icons8.com/clouds/100/000000/handshake.png" width="125" height="120" style="display: block; border: 0px; margin-bottom: -2%;" />
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                            <tr>
                                                <td bgcolor="#f4f4f4" align="center" style="padding: 0px 10px 0px 10px;">
                                                    <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">
                                                        <tr>
                                                            <td bgcolor="#ffffff" align="left" style="padding: 20px 30px 40px 30px; color: #666666; font-family: 'Lato', Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; line-height: 25px;">
                                                                <p style="margin: 0; text-align: center; font-size: 20px;">Enter the number below in the AutoTasks application.</p>
                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <td bgcolor="#ffffff" align="left">
                                                                <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                                                    <tr>
                                                                        <td bgcolor="#ffffff" align="center" style="padding: 20px 30px 60px 30px;">
                                                                            <table border="0" cellspacing="0" cellpadding="0">
                                                                                <tr>
                                                                                    <td align="center" style="border-radius: 3px;" bgcolor="#1368ba"><a onclick="copyToClipboard()" id="number-code" style="font-size: 20px; font-family: Helvetica, Arial, sans-serif; color: #ffffff; text-decoration: none; color: #ffffff; text-decoration: none; padding: 15px 25px; border-radius: 2px; border: 1px solid #1368ba; display: inline-block;">$code1</a>
                                                                                    </td>

                                                                                </tr>
                                                                            </table>
                                                                            <p id="copied?" style="font-size: 18px; font-family: 'Lato', Helvetica, Arial, sans-serif; color: #747474;">&nbsp;</p>
                                                                        </td>
                                                                    </tr>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <td bgcolor="#ffffff" align="left" style="padding: 0px 30px 0px 30px; color: #666666; font-family: 'Lato', Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; line-height: 25px;">
                                                                <p style="margin: 0; margin-bottom: 3%; font-size: 15px; text-align: center;">If you have any questions, just reply to this email. We'll be happy to serve you :)</p>
                                                            </td>
                                                        </tr> <!-- COPY -->
                                                    </table>
                                                </td>
                                            </tr>
                                            <tr>
                                            <tr>
                                                <td bgcolor="#f4f4f4" align="center" style="padding: 0px 10px 0px 10px;">
                                                    <img id="logo" src="https://www.mediafire.com/file/0lx3rwggkr17nez/i01_WhatsApp_Image_2021-09-29_at_19.36.09_auto_x2_light_ai_2_%25281%2529.jpg/file">
                                                </td>
                                            </tr>

                                        </table>
                                    </body>

                                </html>

        """

                final_number_new = final_number
                s1 = Template(html_verison).safe_substitute(code1=str(final_number_new))

                message = Mail(
                    from_email='auto.tasks.service@gmail.com',
                    to_emails=userEmail,
                    subject='AutoTasks | Your Verification Code',
                    html_content=s1)
                sg = SendGridAPIClient('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')
                sg.send(message)
                self.submit()

            except:
                self.validEmail1("Something went wrong")
        else:
            self.validEmail1("Email not exist")

    def validEmail1(self, text):
        self.root.ids.email.text = ""
        self.root.ids.welcome_label.text = text

class EnterNewPassword(MDApp):
    Label = StringProperty(f"We sent a verification code\n to your email")

    def build(self):
        self.title = "Auto Tasks"
        self.theme_cls.theme_style = Theme
        self.theme_cls.primary_palette = Colorr()
        Window.bind(on_key_down=self._on_keyboard_down)
        return Builder.load_string(enterPass)

    def _on_keyboard_down(self, instance, keyboard, keycode, text, modifiers):
        if keycode == 40:
            self.newPass()

    def newPass(self):
        userCode = self.root.ids.code.text

        for i in range(1, 6):
            if userCode == str(final_number):
                self.EnterNewPassword()
            else:
                self.codeLabel = "try again"

    def EnterNewPassword(self):
        EnterNewPassword.get_running_app().stop()
        NewPassword().run()

class NewPassword(MDApp):
    Label = StringProperty(f"We sent a verification code\n to your email")

    def show_password4(self):
        if self.root.ids.password.password == True:
            self.root.ids.password.password = False
            self.root.ids.password.icon_right = "eye"
        else:
            self.root.ids.password.password = True
            self.root.ids.password.icon_right = "eye-off"

    def show_password5(self):
        if self.root.ids.password2.password == True:
            self.root.ids.password2.password = False
            self.root.ids.password2.icon_right = "eye"
        else:
            self.root.ids.password2.password = True
            self.root.ids.password2.icon_right = "eye-off"

    def build(self):
        self.title = "Auto Tasks"
        self.theme_cls.theme_style = Theme
        self.theme_cls.primary_palette = Colorr()
        Window.bind(on_key_down=self._on_keyboard_down)
        return Builder.load_string(newPassword)

    def _on_keyboard_down(self, instance, keyboard, keycode, text, modifiers):

        if keycode == 40:  # 40 - Enter key pressed
            self.checkIfPasswordMatch()

    def checkIfPasswordMatch(self):
        pass1 = self.root.ids.password.text
        pass2 = self.root.ids.password2.text
        lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        z = False
        for x in self.root.ids.password.text:
            if x not in lst:
                z = True

        if z:
            self.root.ids.welcome_label.text = "Password can only contain:\na-z, A-Z, 0-9"

        elif len(pass1) > 15:
            self.root.ids.welcome_label.text = "Passwords are too long"
        elif pass1 == pass2:
            login_password_algoritem.savePasswordForgotPassoword(pass1, Email123)
            self.SavePassword()
        else:
            self.root.ids.welcome_label.text = "Passwords are not match"

    def SavePassword(self):
        NewPassword.get_running_app().stop()
        LoginScreen().run()

class Info(FloatLayout):
    pass


if __name__ == '__main__':

    try:
        with open(f'{path}/{getEmail()}/password.txt') as f:
            code_to_encrypt_with = f.read()
        password_for_encrypt3 = getEmail() + code_to_encrypt_with
    except:
        pass

    try:
        with open(f"{path}/username_remember.txt", "r") as f:
            Email = f.read()
        encrypt_files.decfile(rf"{path}/password_remember.txt", password_for_encrypt3)
        with open(f"{path}/password_remember.txt", "r") as f:
            Password = f.read()
        encrypt_files.encfile(rf"{path}/password_remember.txt", password_for_encrypt3)
    except:
        pass

    try:
        if readFile(rf"{path}/remember.txt") == "yes":
            if getEmail() != "" and login_password_algoritem.user_sign_in(Password, Email):
                Window.size = (1080, 720)
                MainScreen.AutoTask(Password).run()

            else:
                LoginScreen().run()
        else:
            LoginScreen().run()
    except:
        LoginScreen().run()
