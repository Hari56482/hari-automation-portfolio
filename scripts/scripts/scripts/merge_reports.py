import pandas as pd
import glob, os

src_folder = "reports"        # put your CSV/Excel files in a folder named 'reports'
output_file = "merged_reports.csv"

files = sorted(
    glob.glob(os.path.join(src_folder, "*.csv")) +
    glob.glob(os.path.join(src_folder, "*.xlsx")) +
    glob.glob(os.path.join(src_folder, "*.xls"))
)

if not files:
    raise SystemExit("No files found in 'reports' folder.")

frames = []
for f in files:
    ext = os.path.splitext(f)[1].lower()
    df = pd.read_excel(f) if ext in [".xlsx", ".xls"] else pd.read_csv(f)
    df["source_file"] = os.path.basename(f)  # useful for tracking
    frames.append(df)

merged = pd.concat(frames, ignore_index=True, sort=False)
if output_file.lower().endswith(".xlsx"):
    merged.to_excel(output_file, index=False)
else:
    merged.to_csv(output_file, index=False)
print(f"Merged {len(files)} files → {output_file} ✅")
