import RPi.GPIO as GPIO
import tkinter as tk
from tkinter import ttk
import time

# Define Morse code mappings
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', ' ': '/'
}

# GPIO setup
LED_PIN = 10  # Replace with your GPIO pin number
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)

# Function to blink LED in Morse code
def blink_morse_code(name):
    for char in name.upper():
        if char in morse_code_dict:
            morse_code = morse_code_dict[char]
            for symbol in morse_code:
                if symbol == '.':
                    GPIO.output(LED_PIN, GPIO.HIGH)
                    time.sleep(0.2)  # Dot duration
                    GPIO.output(LED_PIN, GPIO.LOW)
                    time.sleep(0.2)  # Gap between dots and dashes
                elif symbol == '-':
                    GPIO.output(LED_PIN, GPIO.HIGH)
                    time.sleep(0.6)  # Dash duration
                    GPIO.output(LED_PIN, GPIO.LOW)
                    time.sleep(0.2)  # Gap between dots and dashes
            time.sleep(0.4)  # Gap between characters
        else:
            # Handle spaces and unknown characters
            time.sleep(0.8)  # Gap between words

# GUI setup
root = tk.Tk()
root.title("Name to Morse Code LED Blinker")

# Function to handle button click
def start_blinking():
    name = entry.get()
    blink_morse_code(name)

# Create a styled frame for the GUI with colorful background
frame = ttk.Frame(root, padding=(100, 100), style="My.TFrame")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

# Create and style label with a colorful font
label = ttk.Label(frame, text="Enter a name:", font=("Arial", 20), foreground="blue")
label.grid(column=0, row=0, columnspan=2, pady=(0, 20))

# Create and style entry widget with colorful background
entry = ttk.Entry(frame, width=20, font=("Arial", 20), background="lightyellow")
entry.grid(column=0, row=1, columnspan=2, pady=(0, 20))

# Create and style button with colorful background
button = ttk.Button(frame, text="Blink Name in Morse Code", command=start_blinking, style="TButton")
button.grid(column=0, row=2, columnspan=2, pady=(0, 20))

# Style for the button and frame
style = ttk.Style()
style.configure("TButton", background="green", foreground="white", font=("Arial", 20))
style.configure("My.TFrame", background="#F0F0F0")  # Light gray background

root.mainloop()

# Clean up GPIO
GPIO.cleanup()
