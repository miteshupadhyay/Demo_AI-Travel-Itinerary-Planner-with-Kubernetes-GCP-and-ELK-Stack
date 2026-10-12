import warnings
warnings.filterwarnings("ignore")

from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from src.core.planner import TravelPlanner
from src.utils.logger import get_logger

logger = get_logger(__name__)

st.set_page_config(page_title="AT Travel Planner", layout="wide")
st.title("AT Travel Itinerary Planner")

with st.form("Planner Form"):
    city = st.text_input("City")
    days = st.slider("Number of days" ,1, 10,3)
    interests = st.text_input("Interests (Comma - Seperated)")
    style = st.selectbox("Travel Style", ["Budget","Mid- Range","Luxury"])
    pace = st.selectbox("Pace", ["Relaxed","Balanced","PAcked"])
    month = st.selectbox("Month (Optional)", ["Any"])

    submitted = st.form_submit_button("Generate Itinerary")

if submitted:
    if city and interests:
        planner = TravelPlanner()

        itinerary = planner.create_itinerary(
            city = city,
            days = days,
            interests=[i.strip() for i in interests.split(",")],
            style=style,
            pace=pace,
            month=None if month == "Any" else month
        )

        st.subheader("Your Travel Plan")
        st.markdown(itinerary)

        logger.info("Response Generated")
    else:
        st.warning("Please enter City and Interests")