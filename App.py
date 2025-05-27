import streamlit as st

st.write("Enter the following information")

Name = st.text_input("Name:")
Starting_Date = st.date_input("Starting Date:")
Ending_Date = st.date_input("Ending Date:")
Board = st.write("Board")

BB = st.button("BB")
HB = st.button("HB")
FB = st.button("FB")

Amount_of_Rooms = st.write("Amount of rooms")

One = st.button("One")
Two = st.button("Two")
Three = st.button("Three")
Four = st.button("Four")

Number_of_Adults = (st.text_input("Amount of Adults(12&above)"))
Number_of_Children_0_5 = (st.text_input("Amount of Children(0-5)"))
Number_of_Children_6_11 = (st.text_input("Amount 0f Children(6-11)"))
