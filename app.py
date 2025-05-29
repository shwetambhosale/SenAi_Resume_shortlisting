import streamlit as st
from PyPDF2 import PdfReader
import docx2txt
import io

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def extract_text_from_docx(file):
    text = docx2txt.process(file)
    return text

def main():
    st.title("Resume Content Extractor")

    uploaded_file = st.file_uploader("Upload your resume", type=["pdf", "docx"])
    
    if uploaded_file is not None:
        file_extension = uploaded_file.name.split(".")[-1].lower()
        
        if file_extension == "pdf":
            text = extract_text_from_pdf(uploaded_file)
        elif file_extension == "docx":
            text = extract_text_from_docx(uploaded_file)
        else:
            st.error("Unsupported file type. Please upload a PDF or DOCX file.")
            return

        if text:
            st.subheader("Extracted Resume Content:")
            st.text_area("Text Content", text, height=400)
        else:
            st.warning("No text could be extracted from the uploaded file.")

if __name__ == "__main__":
    main()
