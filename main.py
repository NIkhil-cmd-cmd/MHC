import openai
import streamlit as st
import textwrap
with open('style.css') as f:
   st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
   
st.title("Mental Health Chatbot")

import base64
@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg('magicpattern-grid-pattern-1694579841254.png')

long_text = "Hello, this is the experiMENTAL health chatbot ui."

# Wrap the text to a specified width
wrapped_text = textwrap.fill(long_text, width=10)

#Add wrapped text to the sidebar
with st.sidebar:
   st.header("About the Project")
   st.write(wrapped_text)
   
openai.api_key = st.secrets["OPENAI_API_KEY"]


if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

system_message = {
    "role": "system",
    "content": "You are a helpful AI Assistant that gives mental health advice and answers any questions the user might have. If the user says anything suicidal or homicidal reply with the word 'WARNING'"
}

st.session_state.messages.append(system_message)

for message in st.session_state.messages:
   if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if prompt := st.chat_input("Say something..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
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


