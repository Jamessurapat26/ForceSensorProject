import streamlit as st
import io
from login import login


def create_download_link(content, filename):
    buffer = io.StringIO()
    buffer.write(content)
    return st.download_button(
        label="Download note as TXT",
        data=buffer.getvalue(),
        file_name=filename,
        mime="text/plain"
    )

def note_taking_app():
    st.title("Note")

    with st.form("note_form"):
        note = st.text_area("Enter your note:", height=200)
        submitted = st.form_submit_button("Save Note")

    if submitted:
        st.success("Note saved successfully!")
        create_download_link(note, "my_note.txt")

    st.markdown("---")
    st.write("Enter your note in the text area above and click 'Save Note' to download it as a text file.")

def main():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        st.session_state.logged_in = login()

    if st.session_state.logged_in:
        note_taking_app()

if __name__ == "__main__":
    main()