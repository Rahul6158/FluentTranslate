import streamlit as st
import page1
import page2

# Create a sidebar navigation using radio buttons
page_choice = st.sidebar.radio("Select a Page", ["Page 1", "Page 2"])

if page_choice == "Page 1":
    page1.main()  # Call the main function for Page 1
elif page_choice == "Page 2":
    page2.main()  # Call the main function for Page 2
