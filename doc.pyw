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
d = a.split('.')[-1]
if d == "docx":
    os.startfile("doc (2).pyw")
elif d == "doc":
    os.startfile("doc (2).pyw")
elif d == "html":
    cwd = os.getcwd()+"\\f.html"
    shutil.copy(a, cwd)
    webbrowser.open("f.html", new=1)
elif d == "rtf":
    os.startfile("rtf.pyw")
elif d == "ppt":
    os.startfile("ppt.pyw")
elif d == "pptx":
    os.startfile("ppt.pyw")
elif d == "pdf":
    os.startfile("pdf.pyw")
elif d == "xls":
    os.startfile("xls.pyw")
elif d == "xlm":
    os.startfile("xls.pyw")
elif d == "xlt":
    os.startfile("xls.pyw")
elif d == "xlsm":
    os.startfile("xls.pyw")
elif d == "xltx":
    os.startfile("xls.pyw")
elif d == "xltm":
    os.startfile("xls.pyw")
elif d == "dot":
    os.startfile("doc (2).py")
elif d == "wbk":
    os.startfile("doc (2).py")
elif d == "docm":
    os.startfile("doc (2).py")
elif d == "dotx":
    os.startfile("doc (2).py")
elif d == "dotm":
    os.startfile("doc (2).py")
elif d == "pot":
    os.startfile("ppt.pyw")
elif d == "pps":
    os.startfile("ppt.pyw")
elif d == "ppa":
    os.startfile("ppt.pyw")
elif d == "pptm":
    os.startfile("ppt.pyw")
elif d == "potx":
    os.startfile("ppt.pyw")
elif d == "potm":
    os.startfile("ppt.pyw")
elif d == "ppsx":
    os.startfile("ppt.pyw")
elif d == "sldx":
    os.startfile("ppt.pyw")
elif d == "sldm":
    os.startfile("ppt.pyw")
elif d=="7z":
    os.startfile("archive.pyw")
elif d=="cb7":
    os.startfile("archive.pyw")
elif d=="ace":
    os.startfile("archive.pyw")
elif d=="ace":
    os.startfile("archive.pyw")
elif d=="adf":
    os.startfile("archive.pyw")
elif d=="alz":
    os.startfile("archive.pyw")
elif d=="ape":
    os.startfile("archive.pyw")
elif d=="a":
    os.startfile("archive.pyw")
elif d=="arj":
    os.startfile("archive.pyw")
elif d=="arc":
    os.startfile("archive.pyw")
elif d=="bz2":
    os.startfile("archive.pyw")
elif d =="bz3":
    os.startfile("archive.pyw")
elif d == "arc":
    os.startfile("archive.pyw")
elif d == "cab":
    os.startfile("archive.pyw")
elif d == "chm":
    os.startfile("archive.pyw")
elif d == "Z":
    os.startfile("archive.pyw")
elif d == "cpio":
    os.startfile("archive.pyw")
elif d == "deb":
    os.startfile("archive.pyw")
elif d == "dms":
    os.startfile("archive.pyw")
elif d == "flac":
    os.startfile("archive.pyw")
elif d == "iso":
    os.startfile("archive.pyw")
elif d == "lrz":
    os.startfile("archive.pyw")
elif d == "lha":
    os.startfile("archive.pyw")
elif d == "lzh":
    os.startfile("archive.pyw")
elif d == "lz":
    os.startfile("archive.pyw")
elif d == "lzma":
    os.startfile("archive.pyw")
elif d == "lzo":
    os.startfile("archive.pyw")
elif d == "rpm":
    os.startfile("archive.pyw")
elif d == "rar":
    os.startfile("archive.pyw")
elif d == "cbr":
    os.startfile("archive.pyw")
elif d == "rz":
    os.startfile("archive.pyw")
elif d == "shn":
    os.startfile("archive.pyw")
elif d == "tar":
    os.startfile("archive.pyw")
elif d == "cbt":
    os.startfile("archive.pyw")
elif d == "xz":
    os.startfile("archive.pyw")
elif d == "zip":
    os.startfile("archive.pyw")
elif d == "jar":
    os.startfile("archive.pyw")
elif d == "cbz":
    os.startfile("archive.pyw")
elif d == "zoo":
    os.startfile("archive.pyw")
elif d == "zst":
    os.startfile("archive.pyw")
else:
    os.startfile("txt.pyw")
