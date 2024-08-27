import os
import shutil
import webbrowser
from docx2pdf import convert
from spire.pdf import *
from spire.doc import *
from spire.xls import *
from spire.presentation import *
with open("data", "r") as f:
    a=f.read()
workbook = Workbook()
workbook.LoadFromFile(a)
for sheet in workbook.Worksheets:
    pageSetup = sheet.PageSetup
    pageSetup.TopMargin = 0.3
    pageSetup.BottomMargin = 0.3
    pageSetup.LeftMargin = 0.3
    pageSetup.RightMargin = 0.3
workbook.ConverterSetting.SheetFitToPage = True
workbook.SaveToFile("f.pdf", FileFormat.PDF)
workbook.Dispose()
doc = PdfDocument()
doc.LoadFromFile("f.pdf")
doc.SaveToFile("f.html", FileFormat.HTML)
doc.Close()
os.remove("f.pdf")
webbrowser.open("f.html", new=1)
