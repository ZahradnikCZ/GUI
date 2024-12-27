import tkinter as tk
import subprocess

# Dictionary to store user credentials
user_credentials = {
    "admin": "admin"
}

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
    
    if username in user_credentials and user_credentials[username] == password:
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
    program.geometry("600x400")
    program.title("System")

    # Label for system online
    label = tk.Label(program, text="System online", font=("Arial", 20))
    label.pack()

    # Entry for command input
    global command_entry
    command_entry = tk.Entry(program)
    command_entry.pack(pady=10)

    # Button to run command
    run_button = tk.Button(program, text="Run Command", command=run_command)
    run_button.pack(pady=10)

    # Frame for user management buttons
    user_frame = tk.Frame(program)
    user_frame.pack(pady=10)

    # Button to add new user
    add_user_button = tk.Button(user_frame, text="Add User", command=useraddd)
    add_user_button.pack(side=tk.LEFT, padx=5)

    # Button to remove user
    remove_user_button = tk.Button(user_frame, text="Remove User", command=manage_users)
    remove_user_button.pack(side=tk.LEFT, padx=5)

    # Exit button to close the application
    exit_button = tk.Button(user_frame, text="Exit", command=program.destroy)
    exit_button.pack(side=tk.LEFT, padx=5)

    # Bind Enter key to run command
    program.bind('<Return>', lambda event: run_command())

    # Text widget for command output
    global console
    console = tk.Text(program)
    console.pack(expand=True, fill='both')

    program.mainloop()

def useraddd():
    useradd = tk.Tk()
    useradd.geometry("300x200")
    useradd.title("Add New User")

    # Widgets in the add user window
    label = tk.Label(useradd, text="Add New User", font=("Arial", 16))
    label.pack()

    username_label = tk.Label(useradd, text="Username")
    username_label.pack()

    username_entry = tk.Entry(useradd)
    username_entry.pack()

    password_label = tk.Label(useradd, text="Password")
    password_label.pack()

    password_entry = tk.Entry(useradd, show="*")
    password_entry.pack()

    # Label for displaying messages
    message_label = tk.Label(useradd, text="", fg="red")
    message_label.pack()

    # OK button to add the user
    ok_button = tk.Button(useradd, text="OK", command=lambda: add(username_entry.get(), password_entry.get(), message_label))
    ok_button.pack(side=tk.LEFT, padx=10, pady=10)

    # Exit button to close the window
    exit_button = tk.Button(useradd, text="Exit", command=useradd.destroy)
    exit_button.pack(side=tk.RIGHT, padx=10, pady=10)

    # Bind Enter key to OK button
    useradd.bind('<Return>', lambda event: add(username_entry.get(), password_entry.get(), message_label))

def add(usernameadd, passwordadd, message_label):
    if usernameadd and passwordadd:  # Check if both fields are filled
        if usernameadd in user_credentials:
            message_label.config(text=f"User   '{usernameadd}' already exists.", fg="red")
        else:
            user_credentials[usernameadd] = passwordadd
            message_label.config(text=f"User   '{usernameadd}' added successfully.", fg="green")
    else:
        message_label.config(text="Both fields are required.", fg="red")

def manage_users():
    manage_window = tk.Tk()
    manage_window.geometry("400x300")  # Increased size for better visibility
    manage_window.title("Manage Users")

    # Label for managing users
    label = tk.Label(manage_window, text="Manage Users", font=("Arial", 16))
    label.pack(pady=10)

    # Listbox to display users
    user_listbox = tk.Listbox(manage_window)
    user_listbox.pack(expand=True, fill='both', padx=10, pady=10)

    # Frame for buttons
    button_frame = tk.Frame(manage_window)
    button_frame.pack(pady=10)

    # Button to remove selected user
    remove_button = tk.Button(button_frame, text="Remove User", command=lambda: remove_user(user_listbox))
    remove_button.pack(side=tk.LEFT, padx=10)

    # Exit button to close the manage users window
    exit_button = tk.Button(button_frame, text="Exit", command=manage_window.destroy)
    exit_button.pack(side=tk.RIGHT, padx=10)

    # Populate the listbox with current users
    for user in user_credentials.keys():
        user_listbox.insert(tk.END, user)

    manage_window.mainloop()

def remove_user(user_listbox):
    selected_user_index = user_listbox.curselection()
    if selected_user_index:
        selected_user = user_listbox.get(selected_user_index)
        del user_credentials[selected_user]  # Remove user from credentials
        user_listbox.delete(selected_user_index)  # Remove user from listbox

# Main login window
top = tk.Tk()
top.geometry("300x200")
top.title("Login")

# Username entry
username_label = tk.Label(top, text="Username")
username_label.pack()

username_entry = tk.Entry(top)
username_entry.pack()

# Password entry
password_label = tk.Label(top, text="Password")
password_label.pack()

password_entry = tk.Entry(top, show="*")
password_entry.pack()

# Login button
login_button = tk.Button(top, text="Login", command=login)
login_button.pack(pady=10)

# Bind Enter key to login function
top.bind('<Return>', lambda event: login())

top.mainloop()