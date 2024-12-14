import subprocess
from os import getenv
from dotenv import load_dotenv

# Funkcja do pobierania wideo z YouTube
def download_youtube(video_url, path):
    
    try:
        # Pobieranie wideo za pomocą yt-dlp
        subprocess.run([
            'yt-dlp',
            '-o', f'{path}/%(title)s.%(ext)s',  # Ścieżka zapisu
            video_url
        ], check=True)
        print("Pobieranie zakończone pomyślnie.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

# Pobranie ścieżki zapisu z pliku .env
load_dotenv()  # Wczytanie zmiennych z pliku .env
output_path = getenv('DOWNLOAD_PATH')  # Zmienna środowiskowa DOWNLOAD_PATH
print(f"Ścieżka zapisu: {output_path}")  # Dodaj ten wydruk, aby sprawdzić, co jest odczytywane
if output_path:
    download_youtube('https://www.youtube.com/watch?v=OabDZn1KYjc', output_path)
else:
    print("Ścieżka zapisu nie została zdefiniowana w pliku .env.")
