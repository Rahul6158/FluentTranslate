import streamlit as st
import page1
import page2
import page3 


def custom_sidebar():
    st.write("Features")
    st.sidebar.title("Available Options")  # Add a sidebar title

    # Create radio button group
    page_choice = st.sidebar.radio("", ["Document and Pdf Translation", "Text Translation", "Text Summarization"])

    return page_choice

# Use the custom sidebar method
page_choice = custom_sidebar()

if page_choice == "Document and Pdf Translation":
    page1.main()  # Call the main function for Page 1
elif page_choice == "Text Translation":
    page2.main()
elif page_choice == "Text Summarization":
    page3.main()  # Call the main function for Page 3
