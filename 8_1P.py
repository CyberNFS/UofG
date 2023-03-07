import tkinter as tk


def print_message():
    """Function to print message on button click"""
    message = "Welcome to Tkinter, {}!".format(name.get())
    message_window = tk.Toplevel(root)
    message_window.title("Message")
    tk.Label(message_window, text=message, bg="white").pack(pady=10)
    tk.Button(message_window, text="Quit", command=message_window.destroy,
              bg="white", activebackground="white").pack(pady=5)


def quit_app():
    """Function to quit the application"""
    root.destroy()


root = tk.Tk()
root.title("Welcome to Tkinter!")
root.geometry("300x200")
root.configure(bg="white")

# Label and Entry widgets for name input
name_label = tk.Label(root, text="Enter your name:", bg="white")
name_label.pack(pady=10)
name = tk.Entry(root, bg="white")
name.pack(pady=5)

# Button to print message
tk.Button(root, text="Print Message",
          command=print_message, bg="white").pack(pady=10)

# Button to quit application
tk.Button(root, text="Quit", command=quit_app, bg="white",
          activebackground="white").pack(pady=5)

root.mainloop()


# Address entry form ––––––––––––––––––––––––––––––––––––––––––––––>

import tkinter as tk


def submit_address():
    """Function to submit address on button click"""
    message = "{} {}\n{}\n{} {} {}\n{}".format(first_name.get(), last_name.get(), address.get(),
                                               city.get(), state.get(), post_code.get(), country.get())
    message_window = tk.Toplevel(root)
    message_window.title("Address")
    message_window.geometry(
        "+{}+{}".format(root.winfo_x() + 50, root.winfo_y() + 50))
    message_window.configure(bg="white")

    # Create labels and buttons in grid layout
    tk.Label(message_window, text="Form", font=("Arial", 14),
             bg="white").grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    tk.Label(message_window, text=message, bg="white").grid(
        row=1, column=0, columnspan=2, padx=10, pady=10)
    tk.Button(message_window, text="OK", command=message_window.destroy, bg="#4CAF50",
              font=("Arial", 12)).grid(row=2, column=0, columnspan=2, pady=10)

    # Resize the window to fit the widgets
    message_window.update_idletasks()
    width = message_window.winfo_width()
    height = message_window.winfo_height()
    message_window.geometry(
        "{}x{}+{}+{}".format(width, height, root.winfo_x() + 50, root.winfo_y() + 50))

    # Clear the inputs
    first_name.set("")
    last_name.set("")
    address.set("")
    city.set("")
    state.set("")
    post_code.set("")
    country.set("")


def clear_inputs():
    """Function to clear all inputs"""
    for entry in entries:
        entry.delete(0, tk.END)


def quit_app():
    """Function to quit the application"""
    root.destroy()


root = tk.Tk()
root.title("Address Entry")
root.geometry("400x300")
root.configure(bg="white")

# Labels and Entry widgets for address input
fields = ["First Name", "Last Name", "Address",
          "City", "State", "Post Code", "Country"]
entries = []
first_name = tk.StringVar()
last_name = tk.StringVar()
address = tk.StringVar()
city = tk.StringVar()
state = tk.StringVar()
post_code = tk.StringVar()
country = tk.StringVar()

for i, field in enumerate(fields):
    label = tk.Label(root, text=field, bg="white")
    label.grid(row=i, column=0, padx=5, pady=5, sticky="W")
    entry = tk.Entry(root, textvariable=eval(
        field.replace(" ", "_").lower()), bg="white")
    entry.grid(row=i, column=1, padx=5, pady=5)
    entries.append(entry)

# Button to submit address
tk.Button(root, text="Submit", command=submit_address, bg="blue",
          font=("Arial", 12)).grid(row=len(fields), column=0, pady=10)

# Button to clear inputs
tk.Button(root, text="Clear", command=clear_inputs, bg="white",
          font=("Arial", 12)).grid(row=len(fields), column=1, pady=10)

# Button to quit application
tk.Button(root, text="Quit", command=quit_app, bg="white", activebackground="white", font=(
    "Arial", 12)).grid(row=len(fields), column=0, columnspan=2, pady=10)

root.mainloop()
