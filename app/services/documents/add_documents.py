from langchain_community.document_loaders import PyMuPDFLoader, TextLoader
import os
from fastapi import HTTPException


class DocumentTextExtractor:
    """
    A class that extract text from various file types.
    -pdf
    -docx
    -txt
    -md
    """

    @staticmethod
    def extract_text(file_path):
        file_type = os.path.splitext(file_path)[-1].lower()
        if file_type == ".pdf":
            return DocumentTextExtractor.extract_text_from_pdf(file_path)
        elif file_type == ".docx" or file_type == ".txt" or file_type == ".md":
            return DocumentTextExtractor.extract_text_from_docx_txt_md(file_path)
        else:
            raise ValueError(f"Unsupported file type: {file_type}")

    @staticmethod
    def extract_text_from_pdf(file):
        try:
            loader = PyMuPDFLoader(file)
            documents = loader.load()
            text = ""
            for doc in documents:
                text += doc.page_content
            return text
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def extract_text_from_docx_txt_md(file):
        try:
            loader = TextLoader(file)
            documents = loader.load()
            text = ""
            for doc in documents:
                text += doc.page_content
            return text
        except Exception as e:
            return None
