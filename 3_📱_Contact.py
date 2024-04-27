import streamlit as st
import base64

st.title("📱Contact")




contact_form = """
<form action="https://formsubmit.co/aniketsaroj63@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="hidden" name="_next" value="http://127.0.0.1:8000/Thanks.html">
     <input type="hidden" name="_template" value="table">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style", unsafe_allow_html=True)
local_css("style.css")    
@st.cache_data
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)   
set_png_as_page_bg('red_mail.png')    