from datetime import datetime, time
from time import strftime
from tkinter import *
from tkinter import messagebox
import hotel_database


def remove(string):
    return string.replace(" ", "")


# CALCULATE TOTAL AMOUNT AND DUES
def DuesandTotal(p, r, a, d):
    if not r.isdigit() or not a.isdigit() or not p.isdigit() or not d.isdigit():
        messagebox.showerror("Error", "Please Enter Correct Value")

    elif p != "" or r != "" or a != "" or d != "":
        RoomCharges = int(r)
        AdditionalCharges = int(a)
        p = int(p)
        days = int(d)
        if days != 0:
            ex = 200 * p * days
            TotalAmt = (RoomCharges * days) + AdditionalCharges + ex

        else:
            ex = 200 * p
            TotalAmt = RoomCharges + AdditionalCharges + ex

        return TotalAmt
    else:
        pass


# CALCULATE TOTAL AMOUNT AND DUES
def calculateTotal(p, r, a, d):
    if not r.isdigit() or not a.isdigit() or not p.isdigit() or not d.isdigit():
        messagebox.showerror("Error", "Please Enter Correct Value")

    elif p != "" or r != "" or a != "" or d != "":
        RoomCharges = int(r)
        AdditionalCharges = int(a)
        p = int(p)
        days = int(d)
        if days != 0:
            ex = 200 * p * days
            TotalAmt = (RoomCharges * days) + AdditionalCharges + ex

        else:
            ex = 200 * p
            TotalAmt = RoomCharges + AdditionalCharges + ex

        return TotalAmt
    else:
        pass


# DateTime Exceptions
#
# ADD BOOKING RECORD
def addBRecord(CustID, Name, gender, address, Mobile, Email, Nationality, idProoftxt, InDate, OutDate, Adults,
               Kids, TotalDays, roomType, roomno, RoomCharges, ExtraPersons, AdditionalCharges, TotalAmt, AdvAmt):
    InDate = InDate
    OutDate = OutDate
    if CustID == "" or Name == "" or roomno == "" or roomType == "" or Mobile == "" or idProoftxt == "" or \
            InDate == "" or OutDate == "" or TotalDays == "" or roomType == "" or roomno == "" or \
            RoomCharges == "" or ExtraPersons == "" or AdditionalCharges == "" or TotalAmt == "" or AdvAmt == "":
        messagebox.showerror("Error", "All fields are Required")

    try:
        InDate = datetime.strptime(InDate, '%d-%m-%y, %H:%M:%S')
        OutDate = datetime.strptime(OutDate, '%d-%m-%y, %H:%M:%S')

    except ValueError as ve:
        messagebox.showerror("Error", "Please Enter Valid Date and Time!\n" + str(ve))

    if not Mobile.isdigit() or len(Mobile) < 10:
        messagebox.showerror("Error", "Please Input Correct Mobile Number")

    elif not RoomCharges.isdigit() or not ExtraPersons.isdigit() or not AdditionalCharges.isdigit() or not \
            TotalAmt.isdigit() or not AdvAmt.isdigit():
        messagebox.showerror("Error", "Please Enter Correct Input")

    elif InDate > OutDate:
        messagebox.showerror("Error", "check-In Date Cannot Come After Check-Out Date")

    elif rnoaval(roomno, InDate, OutDate, roomType) is True:

        messagebox.showerror("Error", "This Room Is Already Booked, Please Check Room Avalability.")

    elif TotalDays.isdigit() or Mobile.isdigit() or len(
            Mobile) >= 10 or RoomCharges.isdigit() or ExtraPersons.isdigit() or AdditionalCharges.isdigit() or \
            TotalAmt.isdigit() or AdvAmt.isdigit():
        # try:
        remainingAmt = int(TotalAmt) - int(AdvAmt)
        print(OutDate)
        booking = [(CustID, Name, gender, address, Mobile, Email,
                    Nationality, idProoftxt, str(InDate), str(OutDate),
                    Adults, Kids, TotalDays, roomType, roomno, RoomCharges,
                    ExtraPersons, AdditionalCharges, TotalAmt, AdvAmt, remainingAmt
                    )]

        (recordID) = hotel_database.addBookingRecord(booking, CustID)
        print('Last Row ID is :', recordID)
        if len(str(recordID)) != 0:
            messagebox.showinfo("Success", "Entry has been added Successfully!")
        else:
            pass
    else:
        messagebox.showerror("Error", "Invalid Entry!")


def rnoaval(rno, cin, cout, rtype):
    y = False
    if rtype == 'All' or rtype == "":
        data = hotel_database.roomAvailability(cin, cout)
        for row in data:
            if rno == row[1]:
                y = True
                break
            else:
                continue
    if y:
        return True


# SEARCH BOOKING RECORD AND CHECKOUT RECORDS
def search(tree, stxt, svar):
    if stxt != "" and svar != "":
        if svar == "Mobile":
            data = hotel_database.searchBookingRecord(2, stxt)
            if len(data) != 0:
                tree.delete(*tree.get_children())
                for i in data:
                    tree.insert("", END, values=i)
        else:
            data = hotel_database.searchBookingRecord(1, stxt)
            if len(data) != 0:
                tree.delete(*tree.get_children())
                for i in data:
                    tree.insert("", END, values=i)
    else:
        messagebox.showerror("Error", "All Search fields are Required")
