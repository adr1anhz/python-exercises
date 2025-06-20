import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path


filepaths = glob.glob("*xlsx")


for path in filepaths:
    df = pd.read_excel(path, sheet_name="Sheet 1")

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    filename = Path(path). stem
    invoice_number = filename.split("-")[0]

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr. {invoice_number}", ln=1)

    date = filename.split("-")[1]

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date: {date}")


    
    pdf.output(f"{filename}.pdf")