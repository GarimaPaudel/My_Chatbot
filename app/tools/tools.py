from app.schema import AppointmentSchema
from app.database import connect_to_mongo
from dateparser import parse
from langchain.tools import Tool
from app.services.answer_query import AnswerQuery
from langchain.agents import AgentExecutor, create_tool_calling_agent, tool
from app.schema import AppointmentSchema
from app.database import connect_to_mongo
from app.services.answer_query import AnswerQuery
from langchain.agents import tool

class CustomTools:
    def __init__(self):
        self.answer_query_service = AnswerQuery()

    def create_appointment(self, name: str, email: str, phone: str, date: str):

        appointment = AppointmentSchema(name=name, email=email, phone=phone, date=date)
        appointments_collection = connect_to_mongo()
        appointment_data = appointment.model_dump()
        result = appointments_collection.insert_one(appointment_data)
        return f"Appointment created successfully for {name} on {date}. Confirmation ID: {str(result.inserted_id)}"

    async def rag_response(self, query: str):

        response = await self.answer_query_service.answer_query_rag(query=query)
        return response

# Instantiate the tools object
custom_tools = CustomTools()

# Tool wrappers for LangChain
@tool
def create_appointment_tool(name: str, email: str, phone: str, date: str):
    """
    Book an appointment with the provided details.
    """
    return custom_tools.create_appointment(name, email, phone, date)

@tool
async def rag_response_tool(query: str):
    """
    Retrieve relevant information from the knowledge base using RAG and answer to user's query.
    """
    return await custom_tools.rag_response(query)

TOOLS = [create_appointment_tool, rag_response_tool]

