import streamlit as st

# Header section
st.title("Meda Syam Gopal's Portfolio")
st.markdown("---")

# Navigation
st.sidebar.title("Navigation")
nav_selection = st.sidebar.radio("Go to", ["About", "Skills", "Projects", "Education", "Work Experience", "Certifications", "Contact"])

# Page content
if nav_selection == "About":
    # About Section
    st.header("About Me")
    st.write("""
    I am Meda Syam Gopal, a passionate and dedicated individual with a keen interest in computer science and technology. I am currently pursuing a B.Tech in Computer Science and Engineering at RVR & JC College of Engineering. I have a strong foundation in programming languages such as C, Java, HTML, and Python. I am highly motivated to learn and grow in the field of technology.
    """)
    st.subheader("Strengths")
    st.write("""
    - Communication
    - Problem-solving
    - Teamwork
    - Learning
    - Analytical thinking
    - Logical reasoning
    """)
    st.subheader("Areas of Interests")
    st.write("Networking, Web development, Mobile development")
    st.subheader("Hobbies")
    st.write("Playing shuttle, writing programming, browsing the internet")

elif nav_selection == "Skills":
    # Skills Section
    st.header("Skills")
    st.subheader("Programming Languages")
    st.write("- C\n- Java\n- HTML\n- Python")
    st.subheader("Databases")
    st.write("- SQL")
    st.subheader("Data Analysis")
    st.write("- Data organization and analysis\n- Data visualization using Python libraries\n- Creating reports and presentations with relevant data")
    st.subheader("Other Skills")
    st.write("- Proficiency in Excel for data entry and management\n- Strong teamwork skills\n- Effective oral communication")

elif nav_selection == "Projects":
    # Projects Section
    st.header("Projects")
    st.subheader("Mango Leaves Disease Detection")
    st.write("""
    - **Role:** Developer
    - **Team Size:** 2
    - **Project Duration:** 1 Month
    - **Technologies Used:** Python, TensorFlow, OpenCV
    - **Description:** Developed a machine learning model to detect diseases in mango leaves. The project involved:
        - Collecting and preprocessing a dataset of healthy and diseased mango leaves.
        - Using image processing techniques with OpenCV to enhance the images.
        - Building a Convolutional Neural Network (CNN) using TensorFlow to classify the leaves as healthy or diseased.
        - Achieving a high accuracy rate in detecting different types of leaf diseases.
        - Deploying the model using a simple web interface for ease of use by farmers and agricultural experts.
    """)

    st.subheader("Cyber Security in Website Scraper Project")
    st.write("""
    - **Role:** Developer
    - **Team Size:** 3
    - **Project Duration:** 2 Months
    - **Technologies Used:** Python, Flask, SQL, Machine Learning
    - **Description:** Developed a secure web scraping application with enhanced cybersecurity measures. The project involved:
        - Implementing authentication mechanisms to ensure only authorized users could access the scraper.
        - Using encryption techniques to secure data transmission and storage.
        - Incorporating access controls to restrict user permissions based on roles.
        - Developing anomaly detection algorithms using machine learning to identify and prevent malicious activities.
        - Creating a user-friendly dashboard with Flask to monitor scraping activities and detected anomalies.
        - Ensuring compliance with legal and ethical standards in web scraping practices.
    """)

elif nav_selection == "Education":
    # Education Section
    st.header("Education")
    st.write("""
    - **B.Tech in Computer Science and Engineering:** RVR & JC College of Engineering, Aacharya Nagarjuna University, 7.6 CGPA (Pursuing)
    - **Diploma in Computer Management Engineering:** A.A.N.M & V.V.R.S.R Polytechnic College, State Board of Technical Education and Training, 83.67%, 2021
    - **SSC:** NIRMALA HIGH SCHOOL, State Board of Secondary Education, 9.0 CGPA, 2018
    """)

elif nav_selection == "Work Experience":
    # Work Experience Section
    st.header("Work Experience")
    st.subheader("Indian Servers Machine Learning Internship")
    st.write("""
    - **Project:** Mango leaves disease detection
    - **Description:** Developed a project for detecting diseased mango leaves using machine learning techniques. The project involved collecting and preprocessing data, building and training a CNN model, and deploying the model for practical use.
    """)
    st.subheader("SpyPro Security Solutions Pvt. Ltd.")
    st.write("""
    - **Project:** Cyber Security in Website Scraper Project
    - **Description:** Implemented advanced security measures including authentication, encryption, and access controls. Developed anomaly detection algorithms using machine learning techniques. Created a user-friendly dashboard to monitor activities and ensure secure web scraping practices.
    """)

elif nav_selection == "Certifications":
    # Certifications Section
    st.header("Certifications")
    st.subheader("CCNA")
    st.write("- Programming Essentials in Python\n- Introduction to Networks\n- Enterprise Networking, Security & Automation\n- Switching, Routing & Wireless Essentials")
    st.subheader("AWS Academy")
    st.write("- AWS Academy Cloud Foundations")
    st.subheader("NPTEL")
    st.write("- Programming in Java, IIT Kharagpur, 2022\n- Principles of Management, IIT Kharagpur, 2022\n- Cloud Computing, IIT Kharagpur, 2022")

elif nav_selection == "Contact":
    # Contact Section
    st.header("Contact")
    st.write("""
    - **Email:** [syamgopalmeda@gmail.com](mailto:syamgopalmeda@gmail.com)
    - **Phone:** 9502524924
    - **Address:** D.no:30/980, Chinna Ullingipalem, Machilipatnam, Andhra Pradesh, 521001
    """)

# Footer
st.markdown("---")
st.write("© 2024 Meda Syam Gopal. All rights reserved")
