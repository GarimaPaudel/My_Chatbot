from app.services.vectorstore import QdrantVectorStoreDB
from qdrant_client import QdrantClient
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from app.utils import settings


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
    
    
