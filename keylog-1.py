# codeblock 1.0

# encoding=utf8
import pynput.keyboard
# import module to capture pressed keys

def process_key_press(key):
    print(key)
    # get the pressed key and print it

keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)
# created a listener for logging each key and passing it to process_key_press
with keyboard_listener:
    keyboard_listener.join()
    # start the listener to record keys