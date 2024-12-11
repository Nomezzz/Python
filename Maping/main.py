from monitoring import save_to_file, on_click, on_move, on_press, on_release
from loading_data import replay_events
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
import threading
import json
from monitoring import start_mapping


def mapowanie():
    """Funkcja mapowania działa dopiero po wyborze w menu."""
    mouse_listener = MouseListener(on_move=on_move, on_click=on_click)
    keyboard_listener = KeyboardListener(on_press=on_press, on_release=on_release)
    mouse_listener.start()
    keyboard_listener.start()
    print('Zaczynam nasłuchiwać... Naciśnij ESC, aby zatrzymać.')
    mouse_listener.join()
    keyboard_listener.join()
    save_to_file('events.json')
    print("Zakończono mapowanie i zapisano dane do 'events.json'.")


def menu():
    while True:
        print("Witaj! Wybierz opcję:")
        print("1 - Zacznij mapowanie akcji")
        print("2 - Odtwórz zapisane zdarzenia")
        print("3 - Zakończ program")
        choice = input("> ")

        if choice == "1":
            start_mapping()
        elif choice == "2":
            try:
                with open("events.json", "r") as file:
                    events = json.load(file)
                replay_events(events)
            except FileNotFoundError:
                print("Nie znaleziono pliku 'events.json'.")
            except json.JSONDecodeError:
                print("Plik 'events.json' jest uszkodzony lub pusty.")
        elif choice == "3":
            print("Zamykanie programu...")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

if __name__ == '__main__':
    menu()
