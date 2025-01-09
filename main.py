from langchain_openai import ChatOpenAI, OpenAI
import streamlit as st
from streamlit.components.v1 import html

st.title("Quokka 😎")

st.sidebar.header('Settings')
api_key = st.sidebar.text_input('Enter Your OpenAI API Key🔑', type='password')
model_name = st.sidebar.selectbox('Select Model', ['gpt-4o-mini', 'gpt-3.5-turbo', 'gpt-4o'])
###
# gpt-4o-mini:
#     $0.150 / 1M input tokens
#     $0.075 / 1M input tokens
# gpt-3.5-turbo-0125:
#     $0.50 / 1M tokens
#     $1.50 / 1M tokens
# gpt-4o:
#     $2.50 / 1M input tokens
#     $1.25 / 1M input tokens
###
button = """
<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="chan7brew" data-color="#40DCA5" data-emoji="" data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#ffffff" data-coffee-color="#FFDD00" ></script>
"""

html(button, height=70, width=220)

st.markdown(
    """
    <style>
        iframe[width="220"] {
            position: fixed;
            bottom: 60px;
            right: 40px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

if api_key and model_name:
    try:
        model = ChatOpenAI(model=model_name,api_key=api_key)

        with st.form(key='message_input'):
            message = st.text_input('Enter your message')
            submit_button = st.form_submit_button(label='🚀')

        if submit_button:
            with st.spinner('Wait for it...'):
                result = model.invoke(message)
                st.write(result.content)
    except Exception as e:
        st.error(f"Error loading the model: {e}")
else:
    st.markdown('<p style="color:red;">❗ Please enter your OpenAI API Key and select a model.</p>', unsafe_allow_html=True)