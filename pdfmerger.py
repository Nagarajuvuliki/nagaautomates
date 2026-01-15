import os
from pypdf import PdfWriter
# 1. Setup the merger tool
merger = PdfWriter()
# 2. Create a list of PDFs you want to join
# Make sure these files exist in your folder!
files_to_merge = ["part1.pdf", "part2.pdf", "invoice.pdf"]
print("Starting PDF Merge...")
try:
    # 3. Loop through the list and append them
    for filename in files_to_merge:
        merger.append(filename)
        print(f"   [+] Added: {filename}")

    merger.write("final_document.pdf")
    merger.close()
    print("Success! Created 'final_document.pdf'")
except Exception as e:
    print(f"Error: {e}")
         