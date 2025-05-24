from fastapi import APIRouter, HTTPException
from app.pipeline import ProjectPipeline
from app.schema import VectorStoreSchema
from fastapi import status

pipeline = ProjectPipeline()
router = APIRouter()
@router.get("/chat")
async def chat():
    """
    Endpoint to handle chat requests.
    """
    try:
        response = {"message": "This is a placeholder response."}
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/create_collection", status_code=status.HTTP_201_CREATED)
async def create_collection(request: VectorStoreSchema):
    """
    Endpoint to store embeddings in the qdrant vector database.
    """
    try:
        response = await pipeline.vectorstore.create_collection(request.collection_name)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/delete_collection/{collection_name}", status_code=status.HTTP_200_OK)
async def delete_collection(collection_name: str):
    """
    Endpoint to delete a collection in the qdrant vector database.
    """
    try:
        response = await pipeline.vectorstore.delete_collection(collection_name)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
