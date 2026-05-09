import streamlit as st
from huggingface_hub import InferenceClient
from PIL import Image
import datetime
import os


client=InferenceClient(token=os.getenv(HF_TOKEN))
MODEL="stabilityai/stable-diffusion-xl-base-1.0"

st.set_page_config(page_title="My Image Generator")
st.write("decribe your imagination to make it real...")
prompt=st.text_input("describe your image...")

if st.button("generate"):
    with st.spinner("image is creating..."):
        image=client.text_to_image(prompt,model=MODEL)
        st.image(image,caption=prompt)
        image.save("myimg.png")
        st.success("image saved in cwd")
