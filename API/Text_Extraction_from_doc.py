from docx import Document

def extract_text_from_docx(file_path):
    # Creating object
    doc = Document(file_path)
    text = []
    # Extracting Text
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    return '\n'.join(text)