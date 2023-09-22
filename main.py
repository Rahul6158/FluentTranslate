import streamlit as st
import page1
import page2
import page4

# Define a custom sidebar method with styled radio buttons
def custom_sidebar():
    st.sidebar.title("Available Options")  # Add a sidebar title

    # Use Streamlit's CSS classes to style the radio buttons
    st.markdown("""
    <style>
    .radio-button-group .css-17qkwz2 label span {
        font-size: 18px !important;
    }
    .radio-button-group .css-17qkwz2 label span:before {
        width: 18px !important;
        height: 18px !important;
        border-radius: 50% !important;
        top: 50% !important;
        transform: translateY(-50%) !important;
    }
    .radio-button-group .css-17qkwz2 label input:checked ~ span:before {
        background-color: #1f77b4 !important;
        border: 2px solid #1f77b4 !important;
    }
    .radio-button-group .css-17qkwz2 label {
        margin-bottom: 10px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # Create radio button group
    page_choice = st.sidebar.radio("", ["Document and Pdf Translation", "Text Translation", "Text Summarization"])

    return page_choice

# Use the custom sidebar method
page_choice = custom_sidebar()

if page_choice == "Document and Pdf Translation":
    page1.main()  # Call the main function for Page 1
if page_choice == "Text Translation":
    page2.main() 
if page_choice == "Text Summarization":
    page4.main()
