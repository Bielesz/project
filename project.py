from pynput import keyboard
from tkinter import Tk, Text, Label, Entry, messagebox
import time

errors = 0
all_letters = 0
current_character = 0
current_sentence = None
current_sentence_dict = None
sentence_count = -1
start_time = 0 

#This are the sentences which will be displayed in the program
sentences = [
    "Hello world",
    "My name is Mariusz",
    "This was CS50"
    ]

# This function shows stats and end of the program
def show_stats(total_time):
    words = sum([sentence.count(" ") + 1 for sentence in sentences])

    messagebox.showinfo("End of a game :(",
    f"""Number of characters: {all_letters}
    Typed words: {words}
    Time in seconds: {total_time:.2f}
    Words per minute (wpm): {int(words * 60 / total_time)}
    """)

# This function is used to display next sentences
def next_sentence():
    global current_sentence, current_character, current_sentence_dict, sentence_count

    sentence_count += 1 

    if sentence_count >= len(sentences):
        total_time = time.time() - start_time
        show_stats(total_time)
        return

    current_sentence = sentences[sentence_count]
    sentence_label.config(text = current_sentence)
    current_sentence_dict = dict(enumerate(current_sentence))
    current_character = 0
    user_entry.delete(0, "end")


# This function catches words that are not to be counted
def ignore(key):
    if key in (
        keyboard.Key.alt_l,
        keyboard.Key.alt_r,
        keyboard.Key.shift_l,
        keyboard.Key.shift_r,
        keyboard.Key.left,
        keyboard.Key.right):
        return True
    else:
        return False
    
def add_error():
    global errors

    errors += 1
    error_label.config(text = str(errors))

def add_to_all_letters():
    global all_letters, current_character

    all_letters += 1
    all_letters_label.config(text = str(all_letters))
    current_character += 1

# This is our main function. If the sentence's are identical, we get another one. 
# If they are not identical we add bugs to the UI
def on_press(key):
    global errors, all_letters, current_character, start_time

    if start_time == 0:
        start_time = time.time()

    try:
        if key == keyboard.Key.enter:
            if current_sentence == user_entry.get():
                next_sentence()
        elif key == keyboard.Key.backspace:
            if current_character > 0:
                current_character -= 1
                all_letters -= 1
                all_letters_label.config(text = str(all_letters))
            print(current_character)
        elif ignore(key):
             return
        else:
            if (key == keyboard.Key.space and current_sentence_dict[current_character] == ' ') or (current_sentence_dict[current_character] == key.char):
                pass
            else:
                add_error()

            add_to_all_letters()
    except (AttributeError, KeyError):
        add_to_all_letters()
        add_error()

# This is our user interface imported from tkinter libraries
root = Tk()
root.title("Fast typing")
root.geometry("800x400")

sentence_label = Label(root, text = current_sentence, width = 50, font=("Arial", 25))
sentence_label.pack()

user_entry = Entry(root, width = 50, font=("Arial", 25))
user_entry.pack()
user_entry.focus()

error_label = Label(root, text = "0", fg = "red", font=("Arial", 25))
error_label.pack()

all_letters_label = Label(root, text = "0", font=("Arial", 25))
all_letters_label.pack()

listener = keyboard.Listener(on_press=on_press)
listener.start()

next_sentence()

root.mainloop()