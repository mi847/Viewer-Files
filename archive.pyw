import glob
import os
import patoolib
import random
import shutil
import sys
b=random.randint(1, 10000000000000000000000000000000000000000000)
i=str(b)
os.mkdir(i)
cwd = os.getcwd()
with open("data", "r") as f:
    b=f.read()
try:
    patoolib.extract_archive(b, outdir=i)
    os.chdir(i)
    s=glob.glob("**\\*")
    print("Files found in the archive:")
    print('\n'.join(s))
    print('To close the program, enter "||".')
except:
    print("This format is not supported:")
    input()
    sys.exit()
while True:
    print("Enter the received path to the desired file:")
    c=input()
    if c=="||":
        os.chdir(cwd)
        shutil.rmtree(i)
        break
    j=cwd+"\\"+c
    with open("data", "w") as f:
        f.write(j)
    os.startfile("doc.pyw")
