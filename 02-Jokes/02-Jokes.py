import tkinter as tk
import random # I planned on implementing random to 01-Math Quiz as well. But I have already uploaded it to github

# Load jokes from file
def load_jokes():
    jokes = []
    try:
        with open(r"C:\Users\Lenovo\Documents\02-Jokes\randomJokes.txt", "r", encoding="utf-8") as f:
            for line in f:
                if "?" in line:
                    setup, punchline = line.strip().split("?", 1)
                    jokes.append((setup + "?", punchline))
    except FileNotFoundError:
        print("randomJokes.txt not found!")
    return jokes

# Check user input for "Alexa tell me a joke"
def check_input(event=None):
    user_text = user_entry.get().strip().lower()
    if user_text == "alexa tell me a joke":
        show_joke()
    else:
        setup_label.config(text="Type exactly: Alexa tell me a joke")
        punchline_label.config(text="")

# Show a random joke setup
def show_joke():
    global current_joke
    current_joke = random.choice(jokes)
    setup_label.config(text=current_joke[0])
    punchline_label.config(text="")
    punch_btn.config(state="normal")
    user_entry.delete(0, tk.END)

# Show the punchline
def show_punchline(event=None):
    punchline_label.config(text=current_joke[1])
    punch_btn.config(state="disabled")

root = tk.Tk()
root.title("Alexa Joke Teller")
root.geometry("450x300")
root.resizable(False, False)

jokes = load_jokes()
current_joke = ("", "")

tk.Label(root, text="Type 'Alexa tell me a joke' and press Enter", font=("Arial", 12)).pack(pady=5)

user_entry = tk.Entry(root, width=40, font=("Arial", 12))
user_entry.pack(pady=5)
user_entry.bind("<Return>", check_input)  # Enter key triggers check_input

setup_label = tk.Label(root, text="", wraplength=400, font=("Arial", 12))
setup_label.pack(pady=15)

punchline_label = tk.Label(root, text="", wraplength=400, fg="blue", font=("Arial", 12, "italic"))
punchline_label.pack(pady=10)

punch_btn = tk.Button(root, text="Show punchline", command=show_punchline, state="disabled")
punch_btn.pack(pady=5)

tk.Button(root, text="Quit", command=root.destroy, fg="red").pack(pady=5)

root.mainloop()
