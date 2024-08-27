import os
import shutil
import webbrowser
from docx2pdf import convert
from spire.pdf import *
from spire.doc import *
with open("data", "r") as f:
    a=f.read()
d = a.split('.')[-1]
doc = Document()
doc.LoadFromFile(a)
doc.SaveToFile("f.pdf", FileFormat.PDF)
doc.Close()
doc = PdfDocument()
doc.LoadFromFile("f.pdf")
doc.SaveToFile("f.html", FileFormat.HTML)
doc.Close()
os.remove("f.pdf")
webbrowser.open("f.html", new=1)
