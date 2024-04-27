import pickle
from pathlib import Path

import streamlit_authenticator as stauth

names= ["Aniket Saroj", "Dr.Rishi Dutt Sharma", "Himanshu Gupta"]
usernames= ["anii08", "rdx" ,"himayu13"]
passwords= ["abcd", "1234", "0987"]

hashed_passwords= stauth.Hasher(passwords).generate()

file_path=Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)
