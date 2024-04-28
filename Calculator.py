import tkinter as tk

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

def clear_display():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create the display entry
entry = tk.Entry(root, width=20, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Create buttons
for (text, row, column) in buttons:
    button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14),
                       command=lambda t=text: button_click(t))
    button.grid(row=row, column=column, padx=5, pady=5)

# Clear button
clear_button = tk.Button(root, text="C", width=5, height=2, font=('Arial', 14), command=clear_display)
clear_button.grid(row=5, column=0, padx=5, pady=5)

# Calculate button
calc_button = tk.Button(root, text="=", width=5, height=2, font=('Arial', 14), command=calculate)
calc_button.grid(row=5, column=1, padx=5, pady=5)

# Run the main loop
root.mainloop()
