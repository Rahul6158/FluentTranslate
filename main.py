import streamlit as st

# Display a bigger heading in the sidebar
st.sidebar.markdown("<h1 style='text-align: center;'>Available Options</h1>", unsafe_allow_html=True)

# Create a sidebar navigation using radio buttons with increased size
page = st.sidebar.radio("Select a Page", ["<h2 style='font-size: 20px;'>Documents and Pdfs Translation</h2>", "<h2 style='font-size: 20px;'>Additional Features</h2>"], format_func=lambda option: "")

if page == "<h2 style='font-size: 20px;'>Required Page</h2>":
    st.header("This is the Required Page")
    # Add content for the required page here...
elif page == "<h2 style='font-size: 20px;'>Additional Features</h2>":
    st.header("This is the Additional Features Page")
    # Add content for the additional features page here...

# Rest of your Streamlit app...
