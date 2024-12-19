import streamlit as st
from langchain.chains import load_chain
import json

# Load LangFlow configuration
with open("simple agent.json", "r") as f:
    flow_config = json.load(f)

chain = load_chain(flow_config)

def chatbot(message):
    response = chain.run(message)
    return response

# Streamlit app
def main():
    st.title("LangFlow Chatbot")
    user_input = st.text_area("Type your message:")
    
    if st.button("Send"):
        if not user_input.strip():
            st.error("Please type a message!")
        else:
            response = chatbot(user_input)
            st.markdown(f"**Bot:** {response}")

if __name__ == "__main__":
    main()
