import tkinter as tk
from tkinter import ttk, messagebox

# Function to convert temperatures
def convert_temperature():
    try:
        temp = float(entry_temperature.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()

        if from_unit == to_unit:
            result = temp
        elif from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                result = (temp * 9/5) + 32
            elif to_unit == "Kelvin":
                result = temp + 273.15
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                result = (temp - 32) * 5/9
            elif to_unit == "Kelvin":
                result = (temp - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                result = temp - 273.15
            elif to_unit == "Fahrenheit":
                result = (temp - 273.15) * 9/5 + 32

        label_result.config(text=f"Result: {result:.2f} {to_unit}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Create main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x250")
root.resizable(False, False)

# Input temperature
tk.Label(root, text="Enter Temperature:").pack(pady=5)
entry_temperature = tk.Entry(root, width=20)
entry_temperature.pack()

# From unit
tk.Label(root, text="From:").pack(pady=5)
combo_from = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
combo_from.pack()
combo_from.current(0)

# To unit
tk.Label(root, text="To:").pack(pady=5)
combo_to = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
combo_to.pack()
combo_to.current(1)

# Convert button
tk.Button(root, text="Convert", command=convert_temperature, bg="lightblue").pack(pady=10)

# Result label
label_result = tk.Label(root, text="Result: ", font=("Arial", 14))
label_result.pack(pady=10)

root.mainloop()
