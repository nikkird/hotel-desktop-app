from datetime import datetime
import time
from random import randint
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import backend
import hotel_database
import preview_window
import pdf_generate

Font_label = ("Franklin Gothic Medium Cond", 10)
Font_txthead = ("Courier", 11, "bold")
Font_txt = ("Bookman Old Style", 11, "italic")
Font_entry = ("Bookman Old Style", 10)
Font_btn_title = ("Bookman Old Style", 10, "bold")

# ----------- main project----------------------------------------------------------------------------
class HotelApp:
    def __init__(self, root):
        self.root = root
        themestyle = ttk.Style(self.root)
        st = themestyle.theme_names()
        print(st)
        current_theme = themestyle.theme_use('clam')
        # ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')

        self.root.geometry('1080x730+0+0')
        self.root.minsize(width=1080, height=730)
        self.root.maxsize(width=1080, height=730)
        self.root.configure(bg='#90B2B2')
        self.root.title("Hotel Vishwa Chakra - Front Desk App")
        titleBarIcon = PhotoImage(file='images/hvcicon.png')
        self.root.iconphoto(False, titleBarIcon)
        # --------------TIME-------------------------------------------------------------------------
        n = datetime.now()
        self.now = n.strftime("%H:%M:%S")
        # ----------------STRVAR DATABASE VARIABLES --------------------------------------------
        self.CustID = StringVar()
        self.Name = StringVar()
        self.recordID = StringVar()
        self.Address = StringVar()
        self.Gender = StringVar()
        self.Mobile = StringVar()
        self.Nationality = StringVar()
        self.IdProof = StringVar()
        self.DateIn = StringVar()
        self.DateOut = StringVar()
        self.Email = StringVar()
        self.TotalDays = StringVar()
        self.SearchVar = StringVar()
        self.Roomno = StringVar()
        self.DateIn.set(time.strftime("%d-%m-%y, %H:%M:%S"))
        self.DateOut.set(time.strftime("%d-%m-%y, %H:%M:%S"))
        self.RoomType = StringVar()
        self.totalDays = StringVar()
        self.Adults = StringVar()
        self.Kids = StringVar()
        self.AdditionalCharges = StringVar()
        self.AdvAmt = StringVar()
        self.RoomCharges = StringVar()
        self.ExtraPersons = StringVar()
        self.TotalAmt = StringVar()
        self.remainingAmt = StringVar()

        x = randint(1000, 9999)
        randomRef = str(x)
        d = str(time.strftime("%m%d%y"))
        self.CustID.set("HV" + randomRef + d)

        self.today = StringVar()
        self.today.set(time.strftime("%d-%m-%y, %H:%M:%S"))
        self.totalDaysP = StringVar()
        self.RoomTypeP = StringVar()
        self.RoomnoP = StringVar()
        self.RoomChargesP = StringVar()
        self.ExtraPersonsP = StringVar()
        self.AdditionalChargesP = StringVar()
        self.TotalAmtP = StringVar()
        self.AdvAmtP = StringVar()
        self.CustIDP = StringVar()
        self.NameP = StringVar()
        self.DateInP = StringVar()
        self.DateOutP = StringVar()
        self.MobileP = StringVar()
        self.AdultsP = StringVar()
        self.KidsP = StringVar()
        self.EmailP = StringVar()
        self.AddressP = StringVar()

        # ---------------Hotel TITLE-----------------------------------------------------------------------------

        title_frame = Frame(self.root, height=70, width=1080, bg='#258389')
        title_frame.place(x=0, y=0)
        self.title_label = Label(title_frame, text='Hotel Vishwa Chakra', font=('Harrington', 38, 'bold'), fg='white',
                              bg='#258389',
                              height=60)
        self.title_label.pack(anchor='center')
        title_frame.pack_propagate(False)

        # ---------------BOTTOM FRAME TOGGLES--------------------------------------------------------------------
        toggleFrame = Frame(self.root, height=140, width=1080, highlightthickness=4, highlightbackground='#90B2B2',
                        highlightcolor='#90B2B2', bg='lavender')
        toggleFrame.place(x=0, y=585)
        self.path1 = "C:/Users/win/PycharmProjects/hFDapp/images/hotelstats.png"
        img = Image.open(self.path1)
        image = img.resize((213, 100), Image.ANTIALIAS)
        self.img1 = ImageTk.PhotoImage(image)
        self.btn1 = Button(toggleFrame, image=self.img1, text='b2', bg='lavender', width=213,
                           command=self.hotelStatusFrame)
        self.btn1.image = self.img1
        self.btn1.place(x=0, y=0)

        self.path2 = "C:/Users/win/PycharmProjects/hFDapp/images/room.png"
        img = Image.open(self.path2)
        image = img.resize((213, 100), Image.ANTIALIAS)
        self.img2 = ImageTk.PhotoImage(image)
        self.btn2 = Button(toggleFrame, image=self.img2, text='b1', bg='lavender', width=213, command=self.roomFrame)
        self.btn2.image = self.img2
        self.btn2.place(x=215, y=0)

        self.path3 = 'C:/Users/win/PycharmProjects/hFDapp/images/booking.png'
        img = Image.open(self.path3)
        image = img.resize((213, 100), Image.ANTIALIAS)
        self.img3 = ImageTk.PhotoImage(image)
        self.btn3 = Button(toggleFrame, image=self.img3, text='b2', bg='lavender', width=213, command=self.BookingFrame)
        self.btn3.image = self.img3
        self.btn3.place(x=215 * 2, y=0)

        self.path4 = 'C:/Users/win/PycharmProjects/hFDapp/images/checkout.png'
        img = Image.open(self.path4)
        image = img.resize((213, 100), Image.ANTIALIAS)
        self.img4 = ImageTk.PhotoImage(image)
        self.btn4 = Button(toggleFrame, image=self.img4, text='b2', bg='lavender', width=213,
                           command=self.paymentsFrame)
        self.btn4.image = self.img4
        self.btn4.place(x=215 * 3, y=0)

        self.path5 = 'C:/Users/win/PycharmProjects/hFDapp/images/exit.png'
        img = Image.open(self.path5)
        image = img.resize((212, 100), Image.ANTIALIAS)
        self.img5 = ImageTk.PhotoImage(image)
        self.btn5 = Button(toggleFrame, image=self.img5, text='b2', bg='lavender', width=212, height=100,
                           command=self.exitapp)
        self.btn5.image = self.img5
        self.btn5.place(x=215 * 4, y=0)

        Label(toggleFrame, text='Hotel Status', font=Font_btn_title, bg='lavender').place(x=50, y=110)
        Label(toggleFrame, text='Rooms', font=Font_btn_title, bg='lavender').place(x=286, y=110)
        Label(toggleFrame, text='Reservation', font=Font_btn_title,bg='lavender').place(x=246 * 2, y=110)
        Label(toggleFrame, text='Check-Out', font=Font_btn_title, bg='lavender').place(x=236 * 3, y=110)
        Label(toggleFrame, text='Exit', font=Font_btn_title, bg='lavender').place(x=236 * 4, y=110)
        toggleFrame.pack_propagate(False)

        # -------------------extra frame--------------------------------------------------------------------------------
        sep = Frame(self.root, height=4, width=1080, bg='white')
        sep.place(x=0, y=70)

        self.BookingFrame()
        mainloop()

    # ----------------hotel status and default page-------------------------------------------------------------------------------
    def hotelStatusFrame(self):
        b_frame = Frame(self.root, height=510, width=1080, bg='gray89', highlightthickness=4,
                        highlightbackground='#90B2B2', highlightcolor='#90B2B2', relief=RIDGE)

        b_frame.place(x=0, y=70 + 6)
        b_frame.pack_propagate(False)
        b_frame.tkraise()
        topFrame = LabelFrame(b_frame, text="Check No. Of Guests Staying", width=1080, height=35, padx=2, highlightthickness=2, highlightbackground='#90B2B2',
                         highlightcolor='#90B2B2', relief=RIDGE)
        topFrame.pack(side=TOP, fill='both', expand='True')
        topFrame2 = Frame(b_frame, highlightthickness=3, highlightbackground='#90B2B2', highlightcolor='#90B2B2',
                          bg='white', width=1080, height=470, padx=2, relief=RIDGE)
        topFrame2.pack(side=BOTTOM, fill='both', expand='True')
        topFrame.pack_propagate(0)
        topFrame2.pack_propagate(0)

        # -----------------SERACH ID BOX ----------------------------------------------------------
        self.Dfrom = StringVar()
        self.Dto = StringVar()
        self.Dfrom.set(time.strftime("%d-%m-%y, %H:%M:%S"))
        self.Dto.set(time.strftime("%d-%m-%y, %H:%M:%S"))

        self.lbl_searchb = Label(topFrame, font=Font_label, text='Date - From: ', padx=10)
        self.lbl_searchb.grid(row=0, column=0, sticky=W)
        self.in_searchbthis = Entry(topFrame, font=Font_label, textvariable=self.Dfrom)
        self.in_searchbthis.grid(row=0, column=1, pady=2, padx=1)
        self.lbl_searchb = Label(topFrame, font=Font_label, text='To: ', padx=1)
        self.lbl_searchb.grid(row=0, column=2, sticky=W)
        self.in_searchbthat = Entry(topFrame, font=Font_label, textvariable=self.Dto)
        self.in_searchbthat.grid(row=0, column=3, pady=2, padx=1)

        self.btnsearchb = Button(topFrame,width=20, activeforeground='black', activebackground='lavender', foreground="white", bg="black", font=Font_label, text="SEARCH", command=self.searchStats)
        self.btnsearchb.grid(row=0, column=4, padx=2, pady=12)
        # -------------TREEVIEW for DISPLAYING RECORDS---------------------------------------------------
        style = ttk.Style()
        style.configure('Treeview.Heading', font=("Franklin Gothic Medium Cond", 10))
        style.configure('Treeview', background='lavender',
                        foreground='Black')
        self.htreeframe = ttk.Treeview(topFrame2, selectmode='browse')
        scroll_x = ttk.Scrollbar(topFrame2,
                                 orient="horizontal",
                                 command=self.htreeframe.xview)
        scroll_x.pack(side='bottom', fill='x')
        self.htreeframe.configure(xscrollcommand=scroll_x.set)
        scroll_y = ttk.Scrollbar(topFrame2,
                                 orient="vertical",
                                 command=self.htreeframe.yview)
        scroll_y.configure(command=self.htreeframe.yview)
        scroll_y.pack(side='right', fill='y')
        self.htreeframe.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        self.htreeframe["columns"] = (
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
            "20",
            "21", "22")
        self.htreeframe.column("1", anchor='c', minwidth=0, width=60)
        self.htreeframe.column("2", anchor='c')
        self.htreeframe.column("3", anchor='c')
        self.htreeframe.column("4", anchor='c')
        self.htreeframe.column("5", anchor='c')
        self.htreeframe.column("6", anchor='c')
        self.htreeframe.column("7", anchor='c')
        self.htreeframe.column("8", anchor='c')
        self.htreeframe.column("9", anchor='c')
        self.htreeframe.column("10", anchor='c')
        self.htreeframe.column("11", anchor='c')
        self.htreeframe.column("12", anchor='c')
        self.htreeframe.column("13", anchor='c')
        self.htreeframe.column("14", anchor='c')
        self.htreeframe.column("15", anchor='c')
        self.htreeframe.column("16", anchor='c')
        self.htreeframe.column("17", anchor='c')
        self.htreeframe.column("18", anchor='c')
        self.htreeframe.column("19", anchor='c')
        self.htreeframe.column("20", anchor='c')
        self.htreeframe.column("21", anchor='c')
        self.htreeframe.column("22", anchor='c')

        self.htreeframe.heading("1", text="Sr.No.")
        self.htreeframe.heading("2", text="Booking ID")
        self.htreeframe.heading("3", text="Name")
        self.htreeframe.heading("4", text="Gender")
        self.htreeframe.heading("5", text="Address")
        self.htreeframe.heading("6", text="Mobile")
        self.htreeframe.heading("7", text="Email")
        self.htreeframe.heading("8", text="Nationality")
        self.htreeframe.heading("9", text="ID Proof Type")
        self.htreeframe.heading("10", text="Check In")
        self.htreeframe.heading("11", text="Check Out")
        self.htreeframe.heading("12", text="Adults")
        self.htreeframe.heading("13", text="Child")
        self.htreeframe.heading("14", text="Total Days")
        self.htreeframe.heading("15", text="Room Type")
        self.htreeframe.heading("16", text="Room No")
        self.htreeframe.heading("17", text="Room Charges")
        self.htreeframe.heading("18", text="Extra Persons")
        self.htreeframe.heading("19", text="Additional Charges")
        self.htreeframe.heading("20", text="Total Amount")
        self.htreeframe.heading("21", text="Advance Paid")
        self.htreeframe.heading("22", text="Remaining Amount")
        self.htreeframe['show'] = 'headings'
        self.htreeframe.pack(side=RIGHT, fill='both', expand='True')

        # -------------Widget BUTTONS--------------------------------------------------------------------------

        self.btnView1 = Button(topFrame, width=20, activeforeground='black', activebackground='lavender', foreground="white", bg="black",font=Font_label, text="View All", command=self.hsViewAl())
        self.btnView1.place(x=910, y=10)

    # ========== SEARCH STATS FUNCTION---------------------------------------------------------------------
    def searchStats(self):
        records = self.htreeframe.get_children()
        for idx in records:
            self.htreeframe.delete(idx)
        checkInDate = datetime.strptime(self.Dfrom.get(), '%d-%m-%y, %H:%M:%S')
        checkOutDate = datetime.strptime( self.Dto.get(), '%d-%m-%y, %H:%M:%S')
        for row in hotel_database.hotelStats(str(checkInDate), str(checkOutDate)):
            if len(row) == 0:
                messagebox.showinfo("System Manager", "Couldn't Find Any Records.")
            else:
                print(row)
                # --------- CHECK IN DATE ------------------
                r = row[9].split("-")
                y1 = r[2].split(" ")
                t1 = y1[1].split(":")
                row9 = y1[0] + "-" + r[1] + "-" + r[0][2:] + ", " + t1[0] + ":" + t1[1] + ":" + t1[2]

                # --------- CHECK OUT DATE ------------------
                r = row[10].split("-")
                y1 = r[2].split(" ")
                t1 = y1[1].split(":")
                # row9 = datetime(int(r[0]), int(r[1]), int(y1[0]), int(t1[0]), int(t1[1]), int(t1[2]))
                # row9.strftime('%d-%m-%y %H:%M:%S')
                row10 = y1[0] + "-" + r[1] + "-" + r[0][2:] + ", " + t1[0] + ":" + t1[1] + ":" + t1[2]

                self.htreeframe.insert("", END, values=(row[0],
                                                    row[1],
                                                    row[2],
                                                    row[3],
                                                    row[4],
                                                    row[5],
                                                    row[6],
                                                    row[7],
                                                    row[8],
                                                    row9,
                                                    row10,
                                                    row[11],
                                                    row[12],
                                                    row[13],
                                                    row[14],
                                                    row[15],
                                                    row[16],
                                                    row[17],
                                                    row[18],
                                                    row[19],
                                                    row[20],
                                                    row[21]))

    def hsViewAl(self):
        records = self.htreeframe.get_children()
        for idx in records:
            self.htreeframe.delete(idx)
        for row in hotel_database.viewBookingRecord():
            # --------- CHECK IN DATE ------------------
            r = row[9].split("-")
            y1 = r[2].split(" ")
            t1 = y1[1].split(":")
            row9 = y1[0] + "-" + r[1] + "-" + r[0][2:] + ", " + t1[0] + ":" + t1[1] + ":" + t1[2]

            # --------- CHECK OUT DATE ------------------
            r = row[10].split("-")
            y1 = r[2].split(" ")
            t1 = y1[1].split(":")
            # row9 = datetime(int(r[0]), int(r[1]), int(y1[0]), int(t1[0]), int(t1[1]), int(t1[2]))
            # row9.strftime('%d-%m-%y %H:%M:%S')
            row10 = y1[0] + "-" + r[1] + "-" + r[0][2:] + ", " + t1[0] + ":" + t1[1] + ":" + t1[2]

            self.htreeframe.insert("", END, values=(row[0],
                                                        row[1],
                                                        row[2],
                                                        row[3],
                                                        row[4],
                                                        row[5],
                                                        row[6],
                                                        row[7],
                                                        row[8],
                                                        row9,
                                                        row10,
                                                        row[11],
                                                        row[12],
                                                        row[13],
                                                        row[14],
                                                        row[15],
                                                        row[16],
                                                        row[17],
                                                        row[18],
                                                        row[19],
                                                        row[20],
                                                        row[21]))

    # -------------- STAFF INFO -----------------------------------------------------------------------------------------
    def staff(self):
        b_frame = Frame(self.root, height=510, width=1080, bg='gray89', relief=RIDGE)
        b_frame.place(x=0, y=70 + 6 + 20 + 60 + 11)
        b_frame.pack_propagate(False)
        b_frame.tkraise()
        topFrame = Frame(b_frame, width=1080, height=350, padx=2, relief=RIDGE)
        topFrame.pack()

    # -------------- ROOM INFORMATION-----------------------------------------------------------------------------------

    def roomFrame(self):
        b_frame = Frame(self.root, height=510, width=1080, highlightthickness=4, highlightbackground='#90B2B2',
                        highlightcolor='#90B2B2', bg='gray89', relief=RIDGE)
        b_frame.place(x=0, y=70 + 6)
        b_frame.pack_propagate(False)
        b_frame.tkraise()
        topFrame = Frame(b_frame, width=1080, height=510, highlightthickness=3,
                         highlightbackground='#90B2B2', highlightcolor='#90B2B2', relief=RIDGE)
        topFrame.pack(side=TOP, fill='both', expand='True')
        topFrame.pack_propagate(0)
        left_frame = Frame(topFrame, bg='white', width=535, height=510, padx=5, highlightthickness=4,
                           highlightbackground='#90B2B2', highlightcolor='#90B2B2', relief=RIDGE)
        right_frame = Frame(topFrame, bg='white', width=535, height=510, padx=5, highlightthickness=4,
                            highlightbackground='#90B2B2', highlightcolor='#90B2B2', relief=RIDGE)
        left_frame.pack(side=LEFT, fill='both', expand='True')
        right_frame.pack(side=RIGHT, fill='both')

        right_frame.pack_propagate(0)
        left_frame.pack_propagate(0)

        Aframe = LabelFrame(left_frame, fg='black', text='Search Room Availability Between:', width=520,
                            height=250,
                            bg='white',
                            pady=1, relief=RIDGE)
        Aframe.pack(side=TOP, fill='both', expand='True', anchor="center")
        Aframe.pack_propagate(0)
        Bframe = LabelFrame(left_frame, bd=4, fg='black', text="Available Rooms", width=520, height=250,
                            bg='lavender',
                            pady=1, relief=RIDGE)
        Bframe.pack(side=BOTTOM, fill='both', expand='True')
        Bframe.pack_propagate(0)
        Cframe = LabelFrame(right_frame, fg='black', text="Edit Room No. and Type", width=520,
                            height=250,
                            bg='white',
                            pady=1, relief=RIDGE)
        Cframe.pack(side=TOP, fill='both', expand='True', anchor='center')
        Cframe.pack_propagate(0)
        Dframe = LabelFrame(right_frame, bd=4, fg='black', text="View All Rooms", width=520, height=250,
                            bg='lavender',
                            pady=1, relief=RIDGE)
        Dframe.pack(side=BOTTOM, fill='both', expand='True')
        Dframe.pack_propagate(0)

        # --------------LABELS ----------------------------------------------------------------------------------
        style = ttk.Style()
        # ---------------------LABELS IN LEFT LABELFRAME------------------------------------------------------

        self.lbl_checkInDate = Label(Aframe, font=Font_label, bg="white", text='From Date: ', pady=4)
        self.lbl_checkInDate.grid(row=1, column=0, padx=20, sticky=E)
        self.in_FcheckInDate = Entry(Aframe, font=Font_label, justify='center', textvariable=self.DateIn,
                                     width=17)
        self.in_FcheckInDate.grid(row=2, column=0, ipady=4, padx=20, sticky=E)


        self.lbl_checkOutDate = Label(Aframe, font=Font_label, bg="white", text='To Date:  ', pady=4)
        self.lbl_checkOutDate.grid(row=1, column=1, sticky=W)
        self.in_TcheckOutDate = Entry(Aframe, bd=1, font=Font_label, justify='center', textvariable=self.DateOut,
                                      width=17)
        self.in_TcheckOutDate.grid(row=2, column=1, ipady=4, sticky=W)

        self.lbl_roomType = Label(Aframe, font=Font_label, bg="white", text='Room Type: ', pady=8, padx=20)
        self.lbl_roomType.grid(row=3, column=0, sticky=E)
        self.RoomTypeR = StringVar()
        self.in_roomType = ttk.Combobox(Aframe,
                                        font=Font_entry, textvariable=self.RoomTypeR, width=15)
        self.in_roomType.option_add('*TCombobox*Listbox.Justify', 'center')
        self.in_roomType['values'] = ('All',
                                      'Deluxe (Single)',
                                      'Deluxe (Double)',
                                      'Super Deluxe (Single)',
                                      'Super Deluxe (Double)',
                                      'Triple Bed (Double)',
                                      'Family (Double)',
                                      'A/C Room (Single)',
                                      'A/C Room (Double)'
                                      )
        self.in_roomType.current(0)
        self.in_roomType.grid(row=3, column=1, sticky=W)

        self.btnSearch = Button(Aframe, activeforeground='black', activebackground='lavender', foreground="white", bg="black", font=Font_label, text="Search Availability",
                                command=self.availableRoomChecker, width=40)
        self.btnSearch.grid(row=4, column=0, columnspan=2, pady=10, ipady=4, padx=70, sticky='nsew')

        # -------------TABLE for DISPLAYING AVAILABLE ROOMS---------------------------------------------------

        style.configure("Treeview.Heading",
                        background="Paleturquoise3", foreground="black", relief="flat")
        style.map("Custom.Treeview.Heading",
                  relief=[('active', 'groove'), ('pressed', 'sunken')])
        style.configure('Treeview', background='lavender',
                        foreground='Black')
        self.roomAvTable = ttk.Treeview(Bframe, selectmode='browse')
        scroll_x = ttk.Scrollbar(Bframe,
                                 orient="horizontal",
                                 command=self.roomAvTable.xview)
        scroll_x.pack(side='bottom', fill='x')
        self.roomAvTable.configure(xscrollcommand=scroll_x.set)
        scroll_y = ttk.Scrollbar(Bframe,
                                 orient="vertical",
                                 command=self.roomAvTable.yview)
        scroll_y.configure(command=self.roomAvTable.yview)
        scroll_y.pack(side='right', fill='y')
        self.roomAvTable.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        self.roomAvTable["columns"] = ("1", "2", "3")
        self.roomAvTable.column("1", anchor='c', width=20)
        self.roomAvTable.column("2", anchor='c', width=20)
        self.roomAvTable.column("3", anchor='c', width=20)

        self.roomAvTable.heading("1", text="Sr.No.")
        self.roomAvTable.heading("2", text="Room No")
        self.roomAvTable.heading("3", text="Room Type")

        self.roomAvTable['show'] = 'headings'
        self.roomAvTable.pack(side=BOTTOM, fill='both', expand='True')

        # -------------Widget BUTTONS--------------------------------------------------------------------------
        self.lbl_roomno = Label(Cframe, font=Font_label, bd=3,
                                text='Room No: ', bg="white", padx=1)
        self.lbl_roomno.grid(row=0, column=0, sticky=E)
        self.in_roomno = Entry(Cframe, font=Font_label, textvariable=self.Roomno, width=20)
        self.in_roomno.grid(row=0, column=1, pady=10, ipady=4, sticky=W)
        self.RoomTypeA = StringVar()
        self.lbl_roomType = Label(Cframe, font=Font_label, bd=3, bg="white", text='Room Type: ', padx=1)
        self.lbl_roomType.grid(row=1, column=0, sticky=E)
        self.in_roomType = ttk.Combobox(Cframe,
                                        font=Font_entry, textvariable=self.RoomTypeA, width=18)
        self.in_roomType.option_add('*TCombobox*Listbox.Justify', 'center')
        self.in_roomType['values'] = ('',
                                      'Deluxe (Single)',
                                      'Deluxe (Double)',
                                      'Super Deluxe (Single)',
                                      'Super Deluxe (Double)',
                                      'Triple Bed (Double)',
                                      'Family (Double)',
                                      'A/C Room (Single)',
                                      'A/C Room (Double)'
                                      )
        self.in_roomType.current(0)
        self.in_roomType.grid(row=1, column=1, pady=10, ipady=4, sticky=W)

        self.btnAddNew = Button(Cframe, activeforeground='black', activebackground='lavender', foreground="white", bg="black", font=Font_label, text="Submit",
                                command=self.addroom, width=18)
        self.btnAddNew.grid(row=2, column=0, padx=50, ipady=4, pady=10, sticky="nsew")

        self.btnView = Button(Cframe, activeforeground='black', activebackground='lavender', foreground="white", bg="black", font=Font_label, text="View/Refresh",
                              command=self.displayRooms, width=18)
        self.btnView.grid(row=2, column=1, padx=5, ipady=4, pady=10, sticky="nsew")

        self.btnDelete = Button(Cframe, activeforeground='black', activebackground='lavender', foreground="white", bg="black", font=Font_label, text="Delete",
                                command=self.deleteRoom, width=18)
        self.btnDelete.grid(row=3, column=0, padx=50, ipady=4, pady=10, sticky="nsew")

        self.btnUpdate = Button(Cframe, activeforeground='black', activebackground='lavender', foreground="white", bg="black", font=Font_label, text="Update",
                                command=self.updateRoom, width=18)
        self.btnUpdate.grid(row=3, column=1, padx=5, ipady=4, pady=10, sticky="nsew")

        # -------------TABLE for DISPLAYING CURRENT RECORDS---------------------------------------------------
        style = ttk.Style()

        style.configure("Treeview.Heading",
                        background="Paleturquoise3", foreground="black", relief="flat")
        style.map("Custom.Treeview.Heading",
                  relief=[('active', 'groove'), ('pressed', 'sunken')])
        style.configure('Treeview', background='lavender',
                        foreground='Black')
        self.roomInfoTable = ttk.Treeview(Dframe, selectmode='browse')
        scroll_x = ttk.Scrollbar(Dframe,
                                 orient="horizontal",
                                 command=self.roomInfoTable.xview)
        scroll_x.pack(side='bottom', fill='x')
        self.roomInfoTable.configure(xscrollcommand=scroll_x.set)
        scroll_y = ttk.Scrollbar(Dframe,
                                 orient="vertical",
                                 command=self.roomInfoTable.yview)
        scroll_y.configure(command=self.roomInfoTable.yview)
        scroll_y.pack(side='right', fill='y')
        self.roomInfoTable.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        self.roomInfoTable["columns"] = ("1", "2", "3")
        self.roomInfoTable.column("1", anchor='c', width=20)
        self.roomInfoTable.column("2", anchor='c', width=20)
        self.roomInfoTable.column("3", anchor='c', width=20)

        self.roomInfoTable.heading("1", text="Sr.No.")
        self.roomInfoTable.heading("2", text="Room No")
        self.roomInfoTable.heading("3", text="Room Type")

        self.roomInfoTable['show'] = 'headings'
        self.roomInfoTable.pack(side=BOTTOM, fill='both', expand='True')

    def resetP(self):
        self.totalDaysP.set('')
        self.RoomTypeP.set('')
        self.RoomnoP.set('')
        self.RoomChargesP.set('')
        self.ExtraPersonsP.set('')
        self.AdditionalChargesP.set('')
        self.TotalAmtP.set('')
        self.AdvAmtP.set('')
        self.CustIDP.set('')
        self.NameP.set('')
        self.DateInP.set('')
        self.DateOutP.set('')
        self.in_DueAmt.delete(0, END)

    # --------------- CHECKOUT FRAME--------------------------------------------------------------

    def paymentsFrame(self):
        b_frame = Frame(self.root, height=510, width=1080, highlightthickness=4, highlightbackground='#90B2B2',
                        highlightcolor='#90B2B2', bg='gray89', relief=RIDGE)
        b_frame.place(x=0, y=70 + 6)
        b_frame.pack_propagate(False)
        b_frame.tkraise()
        topFrame = Frame(b_frame, width=1080, height=510, padx=2, highlightthickness=3,
                         highlightbackground='#90B2B2', highlightcolor='#90B2B2', relief=RIDGE)
        topFrame.pack()
        topFrame.pack_propagate(0)
        right_frame = Frame(topFrame, bg='white', width=740, height=400, padx=5, highlightthickness=2,
                            highlightbackground='#90B2B2', highlightcolor='#90B2B2', relief=RIDGE)
        left_frame = Frame(topFrame, bg='white', width=400, height=400, highlightthickness=2,
                           highlightbackground='#90B2B2', highlightcolor='#90B2B2', pady=5, relief=RIDGE)

        bottom_frame = Frame(right_frame, bg='white', width=1080, height=60, padx=4, pady=2,
                             highlightthickness=2,
                             highlightbackground='#90B2B2', highlightcolor='#90B2B2', relief=RIDGE)
        # c_frame = LabelFrame(right_frame, fg='white', text="ROOMS", width=300, height=400, bg='#90B2B2', pady=5,
        #                    relief=RIDGE)

        m_frame = LabelFrame(right_frame, fg='black', text="Customer Details", width=340, height=400, bg='white',
                             pady=5, relief=RIDGE)

        left_frame.pack(side=LEFT, fill='both', expand='True')
        left_frame.pack_propagate(0)
        right_frame.pack(side=RIGHT, fill='both', expand='True')
        bottom_frame.pack(side=TOP, fill='both')
        # c_frame.pack(side=LEFT, fill='both', expand='True')

        m_frame.pack(side=LEFT, fill='both', expand='True')
        m_frame.pack_propagate(0)
        right_frame.pack_propagate(0)
        bottom_frame.pack_propagate(0)
        # --------------LABELS ------------------------------------------------------------------

        self.lbl_RoomCharges = Label(left_frame, font=Font_label, text='Room Charges: ', bg='white', padx=11)
        self.lbl_RoomCharges.grid(row=0, column=0, sticky=W)
        self.in_RoomCharges = Entry(left_frame, font=Font_entry,
                                    textvariable=self.RoomChargesP, width=15, state="readonly")
        self.in_RoomCharges.grid(row=0, column=1, pady=5, padx=11, sticky=W)

        self.lbl_ExtraPersons = Label(left_frame, font=Font_label, text='Extra Persons: ',  bg='white',padx=11)
        self.lbl_ExtraPersons.grid(row=1, column=0, sticky=W)
        self.in_ExtraPersons = Entry(left_frame, font=Font_entry,
                                     textvariable=self.ExtraPersonsP, width=15, state="readonly")
        self.in_ExtraPersons.grid(row=1, column=1, pady=5, padx=11, sticky=W)

        self.lbl_totalDays = Label(left_frame, font=Font_label, text='Total Days: ', bg='white', padx=11)
        self.lbl_totalDays.grid(row=2, column=0, sticky=W)
        self.in_totalDays = Entry(left_frame, font=Font_entry,
                                  textvariable=self.totalDaysP, width=15, state="readonly")
        self.in_totalDays.grid(row=2, column=1, pady=5, padx=11, sticky=W)

        # ADDITIONAL CHARGES PLUS NEW ADDED AMOUNT
        self.lbl_AdditionalCharges = Label(left_frame, font=Font_label, text='Additional Charges: ', bg='white', padx=11)
        self.lbl_AdditionalCharges.grid(row=3, column=0, pady=5, sticky=W)
        self.in_AdditionalCharges = Entry(left_frame, font=Font_entry,
                                          textvariable=self.AdditionalChargesP, width=15, state="readonly")
        self.in_AdditionalCharges.grid(row=3, column=1, pady=5, padx=11, sticky=W)
        self.lbl_plus = Label(left_frame, font=Font_label, text='Add Any Other Charges', bg='white', padx=11)
        self.lbl_plus.grid(row=4, column=0, pady=5, padx=1, sticky=W)

        self.AddChargeP = StringVar()
        self.in_AddCharge = Entry(left_frame, font=Font_entry, textvariable=self.AddChargeP, width=15, highlightthickness=1,
                           highlightbackground='grey', highlightcolor='grey')
        self.in_AddCharge.grid(row=4, column=1, pady=5, padx=11, sticky=W)

        self.lbl_AdvAmt = Label(left_frame, font=Font_label, text='Advance Paid: ', bg='white', padx=11)
        self.lbl_AdvAmt.grid(row=5, column=0, sticky=W)
        self.in_AdvAmt = Entry(left_frame, font=Font_entry,
                               textvariable=self.AdvAmtP, width=15, state="readonly")
        self.in_AdvAmt.grid(row=5, column=1, pady=5, padx=11, sticky=W)
        self.lbl_TotalAmt = Label(left_frame, font=Font_label, text='Total Amount: ', bg='white', padx=11)

        self.lbl_TotalAmt.grid(row=6, column=0, sticky=W)
        self.in_TotalAmt = Entry(left_frame, font=Font_entry,
                                 textvariable=self.TotalAmtP, width=15, state="readonly")
        self.in_TotalAmt.grid(row=6, column=1, pady=5, padx=11, sticky=W)
        self.lbl_DueAmt = Label(left_frame, font=Font_label, text='Due Amount: ', bg='white', padx=11)
        self.lbl_DueAmt.grid(row=7, column=0, sticky=W)
        self.in_DueAmt = Entry(left_frame, font=Font_entry, textvariable=self.remainingAmt, width=15, highlightthickness=1,
                           highlightbackground='grey', highlightcolor='grey')
        self.in_DueAmt.grid(row=7, column=1, pady=5, padx=11, sticky=W)

        self.btnsum = Button(left_frame, activeforeground='black', activebackground='lavender', foreground="white", bg="black", command=self.calculateDue, font=Font_label,
                             text="Calculate Due", width=20)
        self.btnsum.grid(row=8, column=1, padx=11, pady=17)

        self.btnReset = Button(left_frame, activeforeground='black', activebackground='lavender', foreground="white", bg="black", command=self.resetP, font=Font_label,
                               text="RESET", width=20)
        self.btnReset.grid(row=8, column=0, padx=11, pady=17)

        self.btnout = Button(left_frame, activeforeground='black', activebackground='lavender', foreground="white", bg="black", font=Font_label, text="Check OUT",
                             command=self.addPayRecord, width=40)
        self.btnout.grid(row=10, column=0, columnspan=2, padx=11, pady=7)
        # ---------------------LABELS IN Bottom LABELFRAME-------------------------------------------------
        self.lbl_customer_ID = Label(m_frame, font=Font_label, bg='white',
                                     text='Booking ID:', padx=1)
        self.lbl_customer_ID.grid(row=0, column=0, sticky=W)
        self.in_customer_ID = Entry(m_frame, font=Font_entry, width=22, textvariable=self.CustIDP, state="readonly")
        self.in_customer_ID.grid(row=0, column=1, pady=10, padx=2, sticky=W)

        self.lbl_Name = Label(m_frame, font=Font_label, text='Name: ', bg='white', padx=3)
        self.lbl_Name.grid(row=1, column=0, sticky=W)
        self.in_Name = Entry(m_frame, font=Font_entry, textvariable=self.NameP, state="readonly", width=22)
        self.in_Name.grid(row=1, column=1, pady=3, padx=2, sticky=W)

        self.lbl_roomType = Label(m_frame, font=Font_label, text='Room Type.: ', bg='white', padx=1)
        self.lbl_roomType.grid(row=2, column=0, sticky=W)
        self.in_roomType = Entry(m_frame, font=Font_entry, width=22, state="readonly", textvariable=self.RoomTypeP)
        self.in_roomType.grid(row=2, column=1, pady=3, padx=1, sticky=W)

        self.lbl_roomno = Label(m_frame, font=Font_label, text='Room No.: ', bg='white', padx=1)
        self.lbl_roomno.grid(row=3, column=0, sticky=W)
        self.in_roomno = Entry(m_frame, font=Font_entry, width=22, state="readonly", textvariable=self.RoomnoP)
        self.in_roomno.grid(row=3, column=1, pady=3, padx=1, sticky=W)

        self.lbl_checkInDate = Label(m_frame, font=Font_label, text='Check In: ', bg='white', padx=3)
        self.lbl_checkInDate.grid(row=4, column=0, sticky=W)
        self.in_checkInDate = Entry(m_frame, font=Font_entry, textvariable=self.DateInP, state="readonly", width=22)
        self.in_checkInDate.grid(row=4, column=1, pady=3, padx=2, sticky=W)

        self.lbl_checkOutDate = Label(m_frame, font=Font_label, text='Check Out: ', bg='white', padx=3)
        self.lbl_checkOutDate.grid(row=5, column=0, sticky=W)
        self.in_checkOutDate = Entry(m_frame, font=Font_entry, textvariable=self.DateOutP, state="readonly", width=22)
        self.in_checkOutDate.grid(row=5, column=1, pady=3, padx=2, sticky=W)

        # Bill Generate
        self.btnBillgen = Button(m_frame, activeforeground='black', activebackground='lavender', foreground="white", bg="black", font=Font_label, command=self.pdfgen,
                                 text="Generate Bill", width=40)
        self.btnBillgen.grid(row=6, column=0, columnspan=2, padx=14, pady=20)
        # Bill Preview
        self.btnBillPre = Button(m_frame, activeforeground='black', activebackground='lavender', foreground="white", bg="black", font=Font_label,
                                 text="Preview Bill", width=40)
        self.btnBillPre.bind("<Button>",
                             lambda e: preview_window.BillPreview(b_frame, self.CustIDP.get(), self.NameP.get()))
        self.btnBillPre.grid(row=7, column=0, columnspan=2, padx=14, pady=20)

        # -------------TABLE for DISPLAYING CURRENT RECORDS-----------------------------------------------

        self.payInfoTable = ttk.Treeview(right_frame, selectmode='browse')
        scroll_x = ttk.Scrollbar(right_frame,
                                 orient="horizontal",
                                 command=self.payInfoTable.xview)
        scroll_x.pack(side='bottom', fill='x')
        self.payInfoTable.configure(xscrollcommand=scroll_x.set)
        scroll_y = ttk.Scrollbar(right_frame,
                                 orient="vertical",
                                 command=self.payInfoTable.yview)
        scroll_y.configure(command=self.payInfoTable.yview)
        scroll_y.pack(side='right', fill='y')
        self.payInfoTable.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        self.payInfoTable["columns"] = (
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
            "20",
            "21", "22")
        self.payInfoTable.column("1", anchor='c', minwidth=0, width=60)
        self.payInfoTable.column("2", anchor='c')
        self.payInfoTable.column("3", anchor='c')
        self.payInfoTable.column("4", anchor='c')
        self.payInfoTable.column("5", anchor='c')
        self.payInfoTable.column("6", anchor='c')
        self.payInfoTable.column("7", anchor='c')
        self.payInfoTable.column("8", anchor='c')
        self.payInfoTable.column("9", anchor='c')
        self.payInfoTable.column("10", anchor='c')
        self.payInfoTable.column("11", anchor='c')
        self.payInfoTable.column("12", anchor='c')
        self.payInfoTable.column("13", anchor='c')
        self.payInfoTable.column("14", anchor='c')
        self.payInfoTable.column("15", anchor='c')
        self.payInfoTable.column("16", anchor='c')
        self.payInfoTable.column("17", anchor='c')
        self.payInfoTable.column("18", anchor='c')
        self.payInfoTable.column("19", anchor='c')
        self.payInfoTable.column("20", anchor='c')
        self.payInfoTable.column("21", anchor='c')
        self.payInfoTable.column("22", anchor='c')

        self.payInfoTable.heading("1", text="Sr.No.")
        self.payInfoTable.heading("2", text="Booking ID")
        self.payInfoTable.heading("3", text="Name")
        self.payInfoTable.heading("4", text="Gender")
        self.payInfoTable.heading("5", text="Address")
        self.payInfoTable.heading("6", text="Mobile")
        self.payInfoTable.heading("7", text="Email")
        self.payInfoTable.heading("8", text="Nationality")
        self.payInfoTable.heading("9", text="ID Proof Type")
        self.payInfoTable.heading("10", text="Check In")
        self.payInfoTable.heading("11", text="Check Out")
        self.payInfoTable.heading("12", text="Adults")
        self.payInfoTable.heading("13", text="Child")
        self.payInfoTable.heading("14", text="Total Days")
        self.payInfoTable.heading("15", text="Room Type")
        self.payInfoTable.heading("16", text="Room No")
        self.payInfoTable.heading("17", text="Room Charges")
        self.payInfoTable.heading("18", text="Extra Persons")
        self.payInfoTable.heading("19", text="Additional Charges")
        self.payInfoTable.heading("20", text="Total Amount")
        self.payInfoTable.heading("21", text="Advance Paid")
        self.payInfoTable.heading("22", text="Remaining Amount")
        self.payInfoTable['show'] = 'headings'
        self.payInfoTable.pack(side=RIGHT, fill='both', expand='True')
        self.payInfoTable.bind("<ButtonRelease-1>", self.get_cursor2)

        # -------------Widget BUTTONS-------------------------------------------------------------------

        self.lbl_searchID = Label(bottom_frame, font=Font_label, bg='white', text='Search by ', padx=6)
        self.lbl_searchID.grid(row=0, column=2, sticky=W)
        self.in_searchvar = ttk.Combobox(bottom_frame, state="readonly", font=Font_entry,
                                         textvariable=self.SearchVar, width=12)
        self.in_searchvar['values'] = ('',
                                       'Name',
                                       'Mobile'
                                       )
        self.in_searchvar.current(0)
        self.Searchtxt = StringVar()
        self.in_searchvar.grid(row=0, column=3, pady=3, padx=1, sticky=W)
        self.in_searchID = Entry(bottom_frame, font=Font_label, textvariable=self.Searchtxt, highlightthickness=1,
                           highlightbackground='grey', highlightcolor='grey')
        self.in_searchID.grid(row=0, column=4, pady=3, padx=4)
        self.btnSearch = Button(bottom_frame, activeforeground='black', activebackground='lavender', foreground="white", bg="black", font=Font_label, text="SEARCH",
                                command=self.searchPayRecord, width=11)
        self.btnSearch.grid(row=0, column=5, padx=1, pady=12)

        self.btnViewAll = Button(bottom_frame, activeforeground='black', activebackground='lavender', foreground="white", bg="black", font=Font_label, text="VIEW ALL",
                                 command=self.displayPayRecords, width=20)
        self.btnViewAll.grid(row=0, column=6, padx=60, pady=7)

    # -----------------GENERATE PDF-------------------------------------------------------------------------------

    def pdfgen(self):
        pdf_generate.pdfReceiptGenerate(self.CustIDP.get(), self.in_checkInDate.get(), self.in_checkOutDate.get(),
                                self.totalDaysP.get(), self.AdultsP.get(), self.KidsP.get(), self.RoomTypeP.get(),
                                self.RoomnoP.get(), self.NameP.get(), self.MobileP.get(), self.EmailP.get(),
                                self.AddressP.get(), self.RoomChargesP.get(), self.ExtraPersonsP.get(),
                                self.AdditionalChargesP.get(), self.TotalAmtP.get())

    # ----------------Databse Methods---------------------------------------------------------------------------
    def reset(self):
        self.in_Name.delete(0, END)
        self.in_address.delete(0, END)
        self.in_Mobile.delete(0, END)
        self.in_Email.delete(0, END)
        self.in_Nationality.delete(0, END)
        self.in_gender.delete(0, END)
        self.in_idProoftxt.delete(0, END)
        self.in_checkInDate.delete(0, END)
        self.in_checkOutDate.delete(0, END)
        self.in_roomno.delete(0, END)
        self.in_roomType.delete(0, END)
        self.in_TotalDays.delete(0, END)
        self.in_Adults.delete(0, END)
        self.in_Kids.delete(0, END)
        self.in_AdditionalCharges.delete(0, END)
        self.in_ExtraPersons.delete(0, END)
        self.in_TotalAmt.delete(0, END)
        self.in_AdvAmt.delete(0, END)
        self.in_RoomCharges.delete(0, END)

        self.DateIn.set(time.strftime("%d-%m-%y, %H:%M:%S"))
        self.DateOut.set(time.strftime("%d-%m-%y, %H:%M:%S"))

        x = randint(1000, 9999)
        randomRef = str(x)
        d = str(time.strftime("%m%d%y"))
        self.CustID.set("HV" + randomRef + d)

    # ---------------reserve--------------------------------------------------------------------------------------------

    def BookingFrame(self):
        b_frame = Frame(self.root, height=510, width=1080, highlightthickness=4, highlightbackground='#90B2B2',
                        highlightcolor='#90B2B2', bg='gray89', relief=RIDGE)
        b_frame.place(x=0, y=70 + 6)
        b_frame.pack_propagate(False)
        b_frame.tkraise()
        topFrame = Frame(b_frame, width=1080, height=460, padx=2, highlightthickness=3,
                         highlightbackground='#90B2B2', highlightcolor='#90B2B2', relief=RIDGE)
        topFrame.pack()
        left_frame = Frame(topFrame, bg='white', width=400, height=420, highlightthickness=2,
                           highlightbackground='#90B2B2', highlightcolor='#90B2B2', pady=5, relief=RIDGE)
        right_frame = Frame(topFrame, bg='white', width=680, height=420, padx=5, highlightthickness=2,
                            highlightbackground='#90B2B2', highlightcolor='#90B2B2', relief=RIDGE)
        bottom_frame = Frame(b_frame, bg='white', width=1080, height=80, padx=4, pady=2, highlightthickness=2,
                             highlightbackground='#90B2B2', highlightcolor='#90B2B2', relief=RIDGE)
        rTop_frame = LabelFrame(right_frame, bd=1, bg='white', width=680, height=200, padx=5, highlightthickness=2,
                                highlightbackground='#90B2B2', highlightcolor='#90B2B2', relief=RIDGE)
        rBottom_frame = LabelFrame(right_frame, bd=1, bg='white', width=680, height=220, padx=5, highlightthickness=2,
                                   highlightbackground='#90B2B2', highlightcolor='#90B2B2', relief=RIDGE)
        left_frame.pack(side=LEFT, fill='both', expand='True')
        right_frame.pack(side=RIGHT, fill='both', expand='True')
        bottom_frame.pack(side=BOTTOM, fill='both', expand='True')
        rTop_frame.pack(side=TOP, fill='both', expand='True')
        rBottom_frame.pack(side=BOTTOM, fill='both', expand='True')
        left_frame.pack_propagate(0)
        right_frame.pack_propagate(0)
        bottom_frame.pack_propagate(0)
        rTop_frame.pack_propagate(0)
        rBottom_frame.pack_propagate(0)

        # --------------LABELS ----------------------------------------------------------------------------------
        self.lbl_customer_ID = Label(left_frame, font=Font_label, bg='white',
                                     text='Booking ID:* ', padx=6)
        self.lbl_customer_ID.grid(row=0, column=0, columnspan=2, sticky=W)
        self.in_customer_ID = Entry(left_frame, font=Font_entry, width=29, textvariable=self.CustID, state="readonly")
        self.in_customer_ID.grid(row=0, column=2, columnspan=2, pady=3, padx=6, sticky=W)

        self.lbl_Name = Label(left_frame, font=Font_label, text='Name:* ', bg='white', padx=6)
        self.lbl_Name.grid(row=1, column=0, columnspan=2, sticky=W)
        self.in_Name = Entry(left_frame, font=Font_entry, highlightthickness=1,
                           highlightbackground='grey', highlightcolor='grey', textvariable=self.Name, width=29)
        self.in_Name.grid(row=1, column=2, columnspan=2, pady=3, padx=6, sticky=W)

        self.lbl_gender = Label(left_frame, font=Font_label, text='Gender: ', bg='white', padx=6)
        self.lbl_gender.grid(row=2, column=0, columnspan=2, sticky=W)
        self.in_gender = ttk.Combobox(left_frame,
                                      font=Font_entry,
                                      textvariable=self.Gender, width=27)
        self.in_gender['values'] = ('',
                                    'Male',
                                    'Female',
                                    'Transexual',
                                    'Other'
                                    )
        self.in_gender.current(0)
        self.in_gender.grid(row=2, column=2, columnspan=2, pady=3, padx=6, sticky=W)

        self.lbl_address = Label(left_frame, font=Font_label, text='Address: ', bg='white', padx=6)
        self.lbl_address.grid(row=3, column=0, columnspan=2, sticky=W)
        self.in_address = Entry(left_frame, font=Font_entry, highlightthickness=1,
                           highlightbackground='grey', highlightcolor='grey',
                                textvariable=self.Address, width=29)
        self.in_address.grid(row=3, column=2, columnspan=2, pady=3, padx=6, sticky=W)

        self.lbl_Mobile = Label(left_frame, font=Font_label, text='Mobile No.:* ', bg='white', padx=6)
        self.lbl_Mobile.grid(row=4, column=0, columnspan=2, sticky=W)
        self.in_Mobile = Entry(left_frame, font=Font_entry, highlightthickness=1,
                           highlightbackground='grey', highlightcolor='grey',
                               textvariable=self.Mobile, width=29)
        self.in_Mobile.grid(row=4, column=2, columnspan=2, pady=3, padx=6, sticky=W)

        self.lbl_Email = Label(left_frame, font=Font_label, text='Email: ', bg='white', padx=6)
        self.lbl_Email.grid(row=5, column=0, columnspan=2, sticky=W)
        self.in_Email = Entry(left_frame, font=Font_entry, highlightthickness=1,
                           highlightbackground='grey', highlightcolor='grey',
                              textvariable=self.Email, width=29)
        self.in_Email.grid(row=5, column=2, columnspan=2, pady=3, padx=6, sticky=W)

        self.lbl_Nationality = Label(left_frame, font=Font_label, text='Nationality: ', bg='white', padx=6)
        self.lbl_Nationality.grid(row=6, column=0, columnspan=2, sticky=W)
        self.in_Nationality = Entry(left_frame, font=Font_entry, highlightthickness=1,
                           highlightbackground='grey', highlightcolor='grey',
                                    textvariable=self.Nationality, width=29)
        self.in_Nationality.grid(row=6, column=2, columnspan=2, pady=3, padx=6, sticky=W)

        self.lbl_idProoftxt = Label(left_frame, font=Font_label, text='Type of ID Proof:* ', bg='white', padx=6)
        self.lbl_idProoftxt.grid(row=7, column=0, columnspan=2, sticky=W)
        self.in_idProoftxt = ttk.Combobox(left_frame, font=Font_entry,
                                          textvariable=self.IdProof, width=27)
        self.in_idProoftxt['values'] = ('',
                                        'Aadhaar',
                                        'Driving Licence',
                                        'Student ID',
                                        'Passport',
                                        'PAN Card',
                                        'Voters ID'
                                        'Birth Certificate',
                                        'Others'
                                        )
        self.in_idProoftxt.current(0)
        self.in_idProoftxt.grid(row=7, column=2, columnspan=2, pady=3, padx=6, sticky=W)

        self.lbl_checkInDate = Label(left_frame, font=Font_label, text='Check In Date:* ', bg='white', padx=6)
        self.lbl_checkInDate.grid(row=10, column=0, columnspan=2, sticky=W)
        self.in_checkInDate = Entry(left_frame, font=Font_entry, highlightthickness=1,
                           highlightbackground='grey', highlightcolor='grey',
                                    textvariable=self.DateIn, width=29)
        self.in_checkInDate.grid(row=10, column=2, columnspan=2, pady=3, padx=6, sticky=W)

        self.lbl_checkOutDate = Label(left_frame, font=Font_label, text='Check Out Date:* ', bg='white', padx=6)
        self.lbl_checkOutDate.grid(row=11, column=0, columnspan=2, sticky=W)
        self.in_checkOutDate = Entry(left_frame, font=Font_entry, highlightthickness=1,
                           highlightbackground='grey', highlightcolor='grey',
                                     textvariable=self.DateOut, width=29)
        self.in_checkOutDate.grid(row=11, column=2, columnspan=2, pady=3, padx=6, sticky=W)

        self.lbl_Kids = Label(left_frame, font=Font_label, text='Kids: ', bg='white', padx=6)
        self.lbl_Kids.grid(row=12, column=0, sticky=W)
        self.in_Kids = Entry(left_frame, font=Font_entry, highlightthickness=1,
                           highlightbackground='grey', highlightcolor='grey',
                             textvariable=self.Kids, width=9)
        self.in_Kids.grid(row=12, column=1, pady=3, padx=6, sticky=W)

        self.lbl_Adults = Label(left_frame, font=Font_label, text='Adults: ', bg='white', padx=6)
        self.lbl_Adults.grid(row=12, column=2, sticky=W)
        self.in_Adults = Entry(left_frame, font=Font_entry, highlightthickness=1,
                           highlightbackground='grey', highlightcolor='grey',
                               textvariable=self.Adults, width=9)
        self.in_Adults.grid(row=12, column=3, pady=3, padx=6, sticky=W)

        self.lbl_TotalDays = Label(left_frame, font=Font_label, text='Total Days: ', bg='white', padx=6)
        self.lbl_TotalDays.grid(row=14, column=0, columnspan=2, sticky=W)
        self.in_TotalDays = Entry(left_frame, font=Font_entry, highlightthickness=1,
                           highlightbackground='grey', highlightcolor='grey',
                                  textvariable=self.totalDays, width=29)
        self.in_TotalDays.grid(row=14, column=2, columnspan=2, pady=3, padx=6, sticky=W)

        self.lbl_roomno = Label(rBottom_frame, font=Font_label, text='Room No.:* ', bg='white', padx=6)
        self.lbl_roomno.grid(row=1, column=0, sticky=W)
        self.in_roomno = Entry(rBottom_frame, font=Font_entry, highlightthickness=1,
                           highlightbackground='grey', highlightcolor='grey', width=23, textvariable=self.Roomno)
        self.in_roomno.grid(row=1, column=1, pady=3, padx=2, sticky=W)

        self.lbl_roomType = Label(rBottom_frame, font=Font_label, text='Room Type.:* ', bg='white', padx=6)
        self.lbl_roomType.grid(row=2, column=0, sticky=W)
        self.in_roomType = ttk.Combobox(rBottom_frame,
                                        font=Font_entry, textvariable=self.RoomType, width=21)
        self.in_roomType.option_add('*TCombobox*Listbox.Justify', 'center')
        self.in_roomType['values'] = ('',
                                      'Deluxe (Single)',
                                      'Deluxe (Double)',
                                      'Super Deluxe (Single)',
                                      'Super Deluxe (Double)',
                                      'Triple Bed (Double)',
                                      'Family (Double)',
                                      'A/C Room (Single)',
                                      'A/C Room (Double)'
                                      )
        self.in_roomType.current(0)
        self.in_roomType.grid(row=2, column=1, pady=3, padx=6, sticky=W)

        self.lbl_RoomCharges = Label(rBottom_frame, font=Font_label, text='Room Charges: ', bg='white', padx=6)
        self.lbl_RoomCharges.grid(row=3, column=0, sticky=W)
        self.in_RoomCharges = Entry(rBottom_frame, font=Font_entry, highlightthickness=1,
                           highlightbackground='grey', highlightcolor='grey',
                                    textvariable=self.RoomCharges, width=23)
        self.in_RoomCharges.grid(row=3, column=1, pady=3, padx=6, sticky=W)

        self.lbl_ExtraPersons = Label(rBottom_frame, font=Font_label, text='Extra Persons: ', bg='white', padx=6)
        self.lbl_ExtraPersons.grid(row=4, column=0, sticky=W)
        self.in_ExtraPersons = Entry(rBottom_frame, font=Font_entry,
                                     textvariable=self.ExtraPersons, highlightthickness=1,
                           highlightbackground='grey', highlightcolor='grey', width=23)
        self.in_ExtraPersons.grid(row=4, column=1, pady=3, padx=6, sticky=W)

        self.lbl_AdditionalCharges = Label(rBottom_frame, font=Font_label, bg='white', text='Additional Charges: ', padx=6)
        self.lbl_AdditionalCharges.grid(row=1, column=2, sticky=W)
        self.in_AdditionalCharges = Entry(rBottom_frame, font=Font_entry,
                                          textvariable=self.AdditionalCharges, highlightthickness=1,
                           highlightbackground='grey', highlightcolor='grey', width=23)
        self.in_AdditionalCharges.grid(row=1, column=3, pady=3, padx=6, sticky=W)

        self.lbl_TotalAmt = Label(rBottom_frame, font=Font_label, text='Total Amount: ', bg='white', padx=6)
        self.lbl_TotalAmt.grid(row=2, column=2, sticky=W)
        self.in_TotalAmt = Entry(rBottom_frame, font=Font_entry, highlightthickness=1,
                           highlightbackground='grey', highlightcolor='grey',
                                 textvariable=self.TotalAmt, width=23)
        self.in_TotalAmt.grid(row=2, column=3, pady=3, padx=6, sticky=W)

        self.lbl_AdvAmt = Label(rBottom_frame, font=Font_label, bg='white', text='Advance Paid: ', padx=6)
        self.lbl_AdvAmt.grid(row=3, column=2, sticky=W)
        self.in_AdvAmt = Entry(rBottom_frame, font=Font_entry, highlightthickness=1,
                           highlightbackground='grey', highlightcolor='grey',
                               textvariable=self.AdvAmt, width=23)
        self.in_AdvAmt.grid(row=3, column=3, pady=3, padx=6, sticky=W)

        self.btnsum = Button(rBottom_frame, activeforeground='black', activebackground='lavender', foreground="white", bg="black", font=Font_label, text="Calculate",
                             command=self.calculateT, width=20)
        self.btnsum.grid(row=4, column=3, padx=4, ipady=3, pady=12)

        # -------------TABLE for DISPLAYING CURRENT RECORDS---------------------------------------------------
        style = ttk.Style()
        style.configure("Treeview.Heading",
                        background="Paleturquoise3", foreground="black", relief="flat")
        style.map("Custom.Treeview.Heading",
                  relief=[('active', 'groove'), ('pressed', 'sunken')])
        style.configure('Treeview', background='lavender',
                        foreground='Black')

        self.currecordtable = ttk.Treeview(rTop_frame, selectmode='browse',
                                           column=("SNo.", "CustomerID", "FirstName",
                                                   "LastName", "Gender", "Mobile", "Email", "Check", "out"))
        scroll_x = ttk.Scrollbar(rTop_frame,
                                 orient="horizontal",
                                 command=self.currecordtable.xview)

        scroll_x.pack(side='bottom', fill='x')

        self.currecordtable.configure(xscrollcommand=scroll_x.set)
        scroll_y = ttk.Scrollbar(rTop_frame,
                                 orient="vertical",
                                 command=self.currecordtable.yview)

        scroll_y.configure(command=self.currecordtable.yview)
        scroll_y.pack(side='right', fill='y')
        self.currecordtable.configure(xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        self.currecordtable["columns"] = (
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
            "20",
            "21", "22")
        self.currecordtable['show'] = 'headings'

        self.currecordtable.column("1", anchor='c', minwidth=0, width=60)
        self.currecordtable.column("2", anchor='c')
        self.currecordtable.column("3", anchor='c')
        self.currecordtable.column("4", anchor='c')
        self.currecordtable.column("5", anchor='c')
        self.currecordtable.column("6", anchor='c')
        self.currecordtable.column("7", anchor='c')
        self.currecordtable.column("8", anchor='c')
        self.currecordtable.column("9", anchor='c')
        self.currecordtable.column("10", anchor='c')
        self.currecordtable.column("11", anchor='c')
        self.currecordtable.column("12", anchor='c')
        self.currecordtable.column("13", anchor='c')
        self.currecordtable.column("14", anchor='c')
        self.currecordtable.column("15", anchor='c')
        self.currecordtable.column("16", anchor='c')
        self.currecordtable.column("17", anchor='c')
        self.currecordtable.column("18", anchor='c')
        self.currecordtable.column("19", anchor='c')
        self.currecordtable.column("20", anchor='c')
        self.currecordtable.column("21", anchor='c')
        self.currecordtable.column("22", anchor='c')

        self.currecordtable.heading("1", text="Sr.No.")
        self.currecordtable.heading("2", text="Booking ID")
        self.currecordtable.heading("3", text="Name")
        self.currecordtable.heading("4", text="Gender")
        self.currecordtable.heading("5", text="Address")
        self.currecordtable.heading("6", text="Mobile")
        self.currecordtable.heading("7", text="Email")
        self.currecordtable.heading("8", text="Nationality")
        self.currecordtable.heading("9", text="ID Proof Type")
        self.currecordtable.heading("10", text="Check In")
        self.currecordtable.heading("11", text="Check Out")
        self.currecordtable.heading("12", text="Adults")
        self.currecordtable.heading("13", text="Child")
        self.currecordtable.heading("14", text="Total Days")
        self.currecordtable.heading("15", text="Room Type")
        self.currecordtable.heading("16", text="Room No")
        self.currecordtable.heading("17", text="Room Charges")
        self.currecordtable.heading("18", text="Extra Persons")
        self.currecordtable.heading("19", text="Additional Charges")
        self.currecordtable.heading("20", text="Total Amount")
        self.currecordtable.heading("21", text="Advance Paid")
        self.currecordtable.heading("22", text="Remaining Amount")
        self.currecordtable['show'] = 'headings'
        self.currecordtable.pack(side='top', fill='both', expand='True')
        self.currecordtable.bind("<ButtonRelease-1>", self.get_cursor)

        # -------------Widget BUTTONS--------------------------------------------------------------------------

        self.btnAddNew = Button(bottom_frame, activeforeground='black', activebackground='lavender', foreground="white", bg="black", font=Font_label, text="Add New",
                                command=self.addRecord, width=12)
        self.btnAddNew.grid(row=0, column=0, padx=4, pady=12, ipady=3)

        self.btnReset = Button(bottom_frame, activeforeground='black', activebackground='lavender', foreground="white", bg="black", font=Font_label, text="Reset",
                               command=self.reset, width=12)
        self.btnReset.grid(row=0, column=1, padx=4, pady=12, ipady=3)

        self.btnDelete = Button(bottom_frame, activeforeground='black', activebackground='lavender', foreground="white", bg="black", font=Font_label, text="Delete",
                                command=self.deleteRecord, width=12)
        self.btnDelete.grid(row=0, column=2, padx=4, pady=12, ipady=3)

        self.btnUpdate = Button(bottom_frame, activeforeground='black', activebackground='lavender', foreground="white", bg="black", font=Font_label, text="Update",
                                command=self.updateRecord, width=12)
        self.btnUpdate.grid(row=0, column=3, padx=4, pady=12, ipady=3)

        self.lbl_blank = Label(bottom_frame, font=Font_label, bg='white', text='', padx=6, width=15)
        self.lbl_blank.grid(row=0, column=4)


        self.btnViewcur = Button(bottom_frame, activeforeground='black', activebackground='lavender', foreground="white", bg="black", font=Font_label, text="View All",
                                 command=self.displayCurRecord, width=18)
        self.btnViewcur.grid(row=0, column=5, padx=4, pady=12, ipady=2)


        self.lbl_searchID = Label(bottom_frame, font=Font_label, bg='white', text='Search by ', padx=6)
        self.lbl_searchID.grid(row=0, column=6, sticky=W)
        self.in_searchvar = ttk.Combobox(bottom_frame, state="readonly", font=Font_entry,
                                         textvariable=self.SearchVar, width=12)
        self.in_searchvar['values'] = ('',
                                       'Name',
                                       'Mobile'
                                       )
        self.in_searchvar.current(0)
        self.Searchtxt = StringVar()
        self.in_searchvar.grid(row=0, column=7, pady=3, padx=1, sticky=W)
        self.in_searchID = Entry(bottom_frame, font=Font_label, textvariable=self.Searchtxt)
        self.in_searchID.grid(row=0, column=8, pady=3, padx=4)
        self.btnSearch = Button(bottom_frame, activeforeground='black', activebackground='lavender', foreground="white", bg="black", font=Font_label, text="SEARCH",
                                command=self.searchRecord, width=18)
        self.btnSearch.grid(row=0, column=9, padx=1, pady=12, ipady=2)

    # -------------------------EXIT MESSAGEBOX----------------------------------------------------------------------------------------------------------------------
    def exitapp(self):
        self.q = messagebox.askyesno("Exit", "Do you really want to exit ?")
        if (self.q):
            root.destroy()

    # ----------ADD RECORDS------------------------------------------------------------------------------
    def addRecord(self):
        backend.addBRecord(self.CustID.get(),
                                    self.in_Name.get(),
                                    self.in_gender.get(),
                                    self.in_address.get(),
                                    self.in_Mobile.get(),
                                    self.in_Email.get(),
                                    self.in_Nationality.get(),
                                    self.in_idProoftxt.get(),
                                    self.in_checkInDate.get(),
                                    self.in_checkOutDate.get(),
                                    self.in_Adults.get(),
                                    self.in_Kids.get(),
                                    self.in_TotalDays.get(),
                                    self.in_roomType.get(),
                                    self.in_roomno.get(),
                                    self.in_RoomCharges.get(),
                                    self.in_ExtraPersons.get(),
                                    self.in_AdditionalCharges.get(),
                                    self.in_TotalAmt.get(),
                                    self.in_AdvAmt.get())

    # ---------------Calculate Methods--------------------------------------------------------------------------------
    def calculateT(self):
        if self.in_AdditionalCharges.get().isdigit:
            total = backend.calculateTotal(self.ExtraPersons.get(), self.in_RoomCharges.get(),
                                                    self.in_AdditionalCharges.get(), self.in_TotalDays.get())
            if total == None:
                t = 0
                self.TotalAmt.set(t)
            else:
                self.TotalAmt.set(total)
        else:
            messagebox.showerror("Error", "Please use digits!")

    # ----------------------------------------------------------------------------------------
    def calculateDue(self):
        add = self.in_AddCharge.get()
        if add == "":
            messagebox.showerror("Error", "Please use digits!")
        elif add != "" or add.isdigit:
            a = int(self.in_AddCharge.get()) + int(self.AdditionalChargesP.get())
            print(a)
            total = backend.DuesandTotal(self.ExtraPersonsP.get(), self.RoomChargesP.get(),
                                                  str(a), self.totalDaysP.get())
            self.TotalAmtP.set(total)
            self.AddChargeP.set(0)
            self.remainingAmt.set(int(total) - int(self.AdvAmtP.get()))

        else:
            messagebox.showerror("Error", "Please use digits!")

    # ---------------DISPLAY Single Record------------------------------------------------------------------------------

    def displayCurRecord(self):

        records = self.currecordtable.get_children()
        # formt = "%d-%m-%y, %H:%M:%S"
        for idx in records:
            self.currecordtable.delete(idx)
        for row in hotel_database.viewBookingRecord():
            # --------- CHECK IN DATE ------------------
            r = row[9].split("-")
            y1 = r[2].split(" ")
            t1 = y1[1].split(":")
            row9 = y1[0] + "-" + r[1] + "-" + r[0][2:] + ", " + t1[0] + ":" + t1[1] + ":" + t1[2]

            # --------- CHECK OUT DATE ------------------
            r = row[10].split("-")
            y1 = r[2].split(" ")
            t1 = y1[1].split(":")
            # row9 = datetime(int(r[0]), int(r[1]), int(y1[0]), int(t1[0]), int(t1[1]), int(t1[2]))
            # row9.strftime('%d-%m-%y %H:%M:%S')
            row10 = y1[0] + "-" + r[1] + "-" + r[0][2:] + ", " + t1[0] + ":" + t1[1] + ":" + t1[2]

            self.currecordtable.insert("", END, values=(row[0],
                                                        row[1],
                                                        row[2],
                                                        row[3],
                                                        row[4],
                                                        row[5],
                                                        row[6],
                                                        row[7],
                                                        row[8],
                                                        row9,
                                                        row10,
                                                        row[11],
                                                        row[12],
                                                        row[13],
                                                        row[14],
                                                        row[15],
                                                        row[16],
                                                        row[17],
                                                        row[18],
                                                        row[19],
                                                        row[20],
                                                        row[21]))

    def get_cursor(self, event=""):
        if self.currecordtable.focus() != '':
            cur_row = self.currecordtable.focus()
            record = self.currecordtable.item(cur_row)
            data = record["values"]

            self.recordID.set(data[0])
            self.CustID.set(data[1]),
            self.Name.set(data[2]),
            self.Gender.set(data[3]),
            self.Address.set(data[4]),
            self.Mobile.set(data[5]),
            self.Email.set(data[6]),
            self.Nationality.set(data[7]),
            self.IdProof.set(data[8]),
            self.DateIn.set(data[9]),
            self.DateOut.set(data[10]),
            self.Adults.set(data[11]),
            self.Kids.set(data[12]),
            self.totalDays.set(data[13]),
            self.RoomType.set(data[14]),
            self.Roomno.set(data[15]),
            self.RoomCharges.set(data[16]),
            self.ExtraPersons.set(data[17]),
            self.AdditionalCharges.set(data[18]),
            self.TotalAmt.set(data[19]),
            self.AdvAmt.set(data[20])

    def updateRecord(self):
        if self.CustID.get() == "" or self.in_Mobile.get() == "" or self.in_idProoftxt.get() == "" or self.in_checkInDate.get() == "" or self.in_checkOutDate.get() == "":
            messagebox.showerror("Error", "All fields are Required")

        try:
            checkInDate = datetime.strptime(self.in_checkInDate.get(), '%d-%m-%y, %H:%M:%S')
            checkOutDate = datetime.strptime(self.in_checkOutDate.get(), '%d-%m-%y, %H:%M:%S')
        except ValueError as ve:
            messagebox.showerror("Error", "Please Enter Valid Date and Time!\n" + str(ve))

        else:
            print("ADD: " + str(checkInDate))
            remainingAmt = int(self.in_TotalAmt.get()) - int(self.in_AdvAmt.get())
            hotel_database.updateBookingRecord(
                self.in_Name.get(),
                self.in_gender.get(),
                self.in_address.get(),
                self.in_Mobile.get(),
                self.in_Email.get(),
                self.in_Nationality.get(),
                self.in_idProoftxt.get(),
                str(checkInDate),
                str(checkOutDate),
                self.in_Adults.get(),
                self.in_Kids.get(),
                self.in_TotalDays.get(),
                self.in_roomType.get(),
                 self.in_roomno.get(),
                self.in_RoomCharges.get(),
                self.in_ExtraPersons.get(),
                self.in_AdditionalCharges.get(),
                str(self.in_TotalAmt.get()),
                str(self.in_AdvAmt.get()),
                str(remainingAmt),
                self.CustID.get())
            self.displayCurRecord()
            print('Updated Row ID is :', self.CustID.get())
            messagebox.showinfo("Success", "Entry has been UPDATED Successfully!")

    def deleteRecord(self):
        deleteRecord = messagebox.askyesno("System Manager", "Do you want to Delete this Customer?")
        if deleteRecord > 0:
            id = self.CustID.get()
            hotel_database.deleteBookingRecord(id)
        else:
            if not deleteRecord:
                return
        self.displayCurRecord()

    def searchRecord(self):
        backend.search(self.currecordtable, self.Searchtxt.get(), self.SearchVar.get())

    # -----------PAYMENTS BACKEND FUNCTIONS----------------------------------------------------------

    def addPayRecord(self):

        if self.CustIDP.get() == "" or self.in_AddCharge.get() == "" or self.in_DueAmt.get() == "" or self.DateOutP.get():
            messagebox.showerror("Error", "All fields are Required")

        elif int(self.in_DueAmt.get()) > 0:
            messagebox.showerror("Error", "Can't Checkout: {}Rs. Dues Are Not Paid!".format(self.in_DueAmt.get()))

        elif self.DateOutP.get() > self.today.get():
            y = messagebox.askyesno("Check-Out", "Check=Out Date Is Still Ahead, Do You Really Want To Check-Out Now?")
            if y:
                a = int(self.in_AddCharge.get()) + int(self.AdditionalChargesP.get())
                name = hotel_database.addCheckout(str(a), self.TotalAmtP.get(),
                                                  self.AdvAmtP.get(), self.in_DueAmt.get(), self.CustIDP.get())
                messagebox.showinfo("Success", "{} Has Been Checked Out Successfully!".format(name))

        else:
            a = int(self.in_AddCharge.get()) + int(self.AdditionalChargesP.get())
            name = hotel_database.addCheckout(str(a), self.TotalAmtP.get(),
                                              self.AdvAmtP.get(), self.in_DueAmt.get(), self.CustIDP.get())
            messagebox.showinfo("Success", "{} Has Been Checked Out Successfully!".format(name))

    def get_cursor2(self, event=""):
        if self.payInfoTable.focus() != '':
            cur_row = self.payInfoTable.focus()
            record = self.payInfoTable.item(cur_row)
            data = record["values"]

            self.recordID.set(data[0])
            self.CustIDP.set(data[1]),
            self.NameP.set(data[2]),
            self.DateInP.set(data[9]),
            self.DateOutP.set(data[10]),
            self.totalDaysP.set(data[13]),
            self.RoomTypeP.set(data[14]),
            self.RoomnoP.set(data[15]),
            self.RoomChargesP.set(data[16]),
            self.ExtraPersonsP.set(data[17]),
            self.AdditionalChargesP.set(data[18]),
            self.TotalAmtP.set(data[19]),
            self.AdvAmtP.set(data[20]),
            self.remainingAmt.set(data[21]),
            self.AdultsP.set(data[11]),
            self.KidsP.set(data[12]),
            self.AddressP.set(data[4]),
            self.MobileP.set(data[5]),
            self.EmailP.set(data[6]),

    def displayPayRecords(self):
        records = self.payInfoTable.get_children()
        for idx in records:
            self.payInfoTable.delete(idx)

        for row in hotel_database.viewPayRecord():
            # --------- CHECK IN DATE ------------------
            r = row[9].split("-")
            y1 = r[2].split(" ")
            t1 = y1[1].split(":")
            row9 = y1[0] + "-" + r[1] + "-" + r[0][2:] + ", " + t1[0] + ":" + t1[1] + ":" + t1[2]

            # --------- CHECK OUT DATE ------------------
            r = row[10].split("-")
            y1 = r[2].split(" ")
            t1 = y1[1].split(":")
            # row9 = datetime(int(r[0]), int(r[1]), int(y1[0]), int(t1[0]), int(t1[1]), int(t1[2]))
            # row9.strftime('%d-%m-%y %H:%M:%S')
            row10 = y1[0] + "-" + r[1] + "-" + r[0][2:] + ", " + t1[0] + ":" + t1[1] + ":" + t1[2]

            self.payInfoTable.insert('', END,
                                     values=(row[0],
                                             row[1],
                                             row[2],
                                             row[3],
                                             row[4],
                                             row[5],
                                             row[6],
                                             row[7],
                                             row[8],
                                             row9,
                                             row10,
                                             row[11],
                                             row[12],
                                             row[13],
                                             row[14],
                                             row[15],
                                             row[16],
                                             row[17],
                                             row[18],
                                             row[19],
                                             row[20],
                                             row[21]))

    def searchPayRecord(self):
        backend.search(self.payInfoTable, self.Searchtxt.get(), self.SearchVar.get())

    # -----------ROOMS BACKEND FUNCTIONS----------------------------------------------------------

    def addroom(self):
        if self.in_roomno.get() == "" or self.in_roomType.get() == "":
            messagebox.showerror("Error", "All fields are Required")
        else:
            # try:
            booking = [(
                self.in_roomno.get(),
                self.in_roomType.get()
            )]
            hotel_database.addRoomRecord(booking)
            messagebox.showinfo("Success", "New Room Has Been Added Successfully!")

    def displayRooms(self):
        records = self.roomInfoTable.get_children()
        for idx in records:
            self.roomInfoTable.delete(idx)

        for row in hotel_database.viewRoomRecord():
            self.roomInfoTable.insert('', END,
                                      values=(row[0], row[1], row[2]))

    def updateRoom(self):
        if self.in_roomno.get() == "" or self.RoomTypeA.get() == "":
            messagebox.showerror("Error", "All fields are Required")
        else:
            hotel_database.updateRoomRecord(self.RoomTypeA.get(),
                                            self.in_roomno.get())
            messagebox.showinfo("Success", "Entry has been UPDATED Successfully!")

    def deleteRoom(self):
        deleteRoom = messagebox.askyesno("System Manager", "Do you want to Delete this Room?")
        if deleteRoom > 0:
            id = self.in_roomno.get()
            hotel_database.deleteRoomRecord(id)
            self.displayRooms()
        else:
            if not deleteRoom:
                return self.displayRooms()

    def availableRoomChecker(self):
        if self.RoomTypeR.get() == 'All' or self.RoomTypeR.get() == "":
            checkInDate = datetime.strptime(self.in_FcheckInDate.get(), '%d-%m-%y, %H:%M:%S')
            checkOutDate = datetime.strptime(self.in_TcheckOutDate.get(), '%d-%m-%y, %H:%M:%S')

            data = hotel_database.roomAvailability(str(checkInDate), str(checkOutDate))
            if len(data) != 0:
                self.roomAvTable.delete(*self.roomAvTable.get_children())
                for row in data:
                    self.roomAvTable.insert('', END, values=(row[0], row[1], row[2]))
            else:
                messagebox.showinfo("System Manager", "There are No Rooms Available of {0} Type Between {1} - {2} Date".format(self.RoomTypeR.get(),self.in_FcheckInDate.get(), self.in_TcheckOutDate.get() ))


if __name__ == '__main__':
    root = Tk()
    HotelApp(root)
    root.mainloop()
