import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3

class ContactBookApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Contact Book App")
            
        # Connect to SQLite database
        self.conn = sqlite3.connect('contacts.db')
        self.create_table()

        # Set up frames
        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)
        
        # Title label
        self.title_label = tk.Label(self.frame, text="Contact Book", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        # Create buttons for each operation
        self.create_button = tk.Button(self.frame, text="Create Contact", command=self.create_contact)
        self.create_button.pack(pady=5, fill=tk.X)

        self.view_button = tk.Button(self.frame, text="View Contact", command=self.view_contact)
        self.view_button.pack(pady=5, fill=tk.X)

        self.update_button = tk.Button(self.frame, text="Update Contact", command=self.update_contact)
        self.update_button.pack(pady=5, fill=tk.X)

        self.delete_button = tk.Button(self.frame, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack(pady=5, fill=tk.X)

        self.search_button = tk.Button(self.frame, text="Search Contact", command=self.search_contact)
        self.search_button.pack(pady=5, fill=tk.X)

        self.count_button = tk.Button(self.frame, text="Count Contacts", command=self.count_contacts)
        self.count_button.pack(pady=5, fill=tk.X)

        self.exit_button = tk.Button(self.frame, text="Exit", command=self.exit_app)
        self.exit_button.pack(pady=20, fill=tk.X)

    def create_table(self):
        with self.conn:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS contacts (
                                name TEXT PRIMARY KEY,
                                age INTEGER,
                                email TEXT,
                                mobile TEXT)''')

    def create_contact(self):
        self.contact_form("Create")

    def view_contact(self):
        name = simpledialog.askstring("Input", "Enter contact name to view:")
        contact = self.fetch_contact(name)
        if contact:
            messagebox.showinfo("Contact Info", f"Name: {name}, Age: {contact[1]}, Mobile Number: {contact[3]}, Email: {contact[2]}")
        else:
            messagebox.showwarning("Warning", "Contact not found!")

    def update_contact(self):
        name = simpledialog.askstring("Input", "Enter name to update contact:")
        contact = self.fetch_contact(name)
        if contact:
            self.contact_form("Update", name, contact)
        else:
            messagebox.showwarning("Warning", "Contact not found!")

    def delete_contact(self):
        name = simpledialog.askstring("Input", "Enter contact name to delete:")
        if self.delete_from_db(name):
            messagebox.showinfo("Success", f"Contact name {name} has been deleted successfully!")
        else:
            messagebox.showwarning("Warning", "Contact not found!")

    def search_contact(self):
        search_name = simpledialog.askstring("Input", "Enter contact name to search:")
        contacts = self.search_in_db(search_name)
        if contacts:
            result = "\n".join(f"Name: {contact[0]}, Age: {contact[1]}, Mobile: {contact[3]}, Email: {contact[2]}" for contact in contacts)
            messagebox.showinfo("Search Result", result)
        else:
            messagebox.showinfo("Search Result", "No contacts found with that name.")

    def count_contacts(self):
        count = self.count_in_db()
        messagebox.showinfo("Count", f"Total contacts in your book: {count}")

    def exit_app(self):
        self.conn.close()
        self.root.quit()
                        
    def contact_form(self, action, name=None, contact=None):
        if action == "Create":
            name = simpledialog.askstring("Input", "Enter your name:")
            if self.fetch_contact(name):
                messagebox.showwarning("Warning", f"Contact name {name} already exists!")
                return
        age = simpledialog.askstring("Input", "Enter age:")
        email = simpledialog.askstring("Input", "Enter email:")
        mobile = simpledialog.askstring("Input", "Enter mobile number:")
        try:
            if action == "Create":
                self.insert_into_db(name, int(age), email, mobile)
                messagebox.showinfo("Success", f"Contact {name} has been created successfully!")
            else:
                self.update_in_db(name, int(age), email, mobile)
                messagebox.showinfo("Success", f"Contact {name} has been updated successfully!")
        except ValueError:
            messagebox.showerror("Error", "Invalid age entered. Please enter a number.")

    def fetch_contact(self, name):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM contacts WHERE name = ?", (name,))
        return cursor.fetchone()

    def insert_into_db(self, name, age, email, mobile):
        with self.conn:
            self.conn.execute("INSERT INTO contacts (name, age, email, mobile) VALUES (?, ?, ?, ?)",
                              (name, age, email, mobile))

    def update_in_db(self, name, age, email, mobile):
        with self.conn:
            self.conn.execute("UPDATE contacts SET age = ?, email = ?, mobile = ? WHERE name = ?",
                              (age, email, mobile, name))

    def delete_from_db(self, name):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM contacts WHERE name = ?", (name,))
        return cursor.rowcount > 0

    def search_in_db(self, search_name):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM contacts WHERE name LIKE ?", ('%' + search_name + '%',))
        return cursor.fetchall()

    def count_in_db(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM contacts")
        return cursor.fetchone()[0]

# Set up the main window
root = tk.Tk()
app = ContactBookApp(root)

# Run the application
root.mainloop()