from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
llm=ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

st.title("AskBuddy- AI Qna Bot!")
st.markdown("This is a simple QnA bot that uses Google Gemini API to answer your questions.")

if "messages" not in st.session_state:
    st.session_state.messages=[]

for message in st.session_state.messages:
    role=message["role"]
    content=message["content"]
    st.chat_message(role).markdown(content)


query=st.chat_input("Ask me anything!")
if query:
    st.session_state.messages.append({"role":"user","content":query})
    st.chat_message("User").markdown(query)
    res=llm.invoke(query)
    st.chat_message("AI").markdown(res.text)
    st.session_state.messages.append({"role":"ai","content":res.text})

# while True:
#     query=input("User:")
#     if query.lower() in ["exit","quit"]:
#        print("Goodbye!")
#        break
#     result=llm.invoke(query)
#     print("AI :", result.text)
