import tkinter as tk
from tkinter import messagebox

def calculate():
    # Perform the selected arithmetic operation and display the result.
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero!")
            result = num1 / num2
        else:
            raise ValueError("Invalid operation selected.")

        result_label.config(text=f"Result: {result:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
    except ZeroDivisionError as e:
        messagebox.showerror("Math Error", str(e))

# Initialize Tkinter window
root = tk.Tk()
root.title("Interactive Calculator")

# Input fields
tk.Label(root, text="Enter first number:").grid(row=0, column=0, padx=10, pady=10)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter second number:").grid(row=1, column=0, padx=10, pady=10)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)

# Operation selection
tk.Label(root, text="Select Operation:").grid(row=2, column=0, padx=10, pady=10)
operation_var = tk.StringVar(value="Addition")  # Default value
operations_menu = tk.OptionMenu(root, operation_var, "Addition", "Subtraction", "Multiplication", "Division")
operations_menu.grid(row=2, column=1, padx=10, pady=10)

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Result label
result_label = tk.Label(root, text="Result: ", font=("Arial", 14))
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()
