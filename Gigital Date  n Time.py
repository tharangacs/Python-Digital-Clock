import tkinter as tk
from time import strftime

# Function to update date and time
def update_time():
    current_time = strftime("%H:%M:%S %p")  # Format: HH:MM:SS AM/PM
    current_date = strftime("%A, %d %B %Y")  # Format: Day, DD Month YYYY
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    time_label.after(1000, update_time)  # Update every second

# Creating the GUI window
root = tk.Tk()
root.title("Digital Clock with Date & Time")
root.geometry("400x200")
root.config(bg="black")

# Date Label
date_label = tk.Label(root, font=("Arial", 16, "bold"), bg="black", fg="white")
date_label.pack(pady=10)

# Time Label
time_label = tk.Label(root, font=("Arial", 40, "bold"), bg="black", fg="cyan")
time_label.pack(pady=10)

# Start updating time
update_time()

# Run the GUI application
root.mainloop()
