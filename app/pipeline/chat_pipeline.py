from app.services.vectorstore import QdrantVectorStoreDB
from app.services.documents import DocumentTextExtractor
from qdrant_client import QdrantClient
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from app.utils import settings
from app.utils import clean_text
from app.services.answer_query import AnswerQuery

class ProjectPipeline:
    """
    The main pipeline class for Botanza.
    This class is responsible for orchestrating the entire pipeline.
    """

    def __init__(self):
        self.vector_embeddings = GoogleGenerativeAIEmbeddings(
            google_api_key=settings.GOOGLE_API_KEY, model="models/text-embedding-004"
        )
        self.qdrant_client = QdrantClient(
            url=settings.QDRANT_URL,
        )
        self.vectorstore = QdrantVectorStoreDB(
            qdrant_client=self.qdrant_client, vector_embedding=self.vector_embeddings
        )
        self.add_documents = DocumentTextExtractor()
        self.answer_queries = AnswerQuery()

    async def create_collection(self, collection_name: str):
        """
        Create a new chatbot collection.
        """
        return await self.vectorstore.create_collection(collection_name)
    
    async def delete_collection(self, collection_name: str):

        """
        Delete a chatbot collection.
        """
        return await self.vectorstore.delete_collection(collection_name)
    
    async def upload_documents(self, documents: list[dict], collection_name: str):
        """
        Upload documents to the chatbot
        """
        return await self.vectorstore.upload_documents(documents, collection_name)
    
    def extract_text(self, file_path):
        """
        Extract text from the given file path.
        """
        text = self.add_documents.extract_text(file_path)
        return clean_text(text)
    
    async def answer_query(self, query: str, session_id: str, collection_name: str):
        """
        Answer a query using the chatbot.
        """
        return await self.answer_queries.in_memory_answer_query(query, session_id, collection_name)
    

