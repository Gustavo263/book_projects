import PyPDF2
from PyPDF2 import PdfFileWriter

pdf_file = open('C:/Users/Gustavo/OneDrive/Documentos/tutta.pdf', 'rb')

pdf_dados = PyPDF2.PdfReader(pdf_file)

print(len(pdf_dados.pages))

pagina1 = pdf_dados.pages[0]
texto_pagina1 = pagina1.extract_text()
print(texto_pagina1)