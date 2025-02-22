from tkinter import *
from tkinter import messagebox

# Global balance variable
userBalance = 0.0

# Function to show the main menu
def show_main_menu():
    clear_window()
    
    Label(window, text="Welcome to E-Bank Simulator Inc.", font=("Arial", 14)).pack(pady=10)
    
    Button(window, text="Check Balance", command=show_balance, width=20).pack(pady=5)
    Button(window, text="Deposit Money", command=show_deposit, width=20).pack(pady=5)
    Button(window, text="Withdraw Money", command=show_withdraw, width=20).pack(pady=5)
    Button(window, text="Quit", command=window.quit, width=20, bg="red", fg="white").pack(pady=10)

# Function to clear the window
def clear_window():
    for widget in window.winfo_children():
        widget.destroy()

# Function to show balance
def show_balance():
    clear_window()
    Label(window, text="Your Balance:", font=("Arial", 12)).pack(pady=5)
    Label(window, text=f"${userBalance:.2f}", font=("Arial", 14, "bold")).pack(pady=10)
    Button(window, text="Back", command=show_main_menu, width=15).pack(pady=10)

# Function to handle deposit input
def show_deposit():
    clear_window()
    Label(window, text="Enter Amount to Deposit:", font=("Arial", 12)).pack()
    
    global amount_entry
    amount_entry = Entry(window)
    amount_entry.pack(pady=5)

    Button(window, text="Deposit", command=deposit, width=15).pack(pady=5)
    Button(window, text="Back", command=show_main_menu, width=15).pack(pady=5)

# Function to handle withdrawal input
def show_withdraw():
    clear_window()
    Label(window, text="Enter Amount to Withdraw:", font=("Arial", 12)).pack()
    
    global amount_entry
    amount_entry = Entry(window)
    amount_entry.pack(pady=5)

    Button(window, text="Withdraw", command=withdraw, width=15).pack(pady=5)
    Button(window, text="Back", command=show_main_menu, width=15).pack(pady=5)

# Function to deposit money
def deposit():
    global userBalance
    amount = get_amount()
    if amount is not None:
        userBalance += amount
        messagebox.showinfo("Success", f"${amount:.2f} Deposited!")
        show_balance()

# Function to withdraw money
def withdraw():
    global userBalance
    amount = get_amount()
    if amount is not None:
        if userBalance >= amount:
            userBalance -= amount
            messagebox.showinfo("Success", f"${amount:.2f} Withdrawn!")
            show_balance()
        else:
            messagebox.showwarning("Warning", "Insufficient funds!")

# Function to get and validate user input
def get_amount():
    try:
        amount = float(amount_entry.get())
        if amount <= 0:
            messagebox.showwarning("Warning", "Enter a positive amount!")
            return None
        return amount
    except ValueError:
        messagebox.showwarning("Warning", "Enter a valid number!")
        return None

# Create main window
window = Tk()
window.title("E-Bank Simulator Inc.")
window.geometry("300x250")

# Show main menu
show_main_menu()

# Run the application
window.mainloop()

