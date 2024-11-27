from monitoring import on_click, on_press
import json

def saving_on_click(on_click):
    data = {}
    with open('path.json', 'w') as file:
        json.dump(data, file)