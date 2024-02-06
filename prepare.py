import os
import sys
from langchain.schema import Document

from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("pdfs/Ley_1437_de_2011.pdf")
pages = loader.load_and_split()

print(pages[0])