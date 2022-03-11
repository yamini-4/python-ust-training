import PyPDF2
# from PyPDF2 import PdfFileReader
with open('WBP.pdf', 'rb')as pdf_handle:
    pdf_reader = PyPDF2.PdfFileReader(pdf_handle)

with open('WBP.pdf','rb')as pdf_handle:
    pdf_reader = PyPDF2.PdfFileReader(pdf_handle)
    page = pdf_reader.numPages   #numPages is used to find no of pages present in the pdf
    print(page)


# from PyPDF2 import PdfFileReader
with open('WBP.pdf','rb')as pdf_handle:
    pdf_reader = PyPDF2.PdfFileReader(pdf_handle)
    page_one = pdf_reader.getPage(2)#assigning page number
    ex_text = page_one.extractText()#extracting text for assigned page no
    print(ex_text)

#     copy pages and append pages to new pdf
with open('WBP.pdf', 'rb')as pdf_handle:
    pdf_reader = PyPDF2.PdfFileReader(pdf_handle)
    page_one = pdf_reader.getPage(0)
    pdf_writer = PyPDF2.PdfFileWriter()
    pdf_writer.addPage(page_one)
    pdf_output = open('new.pdf', 'wb')
    pdf_writer.write(pdf_output)
    #pdf_output.close
    

    # read all the text from pdf file
    with open('WBP.pdf', 'rb') as pdf_handle:
        pdf_reader = PyPDF2.PdfFileReader(pdf_handle)
        f = open('WBP.pdf', 'rb')
        text = []
        for i in range(pdf_reader.numPages):
            page = pdf_reader.getPage(i)
            text.append(page.extractText())
        # print(text)#prin all text
        print(text[2])  # perticular page