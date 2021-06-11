import re
import docx2txt

PHONE_REG = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')


def doc_to_text_docx(file_path):
    txt = docx2txt.process(file_path)
    if txt :
        return txt.replace('\t',' ')
    return None


def extract_phone_number(resume_text):
    phone = re.findall(PHONE_REG, resume_text)

    if phone:
        number = ''.join(phone[0])

        if resume_text.find(number) >= 0 and len(number) < 16:
            return number
    return None


if __name__ == '__main__':
    text = doc_to_text_docx('sample.docx')
    phone_number = extract_phone_number(text)

    print(phone_number) 