from langchain_upstage import ChatUpstage

import streamlit as st

st.title("Solar Bot")

chat = ChatUpstage(api_key="up_9wNe4MJes0fmb8IU7TC2o9poYuid0", model="solar-pro")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

st.session_state.update({"messages": st.session_state.messages}, persist=True)

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("what is up?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        model_response = chat.invoke(st.session_state.messages).content
        st.markdown(model_response)
    # Add user message to chat history
    st.session_state.messages.append({"role": "assistant", "content": model_response})