from app.schema import AppointmentSchema
from app.database import connect_to_mongo
from dateparser import parse
from langchain.tools import Tool
from app.services.answer_query import AnswerQuery

class CustomTools:
    def __init__(self):
        self.answer_query_service = AnswerQuery()


    def create_appointment(self, appointment: AppointmentSchema):
        """
        Book an appointment with the provided details.
        Inputs: name, email, phone, date."""
        # Convert Pydantic model to dictionary
        appointments_collection = connect_to_mongo()
        appointment_data = appointment.model_dump()
        # Insert into MongoDB
        result = appointments_collection.insert_one(appointment_data)
        return {"message": "Appointment created successfully", "appointment_id": str(result.inserted_id)}
    
    # def extract_dates(self, text: str):
    #     dt = parse(text)
    #     return dt.strftime("%Y-%m-%d") if dt else None
    
    def rag_response(self, query:str, session_id: str, collection_name: str):
        """"
        Retrieve relevant information from the knowledge base using RAG and answer to user's query.
        Inputs: query."""
        response = self.answer_query_service.in_memory_answer_query(
            query=query, session_id=session_id, collection_name=collection_name
        )
        return response
    


tool = CustomTools()

appointment_tool = Tool(
    name="create_appointment",
    func=tool.create_appointment,
    description="Create an appointment. Inputs: name, email, phone, date."
)

# date_extractor_tool = Tool(
#     name="extract_dates",
#     func=tool.extract_dates,
#     description="Extract a date from free text."
# )

rag_tool = Tool(
    name="rag_response",
    func=tool.rag_response,
    description="Retrieve relevant information from the knowledge base and aswer to user's query. Inputs: query, session_id, collection_name."
)
TOOLS = [appointment_tool, rag_tool]

# if __name__ == "__main__":
#     # Example usage
#     appointment = AppointmentSchema(
#         name="John Doe",
#         email="abc@gmail.com",
#         phone="1234567890",
#         date="2023-10-01"
# )
#     print(create_appointment(appointment=appointment))