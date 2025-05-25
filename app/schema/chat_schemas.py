from pydantic import BaseModel

class VectorStoreSchema(BaseModel):
    collection_name: str

class Message(BaseModel):
    detail: str

class UploadDocumentSchema(BaseModel):
    documents: list[dict]

class DRS(BaseModel):  
    file_name: str
    text: str

class DocumentResponseSchema(BaseModel):
    source_type: str
    results: list[DRS]


class UploadDocumentSchema(BaseModel):
    collection_name: str
    documents: list[dict]


class UploadDocumentsResponse(BaseModel):
    detail: str

class DocumentResponseSchema(BaseModel):
    source_type: str
    results: list[DRS]
