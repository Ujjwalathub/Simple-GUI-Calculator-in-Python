import tkinter as tk

# Function to update expression in the text entry box
def press(key):
    current = str(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, current + key)

# Function to evaluate the final expression
def evaluate():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to clear the text entry box
def clear():
    entry.delete(0, tk.END)

# Main window setup
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry widget to show calculations
entry = tk.Entry(root, font=('Arial', 20), borderwidth=2, relief="solid", justify='right')
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, padx=10, pady=10)

# Button layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+'),
]

# Create and place buttons
for i, row in enumerate(buttons):
    for j, btn in enumerate(row):
        if btn == '=':
            b = tk.Button(root, text=btn, width=5, height=2, font=('Arial', 18),
                          bg='lightgreen', command=evaluate)
        else:
            b = tk.Button(root, text=btn, width=5, height=2, font=('Arial', 18),
                          command=lambda key=btn: press(key))
        b.grid(row=i+1, column=j, padx=5, pady=5)

# Clear button
clear_btn = tk.Button(root, text='C', width=22, height=2, font=('Arial', 18),
                      bg='lightcoral', command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, padx=5, pady=10)

# Start the GUI loop
root.mainloop()
