manual.md

```
# PDF to JSON Transcriber User Manual

Welcome to the PDF to JSON Transcriber user manual. This software is designed to transcribe text from PDF documents, such as guides and manuals, into an efficient JSON format. The resulting JSON documents will be true to the specific text of the PDF, optimized for training GPT models.

## System Requirements

- Python 3.6 or higher
- PyMuPDF 1.18.19

## Installation

Before running the application, you need to install the required dependencies. You can do this by running the following command in your terminal:

```bash
pip install -r requirements.txt
```

This will install PyMuPDF, which is necessary for reading PDF files.

## Starting the Application

To start the application, navigate to the directory containing the `main.py` file and run:

```bash
python main.py
```

This will open the graphical user interface (GUI) of the PDF to JSON Transcriber.

## Using the Software

### Importing a PDF

1. Click on the "Import PDF" button.
2. Navigate to the location of the PDF file you wish to transcribe.
3. Select the file and click "Open".

The path of the imported PDF will be displayed in the application window.

### Exporting to JSON

1. Once a PDF is imported, the "Export JSON" button will become active.
2. Click on the "Export JSON" button.
3. Choose the desired location to save the JSON file and provide a file name.
4. Click "Save".

A success message will appear if the JSON file has been exported successfully. If there is an error during the text extraction process, an error message will be displayed.

## Main Functions

- **Import PDF**: Allows you to select and import a PDF file from your local storage.
- **Export JSON**: Once a PDF is imported, you can export the transcribed text to a JSON file.
- **File Path Display**: Shows the path of the currently imported PDF file.

## Troubleshooting

If you encounter any issues with the software, please ensure that you have the correct version of Python installed and that all dependencies from the `requirements.txt` file have been installed properly.

For further assistance, please contact our support team at support@chatdev.com.

Thank you for choosing ChatDev's PDF to JSON Transcriber for your document transcription needs.
```

This user manual provides clear instructions on how to install and use the PDF to JSON Transcriber software. It includes a brief introduction to the software's main functions, installation instructions, and a step-by-step guide on how to import PDFs and export them as JSON files. Additionally, it provides troubleshooting tips and contact information for further support.