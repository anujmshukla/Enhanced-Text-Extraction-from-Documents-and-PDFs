import PyPDF2

def extract_text_from_pdf(file_path):
    text = ""
    # opeaning file in binary read formate
    with open(file_path, 'rb') as file:
        #creating object
        reader = PyPDF2.PdfReader(file)
        # getting number of pages
        num_pages = len(reader.pages)
        #extracting text
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text
