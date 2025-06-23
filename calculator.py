import tkinter as tk
from math import *

# --- Setup Window ---
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x600")
root.configure(bg="#0f172a")
root.resizable(False, False)

# --- Global Expression ---
expression = ""
input_text = tk.StringVar()

# --- Entry Display Field ---
entry_frame = tk.Frame(root, bg="#0f172a")
entry_frame.pack(fill="x", padx=(10, 30), pady=(15, 10))

entry = tk.Entry(
    entry_frame,
    font=("Segoe UI", 24, "bold"),
    textvariable=input_text,
    bd=2,
    bg="#0f172a",
    fg="#ffffff",
    insertbackground="#38bdf8",
    justify="right",
    relief="ridge",
    highlightcolor="#38bdf8",
    highlightthickness=1
)
entry.pack(fill="x", ipady=15)

# --- Button Functions ---
def click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

def clear():
    global expression
    expression = ""
    input_text.set("")

def delete():
    global expression
    expression = expression[:-1]
    input_text.set(expression)

def evaluate():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

def scientific_function(func):
    global expression
    try:
        result = str(eval(f"{func}({expression})"))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

# --- Buttons Layout ---
btns_frame = tk.Frame(root, bg="#0f172a")
btns_frame.pack(expand=True, fill="both", padx=(10, 10))

buttons = [
    ["sin", "cos", "tan", "log"],
    ["√", "x²", "xʸ", "fact"],
    ["(", ")", "C", "⌫"],
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

def create_button(text, row, col):
    def on_click():
        if text == "=":
            evaluate()
        elif text == "C":
            clear()
        elif text == "⌫":
            delete()
        elif text == "√":
            scientific_function("sqrt")
        elif text == "x²":
            global expression
            expression = f"({expression})**2"
            input_text.set(expression)
        elif text == "xʸ":
            expression += "**"
            input_text.set(expression)
        elif text == "fact":
            scientific_function("factorial")
        elif text in ["sin", "cos", "tan", "log"]:
            scientific_function(text)
        else:
            click(text)

    btn = tk.Button(
        btns_frame,
        text=text,
        font=("Segoe UI", 16, "bold"),
        fg="#38bdf8",
        bg="#1e293b",
        activebackground="#334155",
        activeforeground="#38bdf8",
        bd=0,
        relief="flat",
        command=on_click
    )
    btn.grid(row=row, column=col, sticky="nsew", padx=4, pady=4, ipadx=5, ipady=12)

# Configure rows & columns
for i in range(len(buttons)):
    btns_frame.rowconfigure(i, weight=1)
    for j in range(len(buttons[i])):
        btns_frame.columnconfigure(j, weight=1)
        create_button(buttons[i][j], i, j)

# --- Run the App ---
root.mainloop()
