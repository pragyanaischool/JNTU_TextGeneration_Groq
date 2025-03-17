import streamlit as st
from langchain_groq import ChatGroq

st.title("🤖 Groq-Powered Chatbot")
st.image("PragyanAI_Transperent_github.png")
groq_api_key = st.sidebar.text_input("Groq API Key", type="password")


def generate_response(input_text):
    model = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0.7, api_key=groq_api_key)
    st.info(model.invoke(input_text))


with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "What are the three key pieces of advice for learning how to code?",
    )
    submitted = st.form_submit_button("Submit")
    if not groq_api_key.startswith("gsk_"):
        st.warning("Please enter your Groq API key!", icon="⚠")
    if submitted and groq_api_key.startswith("gsk_"):
        generate_response(text['content'])
