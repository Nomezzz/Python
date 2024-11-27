from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
from pynput import keyboard

running = True  # Flaga działania

def on_move(x, y):
    print(f"Mysz przesunięta na pozycję: ({x}, {y})")

def on_click(x, y, button, pressed):
    global running
    if pressed:
     print(f"Naciśnięto {button} w pozycji ({x}, {y})")
    if not running:
        return False  # Zatrzymanie Listener
def on_press(key):
    try:
        print('Nacisnieto przycisk {0} '.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    global running
    print('{0} zwolniono'.format(
        key))
    if key == keyboard.Key.esc:
        print('Zatzymywanie nagrywania')
        # Stop listener
        running = False
        return False


mouse_listener = MouseListener(on_click=on_click)
keybort_listener = KeyboardListener(on_press=on_press, on_release=on_release)

mouse_listener.start()
keybort_listener.start()

mouse_listener.join()
keybort_listener.join()