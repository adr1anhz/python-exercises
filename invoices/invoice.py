import pandas as pd
import glob


filepaths = glob.glob("*xlsx")


for path in filepaths:
    df = pd.read_excel(path, sheet_name="Sheet 1")
    print(df)