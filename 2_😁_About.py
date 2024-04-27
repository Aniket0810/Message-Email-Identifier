import streamlit as st
import base64

st.title("😁About")

def main():
    st.title("👩🏻‍💻My Portfolio")
    profile="""
        <style>
            body {
                
                background-size: cover;
                background-repeat: no-repeat;
                color: #ffffff;
                font-family: Arial, sans-serif;
            }
            .profile-container {
                display: flex;
                align-items: center;
                margin-bottom: 20px;
                padding: 50px;
                background-color: rgba(0, 0, 0, 0.5); /* Add transparency to the background */
            }
            .profile-info {
                font-size: 18px;
                line-height: 1.6;
            }
            .project-card {
                border: 2px solid #ddd;
                border-radius: 10px;
                padding: 15px;
                margin-bottom: 20px;
                background-color: #212121;
            }
            .project-link {
                color: #0078FF;
                font-weight: bold;
            }
            .contact-info {
                font-size: 16px;
            }
        </style>
        <div class="profile-container">
            <div class="profile-info">
                <h1>Aniket Saroj</h1>
                <p>I am a 2nd-year student at Bennett University, Greater Noida, specializing in Cyber Security. With a keen interest in leveraging technology to ensure digital safety and security, I am dedicated to exploring and contributing to advancements in the field of cybersecurity.</p>
            </div>
        </div>
        """
    st.markdown(profile, unsafe_allow_html=True)

    st.markdown("""
    ## My Projects 💻
    """)

    projects = [
        {
            "name": "🦉SkillGate",
            "description": "An Online Coding Test and Interview Platform.",
            "link": "https://www.linkedin.com/posts/aniket-saroj08_skillgate-onlineinterviews-codingtest-activity-7187876930451333120-xrg7?utm_source=share&utm_medium=member_desktop"
        },
        {
            "name": "📸BlackMart.apk",
            "description": "Our project BlackMart.apk is apk which can be used for various purposes of spying on the criminals' personal and professional communications, such as chats, emails, etc.",
            "link": "https://www.linkedin.com/posts/aniket-saroj08_innovation-bennettuniversity-blackmart-activity-7137802881600004096-2b_E?utm_source=share&utm_medium=member_desktop"
        },
        {
            "name": "🧠Mind_It ",
            "description": ": The Mind_It is like a wellness check-up for your mind. By answering a few questions, the app gives you a glimpse into how you're feeling mentally.",
            "link": "https://www.linkedin.com/posts/aniket-saroj08_mindabrit-medicalabrhealth-innovation-activity-7111679610290880512-TSOw?utm_source=share&utm_medium=member_desktop"
        },
        # Add more projects as needed
    ]

    for project in projects:
        st.markdown(
            f"""
            <div class="project-card">
                <h3>{project['name']}</h3>
                <p>{project['description']}</p>
                <p>Link to project: <a href="{project['link']}" class="project-link">{project['name']}</a></p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("""
    ---
    ## Contact Me 📞
    """)

    st.markdown(
        f"""
    <ul class="contact-info">
        <li><a href="https://www.linkedin.com/in/aniket-saroj08/" class="project-link">LinkedIn</a></li>
        <li><a href="mailto:aniketsaroj63@gmail.com" class="project-link">Email</a></li>
    </ul>
    """,
      unsafe_allow_html=True
                )
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
    set_png_as_page_bg('Portfolio.png')    

if __name__ == "__main__":
    main()

