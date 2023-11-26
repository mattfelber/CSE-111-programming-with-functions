import tkinter as tk
import random

def validate_inputs():
    try:
        tests_per_month = int(tests_per_month_entry.get())
        calibrations_per_month = int(calibrations_per_month_entry.get())
        instruments = int(instruments_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for tests, calibrations, and instruments.")
        return False
    return True

def calculate_gas_usage():
    result = random.randint(0, 10)
    return result

def display_result():
    gas_type = gas_type_listbox.get(tk.ACTIVE)
    tests_per_month = int(tests_per_month_entry.get())
    calibrations_per_month = int(calibrations_per_month_entry.get())
    instruments = int(instruments_entry.get())

    gas_usage_liters = calculate_gas_usage()

    result_text = f"Gas Type: {gas_type}\n" \
                  f"Tests per Month: {tests_per_month}\n" \
                  f"Calibrations per Month: {calibrations_per_month}\n" \
                  f"Instruments: {instruments}\n" \
                  f"Gas Usage (liters): {gas_usage_liters:.2f}"

    result_frame = tk.Toplevel(root)
    result_frame.title("Gas Usage Result")

    result_label = tk.Label(result_frame, text=result_text, justify=tk.LEFT)
    result_label.pack(padx=20, pady=20)


root = tk.Tk()
root.title("Gas Usage Calculator")

input_frame = tk.Frame(root)
input_frame.pack(padx=20, pady=20)


# Gas Type Input with Scrollbar
gas_type_label = tk.Label(input_frame, text="Gas Type:")
gas_type_label.grid(row=0, column=0, padx=5, pady=5)

gas_type_scrollbar = tk.Scrollbar(input_frame, orient=tk.VERTICAL)
gas_type_listbox = tk.Listbox(input_frame, yscrollcommand=gas_type_scrollbar.set, height=5)

gas_types = ["Gas Type " + str(i) for i in range(1, 23)]  # Replace this with your gas type names
for gas in gas_types:
    gas_type_listbox.insert(tk.END, gas)

gas_type_listbox.grid(row=0, column=1, padx=5, pady=5)
gas_type_scrollbar.grid(row=0, column=2, padx=5, pady=5, sticky=tk.NS)
gas_type_scrollbar.config(command=gas_type_listbox.yview)

# Tests per Month Input
tests_per_month_label = tk.Label(input_frame, text="Tests per Month:")
tests_per_month_label.grid(row=1, column=0, padx=5, pady=5)
tests_per_month_entry = tk.Entry(input_frame)
tests_per_month_entry.grid(row=1, column=1, padx=5, pady=5)

# Calibrations per Month Input
calibrations_per_month_label = tk.Label(input_frame, text="Calibrations per Month:")
calibrations_per_month_label.grid(row=2, column=0, padx=5, pady=5)
calibrations_per_month_entry = tk.Entry(input_frame)
calibrations_per_month_entry.grid(row=2, column=1, padx=5, pady=5)

# Instruments Input
instruments_label = tk.Label(input_frame, text="Instruments:")
instruments_label.grid(row=3, column=0, padx=5, pady=5)
instruments_entry = tk.Entry(input_frame)
instruments_entry.grid(row=3, column=1, padx=5, pady=5)

# Submit Button
submit_button = tk.Button(input_frame, text="Calculate Gas Usage", command=lambda: validate_inputs() and display_result())
submit_button.grid(row=4, columnspan=2, padx=5, pady=10)

root.mainloop()