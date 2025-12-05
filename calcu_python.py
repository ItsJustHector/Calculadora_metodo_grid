import tkinter as tk

def on_click(value):
    current = entry.get()
    if value == "C":
        entry.delete(0, tk.END)
    elif value == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    else:
        entry.insert(tk.END, value)

def on_key(event):
    key = event.keysym

    if key in ["0","1","2","3","4","5","6","7","8","9",
               "KP_0","KP_1","KP_2","KP_3","KP_4",
               "KP_5","KP_6","KP_7","KP_8","KP_9"]:
        on_click(key[-1])
    elif key in ["plus", "KP_Add"]:
        on_click("+")
    elif key in ["minus", "KP_Subtract"]:
        on_click("-")
    elif key in ["asterisk", "KP_Multiply"]:
        on_click("*")
    elif key in ["slash", "KP_Divide"]:
        on_click("/")
    elif key in ["Return", "KP_Enter"]:
        on_click("=")
    elif key in ["Escape", "Delete"]:
        on_click("C")

root = tk.Tk()
root.title("Calculadora (grid)")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 18), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="we")

for col in range(4):
    root.grid_columnconfigure(col, weight=1)
root.grid_rowconfigure(0, weight=0)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", "C", "=", "+"
]

row_start = 1
for index, text in enumerate(buttons):
    r = row_start + index // 4
    c = index % 4
    btn = tk.Button(
        root,
        text=text,
        font=("Arial", 14),
        width=4,
        height=2,
        command=lambda v=text: on_click(v)
    )
    btn.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")

for r in range(1, 5):
    root.grid_rowconfigure(r, weight=1)

# Aquí enlazamos el teclado (incluye numpad)
root.bind("<Key>", on_key)

root.mainloop()