import PyPDF2
def readpdf(file_path):
    with open(file_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)

        # Get the number of pages in the PDF
        num_pages = len(pdf_reader.pages)

        # Iterate through each page and extract text
        text = ""
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

        return text

        # Example usage
file_path = 'Sandeep_K_Resume.pdf'
pdf_text = readpdf(file_path)
print(pdf_text)