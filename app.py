# app.py
import streamlit as st
import time

# --- Page Configuration ---
# The title and icon that appear in the browser tab.
st.set_page_config(
    page_title="My GSA Application",
    page_icon="🚀",
    layout="wide"
)

# --- Profile Section ---
# Use columns to create a layout with your photo on the left and intro on the right.
col1, col2 = st.columns([0.3, 0.7], gap="large")
with col1:
    # IMPORTANT: Create a folder named "assets" in the same directory as your app.py
    # and place your professional photo there. Rename it to "profile.png".
    st.image("profile.png", width=250)

with col2:
    st.title("My Google Student Ambassador Application", anchor=False)
    st.subheader("Bharathidasan University, Trichy", anchor=False)
    st.markdown("""
    I'm not just waiting for opportunities; **I'm here to create them.** This interactive application outlines my mission to build a vibrant tech community from the ground up.
    """)

# --- The "Why" Section ---
st.header("The Reality on Our Campus", divider="rainbow")

# Using metrics to create a powerful, visual statement.
metric_col1, metric_col2, metric_col3 = st.columns(3)
metric_col1.metric(label="On-Campus Placements", value="0")
metric_col2.metric(label="Industry Mentorship", value="Lacking")
metric_col3.metric(label="Student Potential", value="Untapped")

st.markdown("""
> This is precisely why I am eager to become a Google Student Ambassador. My goal is to be a **catalyst for change** — a demonstration that innovation and ambition are possible, even in institutions that recruiters often overlook.
""")

# --- The "Mission" Section ---
st.header("My Mission & Vision", divider="rainbow")

# Using tabs for a clean, interactive way to present your core pillars.
tab1, tab2, tab3 = st.tabs(["💡 My Driving Force", "🤝 My Community Focus", "🎯 My Vision"])

with tab1:
    st.subheader("Technology as a Tool for Empowerment")
    st.markdown("""
    My enthusiasm for technology is the driving force behind this ambition. I view technology not merely as code, but as a means to **address real-world challenges.** When resources are inaccessible, I am committed to finding ways to bridge that gap for my peers.
    """)

with tab2:
    st.subheader("Fostering a Culture of Curiosity")
    st.markdown("""
    Community is deeply important to me. I've witnessed how students can lose motivation simply because they lack guidance. I want to change that — to **foster connections, spark curiosity, and prove that we are capable of achieving great things.**
    """)

with tab3:
    st.subheader("Challenging the Norm")
    st.markdown("""
    I see “Googliness” as embodying helpfulness, innovation, and the courage to challenge conventional norms. My vision is to build a culture where, regardless of visiting companies, graduates are **prepared and confident for the future.**
    """)

# --- The "Game Plan" Section ---
st.header("My Game Plan: Turning Potential into Opportunity", divider="rainbow")

st.info("Here is my proposed roadmap for the first year as a GSA. Click on a goal to see the details.", icon="🗺️")

# Using expanders to make the plan interactive and digestible.
with st.expander("**Phase 1: Build the Foundation (Beginner Workshops)**"):
    st.markdown("- Organize workshops to overcome apprehensions regarding technology, focusing on beginner-friendly Google tools.")
    st.markdown("- **Goal:** Make tech accessible and demystify coding for everyone.")

with st.expander("**Phase 2: Spark Collaboration (Hackathons & Learning Circles)**"):
    st.markdown("- Facilitate hackathons to encourage collaborative problem-solving on local issues.")
    st.markdown("- Create learning circles where students support and educate one another in a peer-to-peer model.")
    st.markdown("- **Goal:** Foster teamwork and practical application of skills.")

with st.expander("**Phase 3: Create a Legacy (Sustainable Community)**"):
    st.markdown("- Establish a formal tech club that can continue to run events and workshops independently.")
    st.markdown("- **Goal:** Build a self-sustaining culture of innovation that will outlast my tenure.")

# --- The "Call to Action" / Final Statement ---
st.header("Let's Build the Future, Together.", divider="rainbow")
st.markdown("""
I aspire not only to represent Google on my campus but also to **stand for every student who feels unseen** and every ambition that seems out of reach. I am not simply bringing ideas — I am determined to turn potential into real opportunity.
""")

# A fun, innovative final touch!
if st.button("Click here to see my commitment!", type="primary"):
    progress_text = "Building a new future for my peers..."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)

    st.balloons()

    st.success("Mission Ready! Thank you for your consideration.", icon="✅")
