import fitz  # PyMuPDF
import os
import re

# To convert pdf pages to images
def convert_pdf_to_images_pymupdf(pdf_path, output_folder):
    """
    Converts each page of a PDF file into a separate image file using PyMuPDF.

    Args:
        pdf_path (str): The path to the input PDF file.
        output_folder (str): The folder where the output image files will be saved.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_formats = [
    "PNG",
    "PNM",
    "PGM",
    "PPM",
    "PBM",
    "PAM",
    "PSD",
    "PS",
    "JPG",
    "JPEG"
]
    valid_formats = [fmt.lower() for fmt in image_formats]
    
    while True:
        choose_type = input("Enter a valid image format (e.g., png, jpg): ").strip().lower()
        if choose_type in valid_formats:
            print(f"You chose a valid format: {choose_type.upper()}")
            break
        else:
            print("Invalid format. Please choose one from the list:")
            print(", ".join(image_formats))

    try:
        scale = float(input("Enter scale factor for image quality (e.g., 2 for medium, 4 for high): "))
    except ValueError:
        scale = 2 


    try:
        with fitz.open(pdf_path) as document:
            for page_num in range(len(document)):
                page = document.load_page(page_num)
                pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale)) # increase the number for better resolution, but slower performance
                output_image_path = os.path.join(output_folder, f"page_{page_num + 1}.{choose_type}")
                pix.save(output_image_path)
                print(f"Saved {output_image_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# main function to manage the inputs and outputs
def main():
    pdf_file_name = input("Enter the PDF file path (You can put PDF file together with script and enter only PDF file name): ")
    if pdf_file_name.lower().endswith(".pdf"):
        pdf_file_name = pdf_file_name[:-4]
    output_name = input("Enter the output folder name to save the images (output folder will be created at the same script path): ")
    safe_output_name = re.sub(r'[^a-zA-Z0-9_\-]', '_', output_name)
    convert_pdf_to_images_pymupdf(f"{pdf_file_name}.pdf",f"{safe_output_name}") # choose path for the pdf, choose name for the folder

# run the code
if __name__ == "__main__":
    main()



# For future: we may put a system to convert other formats to pdf then save each pages as pictures like docx to pdf