'''
Main application entry point for the PDF to JSON transcriber.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from pdf_reader import PDFReader
from json_writer import JSONWriter
class ApplicationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF to JSON Transcriber")
        # Create and place GUI elements
        self.create_widgets()
    def create_widgets(self):
        # Button to import PDF
        self.import_button = tk.Button(self.root, text="Import PDF", command=self.import_pdf)
        self.import_button.pack()
        # Button to export JSON
        self.export_button = tk.Button(self.root, text="Export JSON", command=self.export_json, state=tk.DISABLED)
        self.export_button.pack()
        # Label to show the imported file path
        self.file_path_label = tk.Label(self.root, text="")
        self.file_path_label.pack()
    def import_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            self.file_path_label.config(text=file_path)
            self.pdf_reader = PDFReader(file_path)
            self.export_button.config(state=tk.NORMAL)
    def export_json(self):
        if hasattr(self, 'pdf_reader'):
            structured_content = self.pdf_reader.extract_text()
            if structured_content is not None:
                json_content = JSONWriter.convert_to_json(structured_content)
                file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
                if file_path:
                    JSONWriter.write_to_file(json_content, file_path)
                    messagebox.showinfo("Success", "The JSON file has been exported successfully.")
                    self.export_button.config(state=tk.DISABLED)
                    self.file_path_label.config(text="")
            else:
                messagebox.showerror("Error", "Failed to extract text from the PDF.")
def main():
    root = tk.Tk()
    app = ApplicationGUI(root)
    root.mainloop()
if __name__ == "__main__":
    main()