import streamlit as st
from PIL import Image
st.markdown("# Weekly Scrap Rate")
st.markdown("Explore the dataset")
#img=Image.open('images/palmerpenguins.png')
img = Image.open("logo.png")
st.image(img,width=200)
st.markdown("**Penguins** are some of the most recognizable and beloved birds in the world and even have their own holiday: **World Penguin Day is celebrated every year on April 25**. Penguins are also amazing birds because of their physical adaptations to survive in unusual climates and to live mostly at sea. Penguins propel themselves through water by flapping their flippers.  Bills tend to be long and thin in species that are primarily fish eaters, and shorter and stouter in those that mainly eat krill.")
st.markdown("The data presented are of 3 different species of penguins - **Adelie, Chinstrap, and Gentoo,** collected from 3 islands in the **Palmer Archipelago, Antarctica.**")
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

 