from src.helper import load_pdf,text_split,huggging_face_embeddings
from langchain.vectorstores import Pinecone
import pinecone
from dotenv import load_dotenv
import os

load_dotenv()

pinecone_api_key = os.environ.get('pinecone_api_key')
pinecone_env = os.environ.get('pinecone_env')

extracted_data = load_pdf("data/")
text_chunks = text_split(extracted_data)
embeddings = huggging_face_embeddings()

pinecone.init(api_key=pinecone_api_key,
              environment=pinecone_env)

index_name = "medical-chatbot"
if index_name not in pinecone.list_indexes():
    pinecone.create_index("medical-chatbot", dimension=384, metric="cosine")
    docsearch=Pinecone.from_texts([t.page_content for t in text_chunks], embeddings, index_name=index_name)
index = pinecone.Index(index_name)
