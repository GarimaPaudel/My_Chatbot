from pydantic import BaseModel

class VectorStoreSchema(BaseModel):
    collection_name: str

class UploadDocumentSchema(BaseModel):
    collection_name:str
    file: str