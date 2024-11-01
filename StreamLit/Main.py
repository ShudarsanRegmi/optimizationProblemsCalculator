import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Optimization Software",
    page_icon="🧮",
    layout="wide"
)

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-image: url('https://t4.ftcdn.net/jpg/04/94/85/25/360_F_494852538_r8ylVApdAY0YuWYCkWIsg5pDZkboERYI.jpg');  /* Replace with your image URL */
        background-size: cover;
        color: #ffffff;
    }
    .stButton>button {
        background-color: #FF6347;  /* Tomato color */
        color: white;
        border-radius: 5px;
        font-size: 18px;
        height: 50px;
        width: 150px;
        border: none;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #FF4500;  /* OrangeRed */
    }
    .header {
        text-align: center;
        font-size: 36px;
        margin-top: 50px;
    }
    .subheader {
        text-align: center;
        font-size: 24px;
        margin-top: 20px;
    }
    .info {
        text-align: center;
        font-size: 18px;
        margin-top: 10px;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }
    p{
    font-size: 14px;
    font-style: italic;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.markdown("<h1 class='header'>Welcome to the Optimization Software!</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='subheader'>Solve equations with various optimization methods</h2>", unsafe_allow_html=True)

# Information Section
st.markdown("""
<div class='info'>
    <p>This software allows you to input any mathematical equation and choose from a variety of optimization techniques to find the best solutions.</p>
    <p>Use the sidebar to select the methods you want to apply, and let us assist you in solving your optimization problems!</p>
</div>
""", unsafe_allow_html=True)

