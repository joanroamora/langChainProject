                    
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import tiktoken

loader = PyPDFLoader("pdfs/prueba.pdf")
pages = loader.load_and_split()

print(pages[0])

print(len(pages))


text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size=100,
    chunk_overlap=20,
    length_function=len,
    is_separator_regex=False,
)

documents = text_splitter.split_documents(pages)

print(len(pages))
print(len(documents))