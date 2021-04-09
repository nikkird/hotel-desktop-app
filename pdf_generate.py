from tkinter import *
from tkinter import messagebox, ttk
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
import hotel_database
from pathlib import Path
from backend import remove


# CREATE PDF TEMPLATE
styles = getSampleStyleSheet()
title_style1 = styles["Heading2"]
title_style2 = styles["Heading4"]


# 0: left, 1: center, 2: right
def pdfReceiptGenerate(bid, cin, cout, days, adult, kid, rtype, rno, name, pno, email, add, rcharge, exper, addcharges,
                       total):
    try:
        n = name
        cid = bid
        file = Path("{0}_{1}_Receipt.pdf".format(remove(cid), remove(n)))
        if bid == "" and cin == "" and cout == "" and days == "" and adult == "" and kid == "" and rtype == "" and rno == "" and name == "" and pno == "" and email == "" and add == "" and rcharge == "" and exper == "" and addcharges == "" and total == "":
            messagebox.showerror("System Manager", "Insufficient Details, Can't Generate Invoice!")

        elif file.is_file():
            choice = messagebox.askyesno("System Manager", "File Already Exists!\n Do You Want To Add Changes Anyway?")
            if choice is True:
                Hstyle = ParagraphStyle('HotelVishwaChakra', fontName="Times-Bold", textColor="steelblue", fontSize=25,
                                        parent=styles['Heading2'],
                                        alignment=0, spaceBefore=9, borderPadding=10,
                                        spaceAfter=4)
                Hstyle2 = ParagraphStyle('SubHeading', fontName="Helvetica", fontSize=9, parent=styles['Heading2'],
                                         alignment=2, spaceBefore=0, borderPadding=0,
                                         spaceAfter=0)

                Hstyle3 = ParagraphStyle('SubHeading', fontName="Helvetica", fontSize=9, parent=styles['Heading2'],
                                         alignment=2, spaceBefore=6, borderPadding=20,
                                         spaceAfter=4)

                title = Paragraph("Hotel Vishwa Chakra", Hstyle)
                addressline1 = Paragraph("addressline 1,", Hstyle2)
                addressline2 = Paragraph("addressline 2,", Hstyle2)
                addressline3 = Paragraph(" addressline 3", Hstyle2)
                phno = Paragraph("Ph: number1 | number2", Hstyle3)
                # <b>ReportLab Left
                #      <font color=red>Logo</font></b>

                header = [
                    [''],
                    [''],
                    [title, [addressline1, addressline2, addressline3, phno]]
                ]
                lstyle = ParagraphStyle('labels', fontName="Helvetica", fontSize=10,
                                        alignment=0, spaceAfter=4)
                bid = Paragraph(bid, lstyle)
                cin = Paragraph(cin, lstyle)
                cout = Paragraph(cout, lstyle)
                days = Paragraph(days, lstyle)
                numofperson = Paragraph("Adults {0}/ Kids {1}".format(adult, kid), lstyle)
                rtype = Paragraph(rtype, lstyle)
                rno = Paragraph(rno, lstyle)
                name = Paragraph(name, lstyle)
                pno = Paragraph(pno, lstyle)
                email = Paragraph(email, lstyle)
                add = Paragraph(add, lstyle)
                rcharge = Paragraph(rcharge, lstyle)
                exper = Paragraph(exper, lstyle)
                addcharges = Paragraph(addcharges, lstyle)
                total = Paragraph(total, lstyle)

                # sub-titles
                hstyle = ParagraphStyle('labels', fontName="Helvetica-Bold", fontSize=10,
                                        alignment=0, spaceAfter=4)
                rd = Paragraph("RESERVATION DETAILS", hstyle)
                b = Paragraph("Booking ID", hstyle)
                ci = Paragraph("Check In", hstyle)
                co = Paragraph("Check Out", hstyle)
                d = Paragraph("No. of Days", hstyle)
                ak = Paragraph("No. of Adults/ Kids", hstyle)
                rt = Paragraph("Room Type", hstyle)
                rn = Paragraph("Room No.", hstyle)
                gn = Paragraph("Guest Name", hstyle)
                pn = Paragraph("Phone No.", hstyle)
                e = Paragraph("Email", hstyle)
                a = Paragraph("Address", hstyle)
                rc = Paragraph("Room Charges", hstyle)
                ep = Paragraph("Extra Persons", hstyle)
                ac = Paragraph("Additional Charges", hstyle)
                ap = Paragraph("Net Amount paid", hstyle)

                RERERVATIONDATA = [
                    [rd],
                    [
                        b, bid],
                    [ci, cin],
                    [co, cout],
                    [d, days],
                    [ak, numofperson],
                    [rt, rtype],
                    [rn, rno],
                ]

                GUESTDATA = [
                    [""],
                    [gn, name],
                    [pn, pno],
                    [e, email],
                    [a, add],
                    [""]
                ]
                RATEDATA = [
                    [""],
                    [rc, rcharge],
                    [ep, exper],
                    [ac, addcharges],
                    [ap, total]
                ]
                # creating a Base Document Template of page size A4
                pdf = SimpleDocTemplate("{0}_{1}_Receipt.pdf".format(remove(cid), remove(n)), pagesize=A4)

                style = TableStyle(
                    [
                        ("BOX", (0, 0), (-1, -1), 1, colors.black),
                        ("GRID", (0, 1), (4, 9), 1, colors.black),
                        ("BACKGROUND", (0, 0), (3, 0), colors.lightsteelblue),
                        ("TEXTCOLOR", (0, 0), (-1, 0), 1, colors.black),
                        ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                        ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),
                    ]
                )
                styleh = TableStyle(
                    [
                        ("BACKGROUND", (0, 0), (3, 0), colors.lightsteelblue),
                        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                        ('VALIGN', (0, -1), (-1, -1), 'MIDDLE'),
                        ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),
                    ]
                )
                styleheading = TableStyle(
                    [("BOX", (0, 0), (-1, -1), 1, colors.white),
                     ("GRID", (0, 1), (4, 9), 1, colors.white),
                     ("BACKGROUND", (0, 0), (3, 0), colors.white),
                     # ('LINEABOVE', (0, 0), (-1, 1), 1, colors.pink),
                     ("TEXTCOLOR", (0, 0), (-1, 0), colors.steelblue),
                     ('VALIGN', (0, -1), (-1, -1), 'MIDDLE'),
                     ("BACKGROUND", (0, 1), (-1, -1), colors.white),
                     ]
                )
                styleGuest = TableStyle(
                    [
                        ('LINEABOVE', (0, 0), (-1, 0), 1.5, colors.black),
                        ("BACKGROUND", (0, 0), (3, 0), colors.whitesmoke),
                        ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
                        ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                        ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),
                    ]
                )

                invoice_template = []
                invoice_template.append(Table(header, colWidths=[250, 250], style=styleheading))
                invoice_template.append(Table(GUESTDATA, colWidths=[100, 400], style=styleGuest, spaceBefore=10))
                invoice_template.append(Table(RERERVATIONDATA, colWidths=[100, 400], style=style, spaceBefore=10))
                invoice_template.append(Table(RATEDATA, colWidths=[100, 400], style=style, spaceBefore=10))
                # table = Table(DATA, style=style)

                pdf.build(invoice_template)
                messagebox.showinfo("System Manager", "Invoice Generated Successfully!")
    except EXCEPTION as e:
        messagebox.showerror("System Manager", "Something Went Wrong!\n" + str(e))

