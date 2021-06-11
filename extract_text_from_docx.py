import docx2txt 

def extract_text_from_doc(file_location) : 
    txt = docx2txt.process(file_location)

    if txt :
        return txt.replace('/t',' ')
    return None


if __name__ == '__main__' : 
    print(extract_text_from_doc("sample.docx"))