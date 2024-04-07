'''
PDFReader class to handle reading and parsing PDF documents using PyMuPDF, preserving the original structure.
'''
import fitz  # PyMuPDF
class PDFReader:
    def __init__(self, file_path):
        self.file_path = file_path
    def extract_text(self):
        try:
            with fitz.open(self.file_path) as doc:
                structured_content = []
                for page in doc:
                    blocks = page.get_text("dict")["blocks"]
                    for block in blocks:
                        if 'lines' in block:  # Check if block contains lines of text
                            for line in block["lines"]:
                                span_texts = [span['text'].strip() for span in line["spans"]]
                                full_text = ' '.join(span_texts)
                                if full_text:  # Avoid adding empty strings
                                    structured_content.append(full_text)
                return structured_content
        except Exception as e:
            print(f"An error occurred while extracting text: {e}")
            return None