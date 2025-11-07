import pandas as pd

df = pd.read_csv("input.csv")
df = df.drop_duplicates()
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
df.to_csv("cleaned_output.csv", index=False)
print("Cleaning Completed ✅")
