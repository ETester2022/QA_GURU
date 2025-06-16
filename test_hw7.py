from zipfile import ZipFile
from pypdf import PdfReader
import io
import pandas as pd
import csv


def test_read_pdf(create_archive):
    with ZipFile("sources/archive.zip") as zf:
        pdf_bytes = zf.read("example.pdf")
        pdf_file = io.BytesIO(pdf_bytes)
        reader = PdfReader(pdf_file)

        lst_texts = [
            "PDF test file",
            "Document file type: PDF",
            "Version: 1.0"
        ]

        for text in lst_texts:
            assert text in reader.pages[0].extract_text()


def test_read_xlsx(create_archive):
    with ZipFile("sources/archive.zip") as zf:
        xlsx_bytes = zf.read("example.xlsx")
        xlsx_file = io.BytesIO(xlsx_bytes)
        df = pd.read_excel(xlsx_file)
        columns = df.columns

        assert columns[0] == "XLSX test file"


def test_read_csv(create_archive):
    with ZipFile("sources/archive.zip") as zf:
        csv_bytes = zf.read('example.csv').decode('utf-8')
        csv_file = io.StringIO(csv_bytes)
        reader = csv.DictReader(csv_file)
        first_row = next(reader)
        expected = {
            '': '',
            'CSV test file': ''
        }
        assert first_row == expected
