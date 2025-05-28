from langchain.agents import initialize_agent, AgentType
from langchain.agents import AgentExecutor, create_tool_calling_agent, tool
from app.tools import TOOLS
from langchain_groq import ChatGroq
from langchain.agents import AgentExecutor, create_tool_calling_agent, tool


model = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.9,
        max_tokens=100,
        streaming=True,
        timeout=None,
        max_retries=2,
    )

# agent = initialize_agent(
#     tools=TOOLS,
#     llm=model,
#     agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
#     verbose=True,
# )

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.messages import SystemMessage, HumanMessage

# Your prompt must include the variables: "input" and "agent_scratchpad"
prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content=(
        "You are a helpful assistant. "
        "You can answer questions from documents and help users book appointments. "
        "If the user asks to book an appointment, collect their name, email, phone, and date step-by-step. "
        "Do not call the create_appointment tool until you have all 4 fields."
    )),
    MessagesPlaceholder(variable_name="chat_history"),
    HumanMessage(content="{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

agent = create_tool_calling_agent(llm=model, tools=TOOLS, prompt=prompt)
agent_executor = AgentExecutor(agent=agent, tools=TOOLS, verbose=True)