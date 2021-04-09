from tkinter import *
from backend import remove
from tkPDFViewer import tkPDFViewer as pdf


class BillPreview(Toplevel):

    def __init__(self, master=None, cid=None, name=None):
        super().__init__(master=master)
        pdfname = "{0}_{1}_Receipt.pdf".format(remove(cid), remove(name))
        self.title(pdfname)
        self.geometry("600x900")

        # ------------PRINT PREVIEW ---------------------------------------------------------------------------------
        showPDF = pdf.ShowPdf()
        viewPDF = showPDF.pdf_view(self,
                                   pdf_location=pdfname, width=500,
                                   height=900)

        viewPDF.pack(side=LEFT, fill='both', expand='True')
        viewPDF.pack_propagate(0)
