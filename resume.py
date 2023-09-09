from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Sinan_Saglam_CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Sinan Saglam"
PAGE_ICON = ":wave:"
NAME = "Sinan Saglam"
DESCRIPTION = """
Software Developer / Data Engineer
"""
EMAIL = "sinan.saglam99@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/sinan-samil-saglam/",
    "GitHub": "https://github.com/sinansamilsaglam",
    "Kaggle": "https://www.kaggle.com/sinansaglam",
}
# PROJECTS = {
#     "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
#     "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
#     "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
#     "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
# }


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
    st.write("📍", "Izmir, Turkey")
    st.write("📞", "+90 543 247 93 43")


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work Experience")
st.write("---")

# --- JOB 1
st.write("👨‍💻", "**Software Developer / Data Engineer**")
st.write("**Litum Technologies**")
st.write("December 2022 - August 2023   | Izmir, Turkey")
st.write(
    """
- 🔹 Created Analytical Reporting Service and Machine Learning studies with Amazon real time location data
- 🔹 Built ETL pipelines using technologies such as Python, C#, Microsoft SQL Server, Apache Cassandra and more
- 🔹 Built microservices using .NET, .NET Entity Framework, SQL and more technologies
- 🔹 Reduced response times by optimizing microservices
- 🔹 Made classification and prediction on location data using Machine Learning Algorithms with Python
"""
)


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Education")
st.write("---")

# --- EDUCATION 1
st.write("💻", "**Computer Science Department**")
st.write("**Dokuz Eylul University**")
st.write("September 2017 - June 2022   | Izmir, Turkey")


# --- SKILLS ---
st.write('\n')
st.subheader("Skills")
st.write("---")
st.write(
    """
- 🔹Python
- 🔹C#
- 🔹SQL
- 🔹.NET
- 🔹Apache Cassandra
- 🔹Apache Spark
- 🔹ETL
- 🔹RDBMS
- 🔹Microsoft SQL Server
- 🔹Data Engineering
- 🔹Machine Learning
- 🔹Data Analysis
"""
)


st.write('\n')
st.subheader("Languages")
st.write("---")
st.write(
    """
- 🔹English
- 🔹Turkish
"""
)


# --- Projects & Accomplishments ---
# st.write('\n')
# st.subheader("Projects & Accomplishments")
# st.write("---")
# for project, link in PROJECTS.items():
#     st.write(f"[{project}]({link})")
