# from langchain.prompts import (
#     ChatPromptTemplate,  # Yeh class chatbot ke liye chat prompt template banane ke liye import ki gayi hai.
#     HumanMessagePromptTemplate,  # Yeh class human messages ke liye template banane ke liye import ki gayi hai.
#     MessagesPlaceholder,  # Yeh class messages ke placeholders ko rakhne ke liye import ki gayi hai.
#     SystemMessagePromptTemplate,  # Yeh class system message templates banane ke liye import ki gayi hai.
# )

# from langchain_community.chat_message_histories import StreamlitChatMessageHistory  # Yeh class Streamlit mein chat message history manage karne ke liye import ki gayi hai.

# from langchain_core.runnables.history import RunnableWithMessageHistory  # Yeh class aise runnable chains banane ke liye import ki gayi hai jo message history rakh sakti hain.

# from langchain_google_genai import ChatGoogleGenerativeAI  # Yeh class Google ke generative AI model ke sath interact karne ke liye import ki gayi hai.

# from langchain.schema.output_parser import StrOutputParser  # Yeh class output ko string format mein parse karne ke liye import ki gayi hai.

# import streamlit as st  # Yeh Streamlit ko import karta hai jo web app interface banane ke liye istemal hota hai.

# import os
# from dotenv import load_dotenv

# # .env file load karne ke liye
# load_dotenv()


# st.set_page_config(page_title="TalkieAI", page_icon="🤖")


# st.title('Your AI Chat Assistant Speak Freely, AI Listens!')

# st.markdown("Hello! I'm your AI assistant. I can help answer questions about technology, education, and general knowledge. How can I assist you today?")

# # Environment variable read karne ke liye
# google_api_key = os.getenv("GOOGLE_API_KEY")

# # Aapka Google AI ke liye API key; yeh key AI service ke sath requests ko authenticate karne ke liye zaroori hai.
# #api_key = "AIzaSyBErWqV3_0ucOHLmItm3UlPGati9EOmC_4"

# # AI assistant ke liye prompt template create karna, jo yeh define karta hai ke yeh user queries kaise respond karega.
# prompt = ChatPromptTemplate(
#     messages=[
#         # Ek system message create karna jo AI assistant ko instructions deta hai ke kaise respond karna hai.
#         SystemMessagePromptTemplate.from_template(
#             "You are a helpful AI assistant. Please respond to user queries in English, but understand the questions in English."
#         ),
#         # Ek placeholder add karna jo chat history ko track karne ke liye hai.
#         MessagesPlaceholder(variable_name="chat_history"),
#         # User input messages ke liye ek template create karna.
#         HumanMessagePromptTemplate.from_template("{question}"),
#     ]
# )

# # Chat message history ko initialize karna taake session ke doran messages ko track kiya ja sake.
# msgs = StreamlitChatMessageHistory(key="langchain_messages")

# # AI model ko set up karna jis mein specified model name aur API key istemal hota hai.
# model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=google_api_key)

# # Response generate karne ke liye prompt, model, aur output parser ko combine karte hue ek processing chain create karna.
# chain = prompt | model | StrOutputParser()

# # Chain ko message history ke sath combine karna taake peechle interactions ko track kiya ja sake.
# chain_with_history = RunnableWithMessageHistory(
#     chain,
#     lambda session_id: msgs,  # Session ID ke buniyad par message history tak access karne ke liye lambda function istemal karna.
#     input_messages_key="question",  # Input messages ke liye key specify karna.
#     history_messages_key="chat_history",  # Historical messages ke liye key specify karna.
# )

# # User se text input lena jahan user apne questions English mein daal sakta hai.
# user_input = st.text_input("Enter your question in English:", "")

# # Yeh check karna ke user ne koi input diya hai ya nahi.
# if user_input:
#     # Agar user ne text diya hai, to chat interface mein user ka message display karna.
#     st.chat_message("human").write(user_input)
    
#     # Assistant ke response ke liye context create karna.
#     with st.chat_message("assistant"):
#         message_placeholder = st.empty()  # Assistant ke message ko dynamically update karne ke liye ek placeholder create karna.
#         full_response = ""  # Full response ko store karne ke liye variable initialize karna.

#         # Session ke liye configuration dictionary; isay session-specific settings ke sath extend kiya ja sakta hai.
#         config = {"configurable": {"session_id": "any"}}
        
#         # User input aur configuration ka istemal karte hue AI model se response lena.
#         response = chain_with_history.stream({"question": user_input}, config)

#         # Response ko real-time mein user tak stream karna.
#         for res in response:
#             full_response += res or ""  # Response ke har piece ko full response ke sath concatenate karna.
#             message_placeholder.markdown(full_response + "|")  # Current response ke sath placeholder ko update karna.
#             message_placeholder.markdown(full_response)  # Response complete hone par full response ko display karna.

# else:
#     # Agar koi input nahi diya gaya, to user ko warning message dikhana.
#     st.warning("Please enter your query.")


































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
