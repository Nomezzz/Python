import json
from pynput.keyboard import Controller as KeyboardController
from pynput.mouse import Controller as MouseController
from pynput.keyboard import Key, KeyCode
from pynput.mouse import Button
import time

keyboard = KeyboardController()
mouse = MouseController()

from pynput.keyboard import Key, KeyCode

def replay_events(events):
    for event in events:
        if event['event'] == 'key_press':
            key = event['key']
            if key.startswith("Key."):  # Klawisze specjalne
                special_key = getattr(Key, key.split('.')[1], None)
                if special_key:
                    keyboard.press(special_key)
            elif len(key) == 1:  # Zwykłe klawisze (np. 'a', 'b', '1')
                keyboard.press(key)
        elif event['event'] == 'key_release':
            key = event['key']
            if key.startswith("Key."):  # Klawisze specjalne
                special_key = getattr(Key, key.split('.')[1], None)
                if special_key:
                    keyboard.release(special_key)
            elif len(key) == 1:  # Zwykłe klawisze
                keyboard.release(key)
        elif event['event'] == 'mouse_move':
            position = event['position']
            x, y = position['x'], position['y']
            mouse.position = (x, y)
        elif event['event'] == 'mouse_click':
            button = Button.left if event['button'] == "Button.left" else Button.right
            mouse.click(button, event.get('count', 1))
        time.sleep(0.1)  # Symulacja opóźnienia

# Wczytaj dane z pliku
try:
    with open("events.json", "r") as file:
        events = json.load(file)
    
    # Wywołaj funkcję replay_events z wczytanymi zdarzeniami
    replay_events(events)

except FileNotFoundError:
    print("Nie znaleziono pliku 'events.json'. Upewnij się, że dane są zapisane.")
except json.JSONDecodeError:
    print("Plik 'events.json' jest uszkodzony lub pusty.")
