import zipfile
import pandas as pd
import os

print("=== Script started ===")

zip_path = "archive.zip"
extract_folder = "data"

# Extract ZIP
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_folder)

print("ZIP extracted")

texts = []
labels = []
filenames = []

for root, dirs, files in os.walk(extract_folder):
    for file in files:
        if file.lower().endswith(".txt"):
            file_path = os.path.join(root, file)

            # Label = top-level folder name
            relative_path = os.path.relpath(root, extract_folder)
            label = relative_path.split(os.sep)[0]

            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                texts.append(f.read())
                labels.append(label)
                filenames.append(file)

print("Total text files read:", len(texts))

df = pd.DataFrame({
    "filename": filenames,
    "label": labels,
    "text": texts
})

df.to_csv("news_dataset.csv", index=False)

print("✅ news_dataset.csv created successfully")
