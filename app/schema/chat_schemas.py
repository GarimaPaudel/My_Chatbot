from pydantic import BaseModel, EmailStr, Field
from datetime import date

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


# class AppointmentSchema(BaseModel):
#     name: str
#     email: EmailStr
#     phone: str = Field(..., min_length=10, max_length=15)
#     date: date

class AppointmentSchema(BaseModel):
    name: str
    email: EmailStr
    phone: str = Field(..., min_length=10, max_length=15)
    date: str

class ChatSchema(BaseModel):
    query: str
    session_id: str
    collection_name: str