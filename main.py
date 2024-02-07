                    
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
import tiktoken

loader = PyPDFLoader("pdfs/prueba.pdf")
pages = loader.load_and_split()

print(pages[0])

print(pages[1])

print(len(pages))


#text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
#    chunk_size=500, chunk_overlap=50
#)
#texts = text_splitter.split_text(pages)

#print(texts[0])
