from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
from pynput import keyboard
import json
from datetime import datetime

running = True  # Flaga działania
events = []  # Lista do przechowywania zdarzeń

# Funkcja zapisu do pliku JSON
def save_to_file(filename="events.json"):
    with open(filename, "w") as file:
        json.dump(events, file, indent=4)
    print(f"Zapisano zdarzenia do pliku {filename}")

# Funkcje nasłuchujące zdarzenia myszy
def on_move(x, y):
    event = {
        "time": datetime.now().isoformat(),
        "event": "mouse_move",
        "position": {"x": x, "y": y}
    }
    print(f"position{x, y}")
    events.append(event)

def on_click(x, y, button, pressed):
    event = {
        "time": datetime.now().isoformat(),
        "event": "mouse_click",
        "position": {"x": x, "y": y},
        "button": str(button),
        "pressed": pressed
        
    }
    print(button)
    events.append(event)
    
    if not running:
        return False

# Funkcje nasłuchujące zdarzenia klawiatury
def on_press(key):
    try:
        event = {
            "time": datetime.now().isoformat(),
            "event": "key_press",
            "key": key.char
        }
        print(f'Normalny klawisz wcisniety: {key.char}')
    except AttributeError:
        event = {
            "time": datetime.now().isoformat(),
            "event": "key_press",
            "key": str(key)
        }
        print(f'Specjalny klawisz wcisniety: {key}')
    events.append(event)

def on_release(key):
    global running
    event = {
        "time": datetime.now().isoformat(),
        "event": "key_release",
        "key": str(key)
    }
    events.append(event)
    
    if key == keyboard.Key.esc:
        print("Zatrzymuję nasłuchiwacz...")
        running = False
        save_to_file()  # Zapisz dane przed zatrzymaniem
        return False

# Uruchomienie nasłuchiwania
mouse_listener = MouseListener(on_move=on_move, on_click=on_click)
keyboard_listener = KeyboardListener(on_press=on_press, on_release=on_release)

mouse_listener.start()
keyboard_listener.start()

print('Zaczynam nasłuchiwać... Naciśnij ESC, aby zatrzymać.')

mouse_listener.join()
keyboard_listener.join()

