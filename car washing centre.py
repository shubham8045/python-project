import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class CarWashRecord:
    def __init__(self, customer_name, car_plate, wash_type, amount, date):
        self.customer_name = customer_name
        self.car_plate = car_plate
        self.wash_type = wash_type
        self.amount = amount
        self.date = date

class CarWashManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Car Wash Management System")

        self.car_wash_records = []

        self.create_widgets()

    def create_widgets(self):
        self.label_customer_name = tk.Label(self.root, text="Customer Name:")
        self.entry_customer_name = tk.Entry(self.root)

        self.label_car_plate = tk.Label(self.root, text="Car Plate:")
        self.entry_car_plate = tk.Entry(self.root)

        self.label_wash_type = tk.Label(self.root, text="Wash Type:")
        self.entry_wash_type = tk.Entry(self.root)

        self.label_amount = tk.Label(self.root, text="Amount:")
        self.entry_amount = tk.Entry(self.root, validate="key", validatecommand=(root.register(self.validate_amount), '%P'))

        self.button_add_record = tk.Button(self.root, text="Add Record", command=self.add_car_wash_record)
        self.button_view_records = tk.Button(self.root, text="View Records", command=self.view_car_wash_records)
        self.button_total_earnings = tk.Button(self.root, text="Total Earnings", command=self.calculate_total_earnings)

        # Treeview for displaying records
        self.tree = ttk.Treeview(self.root, columns=("Customer Name", "Car Plate", "Wash Type", "Amount", "Date"), show="headings")
        self.tree.heading("Customer Name", text="Customer Name")
        self.tree.heading("Car Plate", text="Car Plate")
        self.tree.heading("Wash Type", text="Wash Type")
        self.tree.heading("Amount", text="Amount")
        self.tree.heading("Date", text="Date")

        self.tree.column("Customer Name", width=150)
        self.tree.column("Car Plate", width=100)
        self.tree.column("Wash Type", width=100)
        self.tree.column("Amount", width=80)
        self.tree.column("Date", width=120)

        # Layout
        self.label_customer_name.grid(row=0, column=0, padx=10, pady=5)
        self.entry_customer_name.grid(row=0, column=1, padx=10, pady=5)

        self.label_car_plate.grid(row=1, column=0, padx=10, pady=5)
        self.entry_car_plate.grid(row=1, column=1, padx=10, pady=5)

        self.label_wash_type.grid(row=2, column=0, padx=10, pady=5)
        self.entry_wash_type.grid(row=2, column=1, padx=10, pady=5)

        self.label_amount.grid(row=3, column=0, padx=10, pady=5)
        self.entry_amount.grid(row=3, column=1, padx=10, pady=5)

        self.button_add_record.grid(row=4, column=0, columnspan=2, pady=10)
        self.button_view_records.grid(row=5, column=0, columnspan=2, pady=10)
        self.button_total_earnings.grid(row=6, column=0, columnspan=2, pady=10)

        self.tree.grid(row=7, column=0, columnspan=2, pady=10)

    def validate_amount(self, new_value):
        try:
            float(new_value)
            return True
        except ValueError:
            return False

    def add_car_wash_record(self):
        customer_name = self.entry_customer_name.get()
        car_plate = self.entry_car_plate.get()
        wash_type = self.entry_wash_type.get()
        amount = float(self.entry_amount.get()) if self.entry_amount.get() else 0.0
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if customer_name and car_plate and wash_type:
            record = CarWashRecord(customer_name, car_plate, wash_type, amount, date)
            self.car_wash_records.append(record)
            self.update_treeview()
            messagebox.showinfo("Success", "Car wash record added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please fill in all required fields.")

    def view_car_wash_records(self):
        if not self.car_wash_records:
            messagebox.showinfo("Information", "No car wash records available.")
        else:
            self.update_treeview()

    def update_treeview(self):
        # Clear existing records in the treeview
        for record in self.tree.get_children():
            self.tree.delete(record)

        # Insert new records into the treeview
        for record in self.car_wash_records:
            self.tree.insert("", "end", values=(record.customer_name, record.car_plate, record.wash_type, record.amount, record.date))

    def calculate_total_earnings(self):
        total_earnings = sum(record.amount for record in self.car_wash_records)
        messagebox.showinfo("Total Earnings", f"Total Earnings: ${total_earnings:.2f}")

    def clear_entries(self):
        self.entry_customer_name.delete(0, tk.END)
        self.entry_car_plate.delete(0, tk.END)
        self.entry_wash_type.delete(0, tk.END)
        self.entry_amount.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = CarWashManagementSystem(root)
    root.mainloop()
