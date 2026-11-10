from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver
import streamlit as st

llm=ChatGroq(model="openai/gpt-oss-20b")
search=GoogleSerperAPIWrapper()
tools=[search.run]


if "memory" not in st.session_state: 
 st.session_state.memory=MemorySaver()
 st.session_state.history=[]

agent=create_agent(
model=llm,
tools=tools,
checkpointer=st.session_state.memory,
system_prompt="You are an agent and you can search from google"
)

st.subheader("Quick Answer - answer at the speed of thought")

for message in st.session_state.history:
   role=message["role"]
   content=message["content"]
   st.chat_message(role).markdown(content)
   


query=st.chat_input("Ask anything...")
if query:
    st.chat_message("user").markdown(query)
    st.session_state.history.append({"role":"user","content":query})
    response=agent.invoke(
    {"messages":[{"role":"user","content":query}]},
    {"configurable":{"thread_id":"1"}}
    )
    answer=(response["messages"][-1].content)
    st.chat_message("ai").markdown(answer)
    st.session_state.history.append({"role":"ai","content":answer})


