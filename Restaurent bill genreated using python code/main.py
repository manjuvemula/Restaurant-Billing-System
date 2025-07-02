import tkinter as tk
from tkinter import StringVar, Label, Entry, Button
import random
import time

# Create the root window
root = tk.Tk()
root.title("Restaurant Billing System")
root.geometry("800x600")

# Define the frame for placing the widgets
f1 = tk.Frame(root)
f1.grid(padx=20, pady=20)

# Current time
localtime = time.asctime(time.localtime(time.time()))

# Header labels
lblInfo = Label(f1, font=('helvetica', 50, 'bold'), text="MANJUSRI RESTAURANT", fg="Black", bd=10, anchor='w')
lblInfo.grid(row=0, column=0, columnspan=4, pady=(0, 20))

lblInfoTime = Label(f1, font=('arial', 20, 'bold'), text=localtime, fg="Steel Blue", bd=10, anchor='w')
lblInfoTime.grid(row=1, column=0, columnspan=4, pady=(0, 20))

# Function to calculate the cost
def Ref():
    x = random.randint(10908, 500876)
    randomRef = str(x)
    rand.set(randomRef)

    # Extract the quantities from the Entry widgets (defaults to 0 if empty)
    CoFries = float(Fries.get() or 0)
    CoNoodles = float(Noodles.get() or 0)
    CoSoup = float(Soup.get() or 0)
    CoBurger = float(Burger.get() or 0)
    CoSandwich = float(Sandwich.get() or 0)
    CoD = float(Drinks.get() or 0)

    # Calculate the costs of individual items
    CostofFries = CoFries * 140
    CostofDrinks = CoD * 65
    CostofNoodles = CoNoodles * 90
    CostofSoup = CoSoup * 140
    CostBurger = CoBurger * 260
    CostSandwich = CoSandwich * 300

    # Total cost of the meal
    TotalCost = CostofFries + CostofDrinks + CostofNoodles + CostofSoup + CostBurger + CostSandwich
    CostofMeal = "Rs", str('%.2f' % TotalCost)

    # Tax and Service Charge
    PayTax = TotalCost * 0.2
    Ser_Charge = TotalCost / 99

    # Update the variables with calculated values
    Service = "Rs", str('%.2f' % Ser_Charge)
    OverAllCost = "Rs", str('%.2f' % (PayTax + TotalCost + Ser_Charge))
    PaidTax = "Rs", str('%.2f' % PayTax)

    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)

# Function to exit the program
def qExit():
    root.destroy()

# Function to reset the entries
def Reset():
    rand.set("")
    Fries.set("")
    Noodles.set("")
    Soup.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Burger.set("")
    Sandwich.set("")

# StringVar() for entries
rand = StringVar()
Fries = StringVar()
Noodles = StringVar()
Soup = StringVar()
SubTotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
Cost = StringVar()
Burger = StringVar()
Sandwich = StringVar()

# Restaurant Info 1 - Entry fields for items
lblReference = Label(f1, font=('arial', 16, 'bold'), text="Reference", bd=16, anchor="w")
lblReference.grid(row=2, column=0, padx=5, pady=5, sticky="w")
txtReference = Entry(f1, font=('arial', 16, 'bold'), textvariable=rand, bd=10, insertwidth=4, bg="powder blue", justify='right')
txtReference.grid(row=2, column=1, padx=5, pady=5)

lblFries = Label(f1, font=('arial', 16, 'bold'), text="Fries", bd=16, anchor="w")
lblFries.grid(row=3, column=0, padx=5, pady=5, sticky="w")
txtFries = Entry(f1, font=('arial', 16, 'bold'), textvariable=Fries, bd=10, insertwidth=4, bg="powder blue", justify='right')
txtFries.grid(row=3, column=1, padx=5, pady=5)

lblNoodles = Label(f1, font=('arial', 16, 'bold'), text="Noodles", bd=16, anchor="w")
lblNoodles.grid(row=4, column=0, padx=5, pady=5, sticky="w")
txtNoodles = Entry(f1, font=('arial', 16, 'bold'), textvariable=Noodles, bd=10, insertwidth=4, bg="powder blue", justify='right')
txtNoodles.grid(row=4, column=1, padx=5, pady=5)

lblSoup = Label(f1, font=('arial', 16, 'bold'), text="Soup", bd=16, anchor="w")
lblSoup.grid(row=5, column=0, padx=5, pady=5, sticky="w")
txtSoup = Entry(f1, font=('arial', 16, 'bold'), textvariable=Soup, bd=10, insertwidth=4, bg="powder blue", justify='right')
txtSoup.grid(row=5, column=1, padx=5, pady=5)

lblBurger = Label(f1, font=('arial', 16, 'bold'), text="Burger", bd=16, anchor="w")
lblBurger.grid(row=6, column=0, padx=5, pady=5, sticky="w")
txtBurger = Entry(f1, font=('arial', 16, 'bold'), textvariable=Burger, bd=10, insertwidth=4, bg="powder blue", justify='right')
txtBurger.grid(row=6, column=1, padx=5, pady=5)

lblSandwich = Label(f1, font=('arial', 16, 'bold'), text="Sandwich", bd=16, anchor="w")
lblSandwich.grid(row=7, column=0, padx=5, pady=5, sticky="w")
txtSandwich = Entry(f1, font=('arial', 16, 'bold'), textvariable=Sandwich, bd=10, insertwidth=4, bg="powder blue", justify='right')
txtSandwich.grid(row=7, column=1, padx=5, pady=5)

# Restaurant Info 2 - Entry fields for cost and totals
lblDrinks = Label(f1, font=('arial', 16, 'bold'), text="Drinks", bd=16, anchor="w")
lblDrinks.grid(row=2, column=2, padx=5, pady=5, sticky="w")
txtDrinks = Entry(f1, font=('arial', 16, 'bold'), textvariable=Drinks, bd=10, insertwidth=4, bg="powder blue", justify='right')
txtDrinks.grid(row=2, column=3, padx=5, pady=5)

lblCost = Label(f1, font=('arial', 16, 'bold'), text="Cost of Meal", bd=16, anchor="w")
lblCost.grid(row=3, column=2, padx=5, pady=5, sticky="w")
txtCost = Entry(f1, font=('arial', 16, 'bold'), textvariable=Cost, bd=10, insertwidth=4, bg="powder blue", justify='right')
txtCost.grid(row=3, column=3, padx=5, pady=5)

lblService = Label(f1, font=('arial', 16, 'bold'), text="Service Charge", bd=16, anchor="w")
lblService.grid(row=4, column=2, padx=5, pady=5, sticky="w")
txtService = Entry(f1, font=('arial', 16, 'bold'), textvariable=Service_Charge, bd=10, insertwidth=4, bg="powder blue", justify='right')
txtService.grid(row=4, column=3, padx=5, pady=5)

lblStateTax = Label(f1, font=('arial', 16, 'bold'), text="State Tax", bd=16, anchor="w")
lblStateTax.grid(row=5, column=2, padx=5, pady=5, sticky="w")
txtStateTax = Entry(f1, font=('arial', 16, 'bold'), textvariable=Tax, bd=10, insertwidth=4, bg="powder blue", justify='right')
txtStateTax.grid(row=5, column=3, padx=5, pady=5)

lblSubTotal = Label(f1, font=('arial', 16, 'bold'), text="Sub Total", bd=16, anchor="w")
lblSubTotal.grid(row=6, column=2, padx=5, pady=5, sticky="w")
txtSubTotal = Entry(f1, font=('arial', 16, 'bold'), textvariable=SubTotal, bd=10, insertwidth=4, bg="powder blue", justify='right')
txtSubTotal.grid(row=6, column=3, padx=5, pady=5)

lblTotalCost = Label(f1, font=('arial', 16, 'bold'), text="Total Cost", bd=16, anchor="w")
lblTotalCost.grid(row=7, column=2, padx=5, pady=5, sticky="w")
txtTotalCost = Entry(f1, font=('arial', 16, 'bold'), textvariable=Total, bd=10, insertwidth=4, bg="powder blue", justify='right')
txtTotalCost.grid(row=7, column=3, padx=5, pady=5)

# Buttons for calculation, reset, and exit
btnTotal = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Total", bg="powder blue", command=Ref)
btnTotal.grid(row=8, column=1, padx=10, pady=20)

btnReset = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Reset", bg="powder blue", command=Reset)
btnReset.grid(row=8, column=2, padx=10, pady=20)

btnExit = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Exit", bg="powder blue", command=qExit)
btnExit.grid(row=8, column=3, padx=10, pady=20)

# Run the application
root.mainloop()
