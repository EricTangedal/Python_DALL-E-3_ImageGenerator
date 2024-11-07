from openai import OpenAI
from PIL import Image
import streamlit as st
from apikey import apikey
from streamlit_carousel import carousel

client=OpenAI(api_key=apikey)

single_img = dict(
    title="",
    text="",
    interval=None,
    img="",
)

def generate_images(image_description, num_of_images):
    images=[]
    image_gallery=[]
    for i in range(num_of_images):
        img_response=client.images.generate(
            model="dall-e-3",
            prompt=image_description,
            size="1024x1024",
            quality="standard",
            n=1
        )
        image_url = img_response.data[0].url
        images.append(image_url)
        new_image=single_img.copy()
        new_image["title"] = f"Image {i+1}"
        new_image["text"] = image_description
        new_image["img"] = image_url
        image_gallery.append(new_image)
    return images

st.set_page_config(page_title="Image Generator", page_icon=":camera:", layout="wide")

st.title("Image Generator")

st.subheader("Powered by DALL-E-3")
img_description = st.text_input("Enter a description for the image you want to generate")
num_of_images = st.number_input("Select the number of images you want to generate", min_value=1, max_value=5, value=1)

if st.button("Generate Images"):
    generate_image = generate_images(img_description, num_of_images)
    carousel(items=generate_image, width=1)
