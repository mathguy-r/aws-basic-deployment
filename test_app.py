import streamlit as st
import time

if __name__ == "__main__":
    st.title("This is a test Return Calculator")
    p = st.number_input("I want to invest (in INR)", min_value=1000, step=500)
    f = st.radio("I want to do it",("One time","Monthly SIP"))
    r = st.number_input("Yearly Interest Rate", min_value=0.5, step=0.1)
    t = st.slider("I want to invest for (in years)", min_value=1,max_value=10)
    if st.button("Calculate"):
        if f == "Monthly SIP":
            r = r/1200
            t = t*12
            total = p*(1+r)*((1+r)**t - 1)/r
        else:
            total = p*(1+r/100)**t
        with st.spinner('computing ...'):
            time.sleep(1)
            st.write(f"You will get INR {round(total,3)} in total")
