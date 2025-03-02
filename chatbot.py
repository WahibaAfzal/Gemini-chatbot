from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder, SystemMessagePromptTemplate
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema.output_parser import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv



# Load environment variables
load_dotenv()

# Streamlit App Config
st.set_page_config(page_title="TalkieAI", page_icon="🤖")
st.title("🤖 TalkieAI - Your AI Chat Assistant")
st.markdown("Hello! I'm your AI assistant. Ask me anything! 🌍✨")

# Fetch API Key
google_api_key = os.getenv("GOOGLE_API_KEY")

# AI Prompt Setup
prompt = ChatPromptTemplate(
    messages=[
        SystemMessagePromptTemplate.from_template(
            "You are a helpful AI assistant. Respond in English but understand queries in any language."
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{question}"),
    ]
)

# Initialize Chat History
msgs = StreamlitChatMessageHistory(key="langchain_messages")

# Set up AI Model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=google_api_key)

# Create Processing Chain
chain = prompt | model | StrOutputParser()

# Add Message History to Chain
chain_with_history = RunnableWithMessageHistory(
    chain, lambda session_id: msgs,
    input_messages_key="question", history_messages_key="chat_history"
)

# User Input
user_input = st.text_input("✍️ Ask me anything:", "")

if user_input:
    st.chat_message("human").write(f"🧑‍💻 {user_input}")
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        config = {"configurable": {"session_id": "any"}}
        response = chain_with_history.stream({"question": user_input}, config)
        for res in response:
            full_response += res or ""
            message_placeholder.markdown(full_response + "|")
            message_placeholder.markdown(full_response)
else:
    st.warning("⚠️ Please enter your query to get started!")
