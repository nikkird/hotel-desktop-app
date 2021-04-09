from datetime import datetime, time
import sqlite3
from time import strptime
from tkinter import messagebox


def hotelDBconn():
    con = sqlite3.connect("HotelDB.db", detect_types=sqlite3.PARSE_DECLTYPES)
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS bookingrecords (id INTEGER PRIMARY KEY, CustID text NOT NULL UNIQUE, Name "
        "text,Gender text, Address text, Mobile text, Email text, Nationality text, IDProofType text,"
        "CheckinDateTime text,CheckoutDateTime text,Adults text,Child text,TotalDays text, RoomType text,RoomNo text,"
        "RoomCharges text, ExtraPersons text, AdditionalCharges text, TotalAmt text, AdvancePaid text, RemainingAmt "
        "text)")
    con.commit()
    print(sqlite3.version)
    cur.execute(
        "CREATE TABLE IF NOT EXISTS Room (Rid INTEGER PRIMARY KEY, RoomNo text, RoomType)")
    con.commit()
    con.close()


# --------------------PAYDETAILS TABLE FUNCTIONS---------------------------------------------------------------------
def addCheckout(AdditionalCharges="", TotalAmt="", AdvancePaid="", RemainingAmt="", CustID=""):
    con = sqlite3.connect("HotelDB.db")
    cur = con.cursor()
    cur.execute("UPDATE bookingrecords SET AdditionalCharges=?, TotalAmt=?, AdvancePaid=?, RemainingAmt=? WHERE "
                "CustID=?", (AdditionalCharges, TotalAmt, AdvancePaid, RemainingAmt, CustID))
    con.commit()
    cur.execute('SELECT Name FROM bookingrecords WHERE CustID=?', (CustID,))
    name = cur.fetchone()[0]
    cur.close()
    con.close()
    return name


def viewPayRecord():
    con = sqlite3.connect("HotelDB.db")
    cur = con.cursor()
    now = datetime.now()
    DateNow = now.strftime("%Y-%m-%d %H:%M:%S")
    cur.execute('SELECT * FROM bookingrecords WHERE CheckoutDateTime > ? ORDER BY CheckoutDateTime DESC', (DateNow,))
    rows = cur.fetchall()
    cur.close()
    con.close()
    print(rows)
    return rows


# --------------------BOOKING RECORDS TABLE FUNCTIONS---------------------------------------------------------------------
def addBookingRecord(booking, CustID):
    con = sqlite3.connect("HotelDB.db")
    cur = con.cursor()
    cur.execute('SELECT id FROM bookingrecords WHERE CustID=?', (CustID,))
    data = cur.fetchall()
    if len(data) == 0:

        sql_booking = " INSERT OR IGNORE INTO bookingrecords(" \
                      "CustID, Name, Gender, Address, Mobile, Email, Nationality, IDProofType, CheckinDateTime, " \
                      "CheckoutDateTime, Adults, Child, TotalDays, RoomType, RoomNo, RoomCharges, ExtraPersons, " \
                      "AdditionalCharges, TotalAmt, AdvancePaid, RemainingAmt) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?," \
                      "?,?,?,?,?,?); "
        cur = con.cursor()
        cur.executemany(sql_booking, booking)
        con.commit()

        cur.execute('SELECT max( id ) FROM bookingrecords')
        max_id = cur.fetchone()[0]
        return max_id
    else:
        messagebox.showerror("Error", "Booking ID Already Exists, Reset And Try Again!")

    cur.close()
    con.close()


def viewBookingRecord():
    con = sqlite3.connect("HotelDB.db")
    cur = con.cursor()
    cur.execute('SELECT id, CustID, Name, Gender, Address, Mobile, Email, Nationality, IDProofType, CheckinDateTime, '
                'CheckoutDateTime, Adults, Child, TotalDays, RoomType, RoomNo, RoomCharges, ExtraPersons, '
                'AdditionalCharges, TotalAmt, AdvancePaid, RemainingAmt FROM bookingrecords ORDER BY id DESC')
    # [('2021-03-27 15:51:04', '2021-03-31 15:51:04'), ('2021-03-28 16:10:48', '2021-04-02 16:10:48')]
    rows = cur.fetchall()
    con.close()
    return rows


def deleteBookingRecord(id):
    con = sqlite3.connect("HotelDB.db")
    cur = con.cursor()

    query = 'DELETE FROM bookingrecords WHERE CustID=?'
    cur.execute(query, (id,))
    con.commit()
    RC = cur.rowcount
    cur.close()
    con.close()
    if RC > 1:
        return 'Successfully Deleted Database Record', RC


def searchBookingRecord(c, txt):
    con = sqlite3.connect("HotelDB.db")
    cur = con.cursor()
    if c == 1:
        cur.execute("SELECT * FROM bookingrecords WHERE Name LIKE ?", ('%' + txt + '%',))
        rows = cur.fetchall()
        return rows
    elif c == 2:
        cur.execute("SELECT * FROM bookingrecords WHERE Mobile LIKE ?", (txt,))
        rows = cur.fetchall()
        return rows
    con.close()


def updateBookingRecord(Name="", Gender="", Address="", Mobile="", Email="", Nationality="", IDProofType="",
                        CheckinDateTime="", CheckoutDateTime="", Adults="", Child="", TotalDays="", RoomType="",
                        RoomNo="", RoomCharges="", ExtraPersons="", AdditionalCharges="", TotalAmt="", AdvancePaid="",
                        RemainingAmt="", CustID=""):
    con = sqlite3.connect("HotelDB.db")
    cur = con.cursor()
    cur.execute("UPDATE bookingrecords SET Name=?, Gender=?, Address=?, Mobile=?, Email=?, Nationality=?, "
                "IDProofType=?, CheckinDateTime=?, CheckoutDateTime=?, Adults=?, Child=?, TotalDays=?, RoomType=?, "
                "RoomNo=?, RoomCharges=?, ExtraPersons=?, AdditionalCharges=?, TotalAmt=?, AdvancePaid=?, "
                "RemainingAmt=? WHERE CustID=?",
                (Name, Gender, Address, Mobile, Email, Nationality, IDProofType, CheckinDateTime, CheckoutDateTime,
                 Adults, Child, TotalDays, RoomType, RoomNo, RoomCharges, ExtraPersons, AdditionalCharges, TotalAmt,
                 AdvancePaid, RemainingAmt, CustID))
    con.commit()
    con.close()


# --------------------ROOM TABLE FUNCTIONS---------------------------------------------------------------------
def updateRoomRecord(roomtype="", roomno=""):
    con = sqlite3.connect("HotelDB.db")
    cur = con.cursor()
    cur.execute("UPDATE Room SET  RoomType=? WHERE RoomNo=?",
                (roomtype, roomno))
    con.commit()
    con.close()


def addRoomRecord(booking):
    con = sqlite3.connect("HotelDB.db", detect_types=sqlite3.PARSE_DECLTYPES)
    cur = con.cursor()

    sql_booking = " INSERT OR IGNORE INTO Room(" \
                  "RoomNo, RoomType) VALUES(?,?); "
    cur.executemany(sql_booking, booking)
    con.commit()
    cur.close()
    con.close()


def viewRoomRecord():
    con = sqlite3.connect("HotelDB.db")
    cur = con.cursor()
    cur.execute('SELECT * FROM Room')
    rows = cur.fetchall()
    con.close()
    return rows


def deleteRoomRecord(id):
    con = sqlite3.connect("HotelDB.db")
    cur = con.cursor()

    query = 'DELETE FROM Room WHERE RoomNo=?'
    cur.execute(query, (id,))
    con.commit()
    RC = cur.rowcount
    cur.close()
    con.close()
    if RC > 1:
        return 'Successfully Deleted Room Table Record', RC


def hotelStats(din, dout):
    con = sqlite3.connect("HotelDB.db")
    cur = con.cursor()
    cur.execute('SELECT * FROM bookingrecords WHERE (CheckinDateTime BETWEEN '
                '? AND ?) OR (CheckoutDateTime BETWEEN ? AND ?)', (din, dout, din, dout))
    rows = cur.fetchall()
    print(rows)
    cur.close()
    con.close()
    return rows


def roomAvailability(din, dout):
    try:
        con = sqlite3.connect("HotelDB.db", detect_types=sqlite3.PARSE_DECLTYPES)
        cur = con.cursor()
        cur.execute('SELECT CheckinDateTime, CheckoutDateTime FROM bookingrecords')
        r = cur.fetchall()
        # [('2021-03-27 15:51:04', '2021-03-31 15:51:04'), ('2021-03-28 16:10:48', '2021-04-02 16:10:48')]
        cur.execute('SELECT * FROM Room WHERE Roomno NOT IN ( '
                    'SELECT RoomNo FROM bookingrecords WHERE '
                    '(CheckinDateTime BETWEEN ? AND ?) '
                    'OR (CheckoutDateTime BETWEEN ? AND ?) )', (din, dout, din, dout))
        rows = cur.fetchall()

        cur.close()
        con.close()
        return rows
    except sqlite3.Error as e:
        print("Something Went Wrong: ", e)
        return ""


hotelDBconn()
