import streamlit as st
from nemoguardrails import RailsConfig, LLMRails
import config.config  # Ensures custom LLM is registered

# Load the configuration
config = RailsConfig.from_path("./config")
rails = LLMRails(config)

# Streamlit UI
st.set_page_config(page_title="NeMo Guardrails Chatbot", layout="centered")
st.title("🤖 NeMo Guardrails Chatbot")
st.write("Interact with the chatbot while ensuring safe and guided conversations.")

# Initialize chat history if not present
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
user_input = st.chat_input("Type your message...")
if user_input:
    # Add user message to session state
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)
    
    # Check if the input passes guardrails
    guardrails_response = rails.generate(messages=[{"role": "user", "content": user_input}])
    
    # If the guardrails reject the query, use the defined rejection response
    if guardrails_response.get("blocked", False):
        chatbot_response = guardrails_response["content"]
    else:
        chatbot_response = guardrails_response["content"]
    
    # Display chatbot response
    with st.chat_message("assistant"):
        st.write(chatbot_response)
    
    # Add chatbot response to session state
    st.session_state.messages.append({"role": "assistant", "content": chatbot_response})
