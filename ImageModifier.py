from PIL import Image
from PIL import ImageFilter as imgf
import streamlit as st
import io

st.title("Image Modifier")
# img = Image.open("/Users/redsparrow/Desktop/Coding/Python/Hacker_Kid/StreamLit_Projects/animals.jpg")
img = st.file_uploader("Upload an image",type=["jpg","jpeg","png","webp"])

options = [
    "None",
    "Black and white",
    "Greyscale",
    "Flip top-bottom",
    "Flip left-right",
    "Edge Enhance",
    "GaussianBlur",
    "CONTOUR",
    "EMBOSS",
    "SMOOTH",
]
choice = st.radio("Choose an option",options)
if img:
    img = Image.open(img)
    if choice == "Black and white":
        img = img.convert("1")
    elif choice == "None":
        pass
    elif choice == "Greyscale":
        img = img.convert("L")
    elif choice == "Flip top-bottom":
        img = img.transpose(Image.FLIP_TOP_BOTTOM)
    elif choice == "Flip left-right":
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
    elif choice == "Edge Enhance":
        img = img.filter(imgf.EDGE_ENHANCE)
    elif choice == "GaussianBlur":
        img = img.filter(imgf.GaussianBlur(2))
    elif choice == "CONTOUR":
        img = img.filter(imgf.CONTOUR)
    elif choice == "EMBOSS":
        img = img.filter(imgf.EMBOSS)
    elif choice == "SMOOTH":
        img = img.filter(imgf.SMOOTH)
    st.image(img)
    var = io.BytesIO()
    img.save(var, format = "PNG")
    st.download_button(
        "Download Image",
        data = var.getvalue(),
        file_name = f"{choice}_image.png",
        mime = "image/png",
    )
