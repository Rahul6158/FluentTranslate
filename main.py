# main.py

import streamlit as st
st.header("Main Page")
# Create a sidebar navigation
page = st.sidebar.radio("Available Options", ["Required Page", "Additional Features"])

if page == "Required Page":
    # Import and run the code from page1.py
    import page1
    page1.main()
else:
    # Import and run the code from page2.py
    import page2
    page2.main()

