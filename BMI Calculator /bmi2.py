import tkinter as tk
from tkinter import ttk

def calculate_bmi():
    try:
       
        category_result.set("")

        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive values.")

        bmi = weight / (height ** 2)
        bmi_result.set(f"BMI: {bmi:.2f}")
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal Weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        category_result.set(f"Category: {category}")

    except ValueError as e:
        bmi_result.set("Invalid input. Please enter valid numbers.")
# Create main window
root = tk.Tk()
root.title("BMI Calculator")

# Label and entry for weight
weight_label = ttk.Label(root, text="Weight (kg):")
weight_label.grid(row=0, column=0, padx=10, pady=10)
weight_entry = ttk.Entry(root)
weight_entry.grid(row=0, column=1, padx=10, pady=10)

# Label and entry for height
height_label = ttk.Label(root, text="Height (m):")
height_label.grid(row=1, column=0, padx=10, pady=10)
height_entry = ttk.Entry(root)
height_entry.grid(row=1, column=1, padx=10, pady=10)

# Button to calculate BMI
calculate_button = ttk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

# Labels to display BMI result and category
bmi_result = tk.StringVar()
bmi_label = ttk.Label(root, textvariable=bmi_result)
bmi_label.grid(row=3, column=0, columnspan=2, pady=10)

category_result = tk.StringVar()
category_label = ttk.Label(root, textvariable=category_result)
category_label.grid(row=4, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()
