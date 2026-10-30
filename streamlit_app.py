import streamlit as st
from app import find_schemes

st.set_page_config(page_title="Scheme Finder", page_icon="🏛")
st.title("Scheme Finder")
st.caption("Find government schemes you may qualify for. Runs locally with an open model.")

col1, col2 = st.columns(2)
age = col1.number_input("Age", 0, 120, 30)
gender = col2.selectbox("Gender", ["Female", "Male", "Other"])
occupation = col1.selectbox(
    "Occupation",
    ["Farmer", "Student", "Daily wage worker", "Self-employed", "Salaried", "Homemaker", "Unemployed", "Retired"],
)
income = col2.selectbox("Yearly family income", ["Below 1 lakh", "1-3 lakh", "3-8 lakh", "Above 8 lakh"])
state = st.text_input("State", "Tamil Nadu")
extra = st.text_area(
    "Anything else? (any language)",
    placeholder="e.g. I own 2 acres of land, no bank account, no pucca house...",
)

if st.button("Find schemes", type="primary"):
    profile = (
        f"I am a {age} year old {gender.lower()}, {occupation.lower()} from {state}. "
        f"Family income: {income}. {extra}"
    )
    with st.spinner("Searching schemes..."):
        try:
            st.markdown(find_schemes(profile, dict(age=age, gender=gender, occupation=occupation, income=income, extra=extra)))
        except Exception as e:
            st.error(f"Could not reach Ollama. Is it running? ({e})")

st.divider()
st.caption("Guide only. Always verify on the official website.")

