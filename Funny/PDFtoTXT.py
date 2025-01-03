import pdfplumber
import os

def pdf_to_txt_folder(pdf_folder, txt_path):
    try:
        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            for file_name in os.listdir(pdf_folder):
                if file_name.lower().endswith('.pdf'):
                    pdf_path = os.path.join(pdf_folder, file_name)
                    with pdfplumber.open(pdf_path) as pdf:
                        txt_file.write(f"\n--- {file_name} ---\n")
                        for page_number, page in enumerate(pdf.pages, start=1):
                            # Extract text from the page
                            text = page.extract_text(layout=True)
                            if text:
                                txt_file.write(f"\n--- Page {page_number} ---\n")
                                txt_file.write(text)
                                txt_file.write("\n")
                            else:
                                print(f"Warning: No text extracted on page {page_number} of {file_name}.")
        print(f"Conversion completed. Text saved to {txt_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    pdf_folder = "C:\\Users\\marqu\\Desktop\\pdfs"
    txt_path = "C:\\Users\\marqu\\Desktop\\TXT\\Input.txt"

    if os.path.exists(pdf_folder) and os.path.isdir(pdf_folder):
        pdf_to_txt_folder(pdf_folder, txt_path)
    else:
        print("Invalid folder path. Please check and try again.")