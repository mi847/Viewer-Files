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
doc = PdfDocument()
doc.LoadFromFile(a)
doc.SaveToFile("f.html", FileFormat.HTML)
doc.Close()
webbrowser.open("f.html", new=1)
