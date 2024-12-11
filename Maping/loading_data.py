def replay_events(events):
    from pynput.keyboard import Controller as KeyboardController
    from pynput.mouse import Controller as MouseController
    from pynput.keyboard import Key
    from pynput.mouse import Button
    import time

    keyboard = KeyboardController()
    mouse = MouseController()

    for event in events:
        if event['event'] == 'key_press':
            key = event['key']
            if key.startswith("Key."):
                special_key = getattr(Key, key.split('.')[1], None)
                if special_key:
                    keyboard.press(special_key)
            elif len(key) == 1:
                keyboard.press(key)
        elif event['event'] == 'key_release':
            key = event['key']
            if key.startswith("Key."):
                special_key = getattr(Key, key.split('.')[1], None)
                if special_key:
                    keyboard.release(special_key)
            elif len(key) == 1:
                keyboard.release(key)
        elif event['event'] == 'mouse_move':
            position = event['position']
            x, y = position['x'], position['y']
            mouse.position = (x, y)
        elif event['event'] == 'mouse_click':
            button = Button.left if event['button'] == "Button.left" else Button.right
            mouse.click(button, event.get('count', 1))
        time.sleep(0.1)