import streamlit as st
import ollama

desiredModel = 'llama3.2:3b'

st.title("Our First LLM Web Application Based on Llama (running locally) and Streamlit")

def generate_response(questionToAsk):
    try:
        response = ollama.chat(model=desiredModel, messages=[
            {
                'role': 'user',
                'content': questionToAsk,
            },
        ])
        st.info(response['message']['content'])
    except Exception as e:
        st.error(f"Error generating response: {e}")

# Form section moved outside the function
with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "Over here, ask a question and press the Submit button.",
    )
    submitted = st.form_submit_button("Submit")
    if submitted:
        generate_response(text)
