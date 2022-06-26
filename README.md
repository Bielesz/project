# Fast typing
#### Video Demo:  <https://www.youtube.com/watch?v=pp7IxrKKRXE>
#### Description: Fast typing is an app which improves our typing speed.

#### libraries
To write this program we used three libraries

This library is used for tracing user input.
[pynput](https://pynput.readthedocs.io/en/latest/keyboard.html)

tkinter is used to create graphical user interface, GUI.

[tkinter](https://realpython.com/python-gui-tkinter/)

time library helps us measure time from the first user input.
[time](https://docs.python.org/3/library/time.html)

###### About
Fast typing is a python application with a simple GUI. Which track the user keyboard input displays the number of typos, measures the number of characters, words, time and the number of words per minute.

First step we import all the libraries we use in this project.

Next, we set the variables and their values that are used in whole app.

Then we create a python list that stores the sentences that are displayed to the user.

show_stats function shows stats and end of the program.

def next_sentence() is used to display next sentences.

We use the ignore function so that the application does not add special characters to our variables like: alt, shify etc.

on_press this is our main function which track keyboard input. If the sentence's are identical, we get another one.  If they are not identical we add error's to the UI.

The last prat are the graphical user interface settings from tkinter libraries.

