from pynput import keyboard

with keyboard.Events() as events:
    for event in events:
        if event.key == keyboard.Key.esc:
            break
        else:
            print(" You {}".format(event))