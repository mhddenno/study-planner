from py_pdf_parser.loaders import load_file
from py_pdf_parser.visualise import visualise
from typing import Any

def load(path:str) -> Any:
    """Load a PDF file from Path. """
    docs = load_file(path)
    return docs

def visualise_book(document):
    visualise(document)

if __name__ == '__main__':
    visualise_book(load('books/simple_memo.pdf')) 