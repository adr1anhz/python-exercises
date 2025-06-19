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
    print(invoice_number)
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr. {invoice_number}")
    pdf.output(f"{filename}.pdf")