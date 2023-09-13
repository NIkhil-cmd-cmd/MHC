import openai
import streamlit as st
import textwrap

st.title("Mental Health Chatbot")

long_text = "This is a long sentence that needs to be wrapped in the sidebar instead of going horizontally."

# Wrap the text to a specified width
wrapped_text = textwrap.fill(long_text, width=10)

# Add wrapped text to the sidebar
#with st.sidebar:
   # st.header("Sidebar Text")
   # st.write(wrapped_text)
#openai.api_key = st.secrets["OPENAI_API_KEY"]


if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

system_message = {
    "role": "system",
    "content": "You are a helpful AI Assistant that gives mental health advice and answers any questions the user might have. If the user says anything suicidal or homicidal reply with the word 'WARNING'"
}

system_message = {
    "role": "assistant",
    "content": "Hello! I am a mental health chatbot designed to help you feel better!"
}

st.session_state.messages.append(system_message)

for message in st.session_state.messages:
   if message["role"] != "system":
        with st.chat_message(message["role"], avatar = 'A'):
            st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar = 'A'):
        message_placeholder = st.empty()
        full_response = ""
        for response in openai.ChatCompletion.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})


