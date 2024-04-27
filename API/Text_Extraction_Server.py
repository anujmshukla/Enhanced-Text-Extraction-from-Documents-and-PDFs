import os

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from Text_Extraction_from_pdf import extract_text_from_pdf
from Text_Extraction_from_doc import extract_text_from_docx
import PyPDF2
from docx import Document

app = FastAPI()

# CORS middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the directory to save the uploaded files
UPLOAD_DIR = "uploads"

# Create the upload directory if it doesn't exist
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def Initial():
    return{"server":"ready"}
        

@app.post("/get_text_from_file")
async def upload_file(file: UploadFile = File(...)):
    # Checking file format
    if not file.filename.lower().endswith((".doc", ".docx", ".pdf")):
        return JSONResponse(status_code=400, content={"message": "Only DOC, DOCX, and PDF files are allowed."})
    
    # Saving the file to disk
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())
        
    if file.filename.lower().endswith((".doc", ".docx")):
        text = extract_text_from_docx(file_path)
    else:
        text = extract_text_from_pdf(file_path)
       

    return {"filename": file.filename, "saved_path": file_path, "text":text}
