import streamlit as st
import page1
import page2

# Create a sidebar navigation using radio buttons with increased size
page_choice = st.sidebar.radio("", ["Page 1", "Page 2"], key="page")

# Add custom CSS styling to increase the size of sidebar elements
st.markdown(
    """
    <style>
    .css-17a69v6 {
        font-size: 24px !important;
    }
    .st-e5 {
        padding: 10px !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

if page_choice == "Page 1":
    page1.main()  # Call the main function for Page 1
elif page_choice == "Page 2":
    page2.main()  # Call the main function for Page 2
