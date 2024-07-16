# Import the required libraries and modules
import tkinter as tk
from tkinter import ttk, messagebox, PhotoImage
import subprocess
import platform
import sqlite3
import datetime

# Database setup function
def init_db():
    # Initialize the SQLite database if not already initialized.
    conn = sqlite3.connect('smart_home.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        username TEXT PRIMARY KEY,
                        password TEXT NOT NULL
                      )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS devices (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL,
                        device_name TEXT NOT NULL,
                        device_ip TEXT NOT NULL
                      )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS history (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL,
                        device_name TEXT NOT NULL,
                        device_ip TEXT NOT NULL,
                        status TEXT NOT NULL,
                        timestamp TEXT NOT NULL
                      )''')
    conn.commit()
    conn.close()

# Base class for creating GUI windows.
class BaseWindow:
    # Initialize the base window with given title and geometry.
    def __init__(self, root, title, geometry):
        self._root = root
        self._root.title(title)
        self._root.geometry(geometry)

# Window for user registration/sign-up.
class SignUpWindow(BaseWindow):
    # Initialize sign-up window with username and password input fields, and sign-up button
    def __init__(self, root, on_success):
        super().__init__(root, "Sign Up", "300x200")
        self._on_success = on_success
        
        self._username_label = ttk.Label(root, text="Username:", background="#AFE1AF")
        self._username_label.pack(pady=5)
        self._username_entry = ttk.Entry(root)
        self._username_entry.pack(pady=5)
        
        self._password_label = ttk.Label(root, text="Password:", background="#AFE1AF")
        self._password_label.pack(pady=5)
        self._password_entry = ttk.Entry(root, show="*")
        self._password_entry.pack(pady=5)
        
        self._signup_button = ttk.Button(root, text="Sign Up", command=self.sign_up)
        self._signup_button.pack(pady=10)
    
    # Process user sign-up: validate input, insert into database, and show success/error messages.
    def sign_up(self):
        username = self._username_entry.get().strip()
        password = self._password_entry.get().strip()
        # Check for empty fields, fields with only whitespace, or username consisting of numbers only
        if not username or not password:
            messagebox.showerror("Error", "Username and password cannot be empty or consist only of whitespace.")
            return
        if username.isdigit():
            messagebox.showerror("Error", "Username cannot consist of numbers only.")
            return
    
        conn = sqlite3.connect('smart_home.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        if cursor.fetchone():
            messagebox.showerror("Error", "Username already exists.")
        else:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Account created successfully!")
            self._root.destroy()

# Login window class
class LoginWindow(BaseWindow):
    # Initialize login window with login and sign-up options.
    def __init__(self, root, on_login_success, on_signup):
        super().__init__(root, "Login", "850x600")
        self._root.resizable(width=False, height=False)

        self._bg_path = PhotoImage(file=r"D:\Programming\College-Programs\Object Oriented Programming\Finals\login_bg.png")
        self._bg_image = tk.Label(root, image=self._bg_path)
        self._bg_image.place(relheight=1, relwidth=1)
        
        self._on_login_success = on_login_success
        self._on_signup = on_signup
        
        self._login_button = tk.Button(root, text="Login", command=self.show_login_window, background="#A6BB8D", borderwidth=0, font=("Bugaki", 12, "bold"), foreground="#FDFCE9")
        self._login_button.pack(pady=(357, 61))

        self._signup_button = tk.Button(root, text="Sign Up", command=self.show_signup_window, background="#A6BB8D", borderwidth=0, font=("Helvetica", 12, "bold"), foreground="#FDFCE9")
        self._signup_button.pack(pady=10)
    
    # Function to display the login window as a pop-up.
    def show_login_window(self):
        login_root = tk.Toplevel(self._root)
        login_root.title("Login")
        login_root.geometry("300x200")
        login_root.config(bg="#AFE1AF")

        username_label = ttk.Label(login_root, text="Username:", background="#AFE1AF")
        username_label.pack(pady=5)
        username_entry = ttk.Entry(login_root)
        username_entry.pack(pady=5)
        
        password_label = ttk.Label(login_root, text="Password:", background="#AFE1AF")
        password_label.pack(pady=5)
        password_entry = ttk.Entry(login_root, show="*")
        password_entry.pack(pady=5)

        login_button = ttk.Button(login_root, text="Login", command=lambda: self.check_login(username_entry.get(), password_entry.get(), login_root))
        login_button.pack(pady=10)

    # Function to display the sign-up window as a pop-up.
    def show_signup_window(self):
        signup_root = tk.Toplevel(self._root)
        signup_app = SignUpWindow(signup_root, self._on_signup)
        signup_root.config(bg="#AFE1AF")
    
    # Validate user credentials against database and handle login.
    def check_login(self, username, password, window):
        conn = sqlite3.connect('smart_home.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        if cursor.fetchone():
            window.destroy()
            self._root.destroy()
            self._on_login_success(username)
        else:
            messagebox.showerror("Error", "Incorrect username or password")

# Base Device class
class Device:
    # Initialize device with a name and IP address.
    def __init__(self, name, ip):
        self._name = name
        self._ip = ip

    # Getters and setters for device name and IP address.
    @property
    def name(self):
        return self._name
    
    @property
    def ip(self):
        return self._ip

    # Abstract method to be implemented by subclasses to get device status.
    def get_status(self):
        raise NotImplementedError("Subclasses should implement this method")

# Smart device class inheriting from Device
class SmartDevice(Device):
    # Initialize smart device with name, IP, and status attributes.
    def __init__(self, name, ip):
        super().__init__(name, ip)
        self._label = None
        self._status_label = None
        self._status = None
        self._last_status_change = None

    # Get and set label and status label attributes.
    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, label):
        self._label = label

    @property
    def status_label(self):
        return self._status_label

    @status_label.setter
    def status_label(self, status_label):
        self._status_label = status_label

    # Check the status of the smart device by pinging its IP address.
    def get_status(self):
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        command = ['ping', param, '1', self.ip]
        try:
            result = subprocess.run(command, capture_output=True, text=True, timeout=5)
            status = 'TTL=' in result.stdout or 'ttl=' in result.stdout
            if self._status is None:
                self._status = status
                self._last_status_change = datetime.datetime.now()
                return status
            elif self._status != status:
                self._status = status
                self._last_status_change = datetime.datetime.now()
                return status
            return self._status
        except subprocess.TimeoutExpired:
            return False
        except Exception as e:
            print(f"Error pinging device: {e}")
            return False

# Class representing the control panel for managing smart devices.
class SmartDeviceControlPanel:
    def __init__(self, root, username):
        # Initialize the control panel with GUI elements and device management logic.
        self._root = root
        self._devices = {}
        self._device_frames = {}
        self._root.title("Smart Device Automation Status Tracker")
        self._root.geometry("850x600")
        self._root.resizable(True, True)

        # Initialize device status images
        self._username = username
        self._running = True
        self._after_id = None
        
        # Path to device status images
        self._on_png_path = PhotoImage(file=r"D:\Programming\College-Programs\Object Oriented Programming\Finals\ON.png")
        self._off_png_path = PhotoImage(file=r"D:\Programming\College-Programs\Object Oriented Programming\Finals\OFF.png")
        self._default_png_path = PhotoImage(file=r"D:\Programming\College-Programs\Object Oriented Programming\Finals\default.png")

        # Set the style for GUI elements
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 12), padding=10)
        style.configure("TLabel", font=("Helvetica", 14))
        
        # Create the main frame for device management
        self._device_frame = ttk.Frame(root)
        self._device_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create buttons for adding devices and signing out
        self._add_device_button = ttk.Button(root, text="Add Device", command=self.add_device)
        self._add_device_button.pack(pady=10)
        
        self._sign_out_button = ttk.Button(root, text="Sign Out", command=self.sign_out)
        self._sign_out_button.pack(pady=10)

        # Initialize device status check
        self.load_devices_from_db()
        self.check_device_statuses()

    # Function to check the status of all devices periodically.
    def check_device_statuses(self):
        if self._running:
            for ip in self._devices.keys():
                device = self._devices[ip]
                prev_status = device._status
                current_status = device.get_status()
                print(f"Checking device: {device.name}, IP: {device.ip}, Previous Status: {prev_status}, Current Status: {current_status}")  # Debug statement
                if prev_status != current_status:
                    status = "On" if current_status else "Off"
                    self.log_history(self._username, device.name, ip, status)
                    device.label.config(text=f"Device: {device.name}\nStatus: {status}")
                    device.status_label.config(image=self._on_png_path if current_status else self._off_png_path)
                    print(f"Status changed for device: {device.name}, new status: {status}")  # Debug statement
                    # Schedule the messagebox to run after the current callback completes
                    self._root.after_idle(messagebox.showinfo, "Device Status Change", f"The device '{device.name}' is now {status}.")
                else:
                    device.label.config(text=f"Device: {device.name}\nStatus: {'On' if prev_status else 'Off'}")
                    device.status_label.config(image=self._on_png_path if prev_status else self._off_png_path)
            self._after_id = self._root.after(5000, self.check_device_statuses)




    # Function to handle user sign-out.
    def sign_out(self):
        self._running = False
        if self._after_id:
            self._root.after_cancel(self._after_id)
        self._root.destroy()
        login_root = tk.Tk()
        login_app = LoginWindow(login_root, on_login_success, lambda: None)
        login_root.mainloop()

    # Load devices associated with the user from the database.
    def load_devices_from_db(self):
        conn = sqlite3.connect('smart_home.db')
        cursor = conn.cursor()
        cursor.execute("SELECT device_name, device_ip FROM devices WHERE username = ?", (self._username,))
        devices = cursor.fetchall()
        conn.close()
        
        for device_name, device_ip in devices:
            self._devices[device_ip] = SmartDevice(device_name, device_ip)
            self.create_device_widgets(device_name, device_ip)
            self.rearrange_devices()

    # Function to open the device addition/edit window.
    def add_device(self):
        self.open_device_window()
    
    def open_device_window(self, name='', ip='', is_edit=False, old_ip=None):
        window = tk.Toplevel(self._root)
        window.title("Add Device" if not is_edit else "Edit Device")
        window.geometry("400x230")
        window.config(bg="#AFE1AF")
        
        name_label = ttk.Label(window, text="Device Name:", background="#AFE1AF")
        name_label.pack(pady=5)
        name_entry = ttk.Entry(window)
        name_entry.pack(pady=5)
        name_entry.insert(0, name)
        
        ip_label = ttk.Label(window, text="Device IP:", background="#AFE1AF")
        ip_label.pack(pady=5)
        ip_entry = ttk.Entry(window)
        ip_entry.pack(pady=5)
        ip_entry.insert(0, ip)
        
        save_button = ttk.Button(window, text="Save Device", command=lambda: self.save_device(name_entry.get(), ip_entry.get(), is_edit, old_ip, window))
        save_button.pack(pady=10)

    # Function to save the device to the database.
    def save_device(self, name, ip, is_edit, old_ip, window):
        if name and ip:
            if not all(char.isdigit() or char == '.' for char in ip):
                messagebox.showerror("Error", "IP address can only contain numbers and dots.")
                return
            conn = sqlite3.connect('smart_home.db')
            cursor = conn.cursor()
            if not is_edit:
                cursor.execute("INSERT INTO devices (username, device_name, device_ip) VALUES (?, ?, ?)", (self._username, name, ip))
            else:
                cursor.execute("UPDATE devices SET device_name = ?, device_ip = ? WHERE username = ? AND device_ip = ?", (name, ip, self._username, old_ip))
            conn.commit()
            conn.close()

            if is_edit and old_ip in self._devices:
                self.delete_device(old_ip, rearrange=False)
            
            self._devices[ip] = SmartDevice(name, ip)
            self.create_device_widgets(name, ip)
            self.rearrange_devices()
            window.destroy()
        else:
            messagebox.showerror("Error", "Please enter both name and IP.")
    
    # Function to create device widgets (name label, status, edit, delete, and 
    #  buttons).
    def create_device_widgets(self, name, ip):
        frame = ttk.Frame(self._device_frame)
        self._device_frames[ip] = frame
        
        label = ttk.Label(frame, text=f"Device: {name}\nStatus: Unknown", anchor="center")
        label.pack(pady=5)
        self._devices[ip].label = label

        status_label = ttk.Label(frame)
        status_label.pack(pady=5)
        status_label.config(image=self._default_png_path)
        self._devices[ip].status_label = status_label
        
        edit_button = ttk.Button(frame, text="Edit Device", command=lambda ip=ip: self.open_device_window(self._devices[ip].name, ip, True, ip))
        edit_button.pack(pady=5)
        
        delete_button = ttk.Button(frame, text="Delete Device", command=lambda ip=ip: self.delete_device(ip))
        delete_button.pack(pady=5)
        
        history_button = ttk.Button(frame, text="View History", command=lambda ip=ip: self.view_history(ip))
        history_button.pack(pady=5)

    # Function to check the status of all devices periodically.
    def check_device_statuses(self):
        if self._running:
            for ip in self._devices.keys():
                device = self._devices[ip]
                prev_status = device._status
                current_status = device.get_status()
                if prev_status != current_status:
                    status = "On" if current_status else "Off"
                    self.log_history(self._username, device.name, ip, status)
                    device.label.config(text=f"Device: {device.name}\nStatus: {status}")
                    device.status_label.config(image=self._on_png_path if current_status else self._off_png_path)
                else:
                    device.label.config(text=f"Device: {device.name}\nStatus: {'On' if prev_status else 'Off'}")
                    device.status_label.config(image=self._on_png_path if prev_status else self._off_png_path)
            self._after_id = self._root.after(5000, self.check_device_statuses)

    # Function to log the device status changes in the database.
    def log_history(self, username, device_name, device_ip, status):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        conn = sqlite3.connect('smart_home.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO history (username, device_name, device_ip, status, timestamp) VALUES (?, ?, ?, ?, ?)", (username, device_name, device_ip, status, timestamp))
        conn.commit()
        conn.close()

    # Function to view the history of a device's status changes.
    def view_history(self, ip):
        history_root = tk.Toplevel(self._root)
        history_root.title("Device History")
        history_root.geometry("400x300")
        history_root.config(bg="#AFE1AF")

        history_listbox = tk.Listbox(history_root, font=("Helvetica", 12))
        history_listbox.pack(fill=tk.BOTH, expand=True)

        conn = sqlite3.connect('smart_home.db')
        cursor = conn.cursor()
        cursor.execute("SELECT status, timestamp FROM history WHERE device_ip = ? ORDER BY timestamp DESC", (ip,))
        history = cursor.fetchall()
        conn.close()

        for entry in history:
            history_listbox.insert(tk.END, f"{entry[1]} - {entry[0]}")

    # Function to delete a device from the database and the GUI.
    def delete_device(self, ip, rearrange=True):
        conn = sqlite3.connect('smart_home.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM devices WHERE username = ? AND device_ip = ?", (self._username, ip))
        conn.commit()
        conn.close()
        
        if ip in self._devices:
            del self._devices[ip]
        
        if ip in self._device_frames:
            self._device_frames[ip].destroy()
            del self._device_frames[ip]
        
        if rearrange:
            self.rearrange_devices()

    # Function to rearrange the device widgets in the GUI.
    def rearrange_devices(self):
        for frame in self._device_frames.values():
            frame.grid_forget()
        row, col = 0, 0
        for frame in self._device_frames.values():
            frame.grid(row=row, column=col, padx=10, pady=10)
            col += 1
            if col > 2:  # Move to the next row after 3 columns
                col = 0
                row += 1
    
    def create_device_widgets(self, name, ip):
        frame = ttk.Frame(self._device_frame)
        self._device_frames[ip] = frame
        
        label = ttk.Label(frame, text=f"Device: {name}\nStatus: Unknown", anchor="center")
        label.pack(pady=5)
        self._devices[ip].label = label

        status_label = ttk.Label(frame)
        status_label.pack(pady=5)
        status_label.config(image=self._default_png_path)
        self._devices[ip].status_label = status_label
        
        edit_button = ttk.Button(frame, text="Edit Device", command=lambda ip=ip: self.open_device_window(self._devices[ip].name, ip, True, ip))
        edit_button.pack(pady=5)
        
        delete_button = ttk.Button(frame, text="Delete Device", command=lambda ip=ip: self.delete_device(ip))
        delete_button.pack(pady=5)
        
        history_button = ttk.Button(frame, text="View History", command=lambda ip=ip: self.view_history(ip))
        history_button.pack(pady=5)

# Function to handle successful login and open the control panel.
def on_login_success(username):
    control_panel_root = tk.Tk()
    control_panel_app = SmartDeviceControlPanel(control_panel_root, username)
    control_panel_root.mainloop()

# Main entry point of the application.
init_db()
root = tk.Tk()
login_app = LoginWindow(root, on_login_success, lambda: None)
root.mainloop()