import streamlit as st
import random
import string
from getApi import getApi
from PIL import Image

# Initialize session state for profile data
if 'proflie' not in st.session_state:
    st.session_state.profile = {
        'name': '',
        'age': '',
        'Gender': '',
        'image': None
    }

if 'notes_count' not in st.session_state:
    st.session_state.notes_count = 0

def add_new_note():
    key = random.choice(string.ascii_uppercase) + str(random.randint(0, 999999))
    note = st.text_input("Add a note", key=key)
    if note:
        if 'notes' not in st.session_state.profile:
            st.session_state.profile['notes'] = []
        st.session_state.profile['notes'].append(note)

st.title("User Profile")

col1, col2 = st.columns(2)

with col1:
    st.header("Personal Information")
    st.session_state.profile['name'] = st.text_input("Name", st.session_state.profile.get('name', ''))
    st.session_state.profile['age'] = st.number_input("Age", min_value=0, max_value=120, value=st.session_state.profile.get('age', 0))
    st.session_state.profile['bio'] = st.text_area("Bio", st.session_state.profile.get('bio', ''))

    uploaded_file = st.file_uploader("Choose a profile picture", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.session_state.profile['image'] = image
        st.image(image, caption="Profile Picture", use_column_width=True)
    elif st.session_state.profile.get('image') is not None:
        st.image(st.session_state.profile['image'], caption="Profile Picture", use_column_width=True)

with col2:
    st.header("Notes")
    if st.button("Add Note"):
        st.session_state.notes_count += 1
        add_new_note()
    
    if st.session_state.notes_count > 0:
        for i in range(st.session_state.notes_count):
            add_new_note()
    
    if 'notes' in st.session_state.profile:
        st.subheader("Your Notes:")
        for note in st.session_state.profile['notes']:
            st.write("- " + note)

if st.button("Save Profile"):
    st.success("Profile saved successfully!")
    st.write("Profile Information:")
    st.write(f"Name: {st.session_state.profile['name']}")
    st.write(f"Age: {st.session_state.profile['age']}")
    st.write(f"Bio: {st.session_state.profile['bio']}")
    if 'notes' in st.session_state.profile:
        st.write("Notes:")
        for note in st.session_state.profile['notes']:
            st.write("- " + note)