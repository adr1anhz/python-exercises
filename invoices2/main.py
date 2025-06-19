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
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()
        splitter = path.strip(".txt")
        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=10, h=8, txt=f"{splitter}", ln=1)
        pdf.set_font("Times", size=12)
        for line in data.splitlines():
            pdf.multi_cell(0, 8, txt=line)
        
        
pdf.output("output.pdf")



#pdf.output("output.pdf")

        #print(data)
        #print("PRZERWA")