import openai
import streamlit as st
import textwrap
import base64
counter = 0
with open('style.css') as f:
   st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
   
st.title("Mental Health Chatbot")

def set_bg_hack(main_bg):
    # set bg name
    main_bg_ext = "png"
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

set_bg_hack('magicpattern-grid-pattern-1694581131805.png')

long_text = "Hello, this is the experiMENTAL health chatbot ui."

# Wrap the text to a specified width
wrapped_text = textwrap.fill(long_text, width=10)

#Add wrapped text to the sidebar
with st.sidebar:
   st.header("About the Project")
   st.write(wrapped_text)
   
openai.api_key = st.secrets["OPENAI_API_KEY"]

if "messages" not in st.session_state:
    st.session_state.messages = []
   
system_message = {
    "role": "system",
    "content": "You are a friendly and funny, helpful AI Assistant that gives mental health advice and answers any questions the user might have. Reply asking further questions, as if trying to understand the user, be  If the user says anything suicidal or homicidal reply with the word 'WARNING'"
}
st.session_state.messages.append(system_message)

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

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
            if "I'm really sorry to hear that you're feeling this way, but I can't provide the help that you need." in str(full_response) and counter == 0:
                full_response = full_response.replace("WARNING", " ")
                st.warning('Your message has been flagged as a potential sign of mental health issues. Please seek appropriate assistance. Refer to the resources tab for further guidance', icon="⚠️")
                counter = 1 
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})


