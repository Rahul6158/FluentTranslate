import streamlit as st
import page1
import page2
import page3  # Import the new page3 module

# Define a custom sidebar method
def custom_sidebar():
    st.sidebar.title("Available Options")  # Add a sidebar title

    # Create radio button group
    page_choice = st.sidebar.radio("", ["Document and Pdf Translation", "Text Translation", "Text Summarization", "Page 3"])

    return page_choice

# Use the custom sidebar method
page_choice = custom_sidebar()

if page_choice == "Document and Pdf Translation":
    page1.main()  # Call the main function for Page 1
elif page_choice == "Text Translation":
    page2.main()
elif page_choice == "Text Summarization":
    page3.main()  # Call the main function for Page 3
elif page_choice == "Page 3":
    st.write("This is Page 3. You can add content and functionality specific to this page here.")
