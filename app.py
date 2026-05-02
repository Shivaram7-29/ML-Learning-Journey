from langchain_community.document_loaders import PyPDFLoader

# Load PDF
loader = PyPDFLoader("sample.pdf")
docs = loader.load()

# Check output
print("Number of pages:", len(docs))
print("\nFirst page content preview:\n")
print(docs[0].page_content[:500])


from langchain_text_splitters import CharacterTextSplitter

# Split text into chunks
splitter = CharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(docs)

# Check result
print("Number of chunks:", len(chunks))
print("\nFirst chunk preview:\n")
print(chunks[0].page_content)

