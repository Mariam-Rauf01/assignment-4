import streamlit as st

st.set_page_config(page_title="My First Streamlit Website", layout="centered")

st.title("🌐 Welcome to My Streamlit Website!")
st.subheader("This site was built in under 15 minutes 😎")

# Add text input
name = st.text_input("What's your name?")

# Add a button and greet the user
if st.button("Greet Me"):
    st.success(f"Hello, {name}! Welcome to the website!")

# Fun fact generator
import random
fun_facts = [
    "Did you know? The Eiffel Tower can grow taller in the summer!",
    "Bananas are berries, but strawberries aren’t!",
    "A day on Venus is longer than a year on Venus!",
    "Honey never spoils—archaeologists found 3,000-year-old honey still good to eat!"
]

if st.button("Give Me a Fun Fact"):
    st.info(random.choice(fun_facts))


# Contact form
st.write("---")
st.markdown("### 📬 Contact Us")
email = st.text_input("Your Email")
message = st.text_area("Your Message")
if st.button("Submit"):
    st.success("Thanks! We'll get back to you soon.")
