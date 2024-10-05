import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
from PIL import Image

# config
genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))


def do_process(imagee, prompt):
    im = Image.open(imagee)
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([prompt, im])
    st.write(response.text)

st.title("I will tell you about the image")
imagee = st.file_uploader("Upload Image")
prompt = st.text_input("What you want to do")
if (imagee != None) and (prompt != None):
    if st.button("Proceed"):
        do_process(imagee, prompt)