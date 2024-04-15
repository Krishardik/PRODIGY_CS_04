# PRODIGY_CS_04

---

# WiZeySenitl

WiZeySenitl is a basic keylogger tool developed to capture keyboard inputs. This tool was created as part of my internship project to explore Python programming for cybersecurity-related tools.

## Overview

The provided Python script implements a keylogger using the pynput library. It captures keyboard inputs and writes them into a log file. Let's break down its functionality:

### Importing Libraries

The script imports the pynput.keyboard module for capturing keyboard inputs, pyfiglet for generating ASCII art, and colorama for colored output. `colorama.init(autoreset=True)` is used to automatically reset color settings after each print statement.

### Displaying Name

The `display_name()` function generates ASCII art for the name "WiZeySenitl" using pyfiglet and prints it in yellow color.

### Keylogger Functions

The script includes two functions to handle key events:
- **`on_press(key)`:** Writes the pressed key into a log file.
- **`on_release(key)`:** Stops the keylogger when the escape key (Key.esc) is pressed.

### Main Function

The main functionality of the script starts the keylogger and listens for key events using pynput.keyboard.Listener. It continues capturing keyboard inputs until the escape key is pressed.

### Execution

The script can be executed by running the `WiZzzeySenitel.py` file. It runs in the background and captures keyboard inputs without any visible interface.

## Usage

### Steps to Run the Tool

1. Clone the repository:
   ```
   git clone https://github.com/Krishardik/PRODIGY_CS_04
   ```

2. Navigate to the project directory:
   ```
   cd PRODIGY_CS_04
   ```

3. Run the script:
   ```
   python WiZzzeySenitel.py
   ```

4. To stop the keylogger, press the escape key (Key.esc).

## Note

- Use this tool responsibly and ethically. Ensure that you have appropriate permissions before capturing keyboard inputs.
- Be cautious when handling sensitive information and respect user privacy.
