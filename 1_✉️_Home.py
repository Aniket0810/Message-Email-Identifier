import streamlit as st   #Used to establish the webapp
import pickle  
import string   # String manupulation
from nltk.corpus import stopwords   # Filtering Common Words
import nltk    #Importing natural language processing functions.
from nltk.stem.porter import PorterStemmer # used for stemming words
import pickle
from pathlib import Path
import streamlit_authenticator as stauth
import base64
import base64
import nltk
import pickle
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import csr_matrix

st.set_page_config(
    page_title="Message/Email Identifier",
    page_icon="👩🏻‍💻"
)
st.sidebar.title("📃Menu")
st.sidebar.success("Select a page above.")


names= ["Aniket Saroj", "Dr.Rishi Dutt Sharma", "Himanshu Gupta"]
usernames= ["anii08", "rdx", "himayu13"]

file_path= Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)
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
    set_png_as_page_bg('login.png')
st.title("Message/Email Identifier ✉️")     
authenticator=stauth.Authenticate(names, usernames, hashed_passwords, "sales_dashboard","abcdef", cookie_expiry_days=0)   
name, authentication_status, username = authenticator.login("LOGIN", "main")


if authentication_status == False:
    st.error("Username/Password is incorrect.")

if authentication_status == None:
    st.error("Please enter your username and password.")    

if authentication_status:


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

    set_png_as_page_bg('login.png')

    import streamlit as st
    import pickle
    import nltk
    from nltk.corpus import stopwords
    from nltk.stem.porter import PorterStemmer
    import string
    from sklearn.feature_extraction.text import TfidfVectorizer
    from scipy.sparse import csr_matrix

    # Download NLTK resources
    nltk.download('punkt')
    nltk.download('stopwords')

    # Load the vectorizer
    with open('vectorizer.pkl', 'rb') as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)

    # Load the MultinomialNB model
    with open('model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)

    ps = PorterStemmer()

    def transform_text(text):
        text = text.lower()
        text = nltk.word_tokenize(text)
        y = []
        for i in text:
            if i.isalnum():
                y.append(i)
        text = y[:]
        y.clear()
        for i in text:
            if i not in stopwords.words('english') and i not in string.punctuation:
                y.append(i)
        text = y[:]
        y.clear()
        for i in text:
            y.append(ps.stem(i))
        return " ".join(y)



    input_sms = st.text_input('Enter the Message')
    option = st.selectbox("You Got Message From :-", ["Via Email ", "Via SMS", "other"])

    if st.checkbox("Check me"):
        st.write("")

    if st.button('PREDICT'):
        # 1. preprocess
        transformed_sms = transform_text(input_sms)
        # 2. vectorize
        vector_input = vectorizer.transform([transformed_sms])

        try:
            # Ensure vector_input is a CSR matrix if using scipy.sparse
            if isinstance(vector_input, csr_matrix):
                if not hasattr(model, 'predict'):
                    st.error("Model is not fitted.")
                else:
                    result = model.predict(vector_input)[0]
                    # 3. Display
                    if result == 1:
                        st.header("Spam, be aware of the message.")
                    else:
                        st.header("Not Spam.\nWithout any worries you could give a reply to the message.")
            else:
                st.error("Vector input is not in the correct format.")
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
            
