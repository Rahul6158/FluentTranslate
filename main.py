import streamlit as st

# Display a bigger heading in the sidebar
st.sidebar.markdown("<h1 style='text-align: center;'>Sidebar Navigation</h1>", unsafe_allow_html=True)

# Create a sidebar navigation using radio buttons with increased size
page = st.sidebar.radio("", ["Required Page", "Additional Features"], key="page")

if page == "Required Page":
    st.header("This is the Required Page")
    # Add content for the required page here...
elif page == "Additional Features":
    st.header("This is the Additional Features Page")
    # Add content for the additional features page here...

# Rest of your Streamlit app...
