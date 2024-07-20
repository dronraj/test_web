import streamlit as st

st.title("Welcome to the page")
st.header("DEMO")
st.subheader("admin dron")

name = st.text_input ("Enter Your Name : ")
fname = st.text_input("Enter Your Father Name : ")
adr = st.text_area("Enter Your Address : ")
classdata = st.selectbox("Enter Your Class :",(0,8,9,10,11,12))

button = st.button("Done")
if button :
    st.markdown(f"""
    Name : {name}
    Father Nmae : {fname}
    address : {adr}
    class : {classdata}""")
end





    
