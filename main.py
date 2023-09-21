import streamlit as st

# Create a sidebar navigation
page = st.sidebar.selectbox("Select a Page", ["Page 1", "Page 2"])

if page == "Page 1":
    # Import and run the code from page1.py
    import page1
    page1.main()
else:
    # Import and run the code from page2.py
    import page2
    page2.main()
