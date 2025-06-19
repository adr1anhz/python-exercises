import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path


filepaths = glob.glob("*txt")
#print(filepaths)
pdf = FPDF(orientation="P", unit="mm", format="A4")

for path in filepaths:
    with open(path, "r") as file:
        data = file.read()
        dupa = path.strip(".txt")
        print(dupa)
        
        
pdf.output("output.pdf")



#pdf.output("output.pdf")

        #print(data)
        #print("PRZERWA")