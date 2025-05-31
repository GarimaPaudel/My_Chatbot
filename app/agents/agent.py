from langchain.agents import AgentExecutor, create_tool_calling_agent
from app.tools import TOOLS
from langchain_groq import ChatGroq
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_redis import RedisChatMessageHistory
from app.utils.config import settings
from langchain_core.prompts import ChatPromptTemplate



class ChatbotAgent:
    def __init__(self):
        self.model = ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=0.9,
            max_tokens=100,
            streaming=True,
            timeout=None,
            max_retries=2,
        )
        self.prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                "You are a helpful assistant. "
                "You have two tools: "
                "1. 'create_appointment_tool' for booking appointments, and "
                "2. 'rag_response_tool' for answering questions from documents. "
                "If the user wants to book an appointment, extract their name,email,phone and date from query and call booking tool to store in database. "
                "If the user asks a question about documents, use the rag_response_tool. "
                "Only call ONE tool ONCE per user question "
                "and AVOID calling the same tool multiple times in a single response. "
            ),
            ("placeholder", "{chat_history}"),
            ("human", "{input}"),
            ("placeholder", "{agent_scratchpad}"),
        ])
        self.agent = create_tool_calling_agent(self.model, TOOLS, self.prompt)
        self.agent_executor = AgentExecutor(agent=self.agent, tools=TOOLS, verbose=True)

    @staticmethod
    def get_redis_history(session_id: str):
        return RedisChatMessageHistory(session_id=session_id, redis_url=settings.REDIS_URL)

    def get_agent_with_chat_history(self):
        return RunnableWithMessageHistory(
            self.agent_executor,
            self.get_redis_history,
            input_messages_key="input",
            history_messages_key="chat_history",
        )

