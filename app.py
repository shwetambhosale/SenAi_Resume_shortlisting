import streamlit as st
import os
from PyPDF2 import PdfReader
import docx2txt

def extract_text_from_pdf(file_path):
    try:
        reader = PdfReader(file_path)
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    except:
        return "Error reading PDF."

def extract_text_from_docx(file_path):
    try:
        return docx2txt.process(file_path)
    except:
        return "Error reading DOCX."

def extract_text_from_file(file_path):
    if file_path.lower().endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif file_path.lower().endswith(".docx"):
        return extract_text_from_docx(file_path)
    else:
        return "Unsupported file type."

def main():
    st.title("Resume Folder Content Viewer")

    folder_path = "Resumes"

    if folder_path and os.path.isdir(folder_path):
        resume_files = [f for f in os.listdir(folder_path) if f.lower().endswith((".pdf", ".docx"))]

        if resume_files:
            for file_name in resume_files:
                file_path = os.path.join(folder_path, file_name)
                st.subheader(f"📄 {file_name}")
                content = extract_text_from_file(file_path)
                st.text_area("Extracted Content", content, height=300)
        else:
            st.warning("No PDF or DOCX files found in the folder.")
    elif folder_path:
        st.error("Invalid folder path.")

if __name__ == "__main__":
    main()
