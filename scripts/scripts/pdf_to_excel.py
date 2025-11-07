import pdfplumber
import pandas as pd
import sys

input_pdf = "input.pdf"
output_file = "output.xlsx"

# Extract tables from all pages into one DataFrame
all_tables = []
with pdfplumber.open(input_pdf) as pdf:
    for page in pdf.pages:
        tables = page.extract_tables() or []
        for t in tables:
            df = pd.DataFrame(t)
            if len(df) > 1:
                df.columns = df.iloc[0].astype(str)
                df = df.iloc[1:].reset_index(drop=True)
            all_tables.append(df)

if all_tables:
    merged = pd.concat(all_tables, ignore_index=True)
else:
    # fallback: dump text lines so client gets something usable
    with pdfplumber.open(input_pdf) as pdf:
        text = "\n".join((p.extract_text() or "") for p in pdf.pages)
    merged = pd.DataFrame({"text": text.splitlines()})

if output_file.lower().endswith(".csv"):
    merged.to_csv(output_file, index=False)
else:
    merged.to_excel(output_file, index=False)
print("PDF → Excel/CSV done ✅")
