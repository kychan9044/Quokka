from langchain_openai import ChatOpenAI, OpenAI
import streamlit as st

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