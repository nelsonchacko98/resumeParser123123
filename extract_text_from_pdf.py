
from pdfminer.high_level import extract_text


def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)


if __name__ == '__main__':
    text = extract_text_from_pdf('Resume_Nelson.pdf')
    
    file = open("text_from_resume_nelson_pdf.txt","w")

    file.write(text)
    file.close()

    print("all operations complete successfully")
