                    
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
#from sentence_transformers import SentenceTransformer
from langchain.embeddings import SentenceTransformerEmbeddings
import tiktoken

loader = PyPDFLoader("pdfs/prueba.pdf")
pages = loader.load_and_split()

print(pages[0])

print(len(pages))


text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size=200,
    chunk_overlap=20,
    length_function=len,
    is_separator_regex=False,
)

documents = text_splitter.split_documents(pages)

print("La cantidad en documents solo con document loader es: " + str(len(pages)))
print("La cantidad en documents luego del text_splitter es: " + str(len(documents)))


sentences = ["This is an example sentence", "Each sentence is converted"]
"""
model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')
embeddings = model.encode(sentences)
print(embeddings) """


embeddings_st = SentenceTransformerEmbeddings(
    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

incrustaciones = embeddings_st.embed_documents(sentences)
len(incrustaciones)

print("Embeddings: " + str(len(incrustaciones)))
print(incrustaciones)