from fastapi import APIRouter, HTTPException, UploadFile, File
from app.pipeline import ProjectPipeline
from app.schema import (VectorStoreSchema, UploadDocumentSchema, UploadDocumentsResponse, DocumentResponseSchema)
from fastapi import status
import tempfile
import os
import uuid

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
    
@router.post("/upload_documents", status_code=status.HTTP_201_CREATED)  
async def upload_documents(request: UploadDocumentSchema) -> UploadDocumentsResponse:
    """
    Upload documents to the collection of chatbot in Qdrant vectorstore.
    """
    try:
        response = await pipeline.upload_documents(request.documents, request.collection_name)
        print("-------------RESPONSE--------------:", response)
        if response:
            return UploadDocumentsResponse(
                detail="Documents Uploaded Successfully"
            )
        raise HTTPException(status_code=500, detail="Failed to upload documents")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post(
    "/documents/extract",
    status_code=status.HTTP_201_CREATED
)
async def extract_text(files: list[UploadFile] = File(...)) -> DocumentResponseSchema:
    """
    Extract text from the uploaded files
    """
    try:
        results = []
        with tempfile.TemporaryDirectory() as temp_dir:
            for file in files:
                file_content = await file.read()

                temp_filename = os.path.join(temp_dir, f"{uuid.uuid4().hex}_{file.filename}")
                with open(temp_filename, "wb") as f:
                    f.write(file_content)
                # Extract text
                text = pipeline.extract_text(temp_filename)
                results.append(
                    {
                        "file_name": file.filename,
                        "text": text,
                    }
                )
        return DocumentResponseSchema(source_type="document", results=results)


    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

