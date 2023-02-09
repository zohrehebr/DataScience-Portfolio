import streamlit as st
from PIL import Image
st.markdown("# Weekly Scrap Rate")
img = Image.open("logo.png")
st.image(img,width=200, )
st.markdown("**Weekly charts and number of saved bottles.....** ")
st.markdown("The data presented are **")
if st.button("MLX4_2022-12-08_2022-12-15.png"):
    img=Image.open("MLX4_2022-12-08_2022-12-15.png")
    st.image(img,width=700, caption="weekly report")
    st.markdown(
    "The data was collected for the dates of **2022-12-08 to 2022-12-15**")
    images=Image.open("MLX4_2022-12-08_2022-12-15.png")
    st.image(images,width=600)
if st.button("MLX11_2022-12-08_2022-12-15.png"):
    img=Image.open("MLX11_2022-12-08_2022-12-15.png")
    st.image(img,width=700, caption="weekly report")
    st.markdown(
    "The data was collected for the dates of **2022-12-08 to 2022-12-15**")
    images=Image.open("MLX11_2022-12-08_2022-12-15.png")
    st.image(images,width=600)

 
