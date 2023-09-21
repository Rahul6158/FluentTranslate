import streamlit as st
import page1
import page2

import streamlit as st

# Define a custom sidebar method with styled radio buttons
def custom_sidebar():
    st.sidebar.title("Sidebar Title")  # Add a sidebar title

    # Increase font size and style radio buttons
    st.sidebar.markdown("""
    <style>
    .css-1v3fvcr label span {
        font-size: 18px !important;
    }
    .css-1v3fvcr label span:before {
        width: 18px !important;
        height: 18px !important;
        border-radius: 50% !important;
        top: 50% !important;
        transform: translateY(-50%) !important;
    }
    .css-1v3fvcr label input:checked ~ span:before {
        background-color: #1f77b4 !important;
        border: 2px solid #1f77b4 !important;
    }
    .css-1v3fvcr label {
        margin-bottom: 10px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # Create radio button group
    page_choice = st.sidebar.radio("Select a Page", ["Page 1", "Page 2"])

    return page_choice

# Use the custom sidebar method
page_choice = custom_sidebar()

# Display the selected page
st.write(f"You selected: {page_choice}")


if page_choice == "Page 1":
    page1.main()  # Call the main function for Page 1
elif page_choice == "Page 2":
    page2.main()  # Call the main function for Page 2
