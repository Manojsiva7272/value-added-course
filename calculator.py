import tkinter as tk

# Function to update the expression in the entry box
def update_expression(value):
    current_expression = expression_entry.get()
    expression_entry.delete(0, tk.END)
    expression_entry.insert(0, current_expression + value)

# Function to evaluate the expression
def evaluate_expression():
    try:
        current_expression = expression_entry.get()
        result = eval(current_expression)
        expression_entry.delete(0, tk.END)
        expression_entry.insert(0, str(result))
    except Exception as e:
        expression_entry.delete(0, tk.END)
        expression_entry.insert(0, "Error")

# Function to clear the entry box
def clear_expression():
    expression_entry.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Create an entry widget for the expression
expression_entry = tk.Entry(window, width=20, font=('Arial', 18), bd=10, insertwidth=2)
expression_entry.grid(row=0, column=0, columnspan=4)

# Create buttons for the calculator
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Add buttons to the window
for (text, row, col) in buttons:
    button = tk.Button(window, text=text, padx=20, pady=20, font=('Arial', 18),
                       command=lambda t=text: update_expression(t) if t != '=' else evaluate_expression())
    button.grid(row=row, column=col)

# Add clear button
clear_button = tk.Button(window, text='C', padx=20, pady=20, font=('Arial', 18), command=clear_expression)
clear_button.grid(row=4, column=2)

# Run the main loop
window.mainloop()
