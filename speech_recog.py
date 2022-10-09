from speech_recognition import Microphone, Recognizer


def get_user_input(print_something=""):
    try:
        r = Recognizer()
        with Microphone() as source:
            print(print_something)
            audio = r.listen(source, 4, 4)
            try:
                user_input = r.recognize_google(audio)
                return user_input.lower()
            except:
                return "could not recognize your voice"
    except:
        return "could not recognize your voice"
