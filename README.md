# Fast typing
#### Video Demo:  <https://www.youtube.com/watch?v=pp7IxrKKRXE>
#### Description: Fast typing is an app which improves our typing speed.

#### libraries

To write this program we used three libraries:

<ul>
  <li>[pynput](https://pynput.readthedocs.io/en/latest/keyboard.html)</li>
  <li>[tkinter](https://realpython.com/python-gui-tkinter/)</li>
  <li>[time](https://docs.python.org/3/library/time.html)</li>
</ul>

 <em><strong>pynput</strong></em>
The pynput library allows you to control and monitor/listen to your input devices such as they keyboard and mouse. The pynput. mouse allows you control and monitor the mouse, while the pynput. keyboard allows you to control and monitor the keyboard.

<em><strong>tkinter</strong></em>
Python has a lot of GUI frameworks, but Tkinter is the only framework that’s built into the Python standard library. Tkinter has several strengths. It’s cross-platform, so the same code works on Windows, macOS, and Linux. Visual elements are rendered using native operating system elements, so applications built with Tkinter look like they belong on the platform where they’re run.

<em><strong>time</strong></em>
Time tracking is critical to managing your projects. If you’re programming in Python, you’re in luck: The language gives you tools to build your own timers. A timer program can be useful for not only monitoring your own time, but measuring how long your Python program takes to run


#### About

Fast typing is a python application with a simple GUI. Which track the user keyboard input displays the number of typos, measures the number of characters, words, time and the number of words per minute.
First step we import all the libraries we use in this project.
I chose the pynput which helped me track the user's input.
I used a tkinter to create a simple graphical user interface.
I think it is a very user-friendly library for new users which I recommend for new developers.
Library time helps us measure the time the user needs to enter all sentences.
It has been programmed to start timing only when the user presses the first key.

Next, we set the variables and their values that are used in whole app.
<ol>
  <li><em>errors = 0</em></li>
  <li><em>all_letters = 0</em></li>
  <li><em>current_character = 0</em></li>
  <li><em>current_sentence = None</em></li>
  <li><em>current_sentence_dict = None</em></li>
  <li><em>sentence_count = -1</em></li>
  <li><em>start_time = 0 </em></li>
</ol>

Then we create a python list that stores the sentences that are displayed to the user.
<ol>
  <li><em>Hello world</em></li>
  <li><em>My name is Mariusz</em></li>
  <li><em>This was CS50</em></li>
</ol>
You can easily add more words to the list. The program is designed so that it automatically counts the words so it will know when you type the last sentence. Remember that each sentence should be separated by "," this little error cost me a lot of time

show_stats function shows stats and end of the program 
It's use a <em>messagebox<em> feature from the tkinter libraries.
It is displayed only after entering the last sentence correctly.
As long as all characters in both sentences are identical, remember that the letters are case sensitive
def next_sentence() is used to display next sentences.
We use the ignore function so that the application does not add special characters to our variables like: alt, shify etc.
on_press this is our main function which track keyboard input. If the sentence's are identical, we get another one.  If they are not identical we add error's to the UI.
The last prat are the graphical user interface settings from tkinter libraries.

