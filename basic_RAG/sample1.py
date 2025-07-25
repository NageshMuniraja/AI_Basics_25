import fitz  # PyMuPDF for PDFs

doc = fitz.open("FAQ.pdf")
text = ""
for page in doc:
    text += page.get_text()
chunks = text.split("\n\n")  # split into paragraphs/questions

