from PyPDF2 import PdfReader
from docx import Document
from typing import Literal

# функция считывает файлы pdf или docx и выводит текст, для более стабильной работы можено добавить
# блок try except и добавить валидацию
async def reader(file_path: str, file_type: str|None = Literal["docx", "pdf"]) -> str:
    if file_type == "docx":
        doc = Document(file_path)

        text_raw = [para.text for para in doc.paragraphs]
        text = "\n".join(text_raw)
        return text
    if file_type == "pdf":
        """
        Для полноценной корректной работы условия, нужно добавить цикл для обработки всех страниц .pdf файла
        """
        pdf_reader = PdfReader(file_path)
        page = pdf_reader.pages[0]
        text = page.extract_text()
        return text
