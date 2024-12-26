import tkinter as tk
import os
import subprocess

# Function to run system commands
def run_command():
    command = command_entry.get()
    if command.strip():  # Check if the command is not empty
        try:
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            output, error = process.communicate()
            output = output.decode("utf-8")
            error = error.decode("utf-8")
            console.insert(tk.END, output + error)  # Show both output and error
        except Exception as e:
            console.insert(tk.END, f"Error: {str(e)}\n")

# Function to handle login
def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == "admin" and password == "admin":
        top.destroy()  # Close the login window
        open_system_window()  # Open the system window
    else:
        incorrect()

# Function to show incorrect login message
def incorrect():
    incorrect_label = tk.Label(top, text="Incorrect username or password", fg="red")
    incorrect_label.pack()

# Function to open the system window
def open_system_window():
    program = tk.Tk()
    program.geometry("1000x500")
    program.title("System")

    # Label for system online
    label = tk.Label(program, text="System online", font=("Arial", 20))
    label.pack()

    # Entry for command input
    global command_entry
    command_entry = tk.Entry(program)
    command_entry.pack(pady=10)

    # Button to run command
    run_button = tk.Button(program, text="Run command", command=run_command)
    run_button.pack(pady=10)

    # Bind Enter key to run command
    program.bind('<Return>', lambda event: run_command())

    # Text widget for command output
    global console
    console = tk.Text(program)
    console.pack(expand=True, fill='both')

    program.mainloop()

# Create the login window
top = tk.Tk()
top.geometry("250x250")
top.title("Login system")

# Widgets in the login window
label = tk.Label(top, text="Login system", font=("Arial", 20))
label.pack()

username_label = tk.Label(top, text="Username")
username_label.pack()

username_entry = tk.Entry(top)
username_entry.pack()

password_label = tk.Label(top, text="Password")
password_label.pack()

password_entry = tk.Entry(top, show="*")
password_entry.pack()

# Login button
login_button = tk.Button(top, text="Login", command=login)
login_button.pack(pady=10)

# Bind Enter key to login
top.bind('<Return>', lambda event: login())

top.mainloop()