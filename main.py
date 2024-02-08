                    
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
#from sentence_transformers import SentenceTransformer
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma
import tiktoken
import chromadb


##DOCUMENT LOADER
loader = PyPDFLoader("pdfs/prueba.pdf")
pages = loader.load_and_split()

print(pages[0])

print(len(pages))



##TEXT SPLITTER
text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size=500,
    chunk_overlap=50,
    length_function=len,
    is_separator_regex=False,
)

documents = text_splitter.split_documents(pages)

print("La cantidad en documents solo con document loader es: " + str(len(pages)))
print("La cantidad en documents luego del text_splitter es: " + str(len(documents)))



##EMBEDDINGS CREATION FOR STR PROMPT SCENARIO
sentences = ["This is an example sentence", "Each sentence is converted"]

embeddings_st = SentenceTransformerEmbeddings(
    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

incrustaciones = embeddings_st.embed_documents(sentences)
len(incrustaciones)

print("Embeddings: " + str(len(incrustaciones)))
print(incrustaciones)

##VECTORIAL DB CHROMA APPLICATION

""" NOMBRE_INDICE_CHROMA = "instruct-embeddings-public-crypto"

vectorstore_chroma = Chroma.from_documents(
    documents=documents,
    embedding=embedding_instruct,
    persist_directory=NOMBRE_INDICE_CHROMA
)

type(embedding_instruct)  """

chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="my_collection")
collection.add(
    embeddings=[incrustaciones],
    documents=[documents],
    metadatas=[{"source": "my_source"}, {"source": "my_source"}],
    ids=["id1", "id2"]
) 

results = collection.query(
    query_texts=["This is a query document"],
    n_results=2
)

print(results)