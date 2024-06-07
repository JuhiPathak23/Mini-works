from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

class BankSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Bank Management System")
        self.master.geometry("400x300")        
        self.users = {}
        self.create_account_frame = Frame(self.master, bg='#F0F0F0')
        self.create_account_frame.pack(pady=20)

        self.name_label = Label(self.create_account_frame, text="Name:", font=('Arial', 12), bg='#F0F0F0')
        self.name_label.grid(row=0, column=0, padx=10, pady=10)
        self.age_label = Label(self.create_account_frame, text="Age:", font=('Arial', 12), bg='#F0F0F0')
        self.age_label.grid(row=1, column=0, padx=10, pady=10)
        self.salary_label = Label(self.create_account_frame, text="Salary:", font=('Arial', 12), bg='#F0F0F0')
        self.salary_label.grid(row=2, column=0, padx=10, pady=10)
        self.pin_label = Label(self.create_account_frame, text="PIN:", font=('Arial', 12), bg='#F0F0F0')
        self.pin_label.grid(row=3, column=0, padx=10, pady=10)

        self.name_entry = Entry(self.create_account_frame, font=('Arial', 12), bg='#FFFFFF', relief='solid', borderwidth=1)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)
        self.age_entry = Entry(self.create_account_frame, font=('Arial', 12), bg='#FFFFFF', relief='solid', borderwidth=1)
        self.age_entry.grid(row=1, column=1, padx=10, pady=10)
        self.salary_entry = Entry(self.create_account_frame, font=('Arial', 12), bg='#FFFFFF', relief='solid', borderwidth=1)
        self.salary_entry.grid(row=2, column=1, padx=10, pady=10)
        self.pin_entry = Entry(self.create_account_frame, show="*", font=('Arial', 12), bg='#FFFFFF', relief='solid', borderwidth=1)
        self.pin_entry.grid(row=3, column=1, padx=10, pady=10)

        self.create_account_button = Button(self.create_account_frame, text="Create Account", font=('Arial', 12), bg='#4CAF50', fg='#FFFFFF', activebackground='#2E8B57', activeforeground='#FFFFFF', relief='raised', borderwidth=0, command=self.create_account)
        self.create_account_button.grid(row=4, column=1, pady=20)

        self.login_frame = Frame(self.master, bg="#FFFFFF")
        self.login_frame.pack(pady=20)
        self.login_name_label = Label(self.login_frame, text="Name:", font=("Arial", 14), bg="#FFFFFF")
        self.login_name_label.grid(row=0, column=0, padx=10, pady=10)
        self.login_name_entry = Entry(self.login_frame, width=30, font=("Arial", 14))
        self.login_name_entry.grid(row=0, column=1, padx=10, pady=10)
        self.login_pin_label = Label(self.login_frame, text="PIN:", font=("Arial", 14), bg="#FFFFFF")
        self.login_pin_label.grid(row=1, column=0, padx=10, pady=10)
        self.login_pin_entry = Entry(self.login_frame, show="*", width=30, font=("Arial", 14))
        self.login_pin_entry.grid(row=1, column=1, padx=10, pady=10)
        
        self.login_button = Button(self.login_frame, text="Login", command=self.login, font=('Arial', 12), bg='#4CAF50', fg='#FFFFFF', activebackground='#2E8B57', activeforeground='#FFFFFF', relief='raised', borderwidth=0)
        self.login_button.grid(row=2, column=1, padx=10, pady=10)
        self.master.bind('<Return>', self.login) # Allow login with "Enter" key
        self.user_details_frame = Frame(self.master)

        label_style = {"fg": "green", "font": ("Calibri", 14)}
        self.name_label2 = Label(self.user_details_frame, text="Name:", **label_style)
        self.name_label2.grid(row=0, column=1, padx=10, pady=10)
        self.age_label2 = Label(self.user_details_frame, text="Age:", **label_style)
        self.age_label2.grid(row=1, column=1, padx=10, pady=10)
        self.salary_label2 = Label(self.user_details_frame, text="Salary:", **label_style)
        self.salary_label2.grid(row=2, column=1, padx=10, pady=10)
        self.current_balance_label = Label(self.user_details_frame, text="Current Balance:", **label_style)
        self.current_balance_label.grid(row=3, column=1, padx=10, pady=10)

        self.view_transaction_button = Button(self.user_details_frame, text="View Transaction Log", command=self.view_transaction_log, bg="green", fg="white")
        self.view_transaction_button.grid(row=4, column=0, padx=10, pady=10)
        self.deposit_button = Button(self.user_details_frame, text="Deposit", command=self.deposit, bg="yellow", fg="black")
        self.deposit_button.grid(row=4, column=1, padx=10, pady=10)
        self.withdraw_button = Button(self.user_details_frame, text="Withdraw", command=self.withdraw, bg="orange", fg="white")
        self.withdraw_button.grid(row=4, column=2, padx=10, pady=10)
        self.logout_button = Button(self.user_details_frame, text="Logout", command=self.logout, bg="red", fg="white")
        self.logout_button.grid(row=4, column=3, padx=10, pady=10)

        self.name = ""
        self.age = ""
        self.salary = ""
        self.pin = ""
        self.current_balance = 0
        self.transaction_log = []

    def create_account(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        salary = self.salary_entry.get()
        pin = self.pin_entry.get()
        user_data = {'name': name, 'age': age, 'salary': salary, 'pin': pin, 'balance': 0, 'transaction_log':[]}
        self.users[pin] = user_data
        if not name or not age or not salary or not pin:
            messagebox.showerror("Error", "All fields are required!")
            return
        if not age.isdigit():
            messagebox.showerror("Error", "Age must be a number!")
            return
        if not salary.isdigit():
            messagebox.showerror("Error", "Salary must be a number!")
            return
        if not pin.isdigit() or len(pin) != 4:
            messagebox.showerror("Error", "PIN must be a 4-digit number!")
            return
        
        self.name = name
        self.age = age
        self.salary = salary
        self.pin = pin
        self.current_balance = 0
        self.transaction_log = []
        self.name_entry.delete(0, END)
        self.age_entry.delete(0, END)
        self.salary_entry.delete(0, END)
        self.pin_entry.delete(0, END)
        
        self.name_label2.config(text="Name: " + self.name)
        self.age_label2.config(text="Age: " + self.age)
        self.salary_label2.config(text="Salary: " + self.salary)
        self.current_balance_label.config(text="Current Balance: " + str(self.current_balance))
        
        self.create_account_frame.pack_forget()
        self.login_frame.pack_forget()
        self.user_details_frame.pack()


    def login(self, event=None):
        name = self.login_name_entry.get()
        pin = self.login_pin_entry.get()
        if pin in self.users and self.users[pin]['name'] == name:
            self.current_user_data = self.users[pin]
            self.user_details_frame.pack(pady=20)
            self.name_label2['text'] = f"Name: {self.current_user_data['name']}"
            self.age_label2['text'] = f"Age: {self.current_user_data['age']}"
            self.salary_label2['text'] = f"Salary: {self.current_user_data['salary']}"
            self.current_balance_label['text'] = f"Current Balance: {self.current_user_data['balance']}"    
            self.login_frame.pack_forget()
            self.create_account_frame.pack_forget()
        else:
            messagebox.showerror("Error", "Invalid PIN or UserName")

    def deposit(self):
        pin = simpledialog.askstring("Deposit", "Enter PIN:")
        amount = simpledialog.askstring("Deposit", "Enter amount:")
        
        if not pin:
            return
        if not amount or not amount.isdigit() or int(amount) <= 0:
            messagebox.showerror("Error", "Invalid input!")
            return
        if pin not in self.users:
            messagebox.showerror("Error", "Invalid PIN!")
            return
        self.users[pin]['balance'] += int(amount)
        self.current_balance_label.config(text="Current Balance: " + str(self.users[pin]['balance']))
        transaction = "Deposit: +" + amount + ", New Balance: " + str(self.users[pin]['balance'])
        self.transaction_log.append(transaction)
        self.users[pin]['transactions'] = self.transaction_log

    def withdraw(self):
        pin = simpledialog.askstring("PIN", "Enter your PIN:")
        amount = simpledialog.askstring("Withdraw", "Enter amount:")
        if not (pin and amount):
            return
        if not amount.isdigit() or int(amount) <= 0:
            messagebox.showerror("Error", "Invalid amount!")
            return
        if pin not in self.users:
            messagebox.showerror("Error", "Invalid PIN!")
            return
        current_balance = self.users[pin]['balance']
        if int(amount) > current_balance:
            messagebox.showerror("Error", "Insufficient balance!")
            return
        current_balance -= int(amount)
        self.users[pin]['balance'] = current_balance
        self.current_balance_label.config(text="Current Balance: " + str(current_balance))
        transaction = "Withdraw: -" + amount + ", New Balance: " + str(current_balance)
        self.transaction_log.append(transaction)
        self.users[pin]['transactions'] = self.transaction_log

    def view_transaction_log(self):
        transaction_log_window = Toplevel(self.master)
        transaction_log_window.title("Transaction Log")
        pin = self.login_pin_entry.get()
        if pin in self.users:
            self.users[pin]['transactions'].extend(self.transaction_log)
        transaction_log_frame = Frame(transaction_log_window)
        transaction_log_frame.pack(padx=10, pady=10)
        transaction_log_label = Label(transaction_log_frame, text="Transaction Log:")
        transaction_log_label.grid(row=0, column=0, padx=10, pady=10)
        transaction_log_listbox = Listbox(transaction_log_frame, width=50)
        transaction_log_listbox.grid(row=1, column=0, padx=10, pady=10)
        if pin in self.users:
            for transaction in self.users[pin]['transactions']:
                transaction_log_listbox.insert(END, transaction)
        else:
            for transaction in self.transaction_log:
                transaction_log_listbox.insert(END, transaction)

    def logout(self):
        self.name = ""
        self.age = ""
        self.salary = ""
        self.pin = ""
        self.current_balance = 0
        self.transaction_log = []
        self.login_pin_entry.delete(0, END)
        self.user_details_frame.pack_forget()
        self.create_account_frame.pack(pady=20)
        self.login_frame.pack()

def main():
    root = Tk()
    bank_system = BankSystem(root)
    root.mainloop()

if __name__ == '__main__':
    main()
